# Verification

Current live-model and local checks, 8–9 October 2026 UTC, followed by the earlier v0.1.0 record.

## 900-case multilingual mode comparison

The [completed mode study](../benchmarks/results/2026-10-09-multilingual-modes-four-workers/report.md) uses 100 new cases per output language across English, Brazilian Portuguese, Spanish, French, German, Japanese, Simplified Chinese, Italian, and Russian. Each locale has 80 native-language tasks and 20 incoming translations. The same cases run without the skill and in `lite`, `full`, `ultra`, and `off`: 900 distinct cases, 3,600 mode tests, 900 baseline answers, 4,500 generated answers, and 9,000 candidate ratings.

- Strict passes across 900 answers per condition: no skill 839 (93.22%); lite 884 (98.22%); full 885 (98.33%); ultra 878 (97.56%); off 879 (97.67%). The [results index](../benchmarks/results/README.md) and [CSV](../benchmarks/results/2026-10-09-multilingual-modes-four-workers/table.csv) give the percentages for every language. `full` gained 51 paired passes and lost 5, a net increase of 5.11 percentage points on this sample.
- Design: `gpt-6.1-sol`, medium generation/review reasoning, Codex CLI 0.161.0, one generation per condition, fresh isolated five-case batches, canonical skill and all three references injected for the modes, no skill in the baseline, and two opaque-label reviews with reversed second-pass display order. `off` loads the skill but disables its optional workflow. These are requested-mode tests, separate from native host activation.
- Meaning coverage: 3,020 authored invariants, assessed across five conditions and two reviews. The stricter result requires every check to be preserved and every exact-format check to pass. It retains disputed omissions and uncertainty; it is not a count of independently established factual errors.
- Calibration: 10 authored good/bad pairs repeated under the five-label protocol and two review passes. All 50 good ratings passed and all 50 deliberately wrong ratings were detected. These repeated controls are separate from the 900 new cases.
- Evidence: the [audit](../benchmarks/results/2026-10-09-multilingual-modes-four-workers/evidence-audit.json) verified all 1,260 primary requests, 4,500 answers, 9,000 ratings, raw usage/events, frozen hashes, reconstructed prompts, and blinding. It recomputed the published table and every answer page without model access. It verifies provenance, not truth.
- Computer load: the initial 32-worker execution was stopped, and the continuation used four live workers. All 185 returned answers were carried unchanged. The [history audit](../benchmarks/results/2026-10-09-multilingual-modes-four-workers/execution-history-audit.json) verifies identical frozen inputs and raw evidence, retention of every successful original answer, and 32 interrupted requests with no returned answers. It does not count those interruptions as new benchmark cases.
- Processing change: after all answers and 775 candidate ratings had returned, one review repeated an invariant ID in four ratings. The [sealed amendment](../benchmarks/results/2026-10-09-multilingual-modes-four-workers/processing-amendment.json) retains 3,772 prior evidence files unchanged. All four affected answers remain uncertain/non-passing; no completed review or answer was regenerated. This conservative policy was adopted after outputs were available and is disclosed separately from the frozen primary design.
- Supplemental source audit: three model assistants reviewed 164 selected cases, covering all 78 cases with a strict flag and 90 seeded cases (four overlap). All 820 candidates received blinded meaning, voice, and format annotations before key release. The [source audit](../benchmarks/results/2026-10-09-multilingual-modes-four-workers/source-audit.md) records real role/uncertainty errors, three changed-meaning judgments on primary passes, and scope/format disagreements. The original strict table is unchanged. The [integrity check](../benchmarks/results/2026-10-09-multilingual-modes-four-workers/source-audit/audit-integrity.json) verifies completeness, blinding inputs, raw-source identity, and sealed hashes, not semantic truth.
- Local software checks: 164 unit tests passed, including 80 added mode-execution, scoring, conservative-processing, interruption-history, source-audit, and focused-retest integrity checks. Structural validation covers the separate 49 public fixtures, nine READMEs, 82 installer IDs, and six SVGs. Whitespace checks for hand-edited files pass; frozen/generated evidence keeps original quoted blank lines and patch context unchanged.

These are automated reviews of a purposive synthetic sample, using one model alias and one repetition. Shared model blind spots, five-case batching, recurring scenario families, different language case sets, no concise-only control, and no independent human/native-speaker or comprehension review limit the conclusions. Compare conditions within each language. A higher score does not guarantee future reliability, native reference loading, or every stylistic preference. `full` averaged 258.0 characters versus 243.4 without the skill; the observed improvement is not a universal shortening result.

## Focused development retest

