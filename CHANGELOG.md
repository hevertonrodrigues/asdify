# Changelog

## Unreleased

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
