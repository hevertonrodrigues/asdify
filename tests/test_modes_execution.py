"""Execution regressions for the multilingual runner; never calls a live model."""
import concurrent.futures
import contextlib
import importlib.util
import io
import json
import sys
import tempfile
import threading
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
with patch.object(sys, "path", [str(ROOT / "scripts"), *sys.path]):
    SPEC = importlib.util.spec_from_file_location("modes_execution", ROOT / "scripts/evaluate_modes.py")
    MODES = importlib.util.module_from_spec(SPEC)
    SPEC.loader.exec_module(MODES)


def event_stream(answer="candidate", *, forbidden=False, separators=None):
    events = []
    if forbidden:
        events.append({"type": "item.completed", "item": {"type": "command_execution"}})
    events.extend([
        {"type": "item.completed", "item": {"type": "agent_message", "text": answer}},
        {"type": "turn.completed", "usage": {"input_tokens": 12, "output_tokens": 4}},
    ])
    return "".join(json.dumps(event, separators=separators) + "\n" for event in events)


def process(stdout, returncode=0):
    return SimpleNamespace(stdout=stdout, stderr="", returncode=returncode)


def metadata(languages, cases_per_language=100):
    count = len(languages) * cases_per_language
    return {
        "study_id": "mock-study", "model": "mock-model", "reasoning_effort": "medium",
        "review_reasoning_effort": "medium", "model_catalog_sha256": None,
        "languages": list(languages), "conditions": list(MODES.CONDITIONS),
        "case_count": count, "mode_tests": count * 4, "baseline_answers": count,
        "generated_answers": count * 5, "candidate_ratings": count * 10,
        "held_out_from_skill_development": True, "limitations": [],
    }


