# Development decision: retain the tested candidate

The joint candidate meets the [prospective retention rule](focused-plan.json): six of seven targeted meaning errors were absent in fresh answers, no new material error was found within those seven answers, and overall strict passes did not decrease in any active mode. The English ultra approval-scope error remains. The candidate is retained with these limits and the other failures published.

The retained changes keep named roles/groups equally specific, avoid added ownership or authority, and distinguish unchecked information and non-implication from negative findings. They preserve possibility inside attributed opinions and add German, Japanese, and Portuguese role examples. The compact AGENTS and Cursor adapters mirror these rules; this experiment tests the injected canonical skill, not native adapter activation.

## Observed before/after counts

Each condition covers the same selected 100 case IDs, with fresh generations and different neighboring tasks in batches. All five conditions are regenerated, including the no-skill control.

| Condition | Earlier strict passes | Fresh strict passes |
| --- | ---: | ---: |
| No skill | 76/100 | 87/100 |
| Lite | 97/100 | 97/100 |
| Full | 96/100 | 97/100 |
| Ultra | 91/100 | 96/100 |
| Off | 93/100 | 95/100 |

The rule uses overall active-mode counts. It does not require every language cell to improve. Per-language results include declines:

| Language | Cases per condition | Lite before → after | Full before → after | Ultra before → after |
| --- | ---: | ---: | ---: | ---: |
| en | 12 | 12 → 12 | 12 → 12 | 10 → 11 |
| pt-BR | 11 | 9 → 10 | 10 → 10 | 10 → 10 |
| es | 11 | 11 → 11 | 11 → 11 | 10 → 11 |
| fr | 11 | 11 → 11 | 11 → 11 | 10 → 11 |
| de | 11 | 11 → 11 | 9 → 11 | 11 → 11 |
| ja | 11 | 11 → 11 | 11 → 11 | 10 → 11 |
| zh-CN | 11 | 11 → 10 | 11 → 10 | 10 → 11 |
| it | 11 | 11 → 11 | 11 → 11 | 11 → 11 |
| ru | 11 | 10 → 10 | 10 → 10 | 9 → 9 |

Chinese lite/full lose a strict pass on a time-attachment error. Russian counts remain unchanged, with meaning and voice failures still present. Italian's targeted possibility error was absent even though that answer already passed the original primary checks. These observations do not establish that all languages improved or that unchanged strict counts imply unchanged meaning.

## Why the joint patch is kept

The [source audit](source-audit.md) confirms the six target corrections at the level of model-assistant source judgments. The original seven targets and the selection/retention rule were frozen before fresh generation. The complete 500-answer/1,000-rating evidence audit and 500-annotation source audit pass. No completed answer, rating, or annotation was repaired, removed, or regenerated to obtain these results.

The joint patch was tested as a whole; individual rule effects were not isolated. No untested extra language rule is included in this decision. The [archived patch](../../experiments/2026-10-09-language-guards/candidate.patch.txt) and [candidate hashes](../../experiments/2026-10-09-language-guards/candidate-file-sha256.json) identify the retained canonical files. The [machine-readable decision](development-decision.json) records the criteria, counts, remaining target, and evidence hashes; [development-comparison.json](development-comparison.json) contains before/after judgments and every supplemental finding.

This is a development observation on previously examined, purposively selected synthetic cases. Sampling, batch changes, reviewer variation, and shared model blind spots prevent a causal or language-wide improvement estimate. The original 900-case table remains unchanged and describes the earlier frozen skill; the retained candidate is evaluated by this separate 100-case retest. This result does not certify future meaning preservation or native host behavior.
