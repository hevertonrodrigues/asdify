#!/usr/bin/env python3
"""Check the blinded meaning grader against authored good/bad controls."""
import argparse
import concurrent.futures
import json
from pathlib import Path

import evaluate_skill as evaluation


def calibrate(study):
    metadata, _ = evaluation.verify_frozen(study)
    cases = evaluation.load_cases(evaluation.ROOT / "benchmarks/judge-calibration.jsonl", expected=10)
    destination = study / "calibration"
    if destination.exists():
        raise ValueError("Calibration already exists; retain its results or use a new study")
    destination.mkdir()
    (destination / "raw").mkdir()
    evaluation.write_json(destination / "frozen-controls.json", {
        "frozen_at_utc": evaluation.now(),
        "description": "Authored positive and deliberately distorted negative controls, "
                       "not model-generated answers. Frozen before primary model grading.",
        "cases": cases,
    })
    outputs, expected = {}, {}
    for i, case in enumerate(cases):
        good_arm = "baseline" if i % 2 == 0 else "skill"
        for arm in evaluation.ARMS:
            outputs[(case["id"], arm)] = {"output": case["good"] if arm == good_arm else case["bad"]}
        expected[case["id"]] = {
            "good": "A" if good_arm == "baseline" else "B",
            "bad": "B" if good_arm == "baseline" else "A",
        }
    paths = evaluation.disabled_skills()
    jobs, results = [], []
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        for reviewer in (1, 2):
            for start in (0, 5):
                batch = cases[start:start + 5]
                identifier = f"calibration-{reviewer}-{start + 1:03d}"
                future = pool.submit(
                    evaluation.call_model, destination, identifier,
                    evaluation.review_prompt(batch, outputs, reviewer), metadata["model"],
                    metadata["review_reasoning_effort"], paths, study / "review-schema.json",
                )
                jobs.append((future, reviewer, batch, identifier))
        for future, reviewer, batch, identifier in jobs:
            result = future.result()
            evaluation.write_json(destination / f"{identifier}-request.json", result)
            if "error" in result:
                raise ValueError(result["error"])
            value = json.loads(result["output"])
            rows = evaluation.validate_review(value, batch)
            evaluation.write_json(destination / f"{identifier}.json", value)
            for row in rows:
                ratings = {r["candidate"]: r for r in row["ratings"]}
                truth = expected[row["case_id"]]
                results.append({
                    "reviewer": reviewer, "case_id": row["case_id"],
                    "negative_detected": ratings[truth["bad"]]["hard_fail"],
                    "positive_passed": not ratings[truth["good"]]["hard_fail"],
                    "preference_correct": row["preference"] == truth["good"],
                })
            print(f"{identifier} complete", flush=True)
    summary = {
        "negative_controls_detected": sum(r["negative_detected"] for r in results),
        "positive_controls_passed": sum(r["positive_passed"] for r in results),
        "reviews": len(results), "preference_correct": sum(r["preference_correct"] for r in results),
        "results": results,
    }
    evaluation.write_json(destination / "summary.json", summary)
    print(json.dumps(summary, indent=2))
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--study", type=Path, required=True)
    args = parser.parse_args()
    calibrate(args.study)
