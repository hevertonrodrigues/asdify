# Focused development retest

100 previously examined tasks: all 34 cases with changed/uncertain meaning or changed voice in the supplemental source audit, plus 66 seeded controls; 12 English and 11 cases in each other locale. All five conditions are generated afresh.

Previously examined cases were reused after a proposed skill edit. These are development regressions, not new held-out tests or updated scores for the original 900 cases. Each condition is a fresh generation, including the no-skill baseline.

| Output language | Cases per condition | No skill | Lite | Full | Ultra | Off |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| en | 12 | 100.00% | 100.00% | 100.00% | 91.67% | 100.00% |
| pt-BR | 11 | 81.82% | 90.91% | 90.91% | 90.91% | 81.82% |
| es | 11 | 81.82% | 100.00% | 100.00% | 100.00% | 100.00% |
| fr | 11 | 81.82% | 100.00% | 100.00% | 100.00% | 100.00% |
| de | 11 | 90.91% | 100.00% | 100.00% | 100.00% | 81.82% |
| ja | 11 | 72.73% | 100.00% | 100.00% | 100.00% | 100.00% |
| zh-CN | 11 | 100.00% | 90.91% | 90.91% | 100.00% | 100.00% |
| it | 11 | 81.82% | 100.00% | 100.00% | 100.00% | 100.00% |
| ru | 11 | 90.91% | 90.91% | 90.91% | 81.82% | 90.91% |
| all | 100 | 87.00% | 97.00% | 97.00% | 96.00% | 95.00% |

500 generated answers; 1000 blinded candidate ratings. Model: `gpt-6.1-sol`; effort: `medium`. Both reviews and exact checks must pass. Incomplete or duplicate invariant coverage is prospectively classified as uncertain/non-passing; raw ratings are retained.

[Frozen plan](focused-plan.json), [metadata](metadata.json), [case results](case-results.json), [numeric summary](summary.json), [table CSV](table.csv), [raw evidence](raw/).

## Limits

- Five cases share context within a batch, so observations are not fully independent.
- Some scenario patterns recur across locales with different facts; distinct tasks are not independent semantic designs.
- One generation model and one repetition per condition; same-family model reviewers can share blind spots.
- No independent human or native-speaker review, user comprehension study, or external fact verification.
- Injected instructions test requested modes; native skill discovery and activation are not tested.
- Meaning/format pass rates do not prove stylistic mode adherence or safety on future tasks.
- Purposive synthetic cases do not establish population-level reliability; off and baseline may differ from sampling noise.
- No generic concise-prompt control; a higher score cannot isolate the skill's unique contribution.
- Selection includes previously observed failures and controls; no held-out improvement estimate.
- Small, unequal locale subsets cannot establish language-wide improvements.
- Before/after generations share case IDs but not draws; sampling and reviewer variation can change scores.

## All answers

[en](answers-en.md) | [pt-BR](answers-pt-BR.md) | [es](answers-es.md) | [fr](answers-fr.md) | [de](answers-de.md) | [ja](answers-ja.md) | [zh-CN](answers-zh-CN.md) | [it](answers-it.md) | [ru](answers-ru.md)
