"""Conservative processing regressions using synthetic evidence and mocked CLI."""
import contextlib
import copy
import importlib.util
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("conservative_processor", ROOT / "scripts/evaluate_modes_conservative.py")
WRAPPER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(WRAPPER)


def events(answer):
    return "\n".join(json.dumps(event) for event in [
        {"type": "item.completed", "item": {"type": "agent_message", "text": answer}},
        {"type": "turn.completed", "usage": {"input_tokens": 10, "output_tokens": 5}},
    ]) + "\n"


class ConservativeProcessingTests(unittest.TestCase):
    def setUp(self):
        self.processor = WRAPPER.Processor()
        self.module = self.processor.module
        self.case = {"id": "modes-en-001", "benchmark_language": "en", "lang": "en",
                     "category": "permission", "task": "Rewrite: You may borrow a cup for free; borrowing is optional.",
                     "invariants": ["Borrowing is permitted.", "Borrowing is optional.", "No fee applies."]}

    def rating(self, label="A", ids=(1, 2, 3)):
        value = {"candidate": label,
                 "checks": [{"invariant_id": identifier, "status": "preserved", "evidence": "may borrow for free"}
                            for identifier in ids],
                 "hard_fail": False, "format_pass": True, "language_pass": True,
                 "unsupported_claims": [], "reason": "Permission and free optional borrowing are preserved."}
        value.update({dimension: 5 for dimension in self.module.base.DIMENSIONS})
        return value

    def review(self, cases=None, *, malformed=False):
        cases = cases or [self.case]
        rows = [{"case_id": case["id"], "ratings": [self.rating(label) for label in self.module.LABELS]}
                for case in cases]
        if malformed:
            for rating in rows[0]["ratings"][:4]:
                rating["checks"].append(copy.deepcopy(rating["checks"][-1]))
        return {"cases": rows}

    def record(self, output, identifier, prompt, answer):
        for directory in ("raw", ".requests"):
            (output / directory).mkdir(exist_ok=True)
        digest = WRAPPER.sha(prompt.encode())
        self.module.base.write_json(output / ".requests" / f"{identifier}.json", {
            "prompt_sha256": digest, "started_at_utc": self.module.base.now(),
        })
        (output / "raw" / f"{identifier}-attempt-1.events.jsonl").write_text(events(answer))
        (output / "raw" / f"{identifier}-attempt-1.stderr.txt").write_text("")
        _, usage = self.module.base.parse_events(events(answer))
        request = {"prompt_sha256": digest, "output": answer, "usage": usage,
                   "attempts": [{"attempt": 1, "exit_code": 0, "error": None,
                                 "output": answer, "usage": usage, "seconds": 0.01}]}
        self.module.base.write_json(output / f"{identifier}-request.json", request)

    def study(self):
        temporary = tempfile.TemporaryDirectory(prefix="asdify-conservative-test-")
        self.addCleanup(temporary.cleanup)
        output = Path(temporary.name)
        cases = [dict(self.case, id=f"modes-en-{index:03d}") for index in range(1, 6)]
        shutil.copytree(ROOT / "skills/asdify", output / "skill")
        (output / "cases.jsonl").write_text("".join(json.dumps(case) + "\n" for case in cases))
        self.module.base.write_json(output / "review-schema.json", self.module.review_schema())
        controls = [dict(self.case, id=f"control-{index}", good="You may borrow for free.",
                         bad="You must borrow for a fee.") for index in range(10)]
        self.module.base.write_json(output / "calibration-controls.json", controls)
        frozen = {str(path.relative_to(output)): WRAPPER.sha(path.read_bytes())
                  for path in output.rglob("*") if path.is_file()}
        count = len(cases)
        metadata = {"study_id": "synthetic", "runner_sha256": WRAPPER.sha(WRAPPER.RUNNER.read_bytes()),
                    "helper_sha256": WRAPPER.sha(WRAPPER.RUNNER.with_name("evaluate_skill.py").read_bytes()),
                    "frozen_file_sha256": frozen, "model_catalog_sha256": None,
                    "model": "mock-model", "reasoning_effort": "medium", "review_reasoning_effort": "low",
                    "languages": ["en"], "conditions": list(self.module.CONDITIONS), "case_count": count,
                    "mode_tests": count * 4, "baseline_answers": count, "generated_answers": count * 5,
                    "candidate_ratings": count * 10, "limitations": [], "held_out_from_skill_development": True}
        self.module.base.write_json(output / "metadata.json", metadata)
        verification = patch.object(self.module, "verify_frozen", return_value=(metadata, cases))
        verification.start()
        self.addCleanup(verification.stop)
        answers = {}
        for condition in self.module.CONDITIONS:
            value = {"answers": [{"case_id": case["id"], "text": "You may borrow a cup for free; borrowing is optional."}
                                 for case in cases]}
            answer = json.dumps(value)
            prompt = self.module.generation_prompt(cases, condition, output / "skill")
            self.record(output, f"generate-{condition}-en-001", prompt, answer)
            answers.update({(case["id"], condition): row["text"] for case, row in zip(cases, value["answers"])})
        prompt = self.module.review_prompt(cases, answers, 1)
        self.record(output, "review-1-en-001", prompt, json.dumps(self.review(cases, malformed=True)))
        calibration = output / "calibration"
        calibration.mkdir()
        _, calibration_answers, _ = self.module.calibration_data(output)
        for reviewer in (1, 2):
            for start in (0, 5):
                batch = controls[start:start + 5]
                prompt = self.module.review_prompt(batch, calibration_answers, reviewer)
                self.record(calibration, f"calibration-{reviewer}-{start + 1:03d}", prompt, json.dumps(self.review(batch)))
        self.module.base.write_json(calibration / "summary.json", self.module.calibration_summary(output, audited=True))
        (output / "execution.json").write_text('{"workers":4,"timeout_seconds":600,"model_catalog_sha256":null}\n')
        (output / "execution-errors.json").write_text('[ {"request":"review-1-en-001", "error":"Incomplete or duplicate invariant checks"} ]\n')
        with contextlib.redirect_stdout(io.StringIO()):
            amendment = self.processor.amend(output)
        return output, cases, metadata, amendment

    def reseal_test_amendment(self, output, amendment):
        """Used only to exercise semantic checks behind the byte-level seal."""
        self.module.base.write_json(output / WRAPPER.AMENDMENT, amendment)
        (output / WRAPPER.SEAL).write_text(WRAPPER.sha((output / WRAPPER.AMENDMENT).read_bytes()) + "\n")

    def complete_reviews(self, output, cases):
        stdout = events(json.dumps(self.review(cases)))
        result = SimpleNamespace(stdout=stdout, stderr="", returncode=0)
        with patch.object(self.module.base, "disabled_skills", return_value=[]), \
                patch.object(self.module.base, "cli_args", return_value=["mock-cli"]) as arguments, \
                patch.object(self.module.subprocess, "run", return_value=result) as cli, \
                patch.object(self.module, "call_model", wraps=self.module.call_model) as calls, \
                contextlib.redirect_stdout(io.StringIO()):
            history = self.processor.run(output, workers=2)
        return history, arguments, cli, calls

    def test_missing_duplicate_extra_and_empty_check_coverage_cannot_pass(self):
        for ids in ((1, 3, 3), (1, 3), (1, 2, 3, 99), ()):
            with self.subTest(ids=ids):
                value = self.review()
                value["cases"][0]["ratings"][0] = self.rating(ids=ids)
                before = copy.deepcopy(value)
                rows = self.processor.validate_review(value, [self.case])
                ratings = rows[0]["ratings"]
                result = self.processor.summarize(self.case, "You may borrow for free.", [ratings[0], self.rating()])
                self.assertFalse(result["confirmed_pass"])
                self.assertTrue(result["uncertain"])
                self.assertFalse(result["hard_fail"])
                self.assertEqual(value, before)
                self.assertIs(rows[0], value["cases"][0])
                self.assertEqual(result["review_structural_errors"][0]["raw_rating"], before["cases"][0]["ratings"][0])

    def test_valid_rating_and_original_strict_scores_are_unchanged(self):
        value = self.review()
        before = copy.deepcopy(value)
        self.processor.validate_review(value, [self.case])
        ratings = [value["cases"][0]["ratings"][0], self.rating()]
        original = self.processor.original["summarize"](self.case, "You may borrow for free.", ratings)
        amended = self.processor.summarize(self.case, "You may borrow for free.", ratings)
        self.assertEqual(amended.pop("review_structural_errors"), [])
        self.assertEqual(amended, original)
        self.assertEqual(value, before)

    def test_raw_negatives_and_contradictory_verdicts_are_retained(self):
        for hard_fail, status in ((True, "preserved"), (False, "changed"), (False, "missing")):
            with self.subTest(hard_fail=hard_fail, status=status):
                rating = self.rating(ids=(1, 3, 3))
                rating["hard_fail"] = hard_fail
                rating["checks"][0]["status"] = status
                before = copy.deepcopy(rating)
                result = self.processor.summarize(self.case, "You must borrow.", [rating, self.rating()])
                self.assertTrue(result["hard_fail"])
                self.assertTrue(result["uncertain"])
                self.assertFalse(result["confirmed_pass"])
                self.assertEqual(rating, before)
                self.assertEqual(result["review_structural_errors"][0]["raw_rating"], before)
                if not hard_fail:
                    self.assertEqual(result["inconsistent_verdicts"], 1)

    def test_all_other_rating_field_types_and_values_remain_fatal(self):
        changes = [lambda r: r.update(checks="not an array"),
                   lambda r: r.update(hard_fail="false"), lambda r: r.update(format_pass=1),
                   lambda r: r.update(language_pass=None), lambda r: r.update(clarity=True),
                   lambda r: r.update(clarity=5.0), lambda r: r.update(clarity=6),
                   lambda r: r.update(unsupported_claims="none"), lambda r: r.update(unsupported_claims=[""]),
                   lambda r: r.update(reason=" "), lambda r: r.update(extra="unexpected"),
                   lambda r: r.pop("checks")]
        for field, values in {"invariant_id": [True, 1.0, "1", [], None],
                              "status": ["wrong", [], False], "evidence": ["", None, 17]}.items():
            for replacement in values:
                changes.append(lambda r, f=field, v=replacement: r["checks"][0].update({f: v}))
        for index, change in enumerate(changes):
            with self.subTest(change=index):
                value = self.review()
                change(value["cases"][0]["ratings"][0])
                with self.assertRaises(ValueError):
                    self.processor.validate_review(value, [self.case])

    def test_unknown_missing_duplicate_case_or_candidate_coverage_is_fatal(self):
        values = [{"cases": []}, {"cases": {}}, {"cases": [dict(self.review()["cases"][0], case_id="unknown")]},
                  {"cases": [dict(self.review()["cases"][0], case_id=[])]}]
        for labels in (("A", "B", "C", "D"), ("A", "B", "C", "D", "D"), ("A", "B", "C", "D", "F")):
            values.append({"cases": [{"case_id": self.case["id"], "ratings": [self.rating(label) for label in labels]}]})
        for value in values:
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.processor.validate_review(value, [self.case])
        second = dict(self.case, id="second")
        duplicated = {"cases": [copy.deepcopy(self.review()["cases"][0])] * 2}
        with self.assertRaises(ValueError):
            self.processor.validate_review(duplicated, [self.case, second])

    def test_private_processing_does_not_contaminate_normal_imports(self):
        with patch.object(sys, "path", [str(ROOT / "scripts"), *sys.path]):
            spec = importlib.util.spec_from_file_location("normal_modes_for_isolation", WRAPPER.RUNNER)
            normal = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(normal)
        original = {name: getattr(normal, name) for name in self.processor.original}
        helper = sys.modules["evaluate_skill"]
        another = WRAPPER.Processor()
        self.assertIs(sys.modules["evaluate_skill"], helper)
        self.assertIsNot(another.module.base, normal.base)
        for name, function in original.items():
            self.assertIs(getattr(normal, name), function)
        value = self.review(malformed=True)
        with self.assertRaises(ValueError):
            normal.validate_review(value, [self.case])
        another.validate_review(value, [self.case])

    def test_amendment_is_once_only_and_preserves_all_existing_evidence(self):
        output, _, _, amendment = self.study()
        manifest = amendment["prior_evidence_sha256"]
        for required in ("execution.json", "execution-errors.json", "metadata.json",
                         "review-1-en-001-request.json", "raw/review-1-en-001-attempt-1.events.jsonl",
                         ".requests/review-1-en-001.json", "calibration/summary.json"):
            self.assertIn(required, manifest)
        self.assertEqual(amendment["processing_policy"], WRAPPER.POLICY)
        self.assertIn("not preregistered", WRAPPER.POLICY["timing"])
        self.assertEqual(len(amendment["observed_strict_review_errors"]), 1)
        old = (output / WRAPPER.AMENDMENT).read_bytes()
        with self.assertRaisesRegex(ValueError, "already exists"):
            self.processor.amend(output)
        self.assertEqual((output / WRAPPER.AMENDMENT).read_bytes(), old)
        self.processor.verify_amendment(output)

    def test_evidence_and_processor_tampering_are_rejected(self):
        output, _, _, amendment = self.study()
        raw = output / "raw/review-1-en-001-attempt-1.events.jsonl"
        saved = raw.read_bytes()
        raw.write_bytes(saved + b"\n")
        with self.assertRaisesRegex(ValueError, "prior evidence changed"):
            self.processor.verify_amendment(output)
        raw.write_bytes(saved)
        amendment["processor_sha256"] = "0" * 64
        self.reseal_test_amendment(output, amendment)
        with self.assertRaisesRegex(ValueError, "processor changed"):
            self.processor.verify_amendment(output)

    def test_amendment_bytes_policy_and_manifest_tampering_are_rejected(self):
        output, _, _, amendment = self.study()
        path = output / WRAPPER.AMENDMENT
        original = path.read_bytes()
        path.write_bytes(original + b"\n")
        with self.assertRaisesRegex(ValueError, "seal changed"):
            self.processor.verify_amendment(output)
        path.write_bytes(original)
        altered = copy.deepcopy(amendment)
        altered["processing_policy"]["coverage"] = "Permit malformed ratings to pass."
        self.reseal_test_amendment(output, altered)
        with self.assertRaisesRegex(ValueError, "policy changed"):
            self.processor.verify_amendment(output)
        altered = copy.deepcopy(amendment)
        altered["prior_evidence_sha256"]["execution-errors.json"] = "0" * 64
        self.reseal_test_amendment(output, altered)
        with self.assertRaisesRegex(ValueError, "prior evidence changed"):
            self.processor.verify_amendment(output)

    def test_unsafe_manifest_paths_and_symlinks_are_rejected(self):
        output, _, _, amendment = self.study()
        for unsafe in ("../outside", "/etc/passwd", "raw/../../outside", "raw//file", "./metadata.json", "C:/outside", "raw\\outside"):
            with self.subTest(path=unsafe):
                altered = copy.deepcopy(amendment)
                altered["prior_evidence_sha256"][unsafe] = "0" * 64
                self.reseal_test_amendment(output, altered)
                with self.assertRaisesRegex(ValueError, "Unsafe manifest"):
                    self.processor.verify_amendment(output)
        self.reseal_test_amendment(output, amendment)
        (output / "linked").symlink_to(output / "metadata.json")
        altered = copy.deepcopy(amendment)
        altered["prior_evidence_sha256"]["linked"] = WRAPPER.sha((output / "metadata.json").read_bytes())
        self.reseal_test_amendment(output, altered)
        with self.assertRaisesRegex(ValueError, "Symlink"):
            self.processor.verify_amendment(output)

    def test_scheduler_requests_only_unstarted_reviews_and_preserves_the_first_stop(self):
        output, cases, metadata, amendment = self.study()
        originals = {name: (output / name).read_bytes() for name in amendment["prior_evidence_sha256"]}
        history, arguments, cli, calls = self.complete_reviews(output, cases)
        self.assertEqual(cli.call_count, 1)
        self.assertEqual(calls.call_count, 1)
        self.assertEqual(calls.call_args.args[1], "review-2-en-001")
        self.assertEqual(arguments.call_args.args[1:3], (metadata["model"], metadata["review_reasoning_effort"]))
        self.assertEqual(history["scheduled_reviews"], ["review-2-en-001"])
        self.assertEqual(history["retained_reviews"], 1)
        self.assertLessEqual(history["workers"], 4)
        for name, content in originals.items():
            self.assertEqual((output / name).read_bytes(), content, name)
        self.processor.verify_amendment(output)
        with patch.object(self.module, "call_model") as call, \
                patch.object(self.module.base, "disabled_skills", return_value=[]), \
                contextlib.redirect_stdout(io.StringIO()):
            self.processor.run(output)
            call.assert_not_called()

    def test_missing_generation_or_catalog_mismatch_stops_before_any_new_call(self):
        output, _, _, _ = self.study()
        with patch.object(self.module, "call_model") as call:
            (output / "catalog.json").write_text("{}")
            with self.assertRaisesRegex(ValueError, "Catalog"):
                self.processor.run(output, catalog=output / "catalog.json")
            call.assert_not_called()
            (output / "generate-full-en-001-request.json").unlink()
            with self.assertRaises(ValueError):
                self.processor.run(output)
            call.assert_not_called()

    def test_new_fatal_review_keeps_raw_response_and_original_error_record(self):
        output, cases, _, _ = self.study()
        old_error = (output / "execution-errors.json").read_bytes()
        invalid = self.review(cases)
        invalid["cases"][0]["ratings"][0]["clarity"] = "five"
        raw = events(json.dumps(invalid))
        with patch.object(self.module.base, "disabled_skills", return_value=[]), \
                patch.object(self.module.base, "cli_args", return_value=["mock-cli"]), \
                patch.object(self.module.subprocess, "run", return_value=SimpleNamespace(stdout=raw, stderr="", returncode=0)) as cli, \
                contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaisesRegex(ValueError, "processing stopped"):
                self.processor.run(output)
        self.assertEqual(cli.call_count, 1)
        self.assertEqual((output / "execution-errors.json").read_bytes(), old_error)
        self.assertEqual((output / "raw/review-2-en-001-attempt-1.events.jsonl").read_text(), raw)
        self.assertTrue((output / "review-2-en-001-request.json").exists())
        history = json.loads(next(output.glob("processing-execution-*.json")).read_text())
        self.assertEqual(history["status"], "failed")
        self.processor.verify_amendment(output)

    def test_new_malformed_coverage_is_saved_and_counted_without_resampling(self):
        output, cases, _, _ = self.study()
        raw = events(json.dumps(self.review(cases, malformed=True)))
        with patch.object(self.module.base, "disabled_skills", return_value=[]), \
                patch.object(self.module.base, "cli_args", return_value=["mock-cli"]), \
                patch.object(self.module.subprocess, "run", return_value=SimpleNamespace(stdout=raw, stderr="", returncode=0)) as cli, \
                contextlib.redirect_stdout(io.StringIO()):
            history = self.processor.run(output)
        self.assertEqual(cli.call_count, 1)
        self.assertEqual(history["status"], "finished")
        self.assertEqual((output / "raw/review-2-en-001-attempt-1.events.jsonl").read_text(), raw)
        _, rows, summary, _, _ = self.processor.result_data(output)
        self.assertEqual(summary["processing"]["structurally_invalid_ratings"], 8)
        self.assertEqual(summary["processing"]["affected_answers"], 4)
        for condition in self.module.CONDITIONS:
            errors = rows[0][condition]["review_structural_errors"]
            if errors:
                self.assertEqual([error["reviewer"] for error in errors], [1, 2])
                self.assertFalse(rows[0][condition]["confirmed_pass"])

    def test_summary_report_and_audit_expose_conservative_policy_and_counts(self):
        output, cases, _, _ = self.study()
        self.complete_reviews(output, cases)
        _, rows, summary, _, _ = self.processor.result_data(output)
        policy = summary["processing"]
        self.assertEqual(policy["structurally_invalid_ratings"], 4)
        self.assertEqual(policy["affected_answers"], 4)
        self.assertEqual(policy["affected_cases"], 1)
        self.assertEqual(policy["calibration_structurally_invalid_ratings"], 0)
        affected = [row[condition] for row in rows for condition in self.module.CONDITIONS
                    if row[condition]["review_structural_errors"]]
        self.assertTrue(all(row["uncertain"] and not row["confirmed_pass"] for row in affected))
        with contextlib.redirect_stdout(io.StringIO()):
            self.module.report(output)
            audit = self.processor.audit(output)
        self.assertEqual(audit["processing"]["affected_answers"], 4)
        self.assertEqual(audit["prior_evidence_preservation"], "verified")
        self.assertIn("not preregistered", (output / "report.md").read_text())
        self.assertIn("Structurally invalid ratings: 4", (output / "report.md").read_text())
        self.assertEqual(json.loads((output / "evidence-audit.json").read_text())["processing"], policy)


if __name__ == "__main__":
    unittest.main()
