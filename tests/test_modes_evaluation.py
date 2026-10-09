"""Integrity checks for the paired five-condition multilingual study."""
import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
with patch.object(sys, "path", [str(ROOT / "scripts"), *sys.path]):
    SPEC = importlib.util.spec_from_file_location("modes_evaluation", ROOT / "scripts/evaluate_modes.py")
    MODES = importlib.util.module_from_spec(SPEC)
    SPEC.loader.exec_module(MODES)


def rating(label):
    value = {"candidate": label, "checks": [{"invariant_id": 1, "status": "preserved", "evidence": "may cancel"}],
             "unsupported_claims": [], "format_pass": True, "language_pass": True,
             "hard_fail": False, "reason": "Permission preserved."}
    value.update({d: 5 for d in MODES.base.DIMENSIONS})
    return value


class ModesEvaluationIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.case = {"id": "example", "lang": "en", "benchmark_language": "en",
                     "category": "modality", "task": "Rewrite: The buyer may cancel.",
                     "invariants": ["Permission survives; cancellation is not mandatory."]}
        self.review = {"cases": [{"case_id": "example", "ratings": [rating(l) for l in MODES.LABELS]}]}

    def test_900_new_cases_cover_all_locales_and_directions(self):
        cases = MODES.load_corpus(ROOT / "benchmarks/multilingual-modes")
        self.assertEqual(len(cases), 900)
        self.assertEqual(sum("target_lang" in c for c in cases), 180)
        self.assertEqual(len({c["task"] for c in cases}), 900)
        self.assertEqual({c["benchmark_language"] for c in cases}, set(MODES.locales()))
        for locale in MODES.locales():
            self.assertEqual(sum(c["benchmark_language"] == locale for c in cases), 100)

    def test_control_does_not_receive_skill_or_scoring_criteria(self):
        prompt = MODES.generation_prompt([self.case], "baseline", ROOT / "skills/asdify")
        self.assertNotIn("ASDify", prompt)
        self.assertNotIn(self.case["invariants"][0], prompt)
        self.assertNotIn('"invariants"', prompt)
        self.assertIn(self.case["task"], prompt)

    def test_all_modes_override_full_default_and_share_same_task(self):
        for mode in MODES.CONDITIONS[1:]:
            with self.subTest(mode=mode):
                prompt = MODES.generation_prompt([self.case], mode, ROOT / "skills/asdify")
                self.assertIn(f"User mode selection: ASDify {mode}.", prompt)
                self.assertIn("references/translation.md", prompt)
                self.assertTrue(prompt.endswith(json.dumps([{"case_id": "example", "task": self.case["task"]}])))
                self.assertNotIn(self.case["invariants"][0], prompt)

    def test_off_is_distinct_from_absent_skill(self):
        off = MODES.generation_prompt([self.case], "off", ROOT / "skills/asdify")
        control = MODES.generation_prompt([self.case], "baseline", ROOT / "skills/asdify")
        self.assertIn("ASDify off", off)
        self.assertNotEqual(off, control)

    def test_unknown_modes_fail_before_generation(self):
        with self.assertRaises(ValueError):
            MODES.generation_prompt([self.case], "invented", ROOT / "skills/asdify")

    def test_per_case_label_randomization_is_stable_and_complete(self):
        maps = [MODES.label_key(f"case-{i}") for i in range(30)]
        self.assertEqual(maps[0], MODES.label_key("case-0"))
        self.assertGreater(len({tuple(m.values()) for m in maps}), 10)
        self.assertTrue(all(set(m) == set(MODES.LABELS) and set(m.values()) == set(MODES.CONDITIONS) for m in maps))

    def test_blinded_reviews_have_all_candidates_and_reverse_positions(self):
        answers = {("example", c): f"Candidate text {i}" for i, c in enumerate(MODES.CONDITIONS)}
        prompts = [MODES.review_prompt([self.case], answers, r) for r in (1, 2)]
        rows = [json.loads(p.split("\n\n", 1)[1])[0] for p in prompts]
        a, b = [r["candidates_in_display_order"] for r in rows]
        self.assertEqual(a, list(reversed(b)))
        self.assertEqual({r["text"] for r in a}, set(answers.values()))
        for p in prompts:
            for private in ("ASDify", '"baseline"', '"lite"', '"full"', '"ultra"', '"off"'):
                self.assertNotIn(private, p)

    def test_incomplete_duplicate_unknown_and_empty_answers_fail(self):
        values = [{"answers": []}, {"answers": [{"case_id": "wrong", "text": "text"}]},
                  {"answers": [{"case_id": "example", "text": " "}]}]
        for v in values:
            with self.subTest(value=v), self.assertRaises(ValueError):
                MODES.validate_answers(v, [self.case])
        value = {"answers": [{"case_id": "example", "text": "one"}] * 2}
        with self.assertRaises(ValueError):
            MODES.validate_answers(value, [self.case, dict(self.case, id="second")])

    def test_transport_preserves_inner_requested_json_and_verbatim_text(self):
        for answer in ('{"amount":3}', "We may pause service."):
            value = {"answers": [{"case_id": "example", "text": answer}]}
            self.assertEqual(MODES.validate_answers(value, [self.case])["example"], answer)

    def test_every_review_requires_all_five_candidates(self):
        for labels in (["A", "B"], ["A", "B", "C", "D", "D"]):
            value = {"cases": [{"case_id": "example", "ratings": [rating(l) for l in labels]}]}
            with self.subTest(labels=labels), self.assertRaises(ValueError):
                MODES.validate_review(value, [self.case])

    def test_review_missing_cases_checks_or_evidence_fail(self):
        values = [{"cases": []}]
        for modification in ({"checks": []}, {"checks": [{"invariant_id": 1, "status": "preserved", "evidence": ""}]},
                             {"checks": [rating("A")["checks"][0]] * 2}):
            v = copy.deepcopy(self.review)
            v["cases"][0]["ratings"][0].update(modification)
            values.append(v)
        for v in values:
            with self.subTest(value=v), self.assertRaises(ValueError):
                MODES.validate_review(v, [self.case])

    def test_boolean_scores_and_unsubstantiated_verdicts_fail(self):
        for modification in ({"clarity": True}, {"language_pass": "yes"}, {"reason": ""},
                             {"unsupported_claims": "none"}, {"unsupported_claims": [42]}):
            v = copy.deepcopy(self.review)
            v["cases"][0]["ratings"][0].update(modification)
            with self.subTest(modification=modification), self.assertRaises(ValueError):
                MODES.validate_review(v, [self.case])

    def test_contradictory_reviewer_verdict_is_retained_but_cannot_pass(self):
        v = copy.deepcopy(self.review)
        first = v["cases"][0]["ratings"][0]
        first["checks"][0].update(status="missing", evidence="Permission is absent.")
        self.assertEqual(MODES.validate_review(v, [self.case]), v["cases"])
        summary = MODES.base.summarize(self.case, "The buyer cancels.", [first, rating("A")])
        self.assertFalse(summary["confirmed_pass"])
        self.assertEqual(summary["inconsistent_verdicts"], 1)

    def test_any_uncertainty_prevents_confirmed_pass(self):
        r = rating("A")
        r["checks"][0].update(status="uncertain", evidence="Permission is unclear.")
        result = MODES.base.summarize(self.case, "The buyer may cancel.", [r, rating("A")])
        self.assertFalse(result["confirmed_pass"])
        self.assertTrue(result["uncertain"])

    def test_raw_success_cannot_be_overwritten(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            (p / "raw").mkdir()
            (p / "raw/id-attempt-1.events.jsonl").write_text("evidence")
            with self.assertRaisesRegex(ValueError, "overwrite"):
                MODES.call_model(p, "id", "prompt", {}, [], p / "schema")

    def test_calibration_labels_are_balanced_without_truth_in_review(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            cases = MODES.base.load_cases(ROOT / "benchmarks/judge-calibration.jsonl", expected=10)
            MODES.base.write_json(p / "calibration-controls.json", cases)
            controls, answers, truth = MODES.calibration_data(p)
            self.assertEqual(sum(g for c in truth.values() for g in c.values()), 25)
            self.assertEqual(len(answers), 50)
            prompt = MODES.review_prompt(controls[:5], answers, 1)
            for hidden in ("authored_good", '"good"', '"bad"'):
                self.assertNotIn(hidden, prompt)

    def request_fixture(self, folder):
        prompt, answer = "A task", '{"answers":[]}'
        usage = {"input_tokens": 12, "output_tokens": 4}
        events = [{"type": "item.completed", "item": {"type": "agent_message", "text": answer}},
                  {"type": "turn.completed", "usage": usage}]
        raw = folder / "raw"
        raw.mkdir()
        (raw / "sample-attempt-1.events.jsonl").write_text("\n".join(json.dumps(e) for e in events) + "\n")
        (raw / "sample-attempt-1.stderr.txt").write_text("")
        attempt = {"attempt": 1, "error": None, "exit_code": 0, "seconds": 1.0,
                   "output": answer, "usage": usage}
        request = {"prompt_sha256": MODES.base.sha(prompt.encode()), "attempts": [attempt],
                   "output": answer, "usage": usage}
        (folder / ".requests").mkdir()
        MODES.base.write_json(folder / ".requests/sample.json", {
            "prompt_sha256": request["prompt_sha256"], "started_at_utc": MODES.base.now()})
        MODES.base.write_json(folder / "sample-request.json", request)
        return prompt, request

    def test_request_audit_matches_raw_output_and_usage(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            prompt, request = self.request_fixture(p)
            self.assertEqual(MODES.audit_request(p, "sample", prompt), request)

    def test_saved_answer_or_usage_tampering_is_detected(self):
        for field in ("output", "usage"):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as d:
                p = Path(d)
                prompt, request = self.request_fixture(p)
                request[field] = "changed" if field == "output" else {"output_tokens": 100}
                MODES.base.write_json(p / "sample-request.json", request)
                with self.assertRaisesRegex(ValueError, "raw output"):
                    MODES.audit_request(p, "sample", prompt)

    def test_raw_answer_or_prompt_tampering_is_detected(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            prompt, _ = self.request_fixture(p)
            with self.assertRaisesRegex(ValueError, "changed prompt"):
                MODES.audit_request(p, "sample", prompt + "changed")
            raw = p / "raw/sample-attempt-1.events.jsonl"
            raw.write_text(raw.read_text().replace("answers", "edited"))
            with self.assertRaisesRegex(ValueError, "raw model answer"):
                MODES.audit_request(p, "sample", prompt)

    def test_unrecorded_raw_attempt_is_detected(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            prompt, _ = self.request_fixture(p)
            (p / "raw/sample-attempt-2.events.jsonl").write_text("unrecorded")
            with self.assertRaisesRegex(ValueError, "Unrecorded raw attempts"):
                MODES.audit_request(p, "sample", prompt)

    def test_duplicate_successful_attempt_is_detected(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            prompt, request = self.request_fixture(p)
            request["attempts"].append(dict(request["attempts"][0], attempt=2))
            for suffix in ("events.jsonl", "stderr.txt"):
                source = p / f"raw/sample-attempt-1.{suffix}"
                (p / f"raw/sample-attempt-2.{suffix}").write_text(source.read_text())
            MODES.base.write_json(p / "sample-request.json", request)
            with self.assertRaisesRegex(ValueError, "Completed earlier answer"):
                MODES.audit_request(p, "sample", prompt)

    def test_missing_stderr_evidence_is_detected(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            prompt, _ = self.request_fixture(p)
            (p / "raw/sample-attempt-1.stderr.txt").unlink()
            with self.assertRaisesRegex(ValueError, "Missing raw evidence"):
                MODES.audit_request(p, "sample", prompt)

    def test_completed_malformed_transport_is_not_resampled(self):
        stdout = '\n'.join(json.dumps(e) for e in [
            {"type": "item.completed", "item": {"type": "agent_message", "text": "not JSON"}},
            {"type": "turn.completed", "usage": {}}])
        proc = type("Process", (), {"returncode": 0, "stdout": stdout, "stderr": ""})()
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            (p / "raw").mkdir()
            with patch.object(MODES.base, "cli_args", return_value=["codex", "-"]), \
                    patch.object(MODES.subprocess, "run", return_value=proc) as call:
                result = MODES.call_model(p, "malformed", "prompt", {"model": "example", "reasoning_effort": "medium"}, [], None)
            self.assertEqual(call.call_count, 1)
            self.assertEqual(result["output"], "not JSON")
            with self.assertRaises(json.JSONDecodeError):
                json.loads(result["output"])

    def test_completed_answer_with_forbidden_tool_is_not_resampled(self):
        stdout = '\n'.join(json.dumps(e) for e in [
            {"type": "item.completed", "item": {"type": "command_execution"}},
            {"type": "item.completed", "item": {"type": "agent_message", "text": "answer"}},
            {"type": "turn.completed", "usage": {}}])
        proc = type("Process", (), {"returncode": 0, "stdout": stdout, "stderr": ""})()
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            (p / "raw").mkdir()
            with patch.object(MODES.base, "cli_args", return_value=["codex", "-"]), \
                    patch.object(MODES.subprocess, "run", return_value=proc) as call:
                result = MODES.call_model(p, "tool", "prompt", {"model": "example", "reasoning_effort": "medium"}, [], None)
            self.assertEqual(call.call_count, 1)
            self.assertIn("Unexpected tool activity", result["error"])

    def test_percentages_count_answers_not_review_ratings(self):
        cases, answers, ratings = [], {}, {}
        for language in MODES.locales():
            for i in range(100):
                case = dict(self.case, id=f"{language}-{i}", benchmark_language=language)
                cases.append(case)
                for condition in MODES.CONDITIONS:
                    answers[(case["id"], condition)] = "The buyer may cancel."
                    for reviewer in (1, 2):
                        ratings[(case["id"], condition, reviewer)] = rating("A")
        # One conservative flag in English/full, recorded by one reviewer only.
        ratings[("en-0", "full", 1)]["checks"][0].update(status="changed", evidence="Requirement changed.")
        fake_evidence = ({"study_id": "test", "languages": MODES.locales(), "mode_tests": 3600}, cases, answers, ratings, 1260)
        with patch.object(MODES, "evidence", return_value=fake_evidence), \
                patch.object(MODES, "calibration_summary", return_value={"results": []}):
            _, rows, summary, _, _ = MODES.result_data(Path("unused"))
        self.assertEqual(len(rows), 900)
        self.assertEqual(summary["candidate_ratings"], 9000)
        self.assertEqual(summary["totals"]["en"]["full"]["tested"], 100)
        self.assertEqual(summary["totals"]["en"]["full"]["pass_percent"], 99)
        self.assertEqual(summary["totals"]["all"]["full"]["tested"], 900)
        self.assertEqual(summary["totals"]["all"]["full"]["pass_percent"], 99.89)
        self.assertEqual(summary["totals"]["all"]["baseline"]["pass_percent"], 100)
        self.assertEqual(summary["totals"]["all"]["full"]["lost_passes_vs_baseline"], 1)

    def test_equivalent_json_numbers_pass_but_bool_and_string_do_not(self):
        case = dict(self.case, json_keys=["count"], json_expected={"count": 60})
        for answer in ('{"count":60}', '{"count":60.0}', '{"count":6e1}'):
            with self.subTest(answer=answer):
                self.assertTrue(MODES.summarize(case, answer, [rating("A")])["confirmed_pass"])
        for answer in ('{"count":true}', '{"count":"60"}', '{"count":60.00000000000000001}'):
            with self.subTest(answer=answer):
                self.assertFalse(MODES.summarize(case, answer, [rating("A")])["confirmed_pass"])

    def test_nonstandard_json_constants_are_rejected(self):
        case = dict(self.case, json_keys=["count"])
        for answer in ('{"count":NaN}', '{"count":Infinity}', '{"count":-Infinity}'):
            with self.subTest(answer=answer):
                self.assertFalse(MODES.summarize(case, answer, [rating("A")])["confirmed_pass"])


if __name__ == "__main__":
    unittest.main()
