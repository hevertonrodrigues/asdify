import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import audit_mode_source as audit


class SourceAuditIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.output = Path(self.temporary.name)
        self.destination = self.output / "source-audit"
        self.destination.mkdir()
        self.identifiers = ["case-one", "case-two"]
        self.conditions = ["baseline", "lite", "full", "ultra", "off"]
        self.mapping = dict(zip(sorted(audit.LABELS), self.conditions))
        self.key = self.output / "private-key.json"
        self.write(self.key, {"cases": {identifier: self.mapping for identifier in self.identifiers}})
        self.write(self.output / "summary.json", {"generated_answers": 10, "candidate_ratings": 20})
        self.write(self.output / "source-audit-plan.json",
                   {"random_case_ids": {"en": [self.identifiers[0]]},
                    "selection_rule": "Union the seeded random sample with all flagged cases."})
        (self.output / "source-audit-instructions.md").write_text("Review only source tasks and opaque answers.\n")
        cases = [{"id": identifier, "benchmark_language": "en", "task": "Source " + identifier}
                 for identifier in self.identifiers]
        self.write_lines(self.output / "cases.jsonl", cases)
        results = [{"case_id": identifier,
                    **{condition: {"confirmed_pass": not (identifier == "case-two" and condition == "full")}
                       for condition in self.conditions}} for identifier in self.identifiers]
        self.write(self.output / "case-results.json", results)
        for condition in self.conditions:
            value = {"answers": [{"case_id": identifier, "text": identifier + " " + condition}
                                  for identifier in self.identifiers]}
            self.write(self.output / f"generate-{condition}-en-001-request.json", {"output": json.dumps(value)})
        sources = [{"case_id": identifier, "output_language": "en", "source_task": "Source " + identifier,
                    "candidates": [{"label": label, "answer": identifier + " " + condition}
                                   for label, condition in self.mapping.items()]} for identifier in self.identifiers]
        self.write_lines(self.destination / "inputs-en.jsonl", sources)
        self.annotations = [{"case_id": identifier,
                             "candidates": [{"label": label, "meaning": "preserved", "voice": "not_applicable",
                                             "format": "not_applicable", "reason": "Source fact is retained."}
                                            for label in sorted(audit.LABELS)]} for identifier in self.identifiers]
        self.annotation_path = self.destination / "annotations-en.jsonl"
        self.write_lines(self.annotation_path, self.annotations)
        manifest = {
            "primary_summary_sha256": audit.sha(self.output / "summary.json"),
            "primary_case_results_sha256": audit.sha(self.output / "case-results.json"),
            "selection_plan_sha256": audit.sha(self.output / "source-audit-plan.json"),
            "audit_instructions_sha256": audit.sha(self.output / "source-audit-instructions.md"),
            "opaque_label_key_sha256": audit.sha(self.key),
            "random_case_ids": ["case-one"], "strict_flagged_case_ids": ["case-two"],
            "selected_case_ids": self.identifiers, "selected_cases_per_language": {"en": 2},
            "selected_cases": 2, "selected_answers": 10,
            "blinded_input_sha256": {"inputs-en.jsonl": audit.sha(self.destination / "inputs-en.jsonl")},
        }
        self.write(self.destination / "selection-manifest.json", manifest)

    @staticmethod
    def write(path, value):
        path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")

    @staticmethod
    def write_lines(path, rows):
        path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows))

    def test_complete_seal_is_auditable_and_cannot_be_replaced(self):
        result = audit.seal(self.output, self.key)
        self.assertEqual((result["selected_cases"], result["candidate_annotations"]), (2, 10))
        self.assertEqual(audit.audit(self.output), result)
        self.assertEqual((self.destination / audit.KEY).read_bytes(), self.key.read_bytes())
        with self.assertRaisesRegex(ValueError, "already sealed"):
            audit.seal(self.output, self.key)

    def test_incomplete_annotations_do_not_release_key(self):
        self.write_lines(self.annotation_path, self.annotations[:1])
        with self.assertRaisesRegex(ValueError, "Incomplete annotation case"):
            audit.seal(self.output, self.key)
        self.assertFalse((self.destination / audit.KEY).exists())

    def test_duplicate_or_unknown_labels_are_rejected(self):
        for label in ("Q", "Z"):
            with self.subTest(label=label):
                rows = copy.deepcopy(self.annotations)
                rows[0]["candidates"][-1]["label"] = label
                self.write_lines(self.annotation_path, rows)
                with self.assertRaisesRegex(ValueError, "Unknown or duplicate annotated candidate"):
                    audit.verify(self.output, self.key)

    def test_invalid_verdict_and_missing_reason_are_rejected(self):
        for field, value in (("meaning", "not_applicable"), ("format", True), ("reason", " ")):
            with self.subTest(field=field):
                rows = copy.deepcopy(self.annotations)
                rows[0]["candidates"][0][field] = value
                self.write_lines(self.annotation_path, rows)
                with self.assertRaises(ValueError):
                    audit.verify(self.output, self.key)

    def test_key_must_match_manifest_and_be_bijective(self):
        value = audit.read(self.key)
        value["cases"]["case-one"]["R"] = "baseline"
        self.write(self.key, value)
        with self.assertRaisesRegex(ValueError, "Changed opaque-label key"):
            audit.verify(self.output, self.key)
        manifest_path = self.destination / "selection-manifest.json"
        manifest = audit.read(manifest_path)
        manifest["opaque_label_key_sha256"] = audit.sha(self.key)
        self.write(manifest_path, manifest)
        with self.assertRaisesRegex(ValueError, "Invalid opaque mapping"):
            audit.verify(self.output, self.key)

    def test_blinded_answer_must_match_original_output_even_if_rehashed(self):
        path = self.destination / "inputs-en.jsonl"
        rows = audit.lines(path)
        rows[0]["candidates"][0]["answer"] = "Substituted answer"
        self.write_lines(path, rows)
        manifest_path = self.destination / "selection-manifest.json"
        manifest = audit.read(manifest_path)
        manifest["blinded_input_sha256"][path.name] = audit.sha(path)
        self.write(manifest_path, manifest)
        with self.assertRaisesRegex(ValueError, "Opaque answer differs"):
            audit.verify(self.output, self.key)

    def test_random_union_all_flagged_selection_is_required(self):
        path = self.destination / "selection-manifest.json"
        manifest = audit.read(path)
        manifest["strict_flagged_case_ids"] = []
        self.write(path, manifest)
        with self.assertRaisesRegex(ValueError, "Changed selection"):
            audit.verify(self.output, self.key)

    def test_annotation_changes_after_seal_are_detected(self):
        audit.seal(self.output, self.key)
        rows = copy.deepcopy(self.annotations)
        rows[0]["candidates"][0]["reason"] = "Edited judgment after unblinding"
        self.write_lines(self.annotation_path, rows)
        with self.assertRaisesRegex(ValueError, "Sealed source-audit evidence changed"):
            audit.audit(self.output)

    def test_complete_case_audit_cannot_exclude_unflagged_cases(self):
        self.write(self.output / "source-audit-plan.json",
                   {"selection_kind": "all_frozen_cases", "random_case_ids": {"en": []}})
        path = self.destination / "selection-manifest.json"
        manifest = audit.read(path)
        manifest["selection_plan_sha256"] = audit.sha(self.output / "source-audit-plan.json")
        manifest["random_case_ids"] = []
        self.write(path, manifest)
        self.assertEqual(audit.verify(self.output, self.key)["selected_cases"], 2)
        manifest["selected_case_ids"] = ["case-two"]
        self.write(path, manifest)
        with self.assertRaisesRegex(ValueError, "Changed selection"):
            audit.verify(self.output, self.key)

    def test_unknown_selection_policy_is_rejected(self):
        self.write(self.output / "source-audit-plan.json",
                   {"selection_kind": "cherry-pick", "random_case_ids": {"en": ["case-one"]}})
        path = self.destination / "selection-manifest.json"
        manifest = audit.read(path)
        manifest["selection_plan_sha256"] = audit.sha(self.output / "source-audit-plan.json")
        self.write(path, manifest)
        with self.assertRaisesRegex(ValueError, "Unknown source-audit selection rule"):
            audit.verify(self.output, self.key)


if __name__ == "__main__":
    unittest.main()
