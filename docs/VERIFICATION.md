# Verification

Local checks for the README refresh and initial ASDify history, 8 October 2026.

## Scope

The English and Portuguese READMEs include a manual trial, separate host installation choices, copyable examples, and six original SVG illustrations. Development notes and the unchanged draft archive are grouped under [docs/archive](archive/INDEX.md).

The SVGs are self-contained vectors with accessible titles and descriptions. The validator checks their XML, dimensions, and references, plus relative Markdown and HTML image/link destinations. It does not make network requests or verify remote URLs and section anchors.

## Checks

Run from the repository root:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
bash -n scripts/install.sh
```

- Structural validation: PASS, including 6 SVGs and 16 bilingual cases.
- Unit tests: PASS, 36 tests covering installation, scoring, fixtures, manifests, links, and vector assets.
- Installer Bash syntax: PASS.
- SVG inspection: all six native vector previews rendered and visually reviewed for layout, text overflow, and contrast. Preview conversion used ReportLab with Arial and Poppler; GitHub browser rendering was not verified.
- README review: no inspiration sections; navigation and recipe anchors checked; copyable revised text matches the illustrations.

Environment: Darwin 27.0.0, Python 3.14.6. All installer tests used temporary directories. No user-level installation was performed.

## Evidence limits

Before/after examples are editorial illustrations. No live-model improvement has been established. Installer tests use temporary directories; actual host activation remains separately tracked in [compatibility](COMPATIBILITY.md).

Public availability and remote CI are not yet verified. Publication uses GitHub CLI; the current session has not authenticated successfully.
