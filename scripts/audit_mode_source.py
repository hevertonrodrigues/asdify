#!/usr/bin/env python3
"""Verify the supplemental mode-study source audit without model calls."""
import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

CONDITIONS = {"baseline", "lite", "full", "ultra", "off"}
LABELS = {"Q", "R", "S", "T", "U"}
RECORD = "audit-integrity.json"
KEY = "opaque-label-key.json"


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def lines(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def indexed(rows, field, expected, label):
    require(isinstance(rows, list), f"Invalid {label} rows")
    result = {}
    for row in rows:
        require(isinstance(row, dict), f"Invalid {label} row")
        identifier = row.get(field)
        require(isinstance(identifier, str) and identifier in expected and identifier not in result,
                f"Unknown or duplicate {label}: {identifier}")
        result[identifier] = row
    require(set(result) == set(expected), f"Incomplete {label} coverage")
    return result


def verify(output, key_path):
    destination = output / "source-audit"
    manifest = read(destination / "selection-manifest.json")
    inputs = {
        "primary_summary_sha256": output / "summary.json",
        "primary_case_results_sha256": output / "case-results.json",
        "selection_plan_sha256": output / "source-audit-plan.json",
        "audit_instructions_sha256": output / "source-audit-instructions.md",
    }
    for field, path in inputs.items():
        require(manifest[field] == sha(path), f"Changed source-audit input: {path.name}")
    require(manifest["opaque_label_key_sha256"] == sha(key_path), "Changed opaque-label key")
    plan = read(output / "source-audit-plan.json")
    results = read(output / "case-results.json")
    cases = {case["id"]: case for case in lines(output / "cases.jsonl")}
    random_ids = {identifier for values in plan["random_case_ids"].values() for identifier in values}
    flagged_ids = {row["case_id"] for row in results
                   if any(not row[condition]["confirmed_pass"] for condition in CONDITIONS)}
    selected = random_ids | flagged_ids
    require(selected <= cases.keys(), "Unknown selected case")
    for field, expected in (("random_case_ids", random_ids), ("strict_flagged_case_ids", flagged_ids),
                            ("selected_case_ids", selected)):
        require(manifest[field] == sorted(expected), f"Changed selection: {field}")
    key = read(key_path)
    require(set(key["cases"]) == selected, "Opaque key case coverage differs")
    answers = {}
    for path in output.glob("generate-*-request.json"):
        condition = path.name.split("-")[1]
        for row in json.loads(read(path)["output"])["answers"]:
            pair = row["case_id"], condition
            require(pair not in answers, "Duplicate source answer")
            answers[pair] = row["text"]
    fingerprints = {"selection-manifest.json": sha(destination / "selection-manifest.json"), KEY: sha(key_path)}
    counts = {}
    judgments = {condition: {dimension: Counter() for dimension in ("meaning", "voice", "format")}
                 for condition in sorted(CONDITIONS)}
    expected_input_names = {f"inputs-{language}.jsonl" for language in plan["random_case_ids"]}
    require(set(manifest["blinded_input_sha256"]) == expected_input_names, "Changed input-file coverage")
    for language in plan["random_case_ids"]:
        expected = {identifier for identifier in selected if cases[identifier]["benchmark_language"] == language}
        input_path = destination / f"inputs-{language}.jsonl"
        require(manifest["blinded_input_sha256"][input_path.name] == sha(input_path), "Changed blinded input")
        sources = indexed(lines(input_path), "case_id", expected, "source case")
        annotation_path = destination / f"annotations-{language}.jsonl"
        annotations = indexed(lines(annotation_path), "case_id", expected, "annotation case")
        for identifier, source in sources.items():
            require(source["source_task"] == cases[identifier]["task"]
                    and source["output_language"] == language, "Changed source task or locale")
            mapping = key["cases"][identifier]
            require(set(mapping) == LABELS and set(mapping.values()) == CONDITIONS, "Invalid opaque mapping")
            candidates = indexed(source["candidates"], "label", LABELS, "input candidate")
            ratings = indexed(annotations[identifier]["candidates"], "label", LABELS, "annotated candidate")
            for label, candidate in candidates.items():
                condition = mapping[label]
                require(candidate["answer"] == answers[identifier, condition], "Opaque answer differs from raw source")
                rating = ratings[label]
                require(set(rating) == {"label", "meaning", "voice", "format", "reason"}, "Invalid annotation fields")
                require(isinstance(rating["reason"], str) and rating["reason"].strip(), "Missing annotation reason")
                for dimension in ("meaning", "voice", "format"):
                    allowed = {"preserved", "changed", "uncertain"}
                    if dimension != "meaning":
                        allowed.add("not_applicable")
                    require(isinstance(rating[dimension], str) and rating[dimension] in allowed,
                            "Invalid source-audit verdict")
                    judgments[condition][dimension][rating[dimension]] += 1
        counts[language] = len(expected)
        fingerprints.update({path.name: sha(path) for path in (input_path, annotation_path)})
    require(counts == manifest["selected_cases_per_language"] and sum(counts.values()) == manifest["selected_cases"]
            and 5 * sum(counts.values()) == manifest["selected_answers"], "Changed selected counts")
    return {"audit": "passed", "selected_cases": sum(counts.values()), "candidate_annotations": 5 * sum(counts.values()),
            "cases_per_language": counts, "random_cases": len(random_ids), "strict_flagged_cases": len(flagged_ids),
            "evidence_sha256": fingerprints, "judgment_counts_in_selected_sample": judgments,
            "scope": "Selection, blinding, raw-source identity, complete annotations, and file integrity only. Judgments are not verified truths or population reliability estimates."}


def audit(output):
    destination = output / "source-audit"
    expected = read(destination / RECORD)
    observed = verify(output, destination / KEY)
    require(expected["verification"] == observed, "Sealed source-audit evidence changed")
    return observed


def seal(output, key_path):
    destination = output / "source-audit"
    require(not (destination / RECORD).exists(), "Source audit already sealed")
    value = verify(output, key_path)  # All annotations must be complete before releasing the key.
    public_key = destination / KEY
    if public_key.exists():
        require(public_key.read_bytes() == key_path.read_bytes(), "Public key differs")
    else:
        with public_key.open("xb") as file:
            file.write(key_path.read_bytes())
    with (destination / RECORD).open("x", encoding="utf-8") as file:
        json.dump({"sealed_at_utc": datetime.now(timezone.utc).isoformat(),
                   "key_released_after_complete_annotation_validation": True, "verification": value},
                  file, ensure_ascii=False, indent=2)
        file.write("\n")
    return audit(output)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--seal", action="store_true", help="Release the key and seal complete annotations once")
    parser.add_argument("--key", type=Path, help="Private opaque key; required only when sealing")
    args = parser.parse_args()
    if args.seal != bool(args.key):
        parser.error("Use --seal and --key together, or neither for a read-only audit")
    try:
        value = seal(args.output, args.key) if args.seal else audit(args.output)
        print(json.dumps({key: value[key] for key in ("audit", "selected_cases", "candidate_annotations", "cases_per_language", "scope")}))
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.exit(1, f"Source audit failed: {error}\n")


if __name__ == "__main__":
    main()
