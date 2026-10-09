# 100-case ASDify comparison

Observed model outputs and automated/model review, not a reliability certification.

Model: gpt-6.1-sol; generation reasoning: medium; one fresh-session output per arm per case. ASDify full mode and all references were injected.

100 synthetic cases produced 200 answers. Two blinded, fresh-session model-review passes checked each answer against 373 source invariants per arm. Review pass 2 reverses candidate display order. Exact JSON, protected-token, and verbatim-output checks supplement semantic review. Any reviewer hard failure or missing/changed invariant counts as a strict flag, even when a reviewer considers that omission immaterial; an uncertain check prevents a confirmed pass. No semantic failures were regenerated or excluded. These are conservative model-review classifications, not established error rates.

Source tasks contain 49–740 Unicode characters including instructions (mean 213.6). This evaluates short supplied passages and questions, not long documents, retrieval, or real-world fact checking.

| Measure | Without ASDify | With ASDify |
| --- | ---: | ---: |
| Confirmed passes / 100 | 92 | 97 |
| Outputs flagged / 100 | 8 | 3 |
| Outputs with uncertain checks / 100 | 0 | 0 |
| Reviewer hard-failure disagreements / 100 | 1 | 1 |
| Verdicts differing from the strict invariant rule | 0 | 1 |

## Scores

Means of 200 model ratings per arm; these ordinal scores are descriptive.

| Dimension (1–5) | Without ASDify | With ASDify |
| --- | ---: | ---: |
| meaning_fidelity | 4.855 | 4.975 |
| clarity | 4.94 | 4.985 |
| signal_density | 4.935 | 4.99 |
| structure | 4.985 | 5.0 |
| calibration | 4.91 | 4.99 |
| fit_for_purpose | 4.8 | 4.95 |

## Length and execution

Descriptive means over the same multilingual case mix; characters and tokens do not measure clarity or translation quality. CLI input tokens include the condition prompt. Generation time includes CLI startup and infrastructure retries, excludes grading, and is not total elapsed study time because requests overlap.

| Measure | Without ASDify | With ASDify |
| --- | ---: | ---: |
| Output characters | 182.0 | 179.9 |
| CLI input tokens | 3745.2 | 6901.1 |
| CLI output tokens | 50.7 | 50.6 |
| Generation request seconds | 38.66 | 38.5 |

## Task groups

Small subgroup counts do not establish performance for the whole language or domain.

| Group | Cases | Without ASDify: passes | With ASDify: passes |
| --- | ---: | ---: | ---: |
| ambiguity | 4 | 3 | 4 |
| analysis | 8 | 4 | 6 |
| conditions | 11 | 11 | 11 |
| format | 4 | 4 | 4 |
| native-rewrite | 16 | 15 | 16 |
| numbers | 10 | 8 | 10 |
| scope | 4 | 4 | 3 |
| summary | 5 | 5 | 5 |
| technical | 10 | 10 | 10 |
| translation | 16 | 16 | 16 |
| translation-format | 8 | 8 | 8 |
| voice | 4 | 4 | 4 |

## Languages and translation directions

Small subgroup counts do not establish performance for the whole language or domain.

| Group | Cases | Without ASDify: passes | With ASDify: passes |
| --- | ---: | ---: | ---: |
| de task | 2 | 2 | 2 |
| de->en | 1 | 1 | 1 |
| en task | 60 | 53 | 57 |
| en->de | 2 | 2 | 2 |
| en->es | 2 | 2 | 2 |
| en->fr | 2 | 2 | 2 |
| en->it | 2 | 2 | 2 |
| en->ja | 2 | 2 | 2 |
| en->pt-BR | 2 | 2 | 2 |
| en->ru | 2 | 2 | 2 |
| en->zh-CN | 2 | 2 | 2 |
| es task | 2 | 2 | 2 |
| es->en | 1 | 1 | 1 |
| fr task | 2 | 2 | 2 |
| fr->en | 1 | 1 | 1 |
| it task | 2 | 2 | 2 |
| it->en | 1 | 1 | 1 |
| ja task | 2 | 1 | 2 |
| ja->en | 1 | 1 | 1 |
| pt-BR task | 2 | 2 | 2 |
| pt-BR->en | 1 | 1 | 1 |
| ru task | 2 | 2 | 2 |
| ru->en | 1 | 1 | 1 |
| zh-CN task | 2 | 2 | 2 |
| zh-CN->en | 1 | 1 | 1 |

## Paired results

{"baseline_only_pass": 1, "both_pass": 91, "neither_confirmed_pass": 2, "skill_only_pass": 6}

