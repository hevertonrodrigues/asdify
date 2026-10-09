#!/usr/bin/env python3
"""Grade complete frozen batches while independent generation is still running."""
import argparse
import concurrent.futures
import json
import time
from pathlib import Path

import evaluate_skill as evaluation


def watch(output, workers=2):
    metadata, cases = evaluation.verify_frozen(output)
    paths = evaluation.disabled_skills()
    pending = []
    for reviewer in (1, 2):
        for start in range(0, 100, metadata["review_batch_size"]):
            batch = cases[start:start + metadata["review_batch_size"]]
            identifier = f"review-{reviewer}-{start + 1:03d}"
            destination = output / f"{identifier}.json"
            if destination.exists():
                evaluation.validate_review(json.loads(destination.read_text()), batch,
                                           evaluation.declared_review_exceptions(output, destination.name))
            else:
                pending.append((reviewer, batch, identifier, destination))
    active, errors = {}, []
    deadline = time.monotonic() + 5400
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        while pending or active:
            if time.monotonic() > deadline:
                raise ValueError("Timed out waiting for complete batches; keep partial evidence")
            try:
                generations = evaluation.successful_generations(output)
            except json.JSONDecodeError:
                # Producer may be in the middle of appending a line.
                time.sleep(1)
                continue
            for job in list(pending):
                if len(active) >= workers:
                    break
                reviewer, batch, identifier, destination = job
                if not all((c["id"], a) in generations for c in batch for a in evaluation.ARMS):
                    continue
                prompt = evaluation.review_prompt(batch, generations, reviewer)
                future = pool.submit(
                    evaluation.call_model, output, identifier, prompt, metadata["model"],
                    metadata["review_reasoning_effort"], paths, output / "review-schema.json",
                )
                active[future] = (batch, identifier, destination)
                pending.remove(job)
                print(f"Started {identifier}: both answers ready for all 5 cases", flush=True)
            if not active:
                time.sleep(5)
                continue
            finished, _ = concurrent.futures.wait(
                active, timeout=5, return_when=concurrent.futures.FIRST_COMPLETED)
            for future in finished:
                batch, identifier, destination = active.pop(future)
                result = future.result()
                evaluation.write_json(output / f"{identifier}-request.json", result)
                try:
                    if "error" in result:
                        raise ValueError(result["error"])
                    value = json.loads(result["output"])
                    evaluation.validate_review(value, batch)
                    evaluation.write_json(destination, value)
                    print(f"Completed {identifier}", flush=True)
                except (ValueError, KeyError, TypeError) as exc:
                    errors.append(f"{identifier}: {exc}")
                    print(f"Rejected {identifier}: {exc}", flush=True)
    if errors:
        raise ValueError("Incomplete reviews; no passing conclusion:\n" + "\n".join(errors))
    print("Both review passes complete for all 100 cases", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--workers", type=int, choices=(1, 2, 3, 4), default=2)
    args = parser.parse_args()
    watch(args.output, args.workers)
