"""Evaluation integrity checks, separate from model-quality scores."""
import copy
import importlib.util
import json
import tempfile
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("skill_evaluation", ROOT / "scripts/evaluate_skill.py")
EVAL = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(EVAL)
with patch.object(sys, "path", [str(ROOT / "scripts"), *sys.path]):
    AUDIT_SPEC = importlib.util.spec_from_file_location("evaluation_audit", ROOT / "scripts/audit_evaluation.py")
    AUDIT = importlib.util.module_from_spec(AUDIT_SPEC)
    AUDIT_SPEC.loader.exec_module(AUDIT)


def rating(label="A"):
    result = {
        "candidate": label,
        "checks": [{"invariant_id": 1, "status": "preserved", "evidence": "may cancel"}],
        "unsupported_claims": [], "format_pass": True, "language_pass": True,
        "hard_fail": False, "reason": "Permission preserved.",
    }
    result.update({dimension: 5 for dimension in EVAL.DIMENSIONS})
    return result


class EvaluationIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.case = {"id": "example", "lang": "en", "category": "conditions",
                     "task": "Rewrite: The buyer may cancel.",
                     "invariants": ["Cancellation is permission, not an obligation."]}
        self.review = {"cases": [{"case_id": "example", "ratings": [rating(), rating("B")],
                                 "preference": "tie", "preference_reason": "Equal meaning."}]}

    def corpus(self, cases):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        path = Path(folder.name) / "cases.jsonl"
        path.write_text("".join(json.dumps(c, ensure_ascii=False) + "\n" for c in cases))
        return path

    def test_100_new_cases_cover_all_locales(self):
        cases = EVAL.load_cases(ROOT / "benchmarks/reliability-100.jsonl")
        public_tasks = {c["task"] for c in EVAL.read_jsonl(ROOT / "benchmarks/cases.jsonl")}
        self.assertTrue(all(c["task"] not in public_tasks for c in cases))
        self.assertEqual(len({c["id"] for c in cases}), 100)
        self.assertEqual(sum(len(c["invariants"]) for c in cases), 373)
        locales = {c["lang"] for c in cases if "target_lang" not in c}
        self.assertEqual(locales, {"en", "pt-BR", "es", "fr", "de", "ja", "zh-CN", "it", "ru"})
        self.assertEqual(sum("target_lang" in c for c in cases), 24)

    def test_partial_and_duplicate_corpus_fail(self):
        with self.assertRaisesRegex(ValueError, "Expected 100"):
            EVAL.load_cases(self.corpus([self.case]))
        with self.assertRaisesRegex(ValueError, "duplicate"):
            EVAL.load_cases(self.corpus([self.case, self.case]), expected=2)

    def test_invalid_invariants_language_and_protected_tokens_fail(self):
        for modification in ({"invariants": []}, {"lang": "unknown"}, {"protected": ["not in source"]}):
            with self.subTest(modification=modification), self.assertRaises(ValueError):
                EVAL.load_cases(self.corpus([dict(self.case, **modification)]), expected=1)

    def test_control_has_no_skill_or_invariant_leakage(self):
        prompt = EVAL.prompt_for(self.case, "baseline", "SECRET SKILL")
        self.assertEqual(prompt, self.case["task"])
        self.assertNotIn("SECRET SKILL", prompt)
        self.assertNotIn(self.case["invariants"][0], prompt)

    def test_review_blinding_and_reversed_second_pass(self):
        outputs = {("example", "baseline"): {"output": "The buyer may cancel."},
                   ("example", "skill"): {"output": "The buyer can cancel."}}
        prompts = [EVAL.review_prompt([self.case], outputs, i) for i in (1, 2)]
        values = [json.loads(p.split("\n\n", 1)[1]) for p in prompts]
        labels = [[c["candidate"] for c in v[0]["candidates_in_display_order"]] for v in values]
        self.assertEqual(labels[0], list(reversed(labels[1])))
        for forbidden in ("ASDify", '"baseline"', '"skill"'):
            self.assertNotIn(forbidden, prompts[0])

    def test_missing_case_candidate_or_invariant_fails(self):
        invalid = [
            {"cases": []},
            {"cases": [dict(self.review["cases"][0], ratings=[rating()])]},
        ]
        for checks in ([], [rating()["checks"][0]] * 2):
            value = copy.deepcopy(self.review)
            value["cases"][0]["ratings"][0]["checks"] = checks
            invalid.append(value)
        for value in invalid:
            with self.subTest(value=value), self.assertRaises(ValueError):
                EVAL.validate_review(value, [self.case])

    def test_material_defect_cannot_be_reported_as_pass(self):
        for modification in (
            {"checks": [{"invariant_id": 1, "status": "missing", "evidence": "Permission absent"}]},
            {"unsupported_claims": ["Cancellation is mandatory."]},
            {"language_pass": False}, {"format_pass": False},
        ):
            value = copy.deepcopy(self.review)
            value["cases"][0]["ratings"][0].update(modification)
            with self.subTest(modification=modification), self.assertRaisesRegex(ValueError, "defect"):
                EVAL.validate_review(value, [self.case])

    def test_failing_candidate_cannot_win_or_tie(self):
        for preference in ("A", "tie"):
            value = copy.deepcopy(self.review)
            value["cases"][0]["ratings"][0]["hard_fail"] = True
            value["cases"][0]["preference"] = preference
            with self.subTest(preference=preference), self.assertRaises(ValueError):
                EVAL.validate_review(value, [self.case])

    def test_both_fail_requires_neither(self):
        value = copy.deepcopy(self.review)
        for candidate in value["cases"][0]["ratings"]:
            candidate["hard_fail"] = True
        value["cases"][0]["preference"] = "neither"
        self.assertEqual(len(EVAL.validate_review(value, [self.case])), 1)

    def test_uncertain_check_is_not_confirmed_pass(self):
        ratings = [rating(), rating("B")]
        ratings[1]["checks"][0]["status"] = "uncertain"
        result = EVAL.summarize(self.case, "The buyer may cancel.", ratings)
        self.assertFalse(result["hard_fail"])
        self.assertTrue(result["uncertain"])
        self.assertFalse(result["confirmed_pass"])

    def test_review_disagreement_keeps_stricter_failure(self):
        ratings = [rating(), rating("B")]
        ratings[1]["hard_fail"] = True
        result = EVAL.summarize(self.case, "The buyer may cancel.", ratings)
        self.assertTrue(result["hard_fail"])
        self.assertTrue(result["review_disagreement"])
        self.assertFalse(result["confirmed_pass"])

    def test_json_fences_keys_and_value_types(self):
        case = dict(self.case, json_keys=["count", "message"], json_expected={"count": 3})
        self.assertFalse(EVAL.mechanical_checks(case, '{"count":3,"message":"Ready"}'))
        fenced = EVAL.FENCE + 'json\n{"count":3,"message":"Ready"}\n' + EVAL.FENCE
        for answer in (fenced, '{"count":"3","message":"Ready"}', '{"count":3,"text":"Ready"}'):
            with self.subTest(answer=answer):
                self.assertTrue(EVAL.mechanical_checks(case, answer))

    def test_verbatim_quote_and_placeholder_protection(self):
        case = dict(self.case, protected=["{{name}}"], exact_output="Hello {{name}}.")
        self.assertFalse(EVAL.mechanical_checks(case, "Hello {{name}}.\n"))
        self.assertTrue(EVAL.mechanical_checks(case, "Hello {name}."))
        self.assertTrue(EVAL.mechanical_checks(case, "Here is the text: Hello {{name}}."))

    def test_tool_activity_and_incomplete_events_fail(self):
        for events in (
            [{"type": "turn.completed", "usage": {}}],
            [{"type": "item.completed", "item": {"type": "command_execution", "command": "cat SKILL.md"}},
             {"type": "item.completed", "item": {"type": "agent_message", "text": "Hello"}},
             {"type": "turn.completed", "usage": {}}],
        ):
            with self.subTest(events=events), self.assertRaises(ValueError):
                EVAL.parse_events("\n".join(json.dumps(e) for e in events))

    def test_final_answer_is_captured_verbatim(self):
        events = [
            {"type": "item.completed", "item": {"type": "agent_message", "text": "Progress"}},
            {"type": "item.completed", "item": {"type": "agent_message", "text": "May cancel; not required."}},
            {"type": "turn.completed", "usage": {"input_tokens": 123, "output_tokens": 8}},
        ]
        answer, usage = EVAL.parse_events("\n".join(json.dumps(e) for e in events))
        self.assertEqual(answer, "May cancel; not required.")
        self.assertEqual(usage["input_tokens"], 123)

    def test_duplicate_successful_generation_fails(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            row = {"case_id": "example", "arm": "baseline", "output": "May cancel."}
            (root / "generations.jsonl").write_text(json.dumps(row) + "\n" + json.dumps(row) + "\n")
            with self.assertRaisesRegex(ValueError, "Duplicate"):
                EVAL.successful_generations(root)

    def test_report_refuses_incomplete_live_generation(self):
        with tempfile.TemporaryDirectory() as folder, \
                patch.object(EVAL, "verify_frozen", return_value=({}, [self.case])):
            with self.assertRaisesRegex(ValueError, "incomplete"):
                EVAL.report(Path(folder))

    def test_evidence_audit_rejects_edited_answer_or_usage(self):
        events = [
            {"type": "item.completed", "item": {"type": "agent_message", "text": "May cancel."}},
            {"type": "turn.completed", "usage": {"output_tokens": 3}},
        ]
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "raw").mkdir()
            (root / "raw/example-attempt-1.events.jsonl").write_text(
                "\n".join(json.dumps(e) for e in events))
            original = {"attempts": [{"attempt": 1}], "output": "May cancel.",
                        "usage": {"output_tokens": 3}}
            AUDIT.verify_raw(root, "example", original)
            for modification in ({"output": "Must cancel."}, {"usage": {"output_tokens": 4}}):
                with self.subTest(modification=modification), self.assertRaisesRegex(ValueError, "differs"):
                    AUDIT.verify_raw(root, "example", dict(original, **modification))

    def test_changed_frozen_input_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "cases.jsonl").write_text("changed input")
            (root / "metadata.json").write_text(json.dumps({"case_file_sha256": EVAL.sha(b"original input")}))
            with self.assertRaisesRegex(ValueError, "Frozen cases changed"):
                EVAL.verify_frozen(root)

    def test_archived_skill_has_identical_prompt_without_installable_manifest(self):
        import shutil
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder) / "skill"
            shutil.copytree(ROOT / "skills/asdify", root)
            original = EVAL.treatment_text(root)
            (root / "SKILL.md").rename(root / "SKILL.txt")
            self.assertEqual(EVAL.treatment_text(root), original)
            self.assertFalse(list(root.rglob("SKILL.md")))
        self.assertFalse(list((ROOT / "benchmarks/results").rglob("SKILL.md")),
                         "Published evidence must not add a duplicate installable skill")

    def test_declared_inconsistency_remains_a_failure_and_keeps_raw_rating(self):
        value = copy.deepcopy(self.review)
        inconsistent = value["cases"][0]["ratings"][0]
        inconsistent["checks"][0]["status"] = "missing"
        EVAL.validate_review(value, [self.case], {("example", "A")})
        self.assertFalse(inconsistent["hard_fail"], "Do not edit a model's original rating")
        result = EVAL.summarize(self.case, "May cancel.", value["cases"][0]["ratings"])
        self.assertTrue(result["hard_fail"])
        self.assertFalse(result["confirmed_pass"])
        self.assertEqual(result["inconsistent_verdicts"], 1)

    def test_calibration_audit_rejects_changed_controls_and_summary(self):
        import shutil
        source = ROOT / "benchmarks/results/2026-10-08-reliability-100/calibration"
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            shutil.copytree(source, root / "calibration")
            self.assertEqual(AUDIT.audit_calibration(root), 40)
            for filename, mutate, message in (
                ("frozen-controls.json", lambda value: value["cases"][0].update(good="Edited answer"),
                 "prompt or display order changed"),
                ("summary.json", lambda value: value.update(negative_controls_detected=0),
                 "summary differs"),
            ):
                path = root / "calibration" / filename
                original = path.read_text()
                value = json.loads(original)
                mutate(value)
                path.write_text(json.dumps(value))
                with self.subTest(filename=filename), self.assertRaisesRegex(ValueError, message):
                    AUDIT.audit_calibration(root)
                path.write_text(original)

    def test_existing_raw_evidence_cannot_be_overwritten_by_a_new_call(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "raw").mkdir()
            evidence = root / "raw/example-attempt-1.events.jsonl"
            evidence.write_text("Original evidence")
            with patch.object(EVAL.subprocess, "run") as invoke:
                with self.assertRaisesRegex(ValueError, "Existing raw evidence"):
                    EVAL.call_model(root, "example", "New prompt", "model", "medium", [])
                invoke.assert_not_called()
            self.assertEqual(evidence.read_text(), "Original evidence")


if __name__ == "__main__":
    unittest.main()