Model-review preferences after strict-rule filtering (200 paired reviews, not 200 independent cases): {"A": 5, "B": 25, "invalid": 1, "neither": 3, "tie": 166}.
Both passes agree on preference in 93/100 cases.

## Cases with a failure or uncertain finding

### rel-005

**baseline:** strict review flag

- Although all listed invariants remain present, “usually takes” materially adds a frequency claim unsupported by the source.
- The later caveat does not remove the unsupported claim about what usually happens.

### rel-006

**baseline:** strict review flag

- Omits the observational design and adds an unspecified direction to the association.
- Omits the observational design and introduces an unsupported direction for the score difference.

### rel-036

**baseline:** strict review flag

- The recommendation is sound, but omits supplied pricing and capacity details required for the comparison.
- The recommendation is sound, but it omits material supplied option specifications, including B’s capacity and A’s price and capacity.

### rel-038

**baseline:** strict review flag

- Preserves the comparison and unknown needs. Calculations are supported, and the quoted per-device figures are qualified by full utilization; monthly billing is less explicit.
- The supplied facts and full-capacity calculations are preserved, but the added 'only' claim incorrectly restricts when B can have a lower per-device cost.

### rel-040

**baseline:** strict review flag

- The tax conclusion is correct, but required item costs are omitted, and the budget condition without optional training is not given.
- The with-training calculation and uncertainty are correct, but omitting training’s price or the without-training total loses the decision-relevant effect of declining the optional expense.

**skill:** strict review flag

- Correctly analyzes both training choices and unknown tax, but omits the required individual equipment and delivery prices.
- Although separate equipment and delivery prices are not repeated, their combined cost preserves the relevant budget information. Both optional-training scenarios and the unknown-tax limitation are retained.

### rel-053

**baseline:** strict review flag

- Retains the counts and conflict but changes the scope of verification and omits the explicit unverified status of both documents.
- Retains the conflicting counts but changes the scope of the verification caveat.

### rel-056

**baseline:** strict review flag

- Correctly communicates uncertainty but omits the damage finding and replacement order.
- It answers the timing question accurately but omits the damaged-connector finding and the confirmed replacement order.

**skill:** strict review flag

- Retains the update but introduces an unsupported actor for the replacement order.
- The timing uncertainty is faithfully conveyed, but the candidate invents the actor responsible for ordering the replacement.

### rel-060

**skill:** strict review flag

- Correctly rejects universal satisfaction and supplies a supported percentage, but omits the explicit self-selection limitation.
- The counts, conclusion, and approximately 73% calculation are supported, but the voluntary selection mechanism is omitted.

### rel-070

**baseline:** strict review flag

- The submission rule is intact, but the added need-based qualification changes the scope of the requesting permission.
- Retains the submission obligation but introduces a need-based qualification to the discretionary request.

## What this supports

These counts describe this frozen sample and model configuration. They do not establish a general failure probability, superiority over every model or prompt, or reliability on unseen high-stakes material. Review failures and disagreements before drawing a conclusion.

## Limits

- One generation model and one repetition; one explicit full-mode instruction condition.
- Two model-review passes share a model family with generation and can share blind spots.
- No independent bilingual/native-speaker review or user comprehension test.
- Small uneven language samples cannot certify any locale or translation direction.
- Neither native activation nor lite/ultra/off modes are evaluated.
- Source material is synthetic; tasks do not verify external factual truth.
- No concise-prompt control; this comparison cannot isolate value beyond Be concise.
- A passing sample cannot guarantee reliability on future tasks.

## Reproduction and evidence

See [metadata](metadata.json), [frozen cases](cases.jsonl), [raw generations](generations.jsonl), [per-case findings](case-results.jsonl), [aggregate data](summary.json), [judge instructions](judge.txt), and [unblinding key](unblinding-key.json). The raw folder retains CLI events, errors, usage and infrastructure attempts. Each review-*.json file retains both candidate ratings and exact-fragment evidence.

From the repository root:

```bash
python3 scripts/evaluate_skill.py report --output benchmarks/results/2026-10-08-reliability-100
```

See the [source-based audit of flagged answers](source-audit.md) for context-dependent omissions and observable meaning changes. This audit is by the implementing assistant, not an independent human reviewer.

[Declared review rule conflicts](review-exceptions.json) retain the original model JSON unchanged. Conservative aggregation counts listed defects as flags and rejects preferences for effectively failing answers. The CSV exports raw model verdicts; use summary.json for the strict combined counts. A reviewer can regard a missing checklist detail as immaterial to the question, while the stricter classifier still flags it; such a rule conflict does not by itself establish a semantic error.
