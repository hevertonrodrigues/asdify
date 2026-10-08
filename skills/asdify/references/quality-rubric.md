# Quality rubric (human or evaluator)

Assess each dimension independently. Use 1–5 (1 = poor, 3 = acceptable, 5 = excellent). Include short evidence for low scores.

| Dimension | What a score of 5 requires | Failure examples |
| --- | --- | --- |
| Meaning fidelity | Every material claim, number, qualifier, deadline, causal relationship, and obligation is intact | `may` becomes `must`; 14 percentage points becomes 14% |
| Clarity | Main answer is understood on first reading; terms are defined where needed | Ambiguous pronouns, layered subordinate clauses |
| Signal density | Almost every sentence informs a decision or understanding | Empty intro, slogans, repetitive caveats |
| Structure | Answer first; logical sequence; appropriate formatting | Key conclusion hidden at end |
| Calibration | Evidence, inference, unknowns, and uncertainty are distinguishable | Unchecked claims written as verified facts |
| Fit for purpose | Meets audience, language, tone, length, and task type | A simple rewrite adds a strategy document |

**Hard fail:** Any material factual distortion, changed obligation, fabricated data, removed safety-critical instruction, or invented citation. A short but incorrect output cannot win a benchmark.

Review procedure:
1. Read source and mark its material invariants.
2. Read candidate output without seeing which system made it.
3. Grade each dimension. Mark any hard fail.
4. Explain failures with exact fragments; don't reward shorter length by itself.
5. Compare candidates only after independent grading.

Optional diagnostics, not targets: sentence length distribution, duplicated phrases, token count, reading time. These measures do not prove comprehension or semantic equivalence.
