# Evaluation: clarity with meaning preserved

The [published 100-case live-model comparisons](results/README.md) record real paired answers, two blinded model-review passes, and exact-format checks. The initial result was 97/100 strict skill-assisted passes versus 92/100 without the skill. After two preservation-rule changes, a fresh regression run on the same cases recorded 99/100 versus 91/100. The remaining skill flag concerns a budget breakdown, while both reviewers consider its totals sufficient for the question. These automated comparisons do not establish general reliability or meet the independent human-review protocol below. Editorial examples and package tests remain separate evidence.

## Compare against the obvious alternative

Run two separate, blinded, paired comparisons with the same held-out case set:

| Study | Control condition | Treatment condition | Question |
| --- | --- | --- | --- |
| `baseline-vs-skill` | Task alone | Same task plus canonical skill in `full` mode | Does the skill improve ordinary output? |
| `concise-vs-skill` | Same task plus `Be concise.` | Same task plus canonical skill in `full` mode | Does it add value beyond a shorter prompt? |

Use a separate ratings CSV and metadata file for each study and each model configuration. Keep any system instruction shared across conditions identical. Do not quietly strengthen the control instruction after looking at results; register any additional comparison in advance.

## Run the study

1. **Freeze inputs.** Record the repository revision (or skill checksum), model/version, host/version, system prompt, exact condition instructions, sampling settings, tools, date, case list, repetitions, and stopping rule. Start with [run-metadata-template.json](run-metadata-template.json); replace every `null` and empty list relevant to the study before running it.
2. **Separate development from evaluation.** `cases.jsonl` is a public regression set. It is useful for development but not held-out evidence. Collect a new frozen set that was not used to edit the skill. Include the languages and translation directions being claimed, long summaries, hard constraints, and already-clear text. Report selection criteria and exclusions; do not generalize a result to untested languages.
3. **Generate independently.** Use fresh sessions with no previous outputs or other writing skills. The control must not inherit this repository's `AGENTS.md` or installed rule. Treatment gets the complete canonical skill and access to its references. Capture raw input and output for every case and repetition, including failures.
4. **Blind the review.** An organizer assigns opaque A/B labels to conditions and keeps their meaning hidden from reviewers. Keep the mapping consistent within each CSV so arm totals are meaningful. Randomize display order separately; remove host/skill labels without changing the writing. Each `run_id` identifies one paired repetition; both arms share it.
5. **Score independently.** At least two reviewers use the [rubric](../skills/asdify/references/quality-rubric.md). For translations, reviewers must understand both source and target languages. Mark a hard failure when a material fact, condition, obligation, citation, or safety detail is changed, invented, or lost. Use the source and invariants together; matching words alone does not establish meaning preservation. Check target language, locale/script, register, identifiers, placeholders, and output format separately.
6. **Record preference separately.** For each paired repetition/reviewer, record A, B, tie, or neither in a separate preference sheet with reviewer, case ID, run ID, reason, and hard-failure notes. A hard-failing output cannot win; if both fail, choose neither. Retain independent ratings before any disagreement resolution.
7. **Report with limits.** Publish per-case outputs and results, fidelity failures, dimension scores, paired preferences, reviewer agreement, and uncertainty. Repeated runs and multiple reviewers are not independent cases. Analyze or resample at the case level when estimating uncertainty. Report length, token usage, and latency as secondary measures. The supplied scorer does not compute preference, reviewer agreement, significance, or confidence intervals.

If a model version, skill revision, or instruction changes, start a new study rather than pooling incompatible rows.

## Public regression inputs

### Multilingual four-mode comparison

The [multilingual mode corpus](multilingual-modes/README.md) adds 100 new cases per output language across all nine registered locales. The same 900 cases run in `lite`, `full`, `ultra`, and `off`, with 900 no-skill control answers. This produces 3,600 mode tests, 4,500 generated answers, and 9,000 blinded model ratings. Meaning and exact-format pass rates use 100 answers per language and condition; reviewer ratings are not counted as additional cases.

[scripts/evaluate_modes.py](../scripts/evaluate_modes.py) freezes all inputs, generates and reviews five-case batches in fresh workspaces, preserves every raw request, and refuses incomplete reports. Per-case candidate labels are randomized and the second review reverses positions. It keeps contradictory judgments unchanged and applies the stricter checks. The corpus guide describes commands, calibration controls, batching, and limitations. This automated study is separate from the independent human protocol above.

