# Changelog

## 0.2.0 (2026-10-09)

- Added 900 new synthetic cases: 100 per documented language, each tested in `lite`, `full`, `ultra`, and `off` against a no-skill control. Published 4,500 generated answers, 9,000 blinded candidate ratings, and a percentage table by language and mode. `full` recorded 98.33% strict passes versus 93.22% without the skill on this sample; these model-reviewed scores do not establish general reliability.
- Added frozen generation/review prompts, calibration controls, raw CLI evidence, complete answer pages, and reproducible audits for the mode study. Added 80 evaluation integrity tests, bringing the repository suite to 164, and included the completed study in CI auditing without model calls.
- Limited the live continuation to four workers after the initial 32-worker attempt caused computer load. Preserved all 185 returned answers and the original interrupted attempts; a separate audit verifies that continuation provenance. Documented explicit worker limits and lower-load options.
- Preserved four malformed review ratings that repeated a meaning-check ID. A sealed processing amendment adopted after outputs were available counts the affected answers as uncertain/non-passing and retains every raw check; the published table discloses this analysis change.
- Published a supplemental blinded source audit of 164 cases and 820 candidates. It separates meaning, voice, and format, documents disagreement and missed errors, and preserves the original strict scores. Added a subset runner with a two-worker default and a four-worker ceiling for prospective development retests.
- Retained stronger role/group and uncertainty rules after a planned 100-case development retest: 500 fresh answers, 1,000 candidate ratings, and 500 additional blinded source annotations with one audit agent at a time. Six of seven targeted errors were absent; the English ultra approval-scope error remains. Strict passes on the same selected cases changed from 97 to 97 in lite, 96 to 97 in full, and 91 to 96 in ultra. Added German/Japanese/Portuguese role guidance and aligned compact adapters. Published remaining errors, Chinese lite/full declines, and unchanged secondary uncertainty; these reused cases do not establish causal or language-wide improvement.
- Verified the documented native Cursor project installation from a fresh public clone without invoking Node or npm; this confirms file copying, not Cursor activation. Added the recorded overall benchmark result to all nine READMEs.

- Added 100 new paired live-model test cases with 373 meaning checks, nine locales, blinded double model review, exact-format checks, grader calibration, and reproducible raw-evidence auditing.
- Published the initial comparison (97/100 strict skill-assisted passes versus 92/100 baseline) and a fresh revised-skill regression (99/100 versus 91/100), including all answers, failures, and context-dependent grading disagreements. Strengthened preservation of unnamed actors and sample-selection methods in the canonical skill and compact adapters. The follow-up reuses development cases and is not held-out evidence of general reliability.
- Earlier evaluation work added 23 integrity tests for corpus coverage, isolation, blinding, completeness, exact formats, calibration integrity, and preservation of raw evidence; these are included in the current 164-test total and do not certify future model answers.
- Added both published studies' raw-evidence audits to the existing Linux/macOS CI matrix without requiring model access.
- Expanded all nine READMEs with installation choices, project/user scope, CLI confirmations, manual/ZIP installation, persistent instructions, Claude Code plugins, supported environment limits, updates, removal, and support routes.
- Added a central support guide and extended installation guidance for Windows, WSL, remote/cloud environments, multiple agents, and the complete local/CLI option sets.
- Clarified npm's optional Skills CLI download prompt across all READMEs and documented native Cursor installation without Node.js or npm, supported paths, discovery checks, and the two separate `--yes` options.
- Added Spanish, French, German, Japanese, Simplified Chinese, Italian, and Russian READMEs, with navigation across all nine documented languages.
- Added explicit target-language handling, translation preservation rules, and an installed translation reference; kept the compact agent and Cursor adapters aligned.
- Added a language registry and validation of locale metadata, README navigation, rewrite coverage, and translation source/target coverage.
- Expanded public regression inputs from 16 to 49, including bidirectional English translations, modality, statistical units, protected JSON/placeholders, mixed-language editing, and ambiguous dates.
- Added multilingual examples, language contribution and support guidance, a documentation-translation issue form, and language fields in meaning-regression reports.
- Added unit coverage for locale registries, Unicode, missing READMEs, language navigation, invalid translation targets, and incomplete coverage. These checks do not establish translation accuracy or native-speaker review.

## 0.1.0 (2026-10-08)

- Expanded the local installer to 79 upstream agent mappings plus 3 compatibility IDs, with a pinned registry and complete destination table.
- Added `--list`, scoped path handling, documented configuration overrides, and native Cursor skills while preserving the earlier Cursor rule IDs.
- Documented Skills CLI discovery and installation, manual chat use, and the limits of installation coverage.
- Recorded one explicit Codex `full`-mode smoke check and local skill discovery with Skills CLI 1.7.1; no broad quality gains or external CLI installation are claimed.
- Expanded regression coverage to 51 passing tests, including 160 supported installations and 4 rejected unsupported scopes.
- Redesigned the English and Portuguese READMEs around a quick trial, visual examples, and focused installation choices.
- Added original accessible SVG illustrations for the product, editing example, and workflow.
- Removed inspiration sections from the READMEs and organized provenance in `docs/archive/`.
- Added HTML image/link and SVG validation, plus direct contribution and installation-report paths.
- Adopted ASDify (`asdify`) as the project name and skill identifier; moved the product to the repository root.
- Updated documentation, prompts, and installation paths for `hevertonrodrigues/asdify` while retaining independent ASD-STE100 inspiration and explicit limits.
- Reworked first-use examples and added complete task recipes in English and Portuguese.
- Corrected recommendation preservation in the Portuguese API example.
- Added meaning-regression reporting, compatibility evidence, and a public roadmap.
- Expanded bilingual regression inputs to 16 and documented concise-only comparison studies.
- Hardened fixture/plugin validation and ratings parsing; added paired repetition IDs and descriptive failure rates.
- Expanded tooling regression coverage and configured Linux/macOS CI across Python 3.12/3.13.
- Initial independent agent skill with `lite`, `full`, and `ultra` modes.
- English/PT-BR usage, preservation guardrails, portable installs, example set, and evaluation framework.
- No benchmark improvement claims have been established yet.
