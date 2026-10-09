# Supplemental source audit instructions

These instructions apply to the blinded source audit described in [the selection plan](source-audit-plan.json). This is a supplemental model-assistant review, not independent human adjudication. It cannot replace or revise the primary strict scores.

Read every source task and all five candidate answers in each assigned input row. Judge the task's requested scope, not whether the answer repeats every background sentence. A direct question can legitimately exclude unrelated source details. A translation or complete rewrite must preserve all material content requested by the source.

Check factual meaning, numbers and units, conditions, negation, obligations, uncertainty, actors, ownership, and sequence. Check requested voice and format separately. Natural equivalent wording is allowed unless the task explicitly protects exact wording. Do not reward length or penalize brevity by itself. Mark a judgment uncertain when the source or translation admits materially different readings; explain the ambiguity rather than forcing a pass or failure.

For each candidate, return:

- `label`: its opaque input label, unchanged.
- `meaning`: `preserved`, `changed`, or `uncertain`.
- `voice`: `preserved`, `changed`, `uncertain`, or `not_applicable`.
- `format`: `preserved`, `changed`, `uncertain`, or `not_applicable`.
- `reason`: a concise explanation anchored in the source and answer. For a change or uncertainty, identify the relevant wording and its consequence. For a preserved answer, identify the important content retained.

Write one JSON object per line in the assigned annotation file:

```json
{"case_id":"input case ID","candidates":[{"label":"Q","meaning":"preserved","voice":"not_applicable","format":"not_applicable","reason":"Source-grounded explanation."}]}
```

The example shows one candidate only to describe the schema. Each real row must contain all five unique input labels. Keep a separate row for every assigned case, including cases whose answers are identical. Do not omit difficult cases. Save completed rows as you work and check completeness before reporting completion.

Auditors receive only these instructions and their assigned `source-audit/inputs-<language>.jsonl` files. Do not read authored invariants, primary reviews, primary results, condition names, selection reasons, other auditors' annotations, the label key, or proposed skill changes. Do not infer or guess the hidden conditions. Do not use live model CLI calls, delegate further, or spawn agents.

Each auditor owns only the annotation files assigned to it. Other people and agents share the repository: do not revert their edits or change the skill, cases, runner, primary evidence, or another auditor's files. This review records judgments; it does not modify the tested answers.
