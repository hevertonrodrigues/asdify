import csv
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("project_validation", ROOT / "scripts/validate.py")
VALIDATION = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATION)
RATING_HEADER = ["reviewer", "case_id", "arm", "meaning_fidelity", "clarity", "signal_density", "structure", "calibration", "fit_for_purpose", "hard_fail", "notes"]


class ProjectTests(unittest.TestCase):
    def test_structure_and_examples(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/validate.py")], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Validation OK", result.stdout)

    def test_installer_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as work:
            args = ["bash", str(ROOT / "scripts/install.sh"), "--agent", "claude", "--scope", "project"]
            first = subprocess.run(args, cwd=work, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            installed = Path(work) / ".claude/skills/asdify/SKILL.md"
            self.assertTrue(installed.exists())
            self.assertEqual({path.name for path in installed.parent.parent.iterdir()}, {"asdify"})
            installed.write_text("local customization", encoding="utf-8")
            again = subprocess.run(args, cwd=work, capture_output=True, text=True)
            self.assertNotEqual(again.returncode, 0)
            self.assertIn("Refusing", again.stderr)
            self.assertEqual(installed.read_text(encoding="utf-8"), "local customization")
            forced = subprocess.run(args + ["--force"], cwd=work, capture_output=True, text=True)
            self.assertEqual(forced.returncode, 0, forced.stderr)
            self.assertEqual(installed.read_bytes(), (ROOT / "skills/asdify/SKILL.md").read_bytes())

    def test_codex_project_install_copies_complete_skill(self):
        with tempfile.TemporaryDirectory(prefix="asdify project ") as work:
            proc = subprocess.run(
                ["bash", str(ROOT / "scripts/install.sh"), "--agent", "codex", "--scope", "project"],
                cwd=work, capture_output=True, text=True,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr)
            source = ROOT / "skills/asdify"
            installed = Path(work) / ".agents/skills/asdify"
            self.assertEqual({path.name for path in installed.parent.iterdir()}, {"asdify"})
            source_files = {path.relative_to(source): path.read_bytes() for path in source.rglob("*") if path.is_file()}
            installed_files = {path.relative_to(installed): path.read_bytes() for path in installed.rglob("*") if path.is_file()}
            self.assertIn(Path("references/quality-rubric.md"), installed_files)
            self.assertIn(Path("references/edge-cases.md"), installed_files)
            self.assertEqual(installed_files, source_files)

    def test_installer_refuses_symlink_without_changing_target(self):
        with tempfile.TemporaryDirectory() as work:
            root = Path(work)
            target = root / "existing"
            target.mkdir()
            sentinel = target / "keep.txt"
            sentinel.write_text("preserve this", encoding="utf-8")
            dest = root / ".claude/skills/asdify"
            dest.parent.mkdir(parents=True)
            dest.symlink_to(target, target_is_directory=True)
            proc = subprocess.run(
                ["bash", str(ROOT / "scripts/install.sh"), "--agent", "claude", "--scope", "project"],
                cwd=work, capture_output=True, text=True,
            )
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("Refusing", proc.stderr)
            self.assertTrue(dest.is_symlink())
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "preserve this")

    def test_installer_rejects_invalid_arguments_without_writing(self):
        invalid_args = [
            [], ["--agent"], ["--agent", "unknown", "--scope", "project"],
            ["--agent", "claude", "--scope", "unknown"], ["--unknown"],
            ["--agent", "cursor", "--scope", "user"],
        ]
        with tempfile.TemporaryDirectory() as work:
            for args in invalid_args:
                with self.subTest(args=args):
                    proc = subprocess.run(["bash", str(ROOT / "scripts/install.sh"), *args], cwd=work, capture_output=True, text=True)
                    self.assertEqual(proc.returncode, 2, proc.stderr)
                    self.assertEqual(list(Path(work).iterdir()), [])

    def test_cursor_adapter(self):
        with tempfile.TemporaryDirectory() as work:
            proc = subprocess.run(["bash", str(ROOT / "scripts/install.sh"), "--agent", "cursor", "--scope", "project"], cwd=work, capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            installed = Path(work) / ".cursor/rules/asdify.mdc"
            self.assertEqual(installed.read_bytes(), (ROOT / "integrations/cursor-rule.mdc").read_bytes())
            self.assertEqual({path.name for path in installed.parent.iterdir()}, {"asdify.mdc"})

    def test_empty_scores_do_not_produce_claims(self):
        proc = subprocess.run([sys.executable, str(ROOT / "scripts/score_ratings.py"), str(ROOT / "benchmarks/ratings-template.csv")], capture_output=True, text=True)
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("No ratings", proc.stderr)

    def test_scoring_paired_rows(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "test.csv"
            with path.open("w", newline="", encoding="utf-8") as fh:
                writer = csv.writer(fh)
                writer.writerow(RATING_HEADER)
                for arm in ("A", "B"):
                    writer.writerow(["reviewer1", "case1", arm, 5, 4, 4, 5, 5, 5, 0, ""])
            proc = subprocess.run([sys.executable, str(ROOT / "scripts/score_ratings.py"), str(path)], capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertIn("Arm A:", proc.stdout)
            self.assertIn("Arm B:", proc.stdout)


class RatingTests(unittest.TestCase):
    def run_ratings(self, rows, header=None):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "ratings.csv"
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.writer(handle)
                writer.writerow(RATING_HEADER if header is None else header)
                writer.writerows(rows)
            return subprocess.run([sys.executable, str(ROOT / "scripts/score_ratings.py"), str(path)], capture_output=True, text=True)

    @staticmethod
    def rating(arm, value=5, case="en-01", hard_fail=0):
        return ["reviewer1", case, arm, *([value] * 6), hard_fail, ""]

    def assert_clean_error(self, proc, message):
        self.assertNotEqual(proc.returncode, 0)
        self.assertEqual(proc.stdout, "")
        self.assertIn(message, proc.stderr)
        self.assertNotIn("Traceback", proc.stderr)

    def test_descriptive_statistics_and_rating_failure_denominator(self):
        proc = self.run_ratings([
            self.rating("A", 1, hard_fail=1), self.rating("B", 4),
            self.rating("A", 3, case="pt-01"), self.rating("B", 5, case="pt-01"),
        ])
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("Arm A: 2 blind ratings, hard failures: 1/2 (50.0% of ratings)", proc.stdout)
        self.assertIn("Arm B: 2 blind ratings, hard failures: 0/2 (0.0% of ratings)", proc.stdout)
        self.assertIn("meaning_fidelity: median 2, mean 2.00", proc.stdout)
        self.assertIn("meaning_fidelity: median 4.5, mean 4.50", proc.stdout)
        self.assertIn("including hard failures", proc.stdout)
        self.assertIn("No winner is inferred", proc.stdout)

    def test_repeated_runs_are_paired_separately(self):
        rows = [self.rating(arm) + [run] for run in ("run-1", "run-2") for arm in ("A", "B")]
        proc = self.run_ratings(rows, RATING_HEADER + ["run_id"])
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("2 run(s), 2 paired reviewer-case evaluations", proc.stdout)
        self.assertIn("Arm A: 2 blind ratings", proc.stdout)

    def test_arms_from_different_runs_do_not_form_a_pair(self):
        proc = self.run_ratings([self.rating("A") + ["run-1"], self.rating("B") + ["run-2"]], RATING_HEADER + ["run_id"])
        self.assert_clean_error(proc, "Unpaired evaluation")

    def test_duplicate_rating_is_rejected(self):
        proc = self.run_ratings([self.rating("A"), self.rating("B"), self.rating("A")])
        self.assert_clean_error(proc, "duplicate arm")

    def test_unpaired_rating_is_rejected(self):
        self.assert_clean_error(self.run_ratings([self.rating("A")]), "both A and B required")

    def test_score_must_be_an_integer_in_range(self):
        for value in (0, 6, "4.5", "", "excellent"):
            with self.subTest(value=value):
                proc = self.run_ratings([self.rating("A", value), self.rating("B")])
                self.assert_clean_error(proc, "meaning_fidelity must be")

    def test_invalid_arm_and_failure_flag(self):
        self.assert_clean_error(self.run_ratings([self.rating("C")]), "arm must be A or B")
        self.assert_clean_error(self.run_ratings([self.rating("A", hard_fail=2)]), "hard_fail must be 0 or 1")

    def test_missing_identity_is_rejected(self):
        for column in (0, 1):
            with self.subTest(column=column):
                row = self.rating("A")
                row[column] = " "
                self.assert_clean_error(self.run_ratings([row]), "must be nonempty")
        self.assert_clean_error(self.run_ratings([self.rating("A") + [""]], RATING_HEADER + ["run_id"]), "must be nonempty")

    def test_malformed_headers_are_rejected(self):
        for header, message in (
            (RATING_HEADER[:-2], "missing required columns"),
            (RATING_HEADER + ["arm"], "duplicate columns"),
            (RATING_HEADER + ["model"], "unsupported columns"),
        ):
            with self.subTest(header=header):
                self.assert_clean_error(self.run_ratings([], header), message)

    def test_truncated_and_extra_rows_have_clean_errors(self):
        for row in (["r1", "en-01", "A"], self.rating("A") + ["extra"]):
            with self.subTest(row=row):
                self.assert_clean_error(self.run_ratings([row]), "number of cells must match")
        # Reproduces the original int(None) crash with hard_fail preceding scores.
        header = ["reviewer", "case_id", "arm", "hard_fail", *RATING_HEADER[3:9]]
        self.assert_clean_error(self.run_ratings([["r1", "en-01", "A", "0"]], header), "number of cells must match")

    def test_optional_notes_column_can_be_omitted(self):
        proc = self.run_ratings([self.rating("A")[:-1], self.rating("B")[:-1]], RATING_HEADER[:-1])
        self.assertEqual(proc.returncode, 0, proc.stderr)


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "benchmarks").mkdir()
        self.patch_root = patch.object(VALIDATION, "ROOT", self.root)
        self.patch_root.start()
        self.addCleanup(self.patch_root.stop)

    @staticmethod
    def valid_cases():
        return [
            {"id": f"case-{n}", "lang": "en" if n % 2 else "pt-BR", "task": "Preserve the condition.", "invariants": ["condition"], "risk": "Lost condition"}
            for n in range(6)
        ]

    def write_cases(self, cases):
        (self.root / "benchmarks/cases.jsonl").write_text("\n".join(json.dumps(case) for case in cases) + "\n", encoding="utf-8")

    def test_readme_images_and_html_links_are_checked(self):
        readme = self.root / "README.md"
        for content in ('![Example](missing.svg)', '<img src="missing.svg" alt="Example">', '<a href="missing.md">Guide</a>', '<source srcset="missing.svg 1x">'):
            with self.subTest(content=content):
                readme.write_text(content, encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "missing"):
                    VALIDATION.validate_links()

    def test_empty_link_destinations_report_clean_errors(self):
        for content in ('[Example]( )', '[Example]()', '<img src="" alt="Example">'):
            with self.subTest(content=content):
                (self.root / "README.md").write_text(content, encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "empty link destination"):
                    VALIDATION.validate_links()

    def test_existing_images_external_links_and_fragments_pass(self):
        (self.root / "example image.svg").write_text("fixture", encoding="utf-8")
        (self.root / "README.md").write_text(
            '<img src="example%20image.svg" alt="Example">\n'
            '[Section](#try-it) [External](https://example.com/guide)\n'
            '<a href="README.md#try-it">Try it</a>', encoding="utf-8",
        )
        VALIDATION.validate_links()

    def write_svg(self, content):
        folder = self.root / "assets/readme"
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "example.svg").write_text(content, encoding="utf-8")

    def test_accessible_vector_asset_passes(self):
        self.write_svg('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><title>Example</title><desc>How it works</desc><path d="M0 0 L100 100"/></svg>')
        self.assertEqual(VALIDATION.validate_readme_assets(), 1)

    def test_malformed_or_inaccessible_vector_assets_fail(self):
        for content, message in (
            ('<svg', 'invalid SVG XML'),
            ('<svg xmlns="http://www.w3.org/2000/svg"/>', 'viewBox'),
            ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"/>', 'accessible title'),
            ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><title>Example</title></svg>', 'accessible desc'),
            ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 NaN 100"/>', 'viewBox'),
        ):
            with self.subTest(content=content):
                self.write_svg(content)
                with self.assertRaisesRegex(ValueError, message):
                    VALIDATION.validate_readme_assets()

    def test_vector_assets_do_not_depend_on_scripts_or_external_images(self):
        for element in ('<script/>', '<foreignObject/>', '<image href="https://example.com/image.png"/>', '<use href="https://example.com/icons.svg#icon"/>'):
            with self.subTest(element=element):
                self.write_svg(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><title>Example</title><desc>Example</desc>{element}</svg>')
                with self.assertRaisesRegex(ValueError, "self-contained|unsupported external"):
                    VALIDATION.validate_readme_assets()

    def test_valid_bilingual_cases(self):
        self.write_cases(self.valid_cases())
        self.assertEqual(VALIDATION.validate_cases(), 6)

    def test_case_fields_have_correct_types(self):
        for field, value in (("id", []), ("task", True), ("risk", {}), ("lang", 3), ("task", " "), ("invariants", [42]), ("invariants", []), ("invariants", [" "]), ("invariants", "condition")):
            with self.subTest(field=field, value=value):
                cases = self.valid_cases()
                cases[0][field] = value
                self.write_cases(cases)
                with self.assertRaisesRegex(ValueError, field):
                    VALIDATION.validate_cases()

    def test_case_must_be_an_object(self):
        self.write_cases([[], *self.valid_cases()])
        with self.assertRaisesRegex(ValueError, "expected a JSON object"):
            VALIDATION.validate_cases()

    def test_duplicate_case_ids_are_rejected(self):
        cases = self.valid_cases()
        cases[1]["id"] = cases[0]["id"]
        self.write_cases(cases)
        with self.assertRaisesRegex(ValueError, "duplicate id"):
            VALIDATION.validate_cases()

    def test_both_languages_are_required(self):
        cases = self.valid_cases()
        for case in cases:
            case["lang"] = "en"
        self.write_cases(cases)
        with self.assertRaisesRegex(ValueError, "both en and pt-BR"):
            VALIDATION.validate_cases()

    def test_unknown_language_is_rejected(self):
        cases = self.valid_cases()
        cases[0]["lang"] = "fr"
        self.write_cases(cases)
        with self.assertRaisesRegex(ValueError, "lang must be en or pt-BR"):
            VALIDATION.validate_cases()

    def test_minimum_case_count_is_enforced(self):
        self.write_cases(self.valid_cases()[:2])
        with self.assertRaisesRegex(ValueError, "at least 6"):
            VALIDATION.validate_cases()

    def test_invalid_json_reports_case_line(self):
        (self.root / "benchmarks/cases.jsonl").write_text("{broken}\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "case 1: invalid JSON"):
            VALIDATION.validate_cases()

    def write_manifests(self, plugin=None, marketplace=None):
        folder = self.root / ".claude-plugin"
        folder.mkdir(exist_ok=True)
        for name, value in (("plugin", plugin), ("marketplace", marketplace)):
            if value is None:
                value = json.loads((ROOT / f".claude-plugin/{name}.json").read_text(encoding="utf-8"))
            (folder / f"{name}.json").write_text(json.dumps(value), encoding="utf-8")

    def test_valid_local_plugin_manifests(self):
        self.write_manifests()
        VALIDATION.validate_manifests()

    def test_plugin_name_and_version_are_checked(self):
        for field, value, message in (("name", "other-skill", "name must match"), ("version", "latest", "major.minor.patch")):
            with self.subTest(field=field):
                plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
                plugin[field] = value
                self.write_manifests(plugin=plugin)
                with self.assertRaisesRegex(ValueError, message):
                    VALIDATION.validate_manifests()

    def test_marketplace_matching_source_and_version_are_checked(self):
        for change, message in (
            ({"name": "other-skill"}, "exactly one entry"),
            ({"source": "./missing"}, "source must resolve"),
            ({"version": "9.9.9"}, "versions must match"),
        ):
            with self.subTest(change=change):
                marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
                marketplace["plugins"][0].update(change)
                self.write_manifests(marketplace=marketplace)
                with self.assertRaisesRegex(ValueError, message):
                    VALIDATION.validate_manifests()


if __name__ == "__main__":
    unittest.main()
