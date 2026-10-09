"""Focused study integrity checks; no live model calls."""
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
with patch.object(sys, "path", [str(ROOT / "scripts"), *sys.path]):
    SPEC = importlib.util.spec_from_file_location("focused_modes", ROOT / "scripts/evaluate_modes_focused.py")
    FOCUSED = importlib.util.module_from_spec(SPEC)
    SPEC.loader.exec_module(FOCUSED)


class FocusedTests(unittest.TestCase):
    def plan(self, ids):
        return {"selected_case_ids": ids, "retention_rule": "Keep only demonstrated improvements.",
                "selection_description": "Previously examined development cases."}

    def freeze(self, adapter, output):
        # CI audits evidence without installing or calling the model CLI.
        with patch.object(adapter.module.subprocess, "check_output",
                          side_effect=["fixture-revision\n", "codex-cli fixture\n"]):
            adapter.freeze(output, ROOT / "benchmarks/multilingual-modes", None, "mock-model", "medium")

    def test_subset_is_exact_and_keeps_corpus_order(self):
        cases = [{"id": "a"}, {"id": "b"}, {"id": "c"}]
        self.assertEqual(FOCUSED.validate_plan(self.plan(["c", "a"]), cases), [cases[0], cases[2]])

    def test_bad_selections_and_missing_retention_rule_are_rejected(self):
        for ids in ([], ["a", "a"], ["missing"], [1]):
            with self.subTest(ids=ids), self.assertRaises(ValueError):
                FOCUSED.validate_plan(self.plan(ids), [{"id": "a"}])
        plan = self.plan(["a"])
        plan["retention_rule"] = ""
        with self.assertRaises(ValueError):
            FOCUSED.validate_plan(plan, [{"id": "a"}])

    def test_freeze_records_real_subset_sizes_and_rejects_evidence_changes(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "study"
            adapter = FOCUSED.Focused(self.plan(["modes-de-087", "modes-en-007"]))
            self.freeze(adapter, output)
            metadata, cases = adapter.verify_frozen(output)
            self.assertEqual(len(cases), 2)
            self.assertEqual(metadata["cases_per_language"], {"en": 1, "de": 1})
            self.assertEqual(metadata["generated_answers"], 10)
            self.assertFalse(metadata["held_out_from_skill_development"])
            (output / "focused-plan.json").write_text("{}")
            with self.assertRaises(ValueError):
                adapter.verify_frozen(output)

    def test_changed_adapter_or_processor_hash_cannot_resume(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "study"
            adapter = FOCUSED.Focused(self.plan(["modes-de-087"]))
            self.freeze(adapter, output)
            original = FOCUSED.read(output / "metadata.json")
            for field in ("focused_adapter_sha256", "coverage_processor_sha256"):
                metadata = dict(original, **{field: "0" * 64})
                (output / "metadata.json").write_text(json.dumps(metadata))
                with self.subTest(field=field), self.assertRaises(ValueError):
                    adapter.verify_frozen(output)

    def test_coverage_errors_are_prospectively_nonpassing_without_rewriting_checks(self):
        adapter = FOCUSED.Focused(self.plan(["a"]))
        checks = [{"invariant_id": 1, "status": "preserved", "evidence": "yes"},
                  {"invariant_id": 1, "status": "preserved", "evidence": "yes"}]
        rating = {"candidate": "A", "checks": checks}
        expected = {"uncertain": False, "confirmed_pass": True, "notes": []}
        with patch.dict(adapter.original, summarize=lambda *args: dict(expected, notes=[])):
            result = adapter.summarize({"invariants": ["one", "two"]}, "answer", [rating])
        self.assertFalse(result["confirmed_pass"])
        self.assertTrue(result["uncertain"])
        self.assertIs(result["review_structural_errors"][0]["raw_rating"], rating)
        self.assertEqual(checks[1]["invariant_id"], 1)

    def test_report_uses_actual_counts_and_development_disclosure(self):
        metadata = {"selection": "Two reused tasks.", "generated_answers": 10, "candidate_ratings": 20,
                    "model": "mock", "reasoning_effort": "medium", "languages": ["de"], "limitations": []}
        values = {mode: {"tested": 2, "pass_percent": 50.0} for mode in
                  ("baseline", "lite", "full", "ultra", "off")}
        report = FOCUSED.Focused.report_text(metadata, {"totals": {"de": values}})
        self.assertIn("| de | 2 |", report)
        self.assertIn("not new held-out tests", report)
        self.assertNotIn("(100)", report)

    def test_cli_rejects_excess_workers_before_reading_or_running_study(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/evaluate_modes_focused.py"),
                                 "run", "--output", "/path/that/does/not/exist", "--workers", "32"],
                                capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("one to four workers", result.stderr)


if __name__ == "__main__":
    unittest.main()