### Focused development retests

[scripts/evaluate_modes_focused.py](../scripts/evaluate_modes_focused.py) reuses an explicitly selected subset of the 900 cases after a proposed skill edit. Its frozen plan records selected IDs and a retention rule before new outputs. It generates all five conditions afresh, records actual locale counts, and labels the report as development evidence. It defaults to two workers and rejects more than four; calibration separately uses at most four workers. Run one model phase at a time.

The [language-guard experiment plan](experiments/2026-10-09-language-guards/plan.json) provides a concrete example. A focused retest cannot replace the original per-language table or establish an improvement on unseen cases. Incomplete/duplicate invariant coverage is prospectively uncertain and cannot pass; other invalid reviews remain fatal. Frozen adapter, runner, processor, source, and skill hashes are checked on resume and audit.

### Automated 100-case comparison

[reliability-100.jsonl](reliability-100.jsonl) is a separate set of 100 synthetic cases with 373 semantic invariants: 60 English tasks, 16 native-language rewrites, and 24 translations across the nine documented locales. It covers numbers, conditions, technical procedures, summaries, analysis, exact output formats, voice, and ambiguity. The initial cases were frozen before generation and before the skill edits motivated by its results. Reusing these cases after those edits is a development regression check, not held-out evidence. They are now public regression material.

[scripts/evaluate_skill.py](../scripts/evaluate_skill.py) uses an authenticated Codex CLI to generate one answer per case without ASDify and one with its complete instructions and references in `full` mode. Each call uses a fresh temporary workspace outside this repository. User configuration, project instructions, installed skills, memory, plugins, model tools, and web search are disabled. The canonical skill is injected into the treatment prompt; this tests writing behavior, not native skill discovery or activation.

Two fresh model-review passes grade the blinded candidates against the source and each invariant. The second pass reverses candidate order. Exact JSON, protected-token, and verbatim-output checks supplement meaning review. Any reviewer hard failure or missing/changed invariant counts as a strict flag; an uncertain check prevents a confirmed pass. Flags can include context-dependent omissions, so they are not established semantic error rates. The runner refuses incomplete generation sets and incomplete reviews. It retains raw answers, failed requests, token usage, model ratings, and exact-fragment evidence.

These model reviews are an automated pilot. They do not meet the independent human-review requirement above, and reviewers from the same model family can share errors. A purposive sample of 100 cases cannot establish a general failure probability. One generation per case, one model, small language samples, and no `Be concise.` control also limit the conclusions.

Run local validation without making model calls:

```bash
python3 scripts/evaluate_skill.py validate
python3 -m unittest discover -s tests -p test_evaluation.py
```

Run a new study with the CLI already authenticated. Generation and review use account capacity; the runner has no pricing estimate. Choose a new output directory so frozen studies remain separate:

```bash
python3 scripts/evaluate_skill.py freeze --output benchmarks/runs/my-study --model gpt-6.1-sol --effort medium
python3 scripts/evaluate_skill.py generate --output benchmarks/runs/my-study --workers 2
python3 scripts/calibrate_grader.py --study benchmarks/runs/my-study
python3 scripts/evaluate_skill.py review --output benchmarks/runs/my-study --workers 2
python3 scripts/audit_evaluation.py --output benchmarks/runs/my-study
python3 scripts/evaluate_skill.py report --output benchmarks/runs/my-study
```

The calibration step uses [ten authored good/bad pairs](judge-calibration.jsonl), not model-generated task answers. Its deliberately distorted controls check whether the reviewer catches numeric, modal, conditional, causal, safety, uncertainty, negation, exact-output, and target-language errors. Keep calibration results separate from the 100-case comparison. Passing these controls does not establish that the grader will catch every subtle error. The evidence audit checks the exact prompts, blinding order, saved answers, and ratings against raw CLI events; it does not replace meaning review.

Sequential generation and review keep computer load lower; use one worker when needed. For overlapping generation and review, run [scripts/review_pending.py](../scripts/review_pending.py) in a second terminal after generation starts, accounting for the additional concurrent workers. It grades the same fixed batches only when all paired answers exist. It does not feed review results into generation. Each archived skill header is named `SKILL.txt`, with unchanged instruction text, so published snapshots do not become duplicate installable skills.

An internally inconsistent review is retained unchanged and recorded in `review-exceptions.json` after inspecting the source. Explicit exceptions permit analysis of the original JSON; they never turn its listed defects into passes. The initial budget case demonstrates why a source-based audit is useful. `ratings.csv` retains raw model verdicts; `summary.json` and `report.md` use strict combined output-level flags. Preserve both rather than silently repairing a model's rating.

