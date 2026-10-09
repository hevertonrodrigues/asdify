# Multilingual mode benchmark

100 new cases per output language, run with no skill and in each of four ASDify modes. Each cell is the percentage of answers that passed both blinded meaning reviews and exact format checks.

| Output language | No skill | Lite | Full | Ultra | Off |
| --- | ---: | ---: | ---: | ---: | ---: |
| en (100) | 95.00% | 98.00% | 98.00% | 96.00% | 97.00% |
| pt-BR (100) | 96.00% | 98.00% | 98.00% | 99.00% | 99.00% |
| es (100) | 91.00% | 96.00% | 97.00% | 96.00% | 96.00% |
| fr (100) | 97.00% | 100.00% | 100.00% | 99.00% | 99.00% |
| de (100) | 93.00% | 99.00% | 97.00% | 96.00% | 96.00% |
| ja (100) | 88.00% | 98.00% | 98.00% | 97.00% | 98.00% |
| zh-CN (100) | 94.00% | 99.00% | 100.00% | 99.00% | 99.00% |
| it (100) | 92.00% | 97.00% | 98.00% | 98.00% | 97.00% |
| ru (100) | 93.00% | 99.00% | 99.00% | 98.00% | 98.00% |
| All (900 per condition) | 93.22% | 98.22% | 98.33% | 97.56% | 97.67% |

Pass means all required meaning survives; a shorter answer alone does not pass. A disagreement, uncertain check, or missing fact prevents a confirmed pass. No cases or semantic failures were removed or regenerated.

Model: `gpt-6.1-sol`; reasoning effort: `medium`. 900 distinct cases, 3,600 mode tests, 900 baseline answers, 4,500 generated answers and 9,000 candidate ratings.

`off` includes the skill with its optional workflow explicitly disabled. The no-skill control contains no skill instructions. The four modes use the same frozen tasks and skill.

## Paired changes from no skill

| Mode | Cases gaining a pass | Cases losing a pass | Net change (percentage points) |
| --- | ---: | ---: | ---: |
| lite | 48 | 3 | +5.00 |
| full | 51 | 5 | +5.11 |
| ultra | 47 | 8 | +4.33 |
| off | 45 | 5 | +4.44 |

These are observed sample differences. They do not establish a statistically reliable improvement or decline. The same model family generated and reviewed the answers, so errors can escape both reviews.

Grader control check: 50/50 positive ratings passed; 50/50 deliberately wrong ratings were detected. Repeated labels are checks of the review protocol, not 100 independent controls.

## Evidence and limits

[Case results](case-results.json), [numeric summary](summary.json), [table CSV](table.csv), [frozen design](metadata.json), [blinding map](unblinding-key.json), and [raw CLI evidence](raw/) are retained. Request JSON files contain the complete generated answers and ratings.

- Five cases share context within a batch, so observations are not fully independent.
- Some scenario patterns recur across locales with different facts; distinct tasks are not independent semantic designs.
- One generation model and one repetition per condition; same-family model reviewers can share blind spots.
- No independent human or native-speaker review, user comprehension study, or external fact verification.
- Injected instructions test requested modes; native skill discovery and activation are not tested.
- Meaning/format pass rates do not prove stylistic mode adherence or safety on future tasks.
- Purposive synthetic cases do not establish population-level reliability; off and baseline may differ from sampling noise.
- No generic concise-prompt control; a higher score cannot isolate the skill's unique contribution.
- Execution resumed at four live workers after a user-requested stop of the 32-worker attempt. All 185 returned answers were retained; remaining answers use the same frozen inputs. Interrupted attempts remain in the original study directory.

## All answers

[en](answers-en.md) | [pt-BR](answers-pt-BR.md) | [es](answers-es.md) | [fr](answers-fr.md) | [de](answers-de.md) | [ja](answers-ja.md) | [zh-CN](answers-zh-CN.md) | [it](answers-it.md) | [ru](answers-ru.md)

## Conservative processing amendment

Post-output processing amendment; not preregistered. Missing, duplicate, or extra integer invariant IDs make an otherwise valid, assignable rating structurally invalid. Affected answers are uncertain and cannot pass. No model check is synthesized, repaired, removed, or rewritten; every existing response and its raw evidence is retained.

Structurally invalid ratings: 4; affected answers: 4; affected cases: 1. Calibration structurally invalid ratings: 0; calibration affected cases: 0. The [sealed policy](processing-amendment.json) preserves 3772 prior evidence files.
