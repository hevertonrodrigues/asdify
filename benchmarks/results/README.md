# Published evaluations

No completed model evaluations have been published in this repository.

Create a directory such as `2026-10-08-concise-vs-skill/` only after collecting real outputs. Do not use editorial examples or synthetic ratings as results.

Include:

- A completed copy of [run-metadata-template.json](../run-metadata-template.json), frozen case inputs, and exact shared/condition prompts.
- Raw outputs for every case, arm, and repetition, with stable IDs; record errors and exclusions.
- Independent anonymized reviewer ratings, paired preferences, disagreement notes, and the final unblinding key.
- A report covering fidelity failures, clarity, preference, uncertainty, limitations, and unsuccessful cases. State the denominator for every rate.
- The command and version used for aggregation; identify any analysis beyond `scripts/score_ratings.py`.

Follow the [protocol](../README.md). A publication can report negative or inconclusive findings. Public evidence belongs here; local `benchmarks/runs/` is intentionally ignored by Git.
