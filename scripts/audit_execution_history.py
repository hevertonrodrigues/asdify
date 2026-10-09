#!/usr/bin/env python3
"""Audit a stopped mode study and every answer carried into its continuation.

This verifies provenance, not semantic correctness. It makes no model calls and
can run before the continuation finishes; the normal result audit still needs
all answers and reviews.
"""
import argparse
import json
from pathlib import Path

import evaluate_modes as modes


def read_json(path):
    return json.loads(path.read_text())


def same_file(original, continuation, relative):
    source, target = original / relative, continuation / relative
    if not source.is_file() or not target.is_file() or source.read_bytes() != target.read_bytes():
        raise ValueError(f"Carried evidence differs: {relative}")


def request_files(identifier, request):
    return {f"{identifier}-request.json", f".requests/{identifier}.json"} | {
        f"raw/{identifier}-attempt-{attempt['attempt']}.{suffix}"
        for attempt in request["attempts"] for suffix in ("events.jsonl", "stderr.txt")
    }


def verify_interrupted(output, identifier, prompt):
    """Reject any discarded answer, including a message without turn.completed."""
    request = read_json(output / f"{identifier}-request.json")
    digest = modes.base.sha(prompt.encode())
    claim = read_json(output / ".requests" / f"{identifier}.json")
    if request.get("prompt_sha256") != digest or claim.get("prompt_sha256") != digest:
        raise ValueError(f"Changed interrupted prompt or claim: {identifier}")
    attempts = request.get("attempts", [])
    if (not request.get("error") or "output" in request or not 1 <= len(attempts) <= 2
            or [a["attempt"] for a in attempts] != list(range(1, len(attempts) + 1))):
        raise ValueError(f"Invalid interruption history: {identifier}")
    for attempt in attempts:
        if not attempt.get("error") or "output" in attempt:
            raise ValueError(f"Successful interrupted attempt was discarded: {identifier}")
        raw = output / "raw" / f"{identifier}-attempt-{attempt['attempt']}.events.jsonl"
        stderr = raw.with_name(raw.name.replace(".events.jsonl", ".stderr.txt"))
        if not raw.is_file() or not stderr.is_file():
            raise ValueError(f"Missing interrupted raw evidence: {identifier}")
        stdout = raw.read_text()
        if modes.completed_turn(stdout):
            raise ValueError(f"Completed interrupted answer was regenerated: {identifier}")
        for line in stdout.splitlines():
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            item = event.get("item", {}) if isinstance(event, dict) else {}
            if isinstance(item, dict) and item.get("type") == "agent_message" and item.get("text"):
                raise ValueError(f"Returned interrupted answer was regenerated: {identifier}")
    return request