A [prospective development plan](../benchmarks/results/2026-10-09-language-guards-development/focused-plan.json) selected 100 previously examined cases after the primary source audit: all 34 cases with changed/uncertain meaning or changed voice, plus 66 seeded comparison cases. The candidate strengthens role/group specificity and uncertainty handling, with role examples for German, Japanese, and Portuguese. The subset has 12 English cases and 11 in each other locale.

- Fresh outputs: 500 answers across no skill and all four modes, with 1,000 blinded candidate ratings. The same 10 authored good/bad calibration pairs produced 50 passing good ratings and 50 detected bad ratings; they remain separate from the generated answers.
- Strict passes on the same selected 100 cases, earlier draw → fresh draw: no skill 76 → 87; lite 97 → 97; full 96 → 97; ultra 91 → 96; off 93 → 95. The [report](../benchmarks/results/2026-10-09-language-guards-development/report.md) and [CSV](../benchmarks/results/2026-10-09-language-guards-development/table.csv) give the actual denominators and percentages by language.
- The [evidence audit](../benchmarks/results/2026-10-09-language-guards-development/evidence-audit.json) passed all 189 primary requests, verified frozen inputs, raw outputs, prompt reconstruction, and blinding, and recomputed the published results without model calls.
- Resource limit: two live CLI workers, followed by one source-audit agent at a time. [Resource samples](../benchmarks/results/2026-10-09-language-guards-development/resource-samples.jsonl) include an explicitly invalid first sample and later process snapshots; they do not establish peak usage or overall computer performance.
- Supplemental source review: all 100 cases and 500 fresh candidates were annotated before key release. The [sealed source audit](../benchmarks/results/2026-10-09-language-guards-development/source-audit.md) passed completeness, blinding, raw-source identity, and integrity checks. Six of seven targeted errors were absent; the English ultra approval-scope error remains. The [decision](../benchmarks/results/2026-10-09-language-guards-development/development-decision.md) retains the tested joint patch under the prospective rule. Chinese lite/full declined on the selected subset, and other errors and ambiguities remain. The source audit found four changed-meaning and 14 uncertain judgments on primary passes; strict scores are unchanged.

The subset reuses known failures and changes neighboring tasks within batches. Every condition is a fresh draw, including the no-skill baseline. Sampling, batch context, and same-family reviewer variation prevent attributing changes solely to the patch. Small language subsets do not establish language-wide improvements. The original 900-case scores remain unchanged.

## 100-case live-model comparison

The [initial recorded comparison](../benchmarks/results/2026-10-08-reliability-100/report.md) generated 100 answers without ASDify and 100 with the canonical skill and all three references in `full` mode. It used `gpt-6.1-sol`, medium reasoning, Codex CLI 0.161.0, fresh sessions, a shared neutral system prompt, and no model tools or other skills. This tests injected instructions, not native host activation.

- Meaning coverage: 373 source invariants per arm across 100 synthetic cases, nine locales, 16 native-language rewrites, and 24 translations. Two blinded same-family model-review passes checked each output, with reversed display order on the second pass.
- Initial strict result: 92/100 baseline passes and 97/100 skill-assisted passes. The counts retain context-dependent omission flags. The [source audit](../benchmarks/results/2026-10-08-reliability-100/source-audit.md) identifies an invented actor and a missing voluntary-survey caveat in skill-assisted answers; both motivated targeted rule changes.
- Revised-skill regression: a [fresh paired run on the same 100 cases](../benchmarks/results/2026-10-09-reliability-100-revised/report.md) recorded 91/100 baseline and 99/100 strict skill-assisted passes. Both targeted problems are absent in the fresh skill outputs. The remaining skill flag is omitted budget component prices; both reviewers consider the correct totals sufficient, but the strict flag is retained. No further material failure was reported by these model reviewers. The second audit passed all 200 answers and 400 ratings; calibration was referenced, not repeated.
- Exact checks: no detected protected-token, JSON, or requested verbatim-output failures in either arm.
- Reviewer calibration: 10 authored good/bad pairs reviewed twice. All 20 deliberately defective ratings were detected and all 20 good ratings passed. These are grader controls, not generated benchmark answers.
- Evidence integrity: all 200 answers and 400 ratings match raw CLI events; frozen inputs, generation/review prompt hashes, display order, and coverage passed the [audit](../benchmarks/results/2026-10-08-reliability-100/evidence-audit.json). One rating differs from the stricter invariant rule because the reviewer considers the omitted detail immaterial. Its original judgment is retained unchanged and explicitly declared; the strict flag remains. CI also audits both published runs without making model calls.
- Local software checks: 84 unit tests passed, including 23 evaluation integrity tests. Corpus validation confirms exactly 100 cases and 373 invariants. Package validation still checks the separate 49 original public fixtures.