class ModesExecutionTests(unittest.TestCase):
    def temporary_study(self):
        temporary = tempfile.TemporaryDirectory(prefix="asdify-execution-test-")
        self.addCleanup(temporary.cleanup)
        output = Path(temporary.name)
        (output / "raw").mkdir()
        return output

    def batch(self):
        return [{"id": f"modes-fr-{i:03d}", "benchmark_language": "fr", "lang": "fr",
                 "category": "permission", "task": "Réécris : le prêt est facultatif.",
                 "invariants": ["Borrowing is optional.", "No obligation is introduced.",
                                "No unsupported fee is introduced."]}
                for i in range(1, 6)]

    def attempt(self, output, identifier, number, stdout, *, error=None, exit_code=0):
        (output / "raw").mkdir(exist_ok=True)
        (output / "raw" / f"{identifier}-attempt-{number}.events.jsonl").write_text(stdout)
        (output / "raw" / f"{identifier}-attempt-{number}.stderr.txt").write_text("")
        record = {"attempt": number, "error": error, "exit_code": exit_code,
                  "seconds": 0.01, "completed_at_utc": MODES.base.now()}
        if error is None:
            answer, usage = MODES.base.parse_events(stdout)
            record.update(output=answer, usage=usage)
        return record

    def request(self, output, identifier, prompt, answer="candidate", *, earlier=None):
        """Create raw/claim evidence; the caller decides when to persist the request."""
        claims = output / ".requests"
        claims.mkdir(exist_ok=True)
        MODES.base.write_json(claims / f"{identifier}.json", {
            "prompt_sha256": MODES.base.sha(prompt.encode()), "started_at_utc": MODES.base.now(),
        })
        attempts = []
        if earlier is not None:
            stdout, error, exit_code = earlier
            attempts.append(self.attempt(output, identifier, 1, stdout, error=error, exit_code=exit_code))
        successful = self.attempt(output, identifier, len(attempts) + 1, event_stream(answer))
        attempts.append(successful)
        return {"prompt_sha256": MODES.base.sha(prompt.encode()), "attempts": attempts,
                "output": successful["output"], "usage": successful["usage"]}

    def save_request(self, output, identifier, request):
        MODES.base.write_json(output / f"{identifier}-request.json", request)

    def test_concurrent_request_owner_is_rejected_before_another_cli_call(self):
        output = self.temporary_study()
        started, release = threading.Event(), threading.Event()
        calls_lock = threading.Lock()
        calls = []

        def cli(*args, **kwargs):
            with calls_lock:
                calls.append(kwargs["input"])
                number = len(calls)
            if number == 1:
                started.set()
                if not release.wait(3):
                    raise RuntimeError("Test owner was not released")
                return process(event_stream("owner candidate"))
            return process(event_stream("overlapping candidate"))

        def invoke():
            return MODES.call_model(output, "same-request", "source", metadata(["fr"]), [], None)

        with patch.object(MODES.base, "cli_args", return_value=["mock-cli"]), \
                patch.object(MODES.subprocess, "run", side_effect=cli), \
                concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            first = pool.submit(invoke)
            try:
                self.assertTrue(started.wait(3))
                # Raw files do not yet exist; the exclusive claim must guard this interval.
                self.assertEqual(list((output / "raw").iterdir()), [])
                second = pool.submit(invoke)
                with self.assertRaisesRegex(ValueError, "claimed|overlap|owner"):
                    second.result(timeout=3)
                self.assertEqual(len(calls), 1)
            finally:
                release.set()
            result = first.result(timeout=3)
        self.assertEqual(result["output"], "owner candidate")
        self.assertEqual(len(result["attempts"]), 1)
        self.assertEqual(len(list((output / "raw").iterdir())), 2)
        claim = json.loads((output / ".requests/same-request.json").read_text())
        self.assertEqual(claim["prompt_sha256"], MODES.base.sha(b"source"))

    def test_run_and_calibration_share_exclusive_process_ownership(self):
        output = self.temporary_study()
        started, release = threading.Event(), threading.Event()

        def verify(*args):
            started.set()
            if not release.wait(3):
                raise RuntimeError("Test process was not released")
            raise ValueError("Synthetic invalid frozen study")

        with patch.object(MODES, "verify_frozen", side_effect=verify) as verification, \
                patch.object(MODES, "call_model") as model, \
                concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
            owner = pool.submit(MODES.run, output, 1, None, 1)
            try:
                self.assertTrue(started.wait(3))
                with self.assertRaisesRegex(ValueError, "owns|overlap"):
                    MODES.calibrate(output, None, 1)
                self.assertEqual(verification.call_count, 1)
                model.assert_not_called()
            finally:
                release.set()
            with self.assertRaisesRegex(ValueError, "Synthetic invalid"):
                owner.result(timeout=3)
        self.assertFalse((output / ".execution.lock").exists())

    def test_completed_invalid_answers_are_not_retried_for_alternate_json_spacing(self):
        streams = [event_stream(forbidden=True, separators=(",", " : ")),
                   event_stream(forbidden=True, separators=(", ", "\t:\t")),
                   "malformed transport prefix\n" + event_stream(separators=(",", " : "))]
        for stdout in streams:
            with self.subTest(stdout=stdout):
                output = self.temporary_study()
                with patch.object(MODES.base, "cli_args", return_value=["mock-cli"]), \
                        patch.object(MODES.subprocess, "run", return_value=process(stdout)) as cli:
                    result = MODES.call_model(output, "completed", "source", metadata(["fr"]), [], None)
                self.assertEqual(cli.call_count, 1)
                self.assertIn("error", result)
                self.assertEqual(len(result["attempts"]), 1)
                self.assertEqual((output / "raw/completed-attempt-1.events.jsonl").read_text(), stdout)
                self.assertFalse((output / "raw/completed-attempt-2.events.jsonl").exists())

    def test_completed_turn_is_not_retried_even_with_nonzero_cli_exit(self):
        output = self.temporary_study()
        stdout = event_stream(separators=(",", " : "))
        with patch.object(MODES.base, "cli_args", return_value=["mock-cli"]), \
                patch.object(MODES.subprocess, "run", return_value=process(stdout, returncode=1)) as cli:
            result = MODES.call_model(output, "exit-error", "source", metadata(["fr"]), [], None)
        self.assertEqual(cli.call_count, 1)
        self.assertIn("error", result)
        self.assertEqual(result["attempts"][0]["exit_code"], 1)

    def test_incomplete_infrastructure_attempt_can_retry_once_with_both_attempts_retained(self):
        output = self.temporary_study()
        with patch.object(MODES.base, "cli_args", return_value=["mock-cli"]), \
                patch.object(MODES.subprocess, "run", side_effect=[
                    process('{"type":"turn.failed"}\n', returncode=1),
                    process(event_stream("completed retry")),
                ]) as cli:
            result = MODES.call_model(output, "retry", "source", metadata(["fr"]), [], None)
        self.assertEqual(cli.call_count, 2)
        self.assertEqual(result["output"], "completed retry")
        self.assertEqual([record["attempt"] for record in result["attempts"]], [1, 2])
        self.assertIsNotNone(result["attempts"][0]["error"])
        self.assertIsNone(result["attempts"][1]["error"])
        self.assertEqual(len(list((output / "raw").iterdir())), 4)

    def test_audit_rejects_completed_earlier_attempt_marked_as_failed(self):
        output = self.temporary_study()
        prompt = "source"
        earlier = (event_stream("first candidate", forbidden=True, separators=(",", " : ")),
                   "Unexpected tool activity", 0)
        request = self.request(output, "sample", prompt, "second candidate", earlier=earlier)
        self.save_request(output, "sample", request)
        with self.assertRaisesRegex(ValueError, "earlier|resampled"):
            MODES.audit_request(output, "sample", prompt)

    def test_audit_accepts_infrastructure_retry_without_an_earlier_completed_turn(self):
        output = self.temporary_study()
        prompt = "source"
        request = self.request(output, "sample", prompt, earlier=(
            '{"type":"turn.failed"}\n', "CLI exit 1", 1,
        ))
        self.save_request(output, "sample", request)
        self.assertEqual(MODES.audit_request(output, "sample", prompt), request)
        MODES.validate_inventory(output, {"sample"})

    def test_inventory_rejects_orphan_raw_files_and_unknown_claims(self):
        extras = ("raw/orphan-attempt-1.events.jsonl", "raw/nested/orphan.events.jsonl",
                  ".requests/orphan.json", "orphan-request.json")
        for extra in extras:
            with self.subTest(extra=extra):
                output = self.temporary_study()
                request = self.request(output, "sample", "source")
                self.save_request(output, "sample", request)
                MODES.validate_inventory(output, {"sample"})
                path = output / extra
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("orphan evidence")
                with self.assertRaisesRegex(ValueError, "inventory|claim"):
                    MODES.validate_inventory(output, {"sample"})

    def test_worker_exception_still_records_every_started_peer_result(self):
        output = self.temporary_study()
        cases = self.batch()
        all_started = threading.Barrier(len(MODES.CONDITIONS))
        release_peers = threading.Event()
        original_result = concurrent.futures.Future.result

        def observed_result(future, *args, **kwargs):
            try:
                return original_result(future, *args, **kwargs)
            except OSError:
                # Peers cannot finish until the failed future is consumed.
                release_peers.set()
                raise

        def worker(folder, identifier, prompt, *args, **kwargs):
            all_started.wait(timeout=3)
            if identifier.startswith("generate-baseline-"):
                raise OSError("Synthetic worker failure")
            if not release_peers.wait(3):
                raise RuntimeError("Failed future was never consumed")
            answer = json.dumps({"answers": [{"case_id": case["id"], "text": "Le prêt est facultatif."}
                                              for case in cases]})
            return self.request(folder, identifier, prompt, answer)

        with patch.object(MODES, "verify_frozen", return_value=(metadata(["fr"], len(cases)), cases)), \
                patch.object(MODES.base, "disabled_skills", return_value=[]), \
                patch.object(MODES, "generation_prompt", side_effect=lambda rows, mode, folder: mode + " source"), \
                patch.object(MODES, "call_model", side_effect=worker), \
                patch.object(concurrent.futures.Future, "result", observed_result), \
                contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaisesRegex(ValueError, "failed validation"):
                MODES.run(output, len(MODES.CONDITIONS), None, 1)
        for condition in MODES.CONDITIONS[1:]:
            identifier = f"generate-{condition}-fr-001"
            request = json.loads((output / f"{identifier}-request.json").read_text())
            self.assertNotIn("error", request)
            self.assertEqual(len(MODES.validate_answers(json.loads(request["output"]), cases)), len(cases))
            MODES.audit_request(output, identifier, condition + " source")
        failure = json.loads((output / "generate-baseline-fr-001-request.json").read_text())
        self.assertIn("Synthetic worker failure", failure["error"])
        self.assertEqual(len(json.loads((output / "execution-errors.json").read_text())), 1)
        self.assertFalse((output / ".execution.lock").exists())

    def test_resume_validation_blocks_new_calls_when_a_retained_review_failed(self):
        output = self.temporary_study()
        cases = self.batch()
        self.save_request(output, "review-1-fr-001", {
            "prompt_sha256": MODES.base.sha(b"review source"), "attempts": [],
            "error": "Retained review failure",
        })
        with patch.object(MODES, "verify_frozen", return_value=(metadata(["fr"], len(cases)), cases)), \
                patch.object(MODES.base, "disabled_skills", return_value=[]), \
                patch.object(MODES, "call_model") as model:
            with self.assertRaisesRegex(ValueError, "Retained.*review failure"):
                MODES.run(output, 2, None, 1)
            model.assert_not_called()
        self.assertFalse((output / ".execution.lock").exists())

    def test_percentage_point_delta_uses_paired_counts_for_subset_design(self):
        design = metadata(["fr", "de", "it"])
        count = design["case_count"]
        for baseline_passed, full_passed, gained, lost, delta in ((1, 2, 1, 0, "+0.33"),
                                                                (2, 1, 0, 1, "-0.33")):
            with self.subTest(gained=gained, lost=lost):
                totals = {}
                for condition in MODES.CONDITIONS:
                    passed = full_passed if condition == "full" else baseline_passed
                    totals[condition] = {"tested": count, "passed": passed,
                                         "pass_percent": round(100 * passed / count, 2)}
                    if condition != "baseline":
                        totals[condition].update(
                            gained_passes_vs_baseline=gained if condition == "full" else 0,
                            lost_passes_vs_baseline=lost if condition == "full" else 0,
                        )
                summary = {"totals": {"all": totals}, "grader_calibration": {
                    "positive_controls_passed": 50, "negative_controls_detected": 50,
                }}
                report = MODES.report_text(design, summary)
                self.assertIn(f"| full | {gained} | {lost} | {delta} |", report)
                self.assertIn(f"All ({count} per condition)", report)
                self.assertIn(f"{count} distinct cases", report)


if __name__ == "__main__":
    unittest.main()