The runner refuses to overwrite an existing request's raw evidence. Resume only requests that have not started; inspect failed or rejected requests before analysis. Do not rerun a semantic failure or replace an inconsistent rating to obtain a better result. If a separate study is needed, freeze it under a new ID and disclose its purpose.

Before using another CLI version, repeat the baseline isolation probe. Version 0.161.0 requires `skills.config` paths to point to `SKILL.md` files; folder paths left the catalog enabled in the observed preflight. The runner overrides the model persona with the same neutral instructions for both arms and retains host policies. Sampling seed and temperature, as well as an immutable backend model snapshot, are not exposed by this CLI. Changing the model, reasoning effort, prompts, corpus, or skill requires a new frozen study.

`cases.jsonl` contains 49 original inputs: 31 same-language rewrite or analysis tasks and 18 translation tasks across English, Brazilian Portuguese, Spanish, French, German, Japanese, Simplified Chinese, Italian, and Russian. The original 16 EN/PT-BR cases remain intact. Added cases cover native-language rewrites, translation to and from English, protected JSON keys and placeholders, intentional language mixing, and ambiguous dates.

Each case has a unique `id`, source `lang`, complete `task`, semantic `invariants`, and failure `risk`. Translation cases also have `target_lang`; omit it for same-language tasks. Tags must match [integrations/languages.json](../integrations/languages.json). Every registered locale needs rewrite coverage and translation source/target coverage. A target identical to the source is rejected; a locale-to-locale translation can use different registered tags.

```jsonl
{"id":"en-to-it-example","lang":"en","target_lang":"it","task":"Translate into Italian: The supplier may terminate with at least 30 days' written notice.","invariants":["Italian output","permission, not requirement","at least 30 days","written notice"],"risk":"changed modality or notice minimum"}
```

Record the evaluated locales and directions in `language_coverage` in the metadata template. Report translation results by source/target direction and same-language results by locale. Public fixtures are unevenly distributed and are not a balanced study. Do not use cross-language word or token counts as proof of better clarity. Structural validation does not generate translations or check their accuracy.

The `invariants` are review criteria, not required substrings. For example, the obligation can be preserved with different words. A human checks whether the meaning survives. The source task remains authoritative if an invariant is incomplete.

Mode and activation checks are separate from this output study. In a real host session, test:

| Request | Expected behavior |
| --- | --- |
| Explicit request to rewrite an executive update | Skill available; follows requested mode |
| `lite` on a well-structured paragraph | Local edits; structure and voice preserved |
| `ultra` on a dense brief | Compression without losing conditions |
| `off` followed by a task | Optional style workflow disabled; higher-priority instructions still apply |
| Return a quote verbatim or an exact JSON object | Exact requested content/format preserved; no style preamble |
| Preserve deliberate humor or poetic voice | Voice survives; no forced business-writing style |

Record activation and behavior in [COMPATIBILITY.md](../docs/COMPATIBILITY.md). A correct output does not prove that the skill loaded; capture host evidence when available.

## Scoring CSV

Copy [ratings-template.csv](ratings-template.csv). Supply one row per **reviewer × case × paired run × arm**. Use integer values 1–5 for the six dimensions and 0/1 for `hard_fail`. `arm` is A or B. Never include condition names in a reviewer-facing CSV. Legacy CSV files without `run_id` are treated as one run; if the column is present, every row needs an ID.

```bash
python3 scripts/score_ratings.py path/to/filled-ratings.csv
```

The empty template deliberately fails. The scorer validates pairing and reports descriptive rating-level failure rates and dimension summaries. Those counts include each reviewer rating; they are not the number of unique failed outputs. Review disagreements and report output-level failures separately. No automatic winner is inferred from these summaries.

## Publish results

Use `benchmarks/runs/` for local drafts (gitignored). Publish reviewed, anonymized evidence in `benchmarks/results/<date>-<study>/`, following the [results checklist](results/README.md). Keep the mapping secret during grading, then publish it with the final study. Do not commit private source documents, API credentials, or identifying reviewer details.

Before making a broad effectiveness claim, seek benefit on every language and translation direction included in the claim and at least two models with no material-fidelity regression. These are evaluation goals, not achieved results. A finding that the skill adds no benefit is a valid result.
