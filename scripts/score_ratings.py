#!/usr/bin/env python3
"""Aggregate blinded human ratings. Does not grade with an LLM or infer causality."""
import csv
import statistics
import sys
from collections import defaultdict

DIMENSIONS = ("meaning_fidelity", "clarity", "signal_density", "structure", "calibration", "fit_for_purpose")
REQUIRED_COLUMNS = ("reviewer", "case_id", "arm", *DIMENSIONS, "hard_fail")
OPTIONAL_COLUMNS = ("notes", "run_id")


def score(filename):
    with open(filename, newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle, strict=True)
        header = reader.fieldnames
        if not header:
            raise ValueError("Missing CSV header. Start from benchmarks/ratings-template.csv.")
        if len(set(header)) != len(header):
            raise ValueError("CSV header contains duplicate columns")
        missing = set(REQUIRED_COLUMNS) - set(header)
        extra = set(header) - set(REQUIRED_COLUMNS + OPTIONAL_COLUMNS)
        if missing:
            raise ValueError(f"CSV header missing required columns: {', '.join(sorted(missing))}")
        if extra:
            raise ValueError(f"CSV header contains unsupported columns: {', '.join(sorted(extra))}")
        rows = [(reader.line_num, row) for row in reader]
    if not rows:
        raise ValueError("No ratings supplied. Fill a copy of benchmarks/ratings-template.csv first.")
    groups = defaultdict(list)
    pairs = defaultdict(set)
    runs = set()
    for n, row in rows:
        if None in row or any(value is None for value in row.values()):
            raise ValueError(f"Row {n}: number of cells must match the CSV header")
        arm = row["arm"].strip().upper()
        if arm not in ("A", "B"):
            raise ValueError(f"Row {n}: arm must be A or B")
        run_id = row["run_id"].strip() if "run_id" in row else "single-run"
        key = (run_id, row["reviewer"].strip(), row["case_id"].strip())
        if not all(key):
            raise ValueError(f"Row {n}: run_id, reviewer, and case_id must be nonempty (omit run_id column for a single run)")
        if arm in pairs[key]:
            raise ValueError(f"Row {n}: duplicate arm for the same run, reviewer, and case")
        pairs[key].add(arm)
        runs.add(run_id)
        if row["hard_fail"] not in ("0", "1"):
            raise ValueError(f"Row {n}: hard_fail must be 0 or 1")
        for dim in DIMENSIONS:
            try:
                score_value = int(row[dim])
            except ValueError as exc:
                raise ValueError(f"Row {n}: {dim} must be an integer from 1 to 5") from exc
            if not 1 <= score_value <= 5:
                raise ValueError(f"Row {n}: {dim} must be 1–5")
        groups[arm].append(row)
    for key, arms in pairs.items():
        if arms != {"A", "B"}:
            raise ValueError(f"Unpaired evaluation {key}: both A and B required")

    print(f"Descriptive summary: {len(runs)} run(s), {len(pairs)} paired reviewer-case evaluations.")
    for arm in ("A", "B"):
        group = groups[arm]
        failures = sum(r["hard_fail"] == "1" for r in group)
        print(f"Arm {arm}: {len(group)} blind ratings, hard failures: {failures}/{len(group)} ({failures / len(group):.1%} of ratings)")
        for dim in DIMENSIONS:
            vals = [int(r[dim]) for r in group]
            print(f"  {dim}: median {statistics.median(vals):g}, mean {statistics.mean(vals):.2f}")
    print("Means, medians, and failure rates are descriptive and include all submitted ratings, including hard failures.")
    print("Ratings share cases/reviewers; they are not independent trials or evidence of causality. No winner is inferred.")
    print("Conditions stay blinded here; unblind only after grading is complete.")


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: python3 scripts/score_ratings.py path/to/ratings.csv")
        score(sys.argv[1])
    except (ValueError, OSError, csv.Error) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
