#!/usr/bin/env python3
"""Sealed, conservative processing amendment for an already-started mode study."""
import argparse
import builtins
import concurrent.futures
import contextlib
import copy
import hashlib
import importlib.util
import io
import json
import os
import re
import tempfile
import uuid
from collections import Counter
from pathlib import Path, PurePosixPath

HERE = Path(__file__).resolve()
RUNNER = HERE.with_name("evaluate_modes.py")
AMENDMENT = "processing-amendment.json"
SEAL = "processing-amendment.sha256"
POLICY = {
    "name": "conservative-invariant-coverage-v1",
    "timing": "Post-output processing amendment; not preregistered.",
    "coverage": "Missing, duplicate, or extra integer invariant IDs make an otherwise valid, assignable rating structurally invalid. Affected answers are uncertain and cannot pass.",
    "strictness": "All other schema, case/candidate assignment, raw-evidence, prompt, and frozen-setting checks remain strict. Raw negative or contradictory verdicts are retained.",
    "retention": "No model check is synthesized, repaired, removed, or rewritten; every existing response and its raw evidence is retained.",
    "resumption": "Only previously unstarted primary review requests may run, with at most four workers. Generation requests are never scheduled.",
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def safe_path(output, relative):
    if (not isinstance(relative, str) or not relative or "\\" in relative or "\x00" in relative
            or PurePosixPath(relative).is_absolute() or ":" in relative.split("/")[0]
            or any(part in {"", ".", ".."} for part in relative.split("/"))):
        raise ValueError(f"Unsafe manifest path: {relative!r}")
    path = output
    for part in relative.split("/"):
        path = path / part
        if path.is_symlink():
            raise ValueError(f"Symlink in manifest path: {relative}")
    if not path.resolve().is_relative_to(output.resolve()):
        raise ValueError(f"Manifest path escapes study: {relative}")
    return path


def write_once(path, value):
    """Publish a complete JSON file without replacing an existing file."""
    temporary = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent,
                                         prefix=".processing-", delete=False) as file:
            temporary = Path(file.name)
            json.dump(value, file, ensure_ascii=False, indent=2)
            file.write("\n")
            file.flush()
            os.fsync(file.fileno())
        os.link(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def isolated_runner(path=RUNNER):
    """Use a private helper import without swapping or changing sys.modules."""
    def load(name, source, importer=None):
        spec = importlib.util.spec_from_file_location(name, source)
        module = importlib.util.module_from_spec(spec)
        if importer:
            module.__dict__["__builtins__"] = dict(vars(builtins), __import__=importer)
        spec.loader.exec_module(module)
        return module
    helper = load("_conservative_frozen_helper", path.with_name("evaluate_skill.py"))

    def importer(name, globals=None, locals=None, fromlist=(), level=0):
        if name == "evaluate_skill" and level == 0:
            return helper
        return builtins.__import__(name, globals, locals, fromlist, level)

    return load("_conservative_frozen_modes", path, importer)


def object_keys(value, keys, label):
    if not isinstance(value, dict) or set(value) != set(keys):
        raise ValueError(f"Invalid {label} fields")


def validate_review(value, cases, module):
    """Relax coverage only. Return original rows and checks without modification."""
    object_keys(value, {"cases"}, "review")
    rows = value["cases"]
    expected = {case["id"]: case for case in cases}
    if not isinstance(rows, list) or len(rows) != len(expected):
        raise ValueError("Incomplete review case coverage")
    schema = module.review_schema()["properties"]["cases"]["items"]
    rating_keys = schema["properties"]["ratings"]["items"]["required"]
    seen = set()
    for row in rows:
        object_keys(row, {"case_id", "ratings"}, "reviewed case")
        identifier = row["case_id"]
        if not isinstance(identifier, str) or identifier not in expected or identifier in seen:
            raise ValueError("Duplicate or unknown reviewed case")
        seen.add(identifier)
        ratings = row["ratings"]
        if not isinstance(ratings, list) or len(ratings) != len(module.LABELS):
            raise ValueError("Incomplete candidate coverage")
        labels = set()
        for rating in ratings:
            object_keys(rating, rating_keys, "rating")
            label = rating["candidate"]
            if not isinstance(label, str) or label not in module.LABELS or label in labels:
                raise ValueError("Duplicate or unknown candidate")
            labels.add(label)
            checks = rating["checks"]
            if not isinstance(checks, list):
                raise ValueError("Checks must be an array")
            for check in checks:
                object_keys(check, {"invariant_id", "status", "evidence"}, "check")
                if type(check["invariant_id"]) is not int:
                    raise ValueError("Invariant ID must be an integer, not a boolean or string")
                if not isinstance(check["status"], str) or check["status"] not in {
                        "preserved", "missing", "changed", "uncertain"}:
                    raise ValueError("Invalid invariant status")
                if not isinstance(check["evidence"], str) or not check["evidence"].strip():
                    raise ValueError("Missing check evidence")
            for dimension in module.base.DIMENSIONS:
                if type(rating[dimension]) is not int or not 1 <= rating[dimension] <= 5:
                    raise ValueError("Invalid quality score")
            if any(type(rating[field]) is not bool for field in ("hard_fail", "format_pass", "language_pass")):
                raise ValueError("Invalid boolean verdict")
            claims = rating["unsupported_claims"]
            if (not isinstance(claims, list) or any(not isinstance(c, str) or not c.strip() for c in claims)
                    or not isinstance(rating["reason"], str) or not rating["reason"].strip()):
                raise ValueError("Invalid claims or reason")
    return rows


def coverage_error(case, rating):
    observed = [check["invariant_id"] for check in rating["checks"]]
    counts = Counter(observed)
    expected = set(range(1, len(case["invariants"]) + 1))
    missing, extra = sorted(expected - counts.keys()), sorted(counts.keys() - expected)
    duplicates = sorted(identifier for identifier, count in counts.items() if count > 1)
    if not (missing or extra or duplicates):
        return None
    return {"missing_invariant_ids": missing, "duplicate_invariant_ids": duplicates,
            "extra_invariant_ids": extra, "observed_invariant_ids": observed}


class Processor:
    def __init__(self, runner=RUNNER):
        self.module = isolated_runner(runner)
        self.original = {name: getattr(self.module, name) for name in
                         ("validate_review", "summarize", "result_data", "report_text", "audit")}
        self.last_processing = None
        for name in self.original:
            setattr(self.module, name, getattr(self, name))

    def validate_review(self, value, cases):
        return validate_review(value, cases, self.module)

    def summarize(self, case, answer, ratings):
        result = self.original["summarize"](case, answer, ratings)
        errors = []
        for reviewer, rating in enumerate(ratings, 1):
            error = coverage_error(case, rating)
            if error:
                errors.append(dict(error, reviewer=reviewer, candidate=rating["candidate"],
                                   raw_rating=copy.deepcopy(rating)))
        result["review_structural_errors"] = errors
        if errors:
            result["uncertain"], result["confirmed_pass"] = True, False
            result["notes"] += [f"Review {error['reviewer']} has invalid invariant coverage: "
                                f"missing {error['missing_invariant_ids']}, duplicate {error['duplicate_invariant_ids']}, "
                                f"extra {error['extra_invariant_ids']}. Raw checks are retained; this answer cannot pass."
                                for error in errors]
        return result

    def identity(self, output, metadata):
        return {"metadata_sha256": sha((output / "metadata.json").read_bytes()),
                "runner_sha256": metadata["runner_sha256"], "helper_sha256": metadata["helper_sha256"],
                "frozen_file_sha256": metadata["frozen_file_sha256"]}

    def frozen(self, output):
        metadata = json.loads(safe_path(output, "metadata.json").read_text())
        for relative in metadata["frozen_file_sha256"]:
            safe_path(output, relative)
        return self.module.verify_frozen(output)

    def verify_amendment(self, output):
        path, seal = safe_path(output, AMENDMENT), safe_path(output, SEAL)
        digest = seal.read_text().strip()
        if not re.fullmatch(r"[0-9a-f]{64}", digest) or sha(path.read_bytes()) != digest:
            raise ValueError("Processing amendment seal changed")
        amendment = json.loads(path.read_text())
        if amendment.get("schema_version") != 1 or amendment.get("processing_policy") != POLICY:
            raise ValueError("Processing policy changed")
        if amendment.get("processor_sha256") != sha(HERE.read_bytes()):
            raise ValueError("Conservative processor changed after sealing")
        metadata, cases = self.frozen(output)
        if amendment.get("frozen_identity") != self.identity(output, metadata):
            raise ValueError("Frozen study identity differs from processing amendment")
        manifest = amendment.get("prior_evidence_sha256")
        if not isinstance(manifest, dict) or not manifest:
            raise ValueError("Missing sealed evidence manifest")
        for relative, expected in manifest.items():
            path = safe_path(output, relative)
            if (not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{64}", expected)
                    or not path.is_file() or sha(path.read_bytes()) != expected):
                raise ValueError(f"Sealed prior evidence changed: {relative}")
        return amendment, metadata, cases

    def retained(self, output, metadata, cases):
        """Audit every saved request before scheduling anything new."""
        module, answers, reviews, observations = self.module, {}, set(), []
        expected = set()
        for key, batch in module.batches(cases):
            for condition in module.CONDITIONS:
                identifier = f"generate-{condition}-{key}"
                expected.add(identifier)
                request = module.audit_request(output, identifier, module.generation_prompt(batch, condition, output / "skill"))
                for case_id, text in module.validate_answers(json.loads(request["output"]), batch).items():
                    answers[(case_id, condition)] = text
            for reviewer in (1, 2):
                identifier = f"review-{reviewer}-{key}"
                expected.add(identifier)
                if not (output / f"{identifier}-request.json").exists():
                    continue
                request = module.audit_request(output, identifier, module.review_prompt(batch, answers, reviewer))
                value = json.loads(request["output"])
                self.validate_review(value, batch)
                reviews.add(identifier)
                try:
                    self.original["validate_review"](value, batch)
                except ValueError as error:
                    observations.append({"request": identifier, "strict_validation_error": str(error)})
        actual = {path.name.removesuffix("-request.json") for path in output.glob("*-request.json")}
        if not actual.issubset(expected):
            raise ValueError("Unknown primary request coverage")
        module.validate_inventory(output, actual)
        module.calibration_summary(output, audited=True)
        module.validate_inventory(output / "calibration", {
            f"calibration-{reviewer}-{start:03d}" for reviewer in (1, 2) for start in (1, 6)})
        return answers, reviews, observations

    def evidence_manifest(self, output, metadata):
        paths = {output / "metadata.json"}
        paths.update(safe_path(output, relative) for relative in metadata["frozen_file_sha256"])
        paths.update(output.glob("*-request.json"))
        paths.update(output.glob("execution*.json"))
        paths.update(output.glob("*errors*.json"))
        for directory in (".requests", "raw", "calibration"):
            root = output / directory
            if root.is_symlink():
                raise ValueError("Symlink evidence directory")
            paths.update(path for path in root.rglob("*") if path.is_file() or path.is_symlink())
        return {str(path.relative_to(output)): sha(safe_path(output, str(path.relative_to(output))).read_bytes())
                for path in sorted(paths)}

    def catalog(self, metadata, catalog):
        if metadata["model_catalog_sha256"] != (sha(catalog.read_bytes()) if catalog else None):
            raise ValueError("Catalog must match the frozen study")

    def amend(self, output, catalog=None):
        return self.module.exclusive_process(self._amend)(output, catalog)

    def _amend(self, output, catalog):
        if (output / AMENDMENT).exists() or (output / SEAL).exists():
            raise ValueError("Processing amendment already exists; never replace its seal")
        metadata, cases = self.frozen(output)
        self.catalog(metadata, catalog)
        _, _, observations = self.retained(output, metadata, cases)
        stop = output / "execution-errors.json"
        amendment = {"schema_version": 1, "created_at_utc": self.module.base.now(),
                     "processing_policy": POLICY, "processor_sha256": sha(HERE.read_bytes()),
                     "frozen_identity": self.identity(output, metadata),
                     "observed_validation_stop_errors": json.loads(stop.read_text()) if stop.exists() else [],
                     "observed_strict_review_errors": observations,
                     "prior_evidence_sha256": self.evidence_manifest(output, metadata)}
        write_once(output / AMENDMENT, amendment)
        with (output / SEAL).open("x", encoding="utf-8") as file:
            file.write(sha((output / AMENDMENT).read_bytes()) + "\n")
            file.flush()
            os.fsync(file.fileno())
        self.verify_amendment(output)
        print(f"Sealed processing amendment preserving {len(amendment['prior_evidence_sha256'])} existing files", flush=True)
        return amendment

    def run(self, output, workers=4, catalog=None, timeout=600):
        if not 1 <= workers <= 4 or timeout < 1:
            raise ValueError("Use one to four workers and a positive timeout")
        return self.module.exclusive_process(self._run)(output, workers, catalog, timeout)

    def _run(self, output, workers, catalog, timeout):
        amendment, metadata, cases = self.verify_amendment(output)
        self.catalog(metadata, catalog)
        answers, saved, _ = self.retained(output, metadata, cases)
        module = self.module
        pending = [(f"review-{reviewer}-{key}", batch, reviewer)
                   for key, batch in module.batches(cases) for reviewer in (1, 2)
                   if f"review-{reviewer}-{key}" not in saved]
        history_path = output / f"processing-execution-{uuid.uuid4().hex}.json"
        history = {"started_at_utc": module.base.now(), "workers": workers, "maximum_workers": 4,
                   "timeout_seconds": timeout, "model": metadata["model"],
                   "review_reasoning_effort": metadata["review_reasoning_effort"],
                   "model_catalog_sha256": metadata["model_catalog_sha256"],
                   "processor_sha256": amendment["processor_sha256"],
                   "amendment_sha256": sha((output / AMENDMENT).read_bytes()),
                   "retained_reviews": len(saved), "scheduled_reviews": [], "saved_reviews": [], "errors": []}
        write_once(history_path, history)
        queue, jobs = iter(pending), {}
        paths = module.base.disabled_skills()
        settings = dict(metadata, reasoning_effort=metadata["review_reasoning_effort"])
        try:
            with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
                def fill():
                    while len(jobs) < workers and not history["errors"]:
                        try:
                            identifier, batch, reviewer = next(queue)
                        except StopIteration:
                            break
                        prompt = module.review_prompt(batch, answers, reviewer)
                        future = pool.submit(module.call_model, output, identifier, prompt, settings,
                                             paths, output / "review-schema.json", catalog, timeout)
                        jobs[future] = (identifier, batch, prompt)
                        history["scheduled_reviews"].append(identifier)
                fill()
                while jobs:
                    done, _ = concurrent.futures.wait(jobs, return_when=concurrent.futures.FIRST_COMPLETED)
                    for future in done:
                        identifier, batch, prompt = jobs.pop(future)
                        try:
                            request = future.result()
                        except Exception as error:
                            request = {"prompt_sha256": sha(prompt.encode()), "attempts": [],
                                       "error": f"Worker exception {type(error).__name__}: {error}"}
                        write_once(output / f"{identifier}-request.json", request)
                        history["saved_reviews"].append(identifier)
                        try:
                            if "error" in request:
                                raise ValueError(request["error"])
                            module.audit_request(output, identifier, prompt)
                            self.validate_review(json.loads(request["output"]), batch)
                        except (ValueError, KeyError, TypeError) as error:
                            history["errors"].append({"request": identifier, "error": str(error)})
                        print(f"Saved review {identifier}; retained {len(saved) + len(history['saved_reviews'])}", flush=True)
                    fill()
            self.verify_amendment(output)
            if history["errors"]:
                raise ValueError("Review processing stopped; new errors retained in " + history_path.name)
            self.retained(output, metadata, cases)
        except Exception as error:
            if not history["errors"]:
                history["errors"].append({"stage": "processing", "error": str(error)})
            raise
        finally:
            history["finished_at_utc"] = module.base.now()
            history["status"] = "failed" if history["errors"] else "finished"
            module.base.write_json(history_path, history)
        return history

    def result_data(self, output):
        amendment, _, _ = self.verify_amendment(output)
        metadata, rows, summary, cases, answers = self.original["result_data"](output)
        affected = [(row, condition) for row in rows for condition in self.module.CONDITIONS
                    if row[condition]["review_structural_errors"]]
        processing = {"policy": POLICY, "amendment_file": AMENDMENT,
                      "amendment_sha256": sha((output / AMENDMENT).read_bytes()),
                      "sealed_prior_files": len(amendment["prior_evidence_sha256"]),
                      "structurally_invalid_ratings": sum(len(row[condition]["review_structural_errors"]) for row, condition in affected),
                      "affected_answers": len(affected),
                      "affected_cases": len({row["case_id"] for row, _ in affected}),
                      "affected_case_ids": sorted({row["case_id"] for row, _ in affected})}
        for language, totals in summary["totals"].items():
            for condition, values in totals.items():
                selected = [row for row in rows if language == "all" or row["language"] == language]
                values["structurally_invalid_ratings"] = sum(len(row[condition]["review_structural_errors"]) for row in selected)
                values["structurally_affected_answers"] = sum(bool(row[condition]["review_structural_errors"]) for row in selected)
        controls, _, _ = self.module.calibration_data(output)
        calibration_errors, calibration_cases = 0, set()
        for reviewer in (1, 2):
            for start in (0, 5):
                request = self.module.get_request(output / "calibration", f"calibration-{reviewer}-{start + 1:03d}")
                for row in self.validate_review(json.loads(request["output"]), controls[start:start + 5]):
                    case = next(case for case in controls[start:start + 5] if case["id"] == row["case_id"])
                    for rating in row["ratings"]:
                        if coverage_error(case, rating):
                            calibration_errors += 1
                            calibration_cases.add(case["id"])
        processing.update(calibration_structurally_invalid_ratings=calibration_errors,
                          calibration_affected_cases=len(calibration_cases))
        summary["processing"] = self.last_processing = processing
        return metadata, rows, summary, cases, answers

    def report_text(self, metadata, summary):
        processing = summary["processing"]
        return self.original["report_text"](metadata, summary) + (
            "\n## Conservative processing amendment\n\n" + POLICY["timing"] + " " + POLICY["coverage"] + " "
            + POLICY["retention"] + "\n\n"
            + f"Structurally invalid ratings: {processing['structurally_invalid_ratings']}; "
            + f"affected answers: {processing['affected_answers']}; affected cases: {processing['affected_cases']}. "
            + f"Calibration structurally invalid ratings: {processing['calibration_structurally_invalid_ratings']}; "
            + f"calibration affected cases: {processing['calibration_affected_cases']}. "
            + f"The [sealed policy]({AMENDMENT}) preserves {processing['sealed_prior_files']} prior evidence files.\n")

    def audit(self, output):
        self.verify_amendment(output)
        self.last_processing = None
        with contextlib.redirect_stdout(io.StringIO()):
            self.original["audit"](output)
        value = json.loads((output / "evidence-audit.json").read_text())
        value.update(processing=self.last_processing, processing_amendment="verified",
                     prior_evidence_preservation="verified")
        self.module.base.write_json(output / "evidence-audit.json", value)
        print(json.dumps(value), flush=True)
        return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("amend", "run", "report", "audit"))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--catalog", type=Path)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--timeout", type=int, default=600)
    args = parser.parse_args()
    if not 1 <= args.workers <= 4 or args.timeout < 1:
        parser.error("workers must be 1–4 and timeout must be positive")
    processor = Processor()
    if args.action == "amend":
        processor.amend(args.output, args.catalog)
    elif args.action == "run":
        processor.run(args.output, args.workers, args.catalog, args.timeout)
    elif args.action == "report":
        processor.verify_amendment(args.output)
        processor.module.report(args.output)
    else:
        processor.audit(args.output)


if __name__ == "__main__":
    main()
