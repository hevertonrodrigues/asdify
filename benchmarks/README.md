# Evaluation: clarity with meaning preserved

**No live model study has been completed.** The fixtures, examples, and software checks establish a way to evaluate the skill; they are not evidence of improved writing.

## Compare against the obvious alternative

Run two separate, blinded, paired comparisons with the same held-out case set:

| Study | Control condition | Treatment condition | Question |
| --- | --- | --- | --- |
| `baseline-vs-skill` | Task alone | Same task plus canonical skill in `full` mode | Does the skill improve ordinary output? |
| `concise-vs-skill` | Same task plus `Be concise.` | Same task plus canonical skill in `full` mode | Does it add value beyond a shorter prompt? |

Use a separate ratings CSV and metadata file for each study and each model configuration. Keep any system instruction shared across conditions identical. Do not quietly strengthen the control instruction after looking at results; register any additional comparison in advance.

## Run the study

1. **Freeze inputs.** Record the repository revision (or skill checksum), model/version, host/version, system prompt, exact condition instructions, sampling settings, tools, date, case list, repetitions, and stopping rule. Start with [run-metadata-template.json](run-metadata-template.json); replace every `null` and empty list relevant to the study before running it.
2. **Separate development from evaluation.** `cases.jsonl` is a public regression set. It is useful for development but not held-out evidence. Collect a new frozen set that was not used to edit the skill. Include EN/PT-BR, long summaries, hard constraints, and already-clear text. Report selection criteria and exclusions.
3. **Generate independently.** Use fresh sessions with no previous outputs or other writing skills. The control must not inherit this repository's `AGENTS.md` or installed rule. Treatment gets the complete canonical skill and access to its references. Capture raw input and output for every case and repetition, including failures.
4. **Blind the review.** An organizer assigns opaque A/B labels to conditions and keeps their meaning hidden from reviewers. Keep the mapping consistent within each CSV so arm totals are meaningful. Randomize display order separately; remove host/skill labels without changing the writing. Each `run_id` identifies one paired repetition; both arms share it.
5. **Score independently.** At least two reviewers use the [rubric](../skills/asdify/references/quality-rubric.md). Mark a hard failure when a material fact, condition, obligation, citation, or safety detail is changed, invented, or lost. Use the source and invariants together; matching words alone does not establish meaning preservation.
6. **Record preference separately.** For each paired repetition/reviewer, record A, B, tie, or neither in a separate preference sheet with reviewer, case ID, run ID, reason, and hard-failure notes. A hard-failing output cannot win; if both fail, choose neither. Retain independent ratings before any disagreement resolution.
7. **Report with limits.** Publish per-case outputs and results, fidelity failures, dimension scores, paired preferences, reviewer agreement, and uncertainty. Repeated runs and multiple reviewers are not independent cases. Analyze or resample at the case level when estimating uncertainty. Report length, token usage, and latency as secondary measures. The supplied scorer does not compute preference, reviewer agreement, significance, or confidence intervals.

If a model version, skill revision, or instruction changes, start a new study rather than pooling incompatible rows.

## Public regression inputs

`cases.jsonl` contains 16 original inputs, evenly split between EN and PT-BR. They cover numerical qualifiers, legal modality, recommended versus required actions, uncertainty, technical identifiers, no-op editing, negation, ordered steps, citation attachment, contradictory sources, exact quotations, and requested voice.

The `invariants` are review criteria, not required substrings. For example, the obligation can be preserved with different words. A human checks whether the meaning survives. The source task remains authoritative if an invariant is incomplete.

Mode and activation checks are separate from this output study. In a real host session, test:

| Request | Expected behavior |
| --- | --- |
| Explicit request to rewrite an executive update | Skill available; follows requested mode |
| `lite` on a well-structured paragraph | Local edits; structure and voice preserved |
| `ultra` on a dense brief | Compression without losing conditions |
| `off` followed by a task | Optional style workflow disabled; higher-priority instructions still apply |
| Return a quote verbatim or an exact JSON object | Exact requested content/format preserved; no style preamble |
| Preserve deliberate humor or poetic voice | Voice survives; no forced business-writing style |

Record activation and behavior in [COMPATIBILITY.md](../docs/COMPATIBILITY.md). A correct output does not prove that the skill loaded; capture host evidence when available.

## Scoring CSV

Copy [ratings-template.csv](ratings-template.csv). Supply one row per **reviewer × case × paired run × arm**. Use integer values 1–5 for the six dimensions and 0/1 for `hard_fail`. `arm` is A or B. Never include condition names in a reviewer-facing CSV. Legacy CSV files without `run_id` are treated as one run; if the column is present, every row needs an ID.

```bash
python3 scripts/score_ratings.py path/to/filled-ratings.csv
```

The empty template deliberately fails. The scorer validates pairing and reports descriptive rating-level failure rates and dimension summaries. Those counts include each reviewer rating; they are not the number of unique failed outputs. Review disagreements and report output-level failures separately. No automatic winner is inferred from these summaries.

## Publish results

Use `benchmarks/runs/` for local drafts (gitignored). Publish reviewed, anonymized evidence in `benchmarks/results/<date>-<study>/`, following the [results checklist](results/README.md). Keep the mapping secret during grading, then publish it with the final study. Do not commit private source documents, API credentials, or identifying reviewer details.

Before making a broad effectiveness claim, seek benefit on both languages and at least two models with no material-fidelity regression. These are evaluation goals, not achieved results. A finding that the skill adds no benefit is a valid result.
