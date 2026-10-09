"""Check preservation across the user-requested reduction in worker count.

Tests mutate temporary evidence copies. They never run a model or modify the
published studies, including the continuation while it is still running.
"""
import importlib.util
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
with patch.object(sys, "path", [str(ROOT / "scripts"), *sys.path]):
    SPEC = importlib.util.spec_from_file_location("execution_history", ROOT / "scripts/audit_execution_history.py")
    HISTORY = importlib.util.module_from_spec(SPEC)
    SPEC.loader.exec_module(HISTORY)

ORIGINAL = "2026-10-09-multilingual-modes"
CONTINUATION = "2026-10-09-multilingual-modes-four-workers"


class ExecutionHistoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary = tempfile.TemporaryDirectory(prefix="asdify-history-tests-")
        cls.root = Path(cls.temporary.name)
        destination = cls.root / "benchmarks/results"
        destination.mkdir(parents=True)
        cls.original = destination / ORIGINAL
        cls.output = destination / CONTINUATION
        shutil.copytree(ROOT / "benchmarks/results" / ORIGINAL, cls.original)
        cls.output.mkdir()
        live = ROOT / "benchmarks/results" / CONTINUATION
        metadata = HISTORY.read_json(live / "metadata.json")
        history = HISTORY.read_json(live / "execution-history.json")
        files = set(metadata["frozen_file_sha256"]) | {"metadata.json", "execution-history.json", "execution.json"}
        for identifier in history["carried_generation_requests"]:
            request = HISTORY.read_json(live / f"{identifier}-request.json")
            files.update(HISTORY.request_files(identifier, request))
        files.update(str(p.relative_to(live)) for p in (live / "calibration").rglob("*") if p.is_file())
        for relative in files:
            target = cls.output / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(live / relative, target)
        cls.retained = history["carried_generation_requests"][0]
        cls.interrupted = HISTORY.read_json(cls.original / "execution-errors.json")[0]["request"]

    @classmethod
    def tearDownClass(cls):
        cls.temporary.cleanup()

    def replace(self, path, value):
        before = path.read_bytes() if path.exists() else None

        def restore():
            if before is None:
                path.unlink(missing_ok=True)
            else:
                path.write_bytes(before)

        self.addCleanup(restore)
        path.write_bytes(value.encode() if isinstance(value, str) else value)

    def json_change(self, path, change):
        value = HISTORY.read_json(path)
        change(value)
        self.replace(path, json.dumps(value))

    def update_history_hash(self):
        digest = HISTORY.modes.base.sha((self.output / "execution-history.json").read_bytes())
        self.json_change(self.output / "metadata.json", lambda value: value.update(execution_history_sha256=digest))

    def test_all_returned_answers_and_original_interruption_are_preserved(self):
        result = HISTORY.audit(self.output, self.root)
        self.assertEqual(result["carried_generation_requests"], 37)
        self.assertEqual(result["carried_answers"], 185)
        self.assertEqual(result["interrupted_requests_without_returned_answers"], 32)
        self.assertEqual(result["continuation_live_workers"], 4)

    def test_omitting_a_successful_request_is_detected_even_with_updated_history_hash(self):
        self.json_change(self.output / "execution-history.json", lambda value: value["carried_generation_requests"].pop())
        self.update_history_hash()
        with self.assertRaisesRegex(ValueError, "every successful"):
            HISTORY.audit(self.output, self.root)

    def test_carried_raw_event_cannot_be_edited(self):
        path = self.output / "raw" / f"{self.retained}-attempt-1.events.jsonl"
        self.replace(path, path.read_text() + "\n")
        with self.assertRaisesRegex(ValueError, "Carried evidence differs"):
            HISTORY.audit(self.output, self.root)

    def test_completed_interrupted_turn_cannot_be_regenerated(self):
        path = self.original / "raw" / f"{self.interrupted}-attempt-1.events.jsonl"
        self.replace(path, '{"type":"turn.completed"}\n')
        with self.assertRaisesRegex(ValueError, "Completed interrupted answer"):
            HISTORY.audit(self.output, self.root)

    def test_returned_message_without_turn_completed_cannot_be_regenerated(self):
        path = self.original / "raw" / f"{self.interrupted}-attempt-1.events.jsonl"
        self.replace(path, json.dumps({"type": "item.completed", "item": {"type": "agent_message", "text": "Returned answer"}}) + "\n")
        with self.assertRaisesRegex(ValueError, "Returned interrupted answer"):
            HISTORY.audit(self.output, self.root)

    def test_original_orphan_raw_attempt_is_detected(self):
        self.replace(self.original / "raw/orphan-attempt-1.events.jsonl", "")
        with self.assertRaisesRegex(ValueError, "Unrecorded or missing original"):
            HISTORY.audit(self.output, self.root)

    def test_new_model_setting_cannot_be_hidden_in_continuation(self):
        self.json_change(self.output / "metadata.json", lambda value: value.update(model="different-model"))
        with self.assertRaisesRegex(ValueError, "metadata: model"):
            HISTORY.audit(self.output, self.root)

    def test_worker_record_matches_the_requested_reduction(self):
        self.json_change(self.output / "execution.json", lambda value: value.update(workers=8))
        with self.assertRaisesRegex(ValueError, "four-worker"):
            HISTORY.audit(self.output, self.root)

    def test_reused_calibration_cannot_be_changed(self):
        path = self.output / "calibration/raw/calibration-1-001-attempt-1.stderr.txt"
        self.replace(path, "Changed calibration attempt")
        with self.assertRaisesRegex(ValueError, "Carried evidence differs"):
            HISTORY.audit(self.output, self.root)

    def test_unhashed_history_edit_is_detected(self):
        path = self.output / "execution-history.json"
        self.replace(path, path.read_text() + "\n")
        with self.assertRaisesRegex(ValueError, "recorded hash"):
            HISTORY.audit(self.output, self.root)


if __name__ == "__main__":
    unittest.main()
