# Multilingual mode cases

This set contains 100 new synthetic cases for each of the nine registered output languages: English, Brazilian Portuguese, Spanish, French, German, Japanese, Simplified Chinese, Italian, and Russian.

Each locale file has 80 native-language tasks and 20 incoming translations, at least 10 categories, at least 10 tasks longer than 1,500 characters, and at least eight cases with exact checks. The same cases run in `lite`, `full`, `ultra`, and `off`, alongside a no-skill control: 900 distinct cases, 3,600 mode tests, and 900 baseline answers.

`benchmark_language` identifies the required output language. `lang` is the source language; `target_lang` is present only for translation. English translations cover every other registered source language. Translations into the other locales start in English. This does not cover every possible language pair.

Three parallel authoring agents prepared separate locale files before scored generation. The sources are invented for testing. They are not professional advice or factual claims about real organizations. Cases are purposively selected, not a random sample of everyday writing. They become public regression inputs after publication.

Each row contains:

- `id`, `benchmark_language`, `lang`, `category`, and the complete `task`.
- Three to eight semantic `invariants`, written in English for the reviewers. They describe relevant meaning, not required wording. The source and requested scope remain authoritative.
- Optional `protected`, `exact_output`, `json_keys`, and `json_expected` checks for literal tokens or required formats. Translatable prose is not frozen as an expected JSON value.

The generation model sees only the task and case ID, plus the skill when a mode is requested. It never receives the invariants or expected checks. Reviewers see all five candidate answers under labels randomized for each case; the second review reverses display order. Both reviews must pass, along with exact checks. Missing, changed, or uncertain meaning prevents a confirmed pass, even if a reviewer's overall verdict disagrees.

Validate the corpus without model access:

```bash
python3 scripts/evaluate_modes.py validate
```

Run a new frozen study with an authenticated Codex CLI:

```bash
python3 scripts/evaluate_modes.py freeze --output benchmarks/runs/my-mode-study
python3 scripts/evaluate_modes.py calibrate --output benchmarks/runs/my-mode-study
python3 scripts/evaluate_modes.py run --output benchmarks/runs/my-mode-study --workers 4
python3 scripts/evaluate_modes.py report --output benchmarks/runs/my-mode-study
python3 scripts/evaluate_modes.py audit --output benchmarks/runs/my-mode-study
```

Pass `--workers` explicitly: the current runner defaults to 16. Use `run --workers 1` or `run --workers 2` for lower memory and CPU use. Calibration separately uses at most four workers.

Generation and review make 1,260 primary requests: five cases per generation batch and five cases with all five candidates per review batch. Four additional calibration requests review 10 authored good/bad controls under the same five-label protocol. These repeated controls are separate from the 900 new cases. Calls use account capacity; the runner does not estimate a price.

Every batch gets a fresh workspace. Five cases share context within a batch, with identical batching across conditions. Each case has one generation per condition. `off` includes the skill and explicitly disables its optional workflow; the control omits the skill. Canonical instructions and all three references are injected, so results test requested modes rather than native activation.

The runner retains raw CLI events, failed attempts, full answers, prompt hashes, ratings, frozen inputs, and the blinding key. It retries an infrastructure failure at most once before a completed answer. It never resamples a semantic failure or a malformed completed answer. A run can resume requests that have not started; existing raw evidence cannot be overwritten. Reports require all 4,500 answers and all 9,000 candidate ratings.

Request claims prevent concurrent calls with the same ID; a study lock prevents overlapping run/calibration processes. Resume validates saved requests before starting calls. The audit checks all raw files and claims, including failed attempts, and rejects completed earlier answers followed by another generation. Runner and helper hashes are frozen; use their recorded code version when auditing a study.

### Invalid review check coverage

A model review can return valid JSON while repeating or omitting a checklist ID. The original runner stops on this error. The conservative processor preserves those reviews and counts each affected answer as uncertain, so it cannot earn a strict pass. It retains every returned check and negative judgment. Invalid case/candidate coverage or other invalid fields still stop processing.

If this happens after all answers have been collected, seal the processing policy and existing evidence before resuming:

```bash
python3 scripts/evaluate_modes_conservative.py amend --output benchmarks/runs/my-mode-study
python3 scripts/evaluate_modes_conservative.py run --output benchmarks/runs/my-mode-study --workers 4
python3 scripts/evaluate_modes_conservative.py report --output benchmarks/runs/my-mode-study
python3 scripts/evaluate_modes_conservative.py audit --output benchmarks/runs/my-mode-study
```

Use the same catalog argument at amendment and resume time if the frozen study used one. This processor can request only reviews that have not started; it cannot regenerate answers or completed reviews. Its seal records the processor hash and all prior evidence. Its report and audit disclose structurally invalid ratings and the affected answers and cases.

The October 2026 continuation adopted this processing amendment after all 4,500 answers and 775 candidate ratings had returned. One review duplicated a checklist ID in four ratings. This is a disclosed change after outputs were available, not a preregistered analysis rule. Frozen tasks, prompts, model settings, skill instructions, and raw responses stay intact; malformed reviews receive no pass credit.

The October 2026 study continued with four live workers after the user stopped the initial 32-worker attempt because of computer load. All 185 returned answers were retained, without selecting them by quality. The original interrupted attempts remain separate. The continuation's `execution-history.json` records their source; `scripts/audit_execution_history.py` checks identical frozen inputs, every carried answer and raw event, and the absence of returned answers in the interrupted requests. This extra audit verifies the interruption record, not study completion or meaning.

If a source audit justifies a language-specific skill change, keep the first study intact and freeze a separate regression for the affected output languages. For example:

```bash
python3 scripts/evaluate_modes.py freeze --output benchmarks/runs/my-language-retest --languages ja ru --regression
```

The remaining calibration, run, report, and audit steps are the same. Every selected locale still uses all 100 cases and all four modes plus fresh no-skill answers. A retest on cases examined during development is disclosed as a regression, not new held-out evidence. A higher result in one fresh run can reflect sampling variation; inspect the source-level corrections and any new failures before keeping a change.

Use `--catalog /absolute/path/catalog.json` only with a compatible Codex model catalog. The supported [`model_catalog_json` setting](https://developers.openai.com/codex/config-reference) can avoid a metadata refresh at every CLI startup. Supply it at freeze, calibration, and run time; the runner requires the same hash throughout. Keep account-specific catalog files outside the published evidence. Authentication stays in the existing CLI configuration and is not copied into the study.

The [results index](../results/README.md) links published reports. A pass rate is an observed result on this synthetic sample. Same-family model reviewers can miss errors; this is not independent native-speaker review, a comprehension study, proof of stylistic mode adherence, or a guarantee for future answers.
