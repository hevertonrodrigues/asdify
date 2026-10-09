# Published evaluations

Real live-model outputs are published below. Model reviewers share the generation model family; these are automated comparisons, not independent human studies or reliability certification.

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
