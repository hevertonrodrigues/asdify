# Supplemental source audit

The original strict benchmark is unchanged. This supplemental, blinded review checked source meaning separately from literary voice and format. It found genuine errors, uncertain wording, and strict checklist flags that another model reviewer judged faithful to the requested scope. It does not replace the two-pass primary scores.

## Selection and blinding

The selection plan was written after primary outputs existed, before this audit. It is a post-output analysis, not a preregistered endpoint. The sample is the union of 90 seeded cases (10 per locale, without outcome filtering) and all 78 cases containing any strict non-pass; four cases overlap. All five candidates for each of the 164 selected cases were reviewed: 820 annotations. This failure-enriched sample cannot estimate population reliability.

Three model assistants reviewed locales different from their original case-authoring assignments. They received the original task and candidates under newly shuffled opaque labels Q/R/S/T/U, without the numbered invariants, original ratings, conditions, or proposed fixes. Each candidate received separate meaning, voice, and format judgments with a source-grounded reason. They were instructed to respect the requested scope and retain source ambiguity. These are model judgments, not human or native-speaker certification; the collaboration API did not expose an immutable reviewer model snapshot.

All three assistants finished before the key was released and the annotations were sealed at `2026-10-09T09:20:55.029424+00:00`. The [integrity audit](source-audit/audit-integrity.json) checks selection, complete coverage, hashes, and identity with the original raw answers. It verifies provenance, not the correctness of judgments.

## Judgments in the selected sample

Every row has 164 candidates. Counts below are supplemental judgments, not revised benchmark pass rates.

| Condition | Meaning preserved | Meaning changed | Meaning uncertain | Voice changed |
| --- | ---: | ---: | ---: | ---: |
| baseline | 142 | 18 | 4 | 0 |
| lite | 163 | 1 | 0 | 1 |
| full | 162 | 1 | 1 | 1 |
| ultra | 155 | 7 | 2 | 1 |
| off | 160 | 4 | 0 | 0 |

Of the 135 strict non-passing answers, this reviewer judged 103 as preserving meaning, 28 as changing meaning, and four as uncertain. This disagreement often concerns requested summary scope, exact wording, or format; it does not automatically establish that the primary reviewer was wrong. Three answers that passed the primary checks received a changed-meaning judgment here, and three received uncertain-meaning judgments. Agreement between two model reviews can therefore miss errors.

## Findings and limits

- **Role changes:** German `full` case 087 substitutes property administration for a caretaker. Japanese `ultra` case 088 turns a baker into a shop proprietor. Portuguese `lite` case 096 assigns an engineer responsibility for the engineering function. These changes are not justified by the source, even if wording is intended to avoid unsupported gender.
- **Scope and uncertainty:** English `ultra` case 002 broadens a visitor-only obligation to anyone. English `ultra` case 007 turns lack of implication into a negative approval claim. Spanish `ultra` case 007 makes a similar shift despite passing the primary reviews. Italian `ultra` case 079 drops a possibility qualifier inside an attributed opinion and also passed the primary reviews.
- **Uncertain wording:** Portuguese case 004 has two skill answers where “Não se verificaram diferenças” can mean no differences were found, while the source says no comparison was made. This remains uncertain rather than a confirmed error. French case 078, Italian cases 046/070, Russian case 029, and Chinese case 029 also retain ambiguity in the annotations.
- **Voice and grammatical gender:** Russian case 089 preserves the events but `lite`, `full`, and `ultra` use stiff passive/impersonal narration. Root inspection additionally notes masculine past-tense narration in the baseline and `off`, although the English source does not establish the narrator’s gender; compare the [Russian past-tense forms](https://gramota.ru/meta/otkryt). A more conversational rewrite must not silently solve the voice problem by inventing gender. No blanket instruction to force gendered active past tense is justified.
- **Strict scope and exact checks:** Several narrow questions or summaries preserve the answer while omitting unrelated background demanded by a numbered invariant. Some identifiers and quotation delimiters also trigger literal checks. Both the strict flags and the supplemental opinions remain public; neither rubric nor raw answer was changed.
- **Incomplete coverage:** Only selected cases received this additional review. One assistant reviewed each selected candidate, using the same general model ecosystem as generation. Ambiguities and grader blind spots remain; this is not a general reliability guarantee.

## Proposed follow-up

A small candidate edit makes role specificity and uncertainty distinctions explicit, with German, Japanese, and Portuguese translation reminders. The [prospective development plan](../../experiments/2026-10-09-language-guards/plan.json) selects 100 already examined cases across all nine locales, freezes its retention rule before new outputs, and uses fresh answers in all five conditions. The original 900-case table remains the score for the original frozen skill. The follow-up is not held-out evidence.

## Reproduce and inspect

Run `python3 scripts/audit_mode_source.py --output benchmarks/results/2026-10-09-multilingual-modes-four-workers` from the repository root.

[Selection plan](source-audit-plan.json), [review instructions](source-audit-instructions.md), [selection manifest](source-audit/selection-manifest.json), [released label key](source-audit/opaque-label-key.json), [all inputs and annotations](source-audit/).
