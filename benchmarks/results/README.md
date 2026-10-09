# Published evaluations

Real live-model outputs are published below. Model reviewers share the generation model family; these are automated comparisons, not independent human studies or reliability certification.

## 900-case multilingual mode benchmark

The primary study uses 100 new cases per output language, each run without the skill and in all four modes. It contains 900 distinct cases, 3,600 mode tests, 900 baseline answers, 4,500 generated answers, and 9,000 blinded candidate ratings. Each cell below is a strict pass percentage; there are 100 answers per language and condition, or 900 in the overall row.

| Output language | No skill | Lite | Full | Ultra | Off |
| --- | ---: | ---: | ---: | ---: | ---: |
| English | 95.00% | 98.00% | 98.00% | 96.00% | 97.00% |
| Portuguese (Brazil) | 96.00% | 98.00% | 98.00% | 99.00% | 99.00% |
| Spanish | 91.00% | 96.00% | 97.00% | 96.00% | 96.00% |
| French | 97.00% | 100.00% | 100.00% | 99.00% | 99.00% |
| German | 93.00% | 99.00% | 97.00% | 96.00% | 96.00% |
| Japanese | 88.00% | 98.00% | 98.00% | 97.00% | 98.00% |
| Chinese (Simplified) | 94.00% | 99.00% | 100.00% | 99.00% | 99.00% |
| Italian | 92.00% | 97.00% | 98.00% | 98.00% | 97.00% |
| Russian | 93.00% | 99.00% | 99.00% | 98.00% | 98.00% |
| All (900 per condition) | 93.22% | 98.22% | 98.33% | 97.56% | 97.67% |

`full` recorded 885/900 strict passes versus 839/900 without the skill, gaining 51 passes and losing 5 on paired cases: a net gain of 5.11 percentage points. All four modes scored higher than the baseline in this sample. `off` loads the skill while disabling its optional workflow; it is distinct from the no-skill control. Answers were not always shorter: `full` averaged 258.0 characters versus 243.4 without the skill.

[Full report](2026-10-09-multilingual-modes-four-workers/report.md), [table CSV](2026-10-09-multilingual-modes-four-workers/table.csv), [case results](2026-10-09-multilingual-modes-four-workers/case-results.json), [raw-evidence audit](2026-10-09-multilingual-modes-four-workers/evidence-audit.json), and [interruption audit](2026-10-09-multilingual-modes-four-workers/execution-history-audit.json) are published. The report links every source and answer by language.

A separate [blinded source audit](2026-10-09-multilingual-modes-four-workers/source-audit.md) reviewed 820 candidates from 164 cases, including every strict-flagged case. It found genuine role and uncertainty errors, scope/format disagreements, and three changed-meaning judgments on primary passes. Its selected sample is enriched for failures and cannot estimate general reliability. The original strict scores remain unchanged; annotations and the released key are sealed and reproducibly audited.

The first 32-worker execution was stopped for computer load. All 185 returned answers were carried into the four-worker continuation unchanged; interrupted attempts remain in the original directory. A later review repeated an invariant ID in four ratings. The disclosed, sealed post-output processing amendment retains those raw ratings and counts all four affected answers as uncertain/non-passing. No completed answers or reviews were regenerated or removed.

These percentages include exact-format flags, reviewer uncertainty, and strict checklist omissions. They are observed scores on purposively selected synthetic cases, not population reliability estimates. Language sets differ, so compare conditions within each language rather than treating this as a language ranking. Five cases share a batch; some scenario patterns recur across locales. One provider model alias and one repetition, same-family review, injected references, and no concise-only control or independent human review limit the conclusions. The results do not establish native host activation or adherence to every stylistic mode preference.

## 100-case development retest

After examining the primary source audit, a candidate patch strengthened role/group specificity and uncertainty handling, with German, Japanese, and Portuguese role examples. A [prospective development plan](2026-10-09-language-guards-development/focused-plan.json) selected 34 cases with source-audit concerns plus 66 seeded comparison cases: 12 English cases and 11 in each other language. These are previously examined cases, not 100 additional new cases per language.

