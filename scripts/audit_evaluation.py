#!/usr/bin/env python3
"""Verify a complete study against raw model events and exact frozen prompts."""
import argparse
import json
from pathlib import Path

import evaluate_skill as evaluation


def audit(output):
    metadata, cases = evaluation.verify_frozen(output)
    generations = evaluation.successful_generations(output)
    expected = {(case["id"], arm) for case in cases for arm in evaluation.ARMS}
    if set(generations) != expected:
        raise ValueError("Missing or unexpected case/arm outputs")
    treatment = (output / "treatment.txt").read_text(encoding="utf-8")
    for case in cases:
        for arm in evaluation.ARMS:
            record = generations[(case["id"], arm)]
            prompt = evaluation.prompt_for(case, arm, treatment)
            if record["prompt_sha256"] != evaluation.sha(prompt.encode()):
                raise ValueError("Generated prompt differs from frozen condition")
            verify_raw(output, f"{case['id']}-{arm}", record)
    reviewed = 0
    for reviewer in (1, 2):
        for start in range(0, 100, metadata["review_batch_size"]):
            batch = cases[start:start + metadata["review_batch_size"]]
            identifier = f"review-{reviewer}-{start + 1:03d}"
            request = json.loads((output / f"{identifier}-request.json").read_text())
            prompt = evaluation.review_prompt(batch, generations, reviewer)
            if request["prompt_sha256"] != evaluation.sha(prompt.encode()):
                raise ValueError("Review prompt or blinding order changed")
            verify_raw(output, identifier, request)
            value = json.loads((output / f"{identifier}.json").read_text())
            if value != json.loads(request["output"]):
                raise ValueError("Published ratings differ from actual model answer")
            rows = evaluation.validate_review(
                value, batch, evaluation.declared_review_exceptions(output, f"{identifier}.json"))
            reviewed += sum(len(row["ratings"]) for row in rows)
    snapshot = output / "runner-snapshot.py"
    if snapshot.exists() and evaluation.sha(snapshot.read_bytes()) != (output / "runner-sha256.txt").read_text().strip():
        raise ValueError("Original runner snapshot changed")
    result = {
        "audited_at_utc": evaluation.now(), "generated_answers": len(generations),
        "model_output_ratings": reviewed, "generation_prompt_hashes_match": True,
        "review_prompt_hashes_and_blinding_match": True, "raw_answers_and_ratings_unchanged": True,
        "no_observed_model_tool_calls": True, "frozen_skill_and_cases_unchanged": True,
    }
    if (output / "calibration").exists():
        result["calibration_ratings_verified_against_raw_events"] = audit_calibration(output)
    evaluation.write_json(output / "evidence-audit.json", result)
    print(json.dumps(result, indent=2))
    return result


def audit_calibration(output):
    folder = output / "calibration"
    cases = json.loads((folder / "frozen-controls.json").read_text())["cases"]
    if len(cases) != 10 or len({c["id"] for c in cases}) != 10:
        raise ValueError("Incomplete or duplicate calibration controls")
    answers, truth = {}, {}
    for i, case in enumerate(cases):
        good_arm = "baseline" if i % 2 == 0 else "skill"
        for arm in evaluation.ARMS:
            answers[(case["id"], arm)] = {"output": case["good"] if arm == good_arm else case["bad"]}
        truth[case["id"]] = {"good": "A" if good_arm == "baseline" else "B",
                             "bad": "B" if good_arm == "baseline" else "A"}
    results = []
    for reviewer in (1, 2):
        for start in (0, 5):
            batch = cases[start:start + 5]
            identifier = f"calibration-{reviewer}-{start + 1:03d}"
            request = json.loads((folder / f"{identifier}-request.json").read_text())
            prompt = evaluation.review_prompt(batch, answers, reviewer)
            if request["prompt_sha256"] != evaluation.sha(prompt.encode()):
                raise ValueError("Calibration prompt or display order changed")
            verify_raw(folder, identifier, request)
            value = json.loads((folder / f"{identifier}.json").read_text())
            if value != json.loads(request["output"]):
                raise ValueError("Calibration rating differs from raw model answer")
            for row in evaluation.validate_review(value, batch):
                ratings = {r["candidate"]: r for r in row["ratings"]}
                labels = truth[row["case_id"]]
                results.append({"reviewer": reviewer, "case_id": row["case_id"],
                                "negative_detected": ratings[labels["bad"]]["hard_fail"],
                                "positive_passed": not ratings[labels["good"]]["hard_fail"],
                                "preference_correct": row["preference"] == labels["good"]})
    expected = {"negative_controls_detected": sum(r["negative_detected"] for r in results),
                "positive_controls_passed": sum(r["positive_passed"] for r in results),
                "reviews": len(results),
                "preference_correct": sum(r["preference_correct"] for r in results),
                "results": results}
    if json.loads((folder / "summary.json").read_text()) != expected:
        raise ValueError("Calibration summary differs from raw ratings")
    return len(results) * 2


def verify_raw(output, identifier, record):
    if "output" not in record:
        raise ValueError("Request has no successful output")
    attempt = record["attempts"][-1]["attempt"]
    raw = output / "raw" / f"{identifier}-attempt-{attempt}.events.jsonl"
    answer, usage = evaluation.parse_events(raw.read_text(encoding="utf-8"))
    if answer != record["output"] or usage != record["usage"]:
        raise ValueError("Saved answer or usage differs from raw CLI events")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    audit(parser.parse_args().output)
