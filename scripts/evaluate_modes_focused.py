#!/usr/bin/env python3
"""Run a frozen, explicitly selected development subset without altering the 900-case runner."""
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

import evaluate_modes_conservative as conservative

HERE = Path(__file__).resolve()
PLAN = "focused-plan.json"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate_plan(plan, cases):
    identifiers = plan.get("selected_case_ids")
    if (not isinstance(identifiers, list) or not identifiers
            or any(not isinstance(identifier, str) for identifier in identifiers)
            or len(set(identifiers)) != len(identifiers)):
        raise ValueError("Invalid focused selection")
    if not set(identifiers) <= {case["id"] for case in cases}:
        raise ValueError("Unknown focused case")
    selected = [case for case in cases if case["id"] in identifiers]
    if not isinstance(plan.get("retention_rule"), str) or not plan["retention_rule"].strip():
        raise ValueError("Missing prospective retention rule")
    if not isinstance(plan.get("selection_description"), str) or not plan["selection_description"].strip():
        raise ValueError("Missing selection disclosure")
    return selected


class Focused:
    def __init__(self, plan):
        self.plan = plan
        self.module = conservative.isolated_runner()
        module = self.module
        self.original = {name: getattr(module, name) for name in
                         ("load_corpus", "verify_frozen", "summarize")}
        module.load_corpus = self.load_corpus
        module.verify_frozen = self.verify_frozen
        module.validate_review = lambda value, cases: conservative.validate_review(value, cases, module)
        module.summarize = self.summarize
        module.report_text = self.report_text

    def load_corpus(self, folder):
        return validate_plan(self.plan, self.original["load_corpus"](folder))

    def verify_frozen(self, output):
        metadata, cases = self.original["verify_frozen"](output)
        if (read(output / PLAN) != self.plan
                or metadata.get("focused_adapter_sha256") != digest(HERE)
                or metadata.get("coverage_processor_sha256") != digest(Path(conservative.__file__))):
            raise ValueError("Focused adapter, policy, or selection changed")
        counts = dict(Counter(case["benchmark_language"] for case in cases))
        if metadata.get("cases_per_language") != counts or metadata.get("held_out_from_skill_development") is not False:
            raise ValueError("Focused development coverage changed")
        if metadata.get("selection") != self.plan["selection_description"]:
            raise ValueError("Focused selection disclosure changed")
        return metadata, cases

    def summarize(self, case, answer, ratings):
        result = self.original["summarize"](case, answer, ratings)
        errors = []
        for reviewer, rating in enumerate(ratings, 1):
            error = conservative.coverage_error(case, rating)
            if error:
                errors.append(dict(error, reviewer=reviewer, candidate=rating["candidate"], raw_rating=rating))
        result["review_structural_errors"] = errors
        if errors:
            result["uncertain"], result["confirmed_pass"] = True, False
            result["notes"].append("Invalid invariant coverage; original checks are retained and this answer cannot pass.")
        return result

    @staticmethod
    def report_text(metadata, summary):
        lines = ["# Focused development retest", "", metadata["selection"], "",
                 "Previously examined cases were reused after a proposed skill edit. These are development "
                 "regressions, not new held-out tests or updated scores for the original 900 cases. "
                 "Each condition is a fresh generation, including the no-skill baseline.", "",
                 "| Output language | Cases per condition | No skill | Lite | Full | Ultra | Off |",
                 "| --- | ---: | ---: | ---: | ---: | ---: | ---: |"]
        for language, values in summary["totals"].items():
            lines.append(f"| {language} | {values['baseline']['tested']} | " +
                         " | ".join(f"{values[c]['pass_percent']:.2f}%" for c in
                                    ("baseline", "lite", "full", "ultra", "off")) + " |")
        lines += ["", f"{metadata['generated_answers']} generated answers; {metadata['candidate_ratings']} "
                  f"blinded candidate ratings. Model: `{metadata['model']}`; effort: `{metadata['reasoning_effort']}`. "
                  "Both reviews and exact checks must pass. Incomplete or duplicate invariant coverage is "
                  "prospectively classified as uncertain/non-passing; raw ratings are retained.", "",
                  "[Frozen plan](focused-plan.json), [metadata](metadata.json), [case results](case-results.json), "
                  "[numeric summary](summary.json), [table CSV](table.csv), [raw evidence](raw/).", "",
                  "## Limits", ""]
        lines += ["- " + item for item in metadata["limitations"]]
        lines += ["", "## All answers", "", " | ".join(
            f"[{language}](answers-{language}.md)" for language in metadata["languages"])]
        return "\n".join(lines) + "\n"

    def freeze(self, output, corpus, catalog, model, effort):
        module = self.module
        module.freeze(output, corpus, model, effort, 5, catalog, regression=True)
        module.base.write_json(output / PLAN, self.plan)
        metadata = read(output / "metadata.json")
        cases = module.base.read_jsonl(output / "cases.jsonl")
        metadata.update(
            cases_per_language=dict(Counter(case["benchmark_language"] for case in cases)),
            languages=[language for language in module.locales()
                       if any(case["benchmark_language"] == language for case in cases)],
            selection=self.plan["selection_description"],
            focused_adapter_sha256=digest(HERE),
            coverage_processor_sha256=digest(Path(conservative.__file__)),
            review_coverage_policy="Prospective: otherwise assignable ratings with missing, duplicate, or extra "
                                   "integer invariant IDs are retained as uncertain/non-passing. Other errors remain fatal.",
        )
        metadata["frozen_file_sha256"][PLAN] = digest(output / PLAN)
        metadata["limitations"] += [
            "Selection includes previously observed failures and controls; no held-out improvement estimate.",
            "Small, unequal locale subsets cannot establish language-wide improvements.",
            "Before/after generations share case IDs but not draws; sampling and reviewer variation can change scores.",
        ]
        module.base.write_json(output / "metadata.json", metadata)
        self.verify_frozen(output)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("freeze", "calibrate", "run", "report", "audit"))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--plan", type=Path, help="Prospective subset and retention rule; required for freeze")
    parser.add_argument("--corpus", type=Path, default=conservative.RUNNER.parents[1] / "benchmarks/multilingual-modes")
    parser.add_argument("--catalog", type=Path)
    parser.add_argument("--model", default="gpt-6.1-sol")
    parser.add_argument("--effort", default="medium")
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--timeout", type=int, default=600)
    args = parser.parse_args()
    if not 1 <= args.workers <= 4 or args.timeout < 1:
        parser.error("Use one to four workers and a positive timeout")
    if args.action == "freeze" and not args.plan:
        parser.error("Freeze requires --plan")
    if args.action != "freeze" and args.plan:
        parser.error("Resume uses only the frozen plan")
    try:
        adapter = Focused(read(args.plan if args.action == "freeze" else args.output / PLAN))
        if args.action == "freeze":
            adapter.freeze(args.output, args.corpus, args.catalog, args.model, args.effort)
        elif args.action == "run":
            adapter.module.run(args.output, args.workers, args.catalog, args.timeout)
        elif args.action == "calibrate":
            adapter.module.calibrate(args.output, args.catalog, args.timeout)
        else:
            getattr(adapter.module, args.action)(args.output)
    except (ValueError, OSError, KeyError, TypeError) as error:
        parser.exit(1, f"Focused study failed: {error}\n")


if __name__ == "__main__":
    main()
