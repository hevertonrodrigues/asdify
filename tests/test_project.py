import csv
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from contextlib import contextmanager
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("project_validation", ROOT / "scripts/validate.py")
VALIDATION = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATION)
RATING_HEADER = ["reviewer", "case_id", "arm", "meaning_fidelity", "clarity", "signal_density", "structure", "calibration", "fit_for_purpose", "hard_fail", "notes"]


class ProjectTests(unittest.TestCase):
    def setUp(self):
        # Even argument-validation regressions must never reach the real user's home.
        self.environment = tempfile.TemporaryDirectory(prefix="asdify isolated home ")
        self.addCleanup(self.environment.cleanup)
        self.env_patch = patch.dict(os.environ, {
            "HOME": self.environment.name,
            "XDG_CONFIG_HOME": str(Path(self.environment.name) / "config"),
            "CODEX_HOME": str(Path(self.environment.name) / "codex"),
            "CLAUDE_CONFIG_DIR": str(Path(self.environment.name) / "claude"),
        })
        self.env_patch.start()
        self.addCleanup(self.env_patch.stop)

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
            self.assertIn(Path("references/translation.md"), installed_files)
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


class InstallerRegistryTests(unittest.TestCase):
    """Exercise host mappings without touching any real agent configuration."""

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="asdify hosts ")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.home = self.root / "home with spaces"
        self.project = self.root / "project with spaces"
        self.home.mkdir()
        self.project.mkdir()
        self.env = dict(os.environ, HOME=str(self.home))
        for name in ("XDG_CONFIG_HOME", "CODEX_HOME", "CLAUDE_CONFIG_DIR", "AUTOHAND_HOME", "GROK_HOME", "HERMES_HOME", "VIBE_HOME", "OPENCLAW_HOME"):
            self.env.pop(name, None)

    def install(self, *args, env=None, cwd=None):
        return subprocess.run(
            ["bash", str(ROOT / "scripts/install.sh"), *args],
            cwd=self.project if cwd is None else cwd, env=self.env if env is None else env,
            capture_output=True, text=True,
        )

    @contextmanager
    def isolated_case(self):
        with tempfile.TemporaryDirectory(dir=self.root) as temporary:
            home = Path(temporary) / "home with spaces"
            project = Path(temporary) / "project with spaces"
            home.mkdir()
            project.mkdir()
            yield home, project, dict(self.env, HOME=str(home))

    @staticmethod
    def registry():
        lines = (ROOT / "integrations/agents.tsv").read_text(encoding="utf-8").splitlines()
        return list(csv.reader((line for line in lines if line and not line.startswith("#")), delimiter="\t"))

    @staticmethod
    def file_contents(folder):
        return {path.relative_to(folder): path.read_bytes() for path in folder.rglob("*") if path.is_file()}

    def assert_complete_skill(self, destination):
        self.assertTrue((destination / "SKILL.md").is_file(), destination)
        self.assertFalse(destination.is_symlink())
        self.assertEqual(self.file_contents(destination), self.file_contents(ROOT / "skills/asdify"))

    def test_every_registered_host_and_scope(self):
        for agent, _, project_path, user_path, kind, _ in self.registry():
            for scope, template in (("project", project_path), ("user", user_path)):
                with self.subTest(agent=agent, scope=scope), self.isolated_case() as (home, project, env):
                    proc = self.install("--agent", agent, "--scope", scope, env=env, cwd=project)
                    if template == "-":
                        self.assertEqual(proc.returncode, 2, proc.stderr)
                        self.assertEqual(list(home.iterdir()), [])
                        self.assertEqual(list(project.iterdir()), [])
                        continue
                    self.assertEqual(proc.returncode, 0, proc.stderr)
                    roots = {
                        "{HOME}": home, "{XDG_CONFIG_HOME}": home / ".config",
                        "{CLAUDE_CONFIG_DIR}": home / ".claude", "{AUTOHAND_HOME}": home / ".autohand",
                        "{GROK_HOME}": home / ".grok", "{HERMES_HOME}": home / ".hermes",
                        "{VIBE_HOME}": home / ".vibe", "{OPENCLAW_HOME}": home / ".openclaw",
                    }
                    if scope == "project":
                        destination = project / template
                        self.assertEqual(list(home.iterdir()), [])
                    else:
                        prefix, relative = template.split("/", 1)
                        destination = roots[prefix] / relative
                        self.assertEqual(list(project.iterdir()), [])
                    if kind == "skill":
                        destination /= "asdify"
                        self.assert_complete_skill(destination)
                    else:
                        self.assertEqual(destination.read_bytes(), (ROOT / "integrations/cursor-rule.mdc").read_bytes())
                    self.assertEqual({path.name for path in destination.parent.iterdir()}, {destination.name})

    def test_representative_destinations_independent_of_registry(self):
        # These literal paths anchor the matrix above to documented host conventions.
        for agent, scope, relative in (
            ("claude-code", "project", ".claude/skills/asdify"),
            ("codex", "user", ".agents/skills/asdify"),
            ("github-copilot", "user", ".copilot/skills/asdify"),
            ("gemini-cli", "user", ".gemini/skills/asdify"),
            ("cursor-skill", "user", ".cursor/skills/asdify"),
            ("opencode", "user", ".config/opencode/skills/asdify"),
            ("windsurf", "user", ".codeium/windsurf/skills/asdify"),
            ("openclaw", "project", "skills/asdify"),
        ):
            with self.subTest(agent=agent, scope=scope), self.isolated_case() as (home, project, env):
                proc = self.install("--agent", agent, "--scope", scope, env=env, cwd=project)
                self.assertEqual(proc.returncode, 0, proc.stderr)
                self.assert_complete_skill((home if scope == "user" else project) / relative)

    def test_list_is_complete_and_never_creates_configuration(self):
        env = dict(self.env, HOME=str(self.root / "nonexistent home"), XDG_CONFIG_HOME="relative")
        proc = self.install("--list", env=env)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        for agent, _, project_path, user_path, kind, _ in self.registry():
            with self.subTest(agent=agent):
                lines = [line.split() for line in proc.stdout.splitlines() if line.split() and line.split()[0] == agent]
                self.assertEqual(len(lines), 1, proc.stdout)
                self.assertIn(kind, lines[0])
                self.assertIn("project", lines[0][1])
                self.assertEqual("user" in lines[0][1], user_path != "-")
        self.assertFalse((self.root / "nonexistent home").exists())
        self.assertEqual(list(self.project.iterdir()), [])
        self.assertEqual(list(self.home.iterdir()), [])

    def test_compatibility_aliases_copy_the_same_content(self):
        for names, relative in (
            (("claude", "claude-code"), ".claude/skills/asdify/SKILL.md"),
            (("cursor", "cursor-rule"), ".cursor/rules/asdify.mdc"),
        ):
            outputs = []
            for agent in names:
                with self.subTest(agent=agent), self.isolated_case() as (_, project, env):
                    proc = self.install("--agent", agent, "--scope", "project", env=env, cwd=project)
                    self.assertEqual(proc.returncode, 0, proc.stderr)
                    outputs.append((project / relative).read_bytes())
            self.assertEqual(outputs[0], outputs[1])

    def test_xdg_user_roots_and_fallbacks(self):
        for agent, suffix in (("opencode", "opencode/skills/asdify"), ("goose", "goose/skills/asdify"), ("amp", "agents/skills/asdify")):
            for value in (None, "", "relative/path", str(self.root / "custom config")):
                with self.subTest(agent=agent, xdg=value), self.isolated_case() as (home, project, env):
                    if value is not None:
                        env["XDG_CONFIG_HOME"] = value
                    base = Path(value) if value and Path(value).is_absolute() else home / ".config"
                    proc = self.install("--agent", agent, "--scope", "user", "--force", env=env, cwd=project)
                    self.assertEqual(proc.returncode, 0, proc.stderr)
                    self.assert_complete_skill(base / suffix)
                    self.assertEqual(list(project.iterdir()), [])

    def test_custom_host_roots_and_invalid_relative_roots(self):
        for agent, variable in (
            ("claude-code", "CLAUDE_CONFIG_DIR"), ("autohand-code", "AUTOHAND_HOME"),
            ("grok", "GROK_HOME"), ("hermes-agent", "HERMES_HOME"),
            ("mistral-vibe", "VIBE_HOME"),
        ):
            with self.subTest(agent=agent), self.isolated_case() as (home, project, env):
                custom = home / "custom config"
                env[variable] = str(custom)
                proc = self.install("--agent", agent, "--scope", "user", env=env, cwd=project)
                self.assertEqual(proc.returncode, 0, proc.stderr)
                self.assert_complete_skill(custom / "skills/asdify")
                env[variable] = "relative/config"
                proc = self.install("--agent", agent, "--scope", "user", env=env, cwd=project)
                self.assertEqual(proc.returncode, 2, proc.stderr)
                self.assertEqual(list(project.iterdir()), [])

    def test_openclaw_existing_home_fallbacks(self):
        for existing, expected in (
            ((".moltbot",), ".moltbot"),
            ((".clawdbot", ".moltbot"), ".clawdbot"),
            ((".openclaw", ".clawdbot", ".moltbot"), ".openclaw"),
        ):
            with self.subTest(existing=existing), self.isolated_case() as (home, project, env):
                for name in existing:
                    (home / name).mkdir()
                proc = self.install("--agent", "openclaw", "--scope", "user", env=env, cwd=project)
                self.assertEqual(proc.returncode, 0, proc.stderr)
                self.assert_complete_skill(home / expected / "skills/asdify")
                for name in set(existing) - {expected}:
                    self.assertEqual(list((home / name).iterdir()), [])

    def test_force_replaces_only_the_selected_skill(self):
        destination = self.home / ".agents/skills/asdify"
        destination.mkdir(parents=True)
        (destination / "local.txt").write_text("custom", encoding="utf-8")
        sibling = destination.parent / "another-skill"
        sibling.mkdir()
        (sibling / "SKILL.md").write_text("keep me", encoding="utf-8")
        args = ("--agent", "codex", "--scope", "user")
        refused = self.install(*args)
        self.assertNotEqual(refused.returncode, 0)
        self.assertEqual(self.file_contents(destination), {Path("local.txt"): b"custom"})
        forced = self.install(*args, "--force")
        self.assertEqual(forced.returncode, 0, forced.stderr)
        self.assert_complete_skill(destination)
        self.assertEqual(self.file_contents(sibling), {Path("SKILL.md"): b"keep me"})

    def test_bad_identifiers_and_arguments_have_no_side_effects(self):
        for args in (
            ["--agent", "../../escape", "--scope", "user"],
            ["--agent", "claude;touch marker", "--scope", "user"],
            ["--agent", "$(touch marker)", "--scope", "project"],
            ["--agent", "Claude", "--scope", "project"],
            ["--agent", "", "--scope", "project"],
            ["--agent", "claude", "--scope", "../../escape"],
            ["--scope", "user"], ["--agent", "claude", "--scope"],
            ["--list", "--agent", "claude"], ["--list", "--force"],
        ):
            with self.subTest(args=args):
                proc = self.install(*args)
                self.assertEqual(proc.returncode, 2, proc.stderr)
                self.assertEqual(list(self.home.iterdir()), [])
                self.assertEqual(list(self.project.iterdir()), [])

    def test_force_never_changes_a_symlink_target(self):
        for agent, relative in (("claude", ".claude/skills/asdify"), ("cursor", ".cursor/rules/asdify.mdc")):
            for dangling in (False, True):
                with self.subTest(agent=agent, dangling=dangling):
                    outside = self.root / f"outside-{agent}-{dangling}"
                    if not dangling:
                        if agent == "claude":
                            outside.mkdir()
                            (outside / "keep.txt").write_text("leave this alone", encoding="utf-8")
                        else:
                            outside.write_text("leave this alone", encoding="utf-8")
                    destination = self.project / relative
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    if destination.exists():
                        if destination.is_dir():
                            shutil.rmtree(destination)
                        else:
                            destination.unlink()
                    destination.symlink_to(outside, target_is_directory=agent == "claude")
                    refused = self.install("--agent", agent, "--scope", "project")
                    self.assertNotEqual(refused.returncode, 0)
                    self.assertTrue(destination.is_symlink())
                    forced = self.install("--agent", agent, "--scope", "project", "--force")
                    self.assertEqual(forced.returncode, 0, forced.stderr)
                    self.assertFalse(destination.is_symlink())
                    if dangling:
                        self.assertFalse(outside.exists())
                    elif agent == "claude":
                        self.assertEqual(self.file_contents(outside), {Path("keep.txt"): b"leave this alone"})
                    else:
                        self.assertEqual(outside.read_text(encoding="utf-8"), "leave this alone")

    def test_symlinked_install_parent_is_refused_even_with_force(self):
        for agent, parent in (("claude", ".claude"), ("cursor", ".cursor")):
            with self.subTest(agent=agent):
                outside = self.root / f"external-{agent}"
                outside.mkdir()
                sentinel = outside / "keep.txt"
                sentinel.write_text("preserve", encoding="utf-8")
                (self.project / parent).symlink_to(outside, target_is_directory=True)
                for force in ([], ["--force"]):
                    proc = self.install("--agent", agent, "--scope", "project", *force)
                    self.assertNotEqual(proc.returncode, 0)
                    self.assertEqual(list(outside.iterdir()), [sentinel])
                    self.assertEqual(sentinel.read_text(encoding="utf-8"), "preserve")


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
        self.write_languages()
        self.patch_root = patch.object(VALIDATION, "ROOT", self.root)
        self.patch_root.start()
        self.addCleanup(self.patch_root.stop)

    @staticmethod
    def valid_cases():
        cases = [
            {"id": f"case-{n}", "lang": "en" if n % 2 else "pt-BR", "task": "Preserve the condition.", "invariants": ["condition"], "risk": "Lost condition"}
            for n in range(6)
        ]
        cases[0]["target_lang"] = "en"
        cases[1]["target_lang"] = "pt-BR"
        return cases

    def write_languages(self, entries=None):
        if entries is None:
            entries = [
                {"tag": "en", "name": "English", "readme": "README.md"},
                {"tag": "pt-BR", "name": "Português (Brasil)", "readme": "README.pt-BR.md"},
            ]
        folder = self.root / "integrations"
        folder.mkdir(exist_ok=True)
        (folder / "languages.json").write_text(json.dumps(entries, ensure_ascii=False), encoding="utf-8")

    def write_language_readmes(self, entries):
        self.write_languages(entries)
        for entry in entries:
            navigation = " · ".join(f"[{item['name']}]({item['readme']})" for item in entries if item != entry)
            (self.root / entry["readme"]).write_text(f"# ASDify\n\n{navigation}\n", encoding="utf-8")

    def write_cases(self, cases):
        (self.root / "benchmarks/cases.jsonl").write_text("\n".join(json.dumps(case) for case in cases) + "\n", encoding="utf-8")

    @staticmethod
    def agent_row():
        return ["claude-code", "Claude Code", ".claude/skills", "{CLAUDE_CONFIG_DIR}/skills", "skill", "https://code.claude.com/docs/en/skills"]

    def write_registry(self, rows):
        (self.root / "integrations").mkdir(exist_ok=True)
        content = "# agent registry fixture\n" + "\n".join("\t".join(row) for row in rows) + "\n"
        (self.root / "integrations/agents.tsv").write_text(content, encoding="utf-8")

    def test_valid_registry_allows_distinct_aliases_and_scope_limits(self):
        row = self.agent_row()
        self.write_registry([
            row, ["claude", *row[1:]],
            ["cursor", "Cursor", ".cursor/rules/asdify.mdc", "-", "rule", "https://cursor.com/docs/rules"],
        ])
        self.assertEqual(VALIDATION.validate_agent_registry(), 3)

    def test_registry_requires_nonempty_unique_identifiers(self):
        for rows, message in (
            ([], "at least one agent"),
            ([self.agent_row(), self.agent_row()], "duplicate agent id"),
            ([["../escape", *self.agent_row()[1:]]], "invalid agent id"),
            ([self.agent_row()[:-1]], "six nonempty"),
            ([["", *self.agent_row()[1:]]], "six nonempty"),
        ):
            with self.subTest(rows=rows):
                self.write_registry(rows)
                with self.assertRaisesRegex(ValueError, message):
                    VALIDATION.validate_agent_registry()

    def test_registry_rejects_unsafe_destinations_and_unknown_kinds(self):
        for index, value, message in (
            (2, "../skills", "unsafe project"), (2, "/tmp/skills", "unsafe project"),
            (2, ".claude//skills", "unsafe project"), (2, "$(touch marker)/skills", "unsafe project"),
            (2, ".claude/other", "skills directory"),
            (3, "{HOME}/../skills", "unsafe user"), (3, "{UNKNOWN}/skills", "supported root"),
            (3, "/tmp/skills", "supported root"), (3, "{HOME}", "unsafe user"),
            (4, "symlink", "kind must be"),
        ):
            with self.subTest(value=value):
                row = self.agent_row()
                row[index] = value
                self.write_registry([row])
                with self.assertRaisesRegex(ValueError, message):
                    VALIDATION.validate_agent_registry()
        row = self.agent_row()
        row[2:4] = ["-", "-"]
        self.write_registry([row])
        with self.assertRaisesRegex(ValueError, "at least one install scope"):
            VALIDATION.validate_agent_registry()

    def test_registry_requires_documentation_source_urls(self):
        for source in ("file:///tmp/docs", "http://example.com/docs", "https://example.com", "https://user:password@example.com/docs", "https://example.com/bad source"):
            with self.subTest(source=source):
                row = self.agent_row()
                row[-1] = source
                self.write_registry([row])
                with self.assertRaisesRegex(ValueError, "documentation HTTPS URL"):
                    VALIDATION.validate_agent_registry()

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

    def test_language_registry_and_navigation_support_unicode(self):
        entries = [
            {"tag": "en", "name": "English", "readme": "README.md"},
            {"tag": "ja", "name": "日本語", "readme": "README.ja.md"},
            {"tag": "zh-CN", "name": "简体中文", "readme": "README.zh-CN.md"},
            {"tag": "sr-Latn", "name": "Srpski", "readme": "README.sr-Latn.md"},
            {"tag": "es-419", "name": "Español", "readme": "README.es-419.md"},
        ]
        self.write_language_readmes(entries)
        self.assertEqual(VALIDATION.validate_languages(), 5)
        self.assertEqual(set(VALIDATION.load_languages()), {entry["tag"] for entry in entries})

    def test_language_registry_rejects_malformed_entries(self):
        entry = {"tag": "en", "name": "English", "readme": "README.md"}
        for entries, message in (
            ([], "nonempty list"), ({"en": entry}, "nonempty list"),
            ([None], "expected tag"), ([{**entry, "extra": "value"}], "expected tag"),
            ([{"tag": "en", "name": "English"}], "expected tag"),
            ([{**entry, "name": True}], "name must be"),
            ([{**entry, "name": " "}], "name must be"),
            ([{**entry, "name": " English"}], "name must be"),
            ([{**entry, "name": "English\n"}], "name must be"),
            ([{**entry, "tag": "pt-br"}], "tag must use"),
            ([{**entry, "tag": "../escape"}], "tag must use"),
            ([entry, entry], "duplicate language tag"),
            ([{**entry, "readme": "../README.md"}], "readme must be"),
            ([{**entry, "readme": "/tmp/README.md"}], "readme must be"),
            ([{**entry, "readme": "README.en.md"}], "readme must be"),
            ([{"tag": "fr", "name": "Français", "readme": "README.fr.md"}], "canonical en"),
        ):
            with self.subTest(entries=entries):
                self.write_languages(entries)
                with self.assertRaisesRegex(ValueError, message):
                    VALIDATION.load_languages()

    def test_language_readmes_must_exist_and_be_nonempty(self):
        entries = list(VALIDATION.load_languages().values())
        self.write_language_readmes(entries)
        path = self.root / "README.pt-BR.md"
        path.unlink()
        with self.assertRaisesRegex(ValueError, "missing README README.pt-BR.md"):
            VALIDATION.validate_languages()
        path.write_text(" \n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "README must be nonempty"):
            VALIDATION.validate_languages()

    def test_all_readmes_must_link_to_every_other_language(self):
        entries = list(VALIDATION.load_languages().values())
        entries.append({"tag": "ru", "name": "Русский", "readme": "README.ru.md"})
        self.write_language_readmes(entries)
        (self.root / "README.pt-BR.md").write_text("[English](README.md)", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "pt-BR: README language navigation missing README.ru.md"):
            VALIDATION.validate_languages()

    def test_language_registry_invalid_json_is_reported(self):
        (self.root / "integrations/languages.json").write_text("{broken}", encoding="utf-8")
        with self.assertRaises(json.JSONDecodeError):
            VALIDATION.load_languages()

    def test_valid_rewrite_and_translation_cases(self):
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

    def test_every_registered_rewrite_language_is_required(self):
        cases = self.valid_cases()
        for case in cases:
            if "target_lang" not in case:
                case["lang"] = "en"
        self.write_cases(cases)
        with self.assertRaisesRegex(ValueError, "missing rewrite coverage: pt-BR"):
            VALIDATION.validate_cases()

    def test_unknown_language_is_rejected(self):
        cases = self.valid_cases()
        cases[0]["lang"] = "xx"
        self.write_cases(cases)
        with self.assertRaisesRegex(ValueError, "lang must be a registered"):
            VALIDATION.validate_cases()

    def test_new_languages_need_no_hardcoded_validator_changes(self):
        entries = [
            {"tag": "en", "name": "English", "readme": "README.md"},
            {"tag": "ja", "name": "日本語", "readme": "README.ja.md"},
            {"tag": "zh-CN", "name": "简体中文", "readme": "README.zh-CN.md"},
        ]
        self.write_languages(entries)
        cases = []
        for index, entry in enumerate(entries):
            case = {"id": f"rewrite-{index}", "lang": entry["tag"], "task": "意味と条件を保つ。", "invariants": ["条件"], "risk": "条件丢失"}
            cases.extend([case, {**case, "id": f"translate-{index}", "target_lang": entries[(index + 1) % len(entries)]["tag"]}])
        self.write_cases(cases)
        self.assertEqual(VALIDATION.validate_cases(), 6)

    def test_invalid_translation_targets_are_rejected(self):
        for target in (None, True, [], {}, "", " ", "xx", "pt-br"):
            with self.subTest(target=target):
                cases = self.valid_cases()
                cases[0]["target_lang"] = target
                self.write_cases(cases)
                with self.assertRaisesRegex(ValueError, "target_lang must be a registered"):
                    VALIDATION.validate_cases()

    def test_translation_target_must_differ_from_source(self):
        cases = self.valid_cases()
        cases[0]["target_lang"] = cases[0]["lang"]
        self.write_cases(cases)
        with self.assertRaisesRegex(ValueError, "target_lang must differ"):
            VALIDATION.validate_cases()

    def test_translation_source_coverage_is_required(self):
        cases = self.valid_cases()
        del cases[0]["target_lang"]
        self.write_cases(cases)
        with self.assertRaisesRegex(ValueError, "missing translation source coverage: pt-BR"):
            VALIDATION.validate_cases()

    def test_translation_target_coverage_is_required(self):
        entries = list(VALIDATION.load_languages().values())
        entries.append({"tag": "fr", "name": "Français", "readme": "README.fr.md"})
        self.write_languages(entries)
        cases = self.valid_cases()
        cases.extend([
            {"id": "fr-rewrite", "lang": "fr", "task": "Préserver le sens.", "invariants": ["condition"], "risk": "Lost condition"},
            {"id": "fr-translate", "lang": "fr", "target_lang": "pt-BR", "task": "Traduire en portugais.", "invariants": ["condition"], "risk": "Lost condition"},
        ])
        self.write_cases(cases)
        with self.assertRaisesRegex(ValueError, "missing translation target coverage: fr"):
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