These are observed outputs and automated/model reviews. The implementing assistant's source audit is not independent human adjudication. One model, one repetition, small language groups, and no concise-prompt control limit the conclusions. Reusing these cases after the resulting skill edits is regression evidence, not held-out evidence of general reliability. See the [published results index](../benchmarks/results/README.md) for separate runs and complete answer comparisons.

## Multilingual update: local checks

- Structural validation: PASS, including 82 installer IDs, 6 existing SVGs, 9 language READMEs, language navigation, and 49 multilingual regression inputs (31 same-language tasks and 18 translations).
- Unit tests: PASS, 61 tests. The 10 added tests cover the language registry, Unicode, missing or empty READMEs, language navigation, dynamic locale coverage, invalid targets, and missing translation source/target coverage. The existing Codex installation check also verifies that the translation reference is copied.
- Installer matrix: PASS across the same 160 supported installations and 4 rejected unsupported scopes, using temporary directories.
- Installer Bash syntax, skill-creator frontmatter validation, and `git diff --check`: PASS.
- Installation guidance: checked npm's CLI-download confirmation against [npm documentation](https://docs.npmjs.com/cli/v11/commands/npm-exec/#description), and native Cursor project/user paths against [Cursor documentation](https://cursor.com/docs/skills#skill-directories). The local Cursor path checks remain filesystem tests, not a Cursor activation session.
- Expanded README/support guidance: all nine READMEs cover CLI, local/ZIP, manual-copy, persistent-instruction, Claude plugin, and manual-chat routes, with scope choices, environment limits, updates, removal, and reporting. All 50 Bash examples across the nine READMEs and installation guide pass `bash -n`; this syntax check did not execute their install commands.

These multilingual package checks preceded the live comparison above. The seven new READMEs and multilingual examples are translations and editorial examples, not recorded model-study outputs or independently reviewed native-speaker output. See [language coverage and support](LANGUAGES.md) for the locale registry and review limits. Local checks do not establish remote CI status for a future commit.

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
- Post-benchmark packaging check: Skills CLI 1.7.1 on an isolated Node 22.20.0 again discovered exactly one skill. Archived headers use `SKILL.txt` to avoid duplicate discovery. The system Node 22.12.0 probe emitted an engine warning, so the final check used a runtime meeting the declared minimum. See [command and scope](../benchmarks/results/2026-10-08-reliability-100/package-discovery.json).
- Remote Skills CLI discovery: `add hevertonrodrigues/asdify --list` was blocked because child Git could not resolve `github.com` in the sandbox. No external CLI installation or skills.sh indexing was verified.

## Public repository and CI

The completed mode benchmark and 164-test suite passed [CI run 37914750012](https://github.com/hevertonrodrigues/asdify/actions/runs/37914750012) at commit `a0f02294a029694b2958f794f5c270df988963e9`: Ubuntu/macOS with Python 3.12/3.13, all four jobs, including model-free evidence audits. The earlier [failed run](https://github.com/hevertonrodrigues/asdify/actions/runs/37912170601) had two unit fixtures requiring an installed `codex` executable. Commit `008ce58` replaced those metadata calls with fixture values; subsequent runs passed without installing Codex or making model calls on CI.

A [fresh public clone](demos/public-clone-2026-10-09.json) of commit `008ce58ac20b7444162dd13c232d3f3edc65cd27` passed the documented native Cursor project installation. All four skill/reference files were copied byte-for-byte into an isolated temporary project without invoking Node or npm. This checks filesystem installation, not Cursor activation or a future revision.

The [public repository](https://github.com/hevertonrodrigues/asdify) and [v0.1.0 release](https://github.com/hevertonrodrigues/asdify/releases/tag/v0.1.0) are confirmed. [CI run 37842301297](https://github.com/hevertonrodrigues/asdify/actions/runs/37842301297) passed for release commit `729b1b7ae54d68a808e051ea6dee331a4915aa6c`: Ubuntu and macOS, each with Python 3.12 and 3.13. All four jobs passed installer syntax, structural validation, and the test suite. This records that commit, not the status of future commits.

## Evidence limits

Before/after illustrations are editorial examples. The native Codex smoke check is separate from the live comparisons using injected instructions and references. The mode study records requested `lite`, `full`, `ultra`, and `off` behavior on its sample. Broad quality gains, automatic activation, native activation of the other modes, native reference loading, and other host sessions remain unverified. See [compatibility](COMPATIBILITY.md) for the distinction between installation layouts, host activation, and model effectiveness.