def audit(output, root=modes.ROOT):
    output, root = output.resolve(), root.resolve()
    metadata, cases = modes.verify_frozen(output)
    history_path = output / "execution-history.json"
    if modes.base.sha(history_path.read_bytes()) != metadata.get("execution_history_sha256"):
        raise ValueError("Execution history differs from its recorded hash")
    history = read_json(history_path)
    relative = Path(history["original_frozen_study"])
    original = (root / relative).resolve()
    if (relative.is_absolute() or ".." in relative.parts
            or not original.is_relative_to(root / "benchmarks/results") or original == output):
        raise ValueError("Invalid original study path")
    original_metadata, original_cases = modes.verify_frozen(original)
    if cases != original_cases or metadata["frozen_file_sha256"] != original_metadata["frozen_file_sha256"]:
        raise ValueError("Continuation changed the frozen cases or inputs")
    variable = {"study_id", "frozen_at_utc", "limitations"}
    for key, value in original_metadata.items():
        if key not in variable and metadata.get(key) != value:
            raise ValueError(f"Continuation changed frozen metadata: {key}")
    if (history["original_inputs_frozen_at_utc"] != original_metadata["frozen_at_utc"]
            or metadata.get("original_inputs_frozen_at_utc") != original_metadata["frozen_at_utc"]):
        raise ValueError("Original freeze time differs")
    if not set(original_metadata["limitations"]).issubset(metadata["limitations"]):
        raise ValueError("Continuation removed study limitations")
    execution = read_json(output / "execution.json")
    if (type(history.get("new_live_worker_limit")) is not int
            or history["new_live_worker_limit"] != 4 or execution.get("workers") != 4):
        raise ValueError("Continuation worker setting differs from four-worker record")
    original_execution = read_json(original / "execution.json")
    if original_execution.get("workers") != 32:
        raise ValueError("Original execution setting differs from interruption record")
    for key in ("timeout_seconds", "model_catalog_sha256"):
        if execution.get(key) != original_execution.get(key):
            raise ValueError(f"Execution setting changed: {key}")
    expected = {f"generate-{condition}-{key}": batch for key, batch in modes.batches(cases)
                for condition in modes.CONDITIONS}
    retained, interrupted, files, answer_count = [], [], set(), 0
    for path in sorted(original.glob("*-request.json")):
        identifier = path.name.removesuffix("-request.json")
        if identifier not in expected:
            raise ValueError(f"Unexpected original primary request: {identifier}")
        condition = identifier.split("-", 2)[1]
        prompt = modes.generation_prompt(expected[identifier], condition, original / "skill")
        if "error" in read_json(path):
            request = verify_interrupted(original, identifier, prompt)
            interrupted.append(identifier)
        else:
            request = modes.audit_request(original, identifier, prompt)
            answer_count += len(modes.validate_answers(json.loads(request["output"]), expected[identifier]))
            retained.append(identifier)
            for relative_file in request_files(identifier, request):
                same_file(original, output, relative_file)
        files.update(request_files(identifier, request))
    actual = {str(p.relative_to(original)) for folder in (original / "raw", original / ".requests")
              for p in folder.rglob("*") if p.is_file()}
    actual.update(p.name for p in original.glob("*-request.json"))
    if actual != files:
        raise ValueError("Unrecorded or missing original request evidence")
    if history.get("carried_generation_requests") != retained or history.get("carried_answers") != answer_count:
        raise ValueError("Continuation did not carry every successful original answer")
    if not retained or not interrupted:
        raise ValueError("Execution history does not describe a partial interrupted study")
    errors = read_json(original / "execution-errors.json")
    if (len(errors) != len(interrupted) or {e["request"] for e in errors} != set(interrupted)
            or any(e["error"] != read_json(original / f"{e['request']}-request.json")["error"] for e in errors)):
        raise ValueError("Interruption errors differ from retained failed requests")
    notice = read_json(original / "interruption-notice.json")
    if (notice.get("completed_generation_requests") != len(retained)
            or notice.get("interrupted_requests") != len(interrupted)
            or notice.get("new_live_worker_limit") != 4
            or (root / notice["continuation_study"]).resolve() != output):
        raise ValueError("Interruption notice differs from execution history")
    calibration_files = {str(p.relative_to(original)) for p in (original / "calibration").rglob("*") if p.is_file()}
    continuation_calibration = {str(p.relative_to(output)) for p in (output / "calibration").rglob("*") if p.is_file()}
    if calibration_files != continuation_calibration:
        raise ValueError("Carried calibration inventory differs")
    for relative_file in calibration_files:
        same_file(original, output, relative_file)
    modes.calibration_summary(original, audited=True)
    modes.validate_inventory(original / "calibration", {
        f"calibration-{reviewer}-{start:03d}" for reviewer in (1, 2) for start in (1, 6)
    })
    return {
        "audit": "passed", "original_study": history["original_frozen_study"],
        "original_live_workers": 32, "continuation_live_workers": 4,
        "carried_generation_requests": len(retained), "carried_answers": answer_count,
        "interrupted_requests_without_returned_answers": len(interrupted),
        "frozen_inputs": "identical", "carried_request_claims_and_raw_events": "byte-identical",
        "all_successful_original_answers": "retained", "calibration": "identical and audited",
        "scope": "Interruption provenance only; completion and meaning require the separate result audit.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--check-only", action="store_true", help="Do not write execution-history-audit.json")
    args = parser.parse_args()
    try:
        value = audit(args.output)
        if not args.check_only:
            modes.base.write_json(args.output / "execution-history-audit.json", value)
        print(json.dumps(value))
    except (ValueError, KeyError, TypeError, OSError) as exc:
        parser.exit(1, f"Execution history audit failed: {exc}\n")


if __name__ == "__main__":
    main()