| Condition | Earlier draw on these 100 cases | Fresh development draw |
| --- | ---: | ---: |
| No skill | 76/100 (76%) | 87/100 (87%) |
| Lite | 97/100 (97%) | 97/100 (97%) |
| Full | 96/100 (96%) | 97/100 (97%) |
| Ultra | 91/100 (91%) | 96/100 (96%) |
| Off | 93/100 (93%) | 95/100 (95%) |

The fresh run contains 500 answers and 1,000 blinded candidate ratings, with at most two live CLI workers. The [report](2026-10-09-language-guards-development/report.md), [language/mode CSV](2026-10-09-language-guards-development/table.csv), and [evidence audit](2026-10-09-language-guards-development/evidence-audit.json) preserve every answer and rating. All five conditions are fresh draws, including the no-skill control. Subset selection also changes neighboring tasks in each batch. Sampling, batch context, reviewer variation, and reuse of known failures prevent a causal or language-wide improvement claim. These results are separate from the unchanged 900-case table.

The subsequent [blinded source audit](2026-10-09-language-guards-development/source-audit.md) covers all 500 fresh answers, with one agent at a time after CLI workers stopped. Six of seven targeted meaning errors were absent; the English ultra approval-scope error remains. The [decision](2026-10-09-language-guards-development/development-decision.md) retains the joint tested patch under the frozen rule. It also reports Chinese lite/full declines, further meaning/voice errors, unchanged secondary uncertainty, and primary-review blind spots. No claim that every language improved is made.

## Earlier 100-case comparisons

| Study | Model and mode | Strict passes without / with skill | Evidence |
| --- | --- | --- | --- |
| Initial 100-case comparison, frozen before the resulting skill edits | `gpt-6.1-sol`, `full` | 92/100 / 97/100 | [Report](2026-10-08-reliability-100/report.md), [all answers](2026-10-08-reliability-100/comparisons.md), [source audit](2026-10-08-reliability-100/source-audit.md) |
| Revised skill, fresh paired regression on the same 100 cases | `gpt-6.1-sol`, `full` | 91/100 / 99/100 | [Report](2026-10-09-reliability-100-revised/report.md), [all answers](2026-10-09-reliability-100-revised/comparisons.md), [source audit](2026-10-09-reliability-100-revised/source-audit.md) |

The initial run found an invented actor and an omitted voluntary-survey caveat in skill-assisted answers. A budget answer also received a strict omission flag despite preserving the relevant totals; that disagreement and the original rating remain visible. The skill was revised using these findings. In the fresh regression run, both targeted corrections were present and neither model reviewer reported a material failure in any skill-assisted answer. The stricter classifier still flags one budget answer for omitted component prices, giving 99/100 rather than silently counting it as a pass. The same budget flag applies to the fresh baseline.

Both runs contain 200 generated answers and 400 answer ratings, for 400 answers and 800 ratings across 100 distinct cases. All raw answers, prompt hashes, frozen inputs, and ratings passed the evidence audits. The initial grader calibration separately contains 10 authored good/bad pairs reviewed twice; the revised run references those controls rather than claiming a new calibration. Reusing development cases and a shared model family cannot establish performance on unseen tasks.

Create a directory such as `2026-10-08-concise-vs-skill/` only after collecting real outputs. Do not use editorial examples or synthetic ratings as results.

Include:

- A completed copy of [run-metadata-template.json](../run-metadata-template.json), frozen case inputs, and exact shared/condition prompts.
- Raw outputs for every case, arm, and repetition, with stable IDs; record errors and exclusions.
- Reviewer ratings, paired preferences, disagreement notes, and the final unblinding key. Identify model reviewers and shared model families explicitly; do not present them as independent humans.
- A report covering fidelity failures, clarity, preference, uncertainty, limitations, and unsuccessful cases. State the denominator for every rate.
- The command and version used for aggregation; identify any analysis beyond `scripts/score_ratings.py`.

Follow the [protocol](../README.md). A publication can report negative or inconclusive findings. Public evidence belongs here; local `benchmarks/runs/` is intentionally ignored by Git.
