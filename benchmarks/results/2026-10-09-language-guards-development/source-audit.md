# Blinded source audit of the development retest

All 100 frozen development cases received a separate source-text review: **500 candidate annotations** across all five conditions. Six of the seven targeted meaning errors were absent in the fresh answers. English `ultra` case 007 still turns a limit on what approval establishes into a claim that other approval was not given. Other errors and ambiguities remain.

## Method and integrity

The [audit plan](source-audit-plan.json) was written during generation, before any fresh primary review returned. It selected every frozen development case, without filtering by outcomes. This is a development audit after the original study, not a preregistered primary-study endpoint or independent human adjudication.

Three existing model assistants reviewed locales different from their original case authorship. They are the same assistants used for the earlier supplemental source audit. Each received only the [audit instructions](source-audit-instructions.md) and assigned source/answer inputs with fresh Q/R/S/T/U labels. They were instructed not to read invariants, primary ratings, conditions, keys, proposed changes, or other annotations, and not to infer hidden conditions. The immutable reviewer snapshot was not exposed.

The CLI run finished before the first auditor started. Agents then ran one at a time: French/German/Italian, Japanese/Chinese/Russian, and English/Portuguese/Spanish. The [execution record](source-audit/execution.json) contains root-assistant dispatch/completion timestamps, not independent process telemetry. All three finished before the key was released and the evidence sealed at **2026-10-09 11:25:49 UTC**.

The [integrity record](source-audit/audit-integrity.json) verifies complete annotations, raw-answer identity, source tasks, selection, blind labels, and file hashes. It does not verify semantic truth. The [selection manifest](source-audit/selection-manifest.json), [released key](source-audit/opaque-label-key.json), and all nine input/annotation pairs are published in [source-audit/](source-audit/). The original strict scores are unchanged.

## Source judgments on this selected sample

Each row covers 100 fresh answers. Counts are model-assistant judgments, not language-wide reliability estimates.

| Condition | Meaning preserved | Meaning changed | Meaning uncertain |
| --- | ---: | ---: | ---: |
| No skill | 89 | 8 | 3 |
| Lite | 94 | 3 | 3 |
| Full | 95 | 2 | 3 |
| Ultra | 95 | 3 | 2 |
| Off | 96 | 1 | 3 |

Four candidates received changed-voice judgments, all in Russian case 089: lite, full, ultra, and off. No changed or uncertain format judgments were recorded. These counts cannot establish that every unflagged answer is correct.

Among the 28 primary strict non-passes, this audit judged 15 as preserving meaning and 13 as changing it. A strict non-pass can also reflect voice, scope, or an exact requirement. Among primary passes, the source audit found four changed-meaning judgments and 14 uncertain judgments. These disagreements remain public; neither the primary ratings nor the strict classifier was revised.

## Seven targeted answers

| Case and mode | Earlier source-supported error | Fresh source judgment |
| --- | --- | --- |
| en-002, ultra | Visitor-only obligation broadened to anyone | Preserved: obligation stays with visitors |
| en-007, ultra | Lack of implication changed to nonapproval | Changed: same error remains |
| es-007, ultra | Invitation approval changed to a claim about other approval | Preserved: approval does not authorize opening or set a date |
| de-087, full | Caretaker replaced by property administration | Preserved: caretaker function retained |
| ja-088, ultra | Baker changed to shop proprietor | Preserved: baker retained without ownership |
| pt-BR-096, lite | Engineer assigned responsibility for engineering | Preserved: engineer role retained |
| it-079, ultra | Possibility removed from an attributed opinion | Preserved: the possible usefulness remains |

The root assistant also inspected all seven fresh source/answer pairs after key release. No additional material error was found within those seven answers. This is another model-based inspection, not an independent human review. See the complete before/after judgments in [development-comparison.json](development-comparison.json) and the [retention decision](development-decision.md).

## Remaining findings

- **Approval scope:** English `ultra` case 007 still says Noor approved labels, “not the lighting, the room,” where the source only limits what label approval establishes.
- **Time attachment:** Chinese case 098 in lite/full puts the earlier appointment before Sunday and loses the explicit Sunday help offer. Portuguese case 045 in lite/full dates the review instead of the invoices. Its omitted future action is consistent with the narrow request for audit results; that scope disagreement does not remove the time-attachment concern or the strict flag.
- **Execution and terminology:** Russian `ultra` case 033 changes restoration “not performed” to “not verified.” Russian case 097 in baseline/lite/ultra/off uses a defect-rate term for a rejection rate, although the source does not establish defects as the rejection reason. Those four case-097 answers passed the primary checks.
- **Voice:** Russian case 089 retains events but uses stiff passive/impersonal narration in four conditions. A more conversational wording must also preserve unknown narrator gender; this study does not establish a safe general solution.
- **Uncertainty:** Portuguese case 004 still has wording that can mean no differences were found, while the source says no comparison was performed. German case 078 has a repairer-pronoun concern; German case 085 leaves the type of “seals” unspecified; Chinese case 029 leaves events per visitor versus unique-visitor share ambiguous; Portuguese case 096 leaves “checker” as potentially a person or software. The annotations retain these uncertainties.

All 35 changed/uncertain meaning or changed-voice findings, including control conditions, appear in [development-comparison.json](development-comparison.json). They do not all have the same severity or imply that the candidate caused the change. Known failures, fresh sampling, different batch neighbors, and shared model blind spots limit this retest. Further testing can contradict these judgments.

Recheck the sealed evidence without model calls:

```bash
python3 scripts/audit_mode_source.py --output benchmarks/results/2026-10-09-language-guards-development
```
