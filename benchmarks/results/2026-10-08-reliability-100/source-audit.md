# Audit of first-run flags

The conservative result is **97/100 skill-assisted passes and 92/100 baseline passes**. These counts retain every model-review flag, including context-dependent omissions. They are not estimated real-world error rates. All 200 generated answers and 400 ratings remain unchanged.

This source-based audit was written by the implementing assistant after unblinding. It is not independent human adjudication, a native-speaker review, or a replacement for the original ratings. See [all source tasks and answer pairs](comparisons.md) and [per-case findings](case-results.jsonl).

## Skill-assisted answers

| Case | Source and answer difference | Assessment |
| --- | --- | --- |
| rel-040 | Source item prices are USD 2,450 and USD 180. The answer gives their correct combined USD 2,630, both optional-training scenarios, available tax headroom, and the inability to confirm the purchase without tax. | The decision-relevant budget meaning is preserved. Requiring both item prices to be repeated is stricter than this question needs. Both reviewers mark that invariant missing; one nevertheless marks the answer as passing and prefers it. Keep the strict flag and declare that internal inconsistency. |
| rel-056 | Source: “The technician found a damaged connector. A replacement has been ordered.” Answer: the technician “found a damaged connector and ordered a replacement.” | Observable actor invention: the source does not identify who ordered the replacement. The unknown completion time remains intact. |
| rel-060 | Source limits the sample to customers who chose to respond. The answer retains the counts, the inability to claim all customers are satisfied, and the distinction from nonrespondents, but omits voluntary participation. | The conclusion remains correct, but the self-selection limitation is lost. The approximately 73% calculation is supported and is not an invented fact. |

Only rel-056 and rel-060 motivated skill changes: keep unnamed actors unnamed and preserve sampling/selection methods. The budget case did not motivate a rule to repeat every input number. The follow-up uses the same frozen cases and judge with new outputs in both arms; it is a development regression check, not a held-out replication. The initial failures remain published.

## Baseline answers

| Case | Observed difference | Assessment |
| --- | --- | --- |
| rel-005 | An estimated delivery interval becomes what delivery “usually takes.” | Adds an unsupported frequency claim; the later estimate disclaimer does not supply evidence for it. |
| rel-006 | “Observational” is omitted; an associated score “difference” becomes scores “higher.” | Loses the study-design qualifier and adds a direction not explicitly stated in the source. The no-causation caveat survives. |
| rel-036 | Recommends the valid plan and explains the capacity/budget decision, but does not repeat A's exact price/capacity or B's full 25-user capacity. | The recommendation is correct. The strict comparison checklist flags omitted specifications; whether all are essential in a recommendation is context-dependent. |
| rel-038 | Says B's lower per-device cost applies “only when all included devices are used.” | Unsupported necessary condition. At nine devices B is CAD 160/device/year, already below A's full-capacity CAD 183.33. The supplied comparison and unknown buyer needs survive. |
| rel-040 | Gives only the with-training USD 2,930 total and USD 270 tax headroom; does not give the without-training scenario or the optional training's USD 300 price. | Correct unknown-tax conclusion. Omitting the alternative loses a useful budget choice; not repeating each component price is separately context-dependent. |
| rel-053 | “Both documents are unverified” becomes “Completed deliveries remain unverified.” | Changes the scope of verification from the source documents to the deliveries. The unresolved 18/21 conflict survives. |
| rel-056 | States that the finish date, arrival date, and installation duration are unknown; omits discovery of damage and the already-placed order. | Directly answers the finish-date question correctly. The strict invariant requires background events that may be optional for this answer. |
| rel-070 | Japanese answer adds “必要に応じて” (“as needed”) to the discretionary request for documents. | A qualification absent from the source. Both automated reviewers flag it; its practical effect needs qualified Japanese review. This audit does not claim such a review took place. |

## Grader and evidence checks

The two reviewer passes caught every deliberately defective calibration answer and passed every authored good answer: 10 pairs reviewed twice, or 20 positive and 20 negative ratings. These simple controls do not establish sensitivity to every subtle defect or eliminate false positives.

The review rule conflict for rel-040/B is recorded in [review-exceptions.json](review-exceptions.json). The reviewer judges omitted component prices immaterial to this question; the stricter classifier flags every missing invariant. This is a rule conflict, not an error in the budget arithmetic. The original JSON is retained byte-for-byte in the raw model answer and unchanged as parsed JSON. Strict aggregation treats the listed omission as a flag and excludes the preference under that rule. CSV ratings retain raw `hard_fail` values, so their rating-level rates differ from the output-level strict result.

No protected-token, JSON, or requested verbatim-output failure was detected in either arm. The [evidence audit](evidence-audit.json) verifies frozen input hashes, exact generation/review prompt hashes, candidate display order, raw-answer fidelity, and complete coverage. It checks provenance and completeness, not semantic truth. The reviewers share the generation model family, so the study cannot certify reliability on unseen material.
