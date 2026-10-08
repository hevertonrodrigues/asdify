# Verification

Local multilingual update checks and the earlier v0.1.0 verification record, 8 October 2026.

## Multilingual update: local checks

- Structural validation: PASS, including 82 installer IDs, 6 existing SVGs, 9 language READMEs, language navigation, and 49 multilingual regression inputs (31 same-language tasks and 18 translations).
- Unit tests: PASS, 61 tests. The 10 added tests cover the language registry, Unicode, missing or empty READMEs, language navigation, dynamic locale coverage, invalid targets, and missing translation source/target coverage. The existing Codex installation check also verifies that the translation reference is copied.
- Installer matrix: PASS across the same 160 supported installations and 4 rejected unsupported scopes, using temporary directories.
- Installer Bash syntax, skill-creator frontmatter validation, and `git diff --check`: PASS.
- Installation guidance: checked npm's CLI-download confirmation against [npm documentation](https://docs.npmjs.com/cli/v11/commands/npm-exec/#description), and native Cursor project/user paths against [Cursor documentation](https://cursor.com/docs/skills#skill-directories). The local Cursor path checks remain filesystem tests, not a Cursor activation session.

These checks ran on the local working tree. They do not establish that the changed revision has passed remote CI. The seven new READMEs and multilingual examples are translations and editorial examples, not recorded live-model results or independently reviewed native-speaker output. No live translation study was run. See [language coverage and support](LANGUAGES.md) for the locale registry and review limits.

## v0.1.0 scope

The English and Portuguese READMEs include a manual trial, installation choices, copyable examples, and six original SVG illustrations. The installer registry covers 79 upstream agent mappings plus 3 compatibility IDs. See the [complete destination table](HARNESSES.md). Development notes and the unchanged draft archive are grouped under [docs/archive](archive/INDEX.md).

The SVGs are self-contained vectors with accessible titles and descriptions. The validator checks their XML, dimensions, and references, plus relative Markdown and HTML image/link destinations. It does not make network requests or verify remote URLs and section anchors.

## v0.1.0 checks

Run from the repository root:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
bash -n scripts/install.sh
```

- Structural validation: PASS, including 82 installer IDs, 6 SVGs, and 16 bilingual cases.
- Unit tests: PASS, 51 tests covering installation, scoring, fixtures, manifests, links, and vector assets.
- Installation matrix: PASS, 160 successful installations across supported ID/scope combinations; 4 unsupported scopes rejected. These are filesystem checks, not 160 host sessions.
- Installer Bash syntax: PASS.
- SVG inspection: all six native vector previews rendered and visually reviewed for layout, text overflow, and contrast. Preview conversion used ReportLab with Arial and Poppler; GitHub browser rendering was not verified.
- README review: no inspiration sections; navigation and recipe anchors checked; copyable revised text matches the illustrations.

Environment: Darwin 27.0.0, Python 3.14.6. All installer tests used temporary directories; no persistent installation into the user's actual host directories was performed.

## Host and CLI checks

- Codex CLI 0.161.0: one explicit `full`-mode smoke check on `macOS-27.0.1-arm64` read the installed `SKILL.md` and retained all seven material details in the revenue example. The model identifier was not emitted. See the [recorded command, output, and limits](demos/codex-full-2026-10-08.md).
- Skills CLI 1.7.1 on Node 26.7.0: `add <local repository> --list` discovered exactly one skill, `asdify`.
- Remote Skills CLI discovery: `add hevertonrodrigues/asdify --list` was blocked because child Git could not resolve `github.com` in the sandbox. No external CLI installation or skills.sh indexing was verified.

## Public repository and CI

The [public repository](https://github.com/hevertonrodrigues/asdify) and [v0.1.0 release](https://github.com/hevertonrodrigues/asdify/releases/tag/v0.1.0) are confirmed. [CI run 37842301297](https://github.com/hevertonrodrigues/asdify/actions/runs/37842301297) passed for release commit `729b1b7ae54d68a808e051ea6dee331a4915aa6c`: Ubuntu and macOS, each with Python 3.12 and 3.13. All four jobs passed installer syntax, structural validation, and the test suite. This records that commit, not the status of future commits.

## Evidence limits

Before/after illustrations are editorial examples. The separate Codex run is one observed result, not a comparative study. Broad quality gains, automatic activation, other modes, reference loading, and other host sessions remain unverified. See [compatibility](COMPATIBILITY.md) for the distinction between installation layouts, host activation, and model effectiveness.
