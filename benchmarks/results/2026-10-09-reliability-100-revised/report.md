# 100-case ASDify comparison

Observed model outputs and automated/model review, not a reliability certification.

Model: gpt-6.1-sol; generation reasoning: medium; one fresh-session output per arm per case. ASDify full mode and all references were injected.

100 synthetic cases produced 200 answers. Two blinded, fresh-session model-review passes checked each answer against 373 source invariants per arm. Review pass 2 reverses candidate display order. Exact JSON, protected-token, and verbatim-output checks supplement semantic review. Any reviewer hard failure or missing/changed invariant counts as a strict flag, even when a reviewer considers that omission immaterial; an uncertain check prevents a confirmed pass. No semantic failures were regenerated or excluded. These are conservative model-review classifications, not established error rates.

Source tasks contain 49–740 Unicode characters including instructions (mean 213.6). This evaluates short supplied passages and questions, not long documents, retrieval, or real-world fact checking.

| Measure | Without ASDify | With ASDify |
| --- | ---: | ---: |
| Confirmed passes / 100 | 91 | 99 |
| Outputs flagged / 100 | 9 | 1 |
| Outputs with uncertain checks / 100 | 0 | 0 |
| Reviewer hard-failure disagreements / 100 | 3 | 0 |
| Verdicts differing from the strict invariant rule | 2 | 2 |

## Scores

Means of 200 model ratings per arm; these ordinal scores are descriptive.

| Dimension (1–5) | Without ASDify | With ASDify |
| --- | ---: | ---: |
| meaning_fidelity | 4.86 | 4.99 |
| clarity | 4.945 | 4.975 |
| signal_density | 4.955 | 4.965 |
| structure | 4.975 | 4.985 |
| calibration | 4.915 | 5.0 |
| fit_for_purpose | 4.815 | 4.975 |

## Length and execution

Descriptive means over the same multilingual case mix; characters and tokens do not measure clarity or translation quality. CLI input tokens include the condition prompt. Generation time includes CLI startup and infrastructure retries, excludes grading, and is not total elapsed study time because requests overlap.

| Measure | Without ASDify | With ASDify |
| --- | ---: | ---: |
| Output characters | 182.8 | 180.2 |
| CLI input tokens | 3745.0 | 7009.0 |
| CLI output tokens | 48.1 | 51.2 |
| Generation request seconds | 38.67 | 40.07 |

## Task groups

Small subgroup counts do not establish performance for the whole language or domain.

| Group | Cases | Without ASDify: passes | With ASDify: passes |
| --- | ---: | ---: | ---: |
| ambiguity | 4 | 3 | 4 |
| analysis | 8 | 5 | 7 |
| conditions | 11 | 10 | 11 |
| format | 4 | 4 | 4 |
| native-rewrite | 16 | 15 | 16 |
| numbers | 10 | 8 | 10 |
| scope | 4 | 4 | 4 |
| summary | 5 | 5 | 5 |
| technical | 10 | 10 | 10 |
| translation | 16 | 15 | 16 |
| translation-format | 8 | 8 | 8 |
| voice | 4 | 4 | 4 |

## Languages and translation directions

Small subgroup counts do not establish performance for the whole language or domain.

| Group | Cases | Without ASDify: passes | With ASDify: passes |
| --- | ---: | ---: | ---: |
| de task | 2 | 2 | 2 |
| de->en | 1 | 0 | 1 |
| en task | 60 | 53 | 59 |
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
| fr task | 2 | 1 | 2 |
| fr->en | 1 | 1 | 1 |
| it task | 2 | 2 | 2 |
| it->en | 1 | 1 | 1 |
| ja task | 2 | 2 | 2 |
| ja->en | 1 | 1 | 1 |
| pt-BR task | 2 | 2 | 2 |
| pt-BR->en | 1 | 1 | 1 |
| ru task | 2 | 2 | 2 |
| ru->en | 1 | 1 | 1 |
| zh-CN task | 2 | 2 | 2 |
| zh-CN->en | 1 | 1 | 1 |

## Paired results

{"both_pass": 91, "neither_confirmed_pass": 1, "skill_only_pass": 8}

Model-review preferences after strict-rule filtering (200 paired reviews, not 200 independent cases): {"A": 8, "B": 29, "invalid": 2, "tie": 161}.
Both passes agree on preference in 89/100 cases.

## Cases with a failure or uncertain finding

### rel-005

**baseline:** strict review flag

- Readable, but materially changes an estimated interval into an unsupported usual-performance claim.
- The readable simplification materially changes the estimate's epistemic status. The non-guarantee disclaimer does not restore the missing estimate qualification.

### rel-006

**baseline:** strict review flag

- Omits the observational design and introduces an unspecified direction for the score difference.
- Omits the observational design, adds an unsupported direction, and weakens the causal limitation.

### rel-020

**baseline:** strict review flag

- Preserves prospective withdrawal and separate retention duties. Unchanged prior lawfulness preserves valid-consent processing without asserting that all prior processing was lawful.
- Readable and otherwise complete, but removes a material qualification from the protection of prior processing.

### rel-036

**baseline:** strict review flag

- Correct recommendation and uncertainty, but the supplied comparison loses A’s price and B’s full capacity.
- The recommendation is correct, but it omits supplied comparison facts: A’s price and B’s actual capacity.

### rel-040

**baseline:** strict review flag

- Individual component prices are omitted, but the correct totals preserve all decision-relevant budget meaning. No tax rate or taxable scope is invented.
- The separate cost breakdown is omitted, but its correct subtotal preserves the decision-relevant budget meaning. Optional training and unknown tax are handled correctly.

**skill:** strict review flag

- Correctly answers the budget question with both optional-training scenarios. The omitted component breakdown does not change the decision-relevant conclusion.
- The separate cost breakdown is omitted, but correct before-tax totals preserve the decision-relevant meaning. No tax rate or guaranteed affordability is invented.

### rel-053

**baseline:** strict review flag

- Changes the object of verification and omits the explicit warning that both documents are unverified.
- Preserves the numerical conflict but loses the explicit, decision-relevant verification status of both source documents.

### rel-056

**baseline:** strict review flag

- Correctly conveys uncertainty but omits the diagnosed damage and the replacement order, material repair-status information.
- Correctly communicates the unknown completion date but omits the damage finding and confirmed replacement order.

### rel-066

**baseline:** strict review flag

- The explicit absence of an obligation is omitted; all other source meaning is retained.
- Preserves all source meaning; optionality is conveyed by “peut” rather than stated separately.

### rel-087

**baseline:** strict review flag

- The source describes the costs as provisional, not estimated. The remaining financial terms and disclaimer are preserved.
- Retains all decision-relevant meaning; “estimated” conveys the tentative pricing in context.

## What this supports

These counts describe this frozen sample and model configuration. They do not establish a general failure probability, superiority over every model or prompt, or reliability on unseen high-stakes material. Review failures and disagreements before drawing a conclusion.

This is a regression run on public/development cases, not held-out evidence of generalization.

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
python3 scripts/evaluate_skill.py report --output benchmarks/results/2026-10-09-reliability-100-revised
```

See the [source-based audit of flagged answers](source-audit.md) for context-dependent omissions and observable meaning changes. This audit is by the implementing assistant, not an independent human reviewer.

[Declared review rule conflicts](review-exceptions.json) retain the original model JSON unchanged. Conservative aggregation counts listed defects as flags and rejects preferences for effectively failing answers. The CSV exports raw model verdicts; use summary.json for the strict combined counts. A reviewer can regard a missing checklist detail as immaterial to the question, while the stricter classifier still flags it; such a rule conflict does not by itself establish a semantic error.
