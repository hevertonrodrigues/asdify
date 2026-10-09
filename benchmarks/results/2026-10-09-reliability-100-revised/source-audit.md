# Audit of revised-run flags

This is a fresh paired run after the initial results prompted two rule changes. It uses the same 100 cases and judge, with new outputs in both arms. The cases are development regression material, not held-out evidence. All model outputs and ratings remain unchanged; consult the [report](report.md) for complete strict counts and [all 100 pairs](comparisons.md) for the source and both answers.

This source-based audit is by the implementing assistant after unblinding. It is not independent human adjudication, native-speaker review, or a replacement for the original ratings. Strict flags include checklist details that may be unnecessary for the actual question. They are not established semantic error rates.

## The two targeted corrections

- **rel-056, unnamed actor:** The revised answer says the technician found the damaged connector and “a replacement has been ordered.” It leaves the ordering actor unspecified and preserves the unknown arrival date, installation duration, and finish date. The earlier invented actor is absent in this fresh output.
- **rel-060, sample selection:** The revised answer explicitly says “only customers who chose to respond were counted.” It retains all three response counts, the 52-person denominator, and the inability to claim satisfaction among all customers. Its approximately 73% figure is a supported calculation about respondents. The earlier omitted voluntary-selection caveat is present in this fresh output.

These are observations on the same cases used to improve the instructions. They do not show that either problem is impossible on unseen tasks. No further skill tuning or rerun was used to force a perfect score.

## Budget flag in both arms

For rel-040, both answers give the correct USD 2,630 without-training total, USD 2,930 with-training total, USD 570/USD 270 tax headroom, USD 3,200 budget, optionality, unknown tax, and inability to confirm the complete purchase. The USD 300 training increment can be recovered from the two totals. They omit the separate USD 2,450 equipment and USD 180 delivery prices; the skill answer also does not label its USD 2,630 subtotal as equipment plus delivery.

The totals preserve the meaning needed for this budget question. A strict checklist still flags the omitted component breakdown. A reviewer can consistently judge that detail missing and immaterial under the semantic rubric while the stricter classifier requires a flag. [Declared rule conflicts](review-exceptions.json) record this distinction and retain the original model judgments unchanged. Strict counts include both flagged answers; preferences conflicting with that strict rule are excluded rather than replacing the originals.

## Baseline flags

| Case | Source-based observation | Assessment limit |
| --- | --- | --- |
| rel-005 | An estimated interval becomes what delivery “usually takes.” | Adds unsupported usual-performance wording; the no-guarantee disclaimer remains. |
| rel-006 | “Observational” is omitted and a score “difference” becomes scores “higher.” | Loses the design qualifier and adds a direction not explicitly supplied. The confidence interval, sample size, and causal caveat survive. |
| rel-020 | Prior processing “under valid consent” becomes processing carried out before withdrawal without that explicit qualification. | The narrower source qualification is absent. The two reviewer passes differ on whether it is sufficiently implied by context; this audit does not decide real-world legal validity. |
| rel-036 | The valid recommendation retains A's 12-user limit, B's USD 590 price, the 19-user need, ceiling, no-splitting rule, and unverified uptime, but omits A's USD 420 price and B's full 25-user capacity. | Correct recommendation; whether the omitted specifications are essential is context-dependent. |
| rel-040 | Correct budget totals without separate component prices. | See the budget discussion above; strict checklist flag, not incorrect arithmetic. |
| rel-053 | The explicit unverified status of both documents is replaced by wording about the unresolved/unverified delivery count. | The counts and conflict survive, but the document-verification qualification is absent or changes scope. |
| rel-056 | Correctly states that finish date, replacement arrival, and installation duration are unknown but does not repeat diagnosis and the placed order. | Directly answers the question correctly. Requiring those background events is a stricter status-summary interpretation. |
| rel-066 | French “peut demander” retains permission, but the explicit “not obliged” clause is omitted. | The permissive verb can express the same discretion; reviewers differ. Treat this as an interpretation-sensitive checklist flag, not proof of a changed obligation. No independent French review took place. |
| rel-087 | German “vorläufigen” is translated as “estimated” rather than “provisional.” | Both retain the financial amounts, VAT exclusion, and nonbinding price caveat. Provisional status and estimation are not necessarily interchangeable; qualified bilingual review would resolve the contextual effect. No such human review is claimed. |

## Evidence and remaining limits

No protected-token, JSON, or requested verbatim-output failure was detected among the 200 fresh answers. The [evidence audit](evidence-audit.json) checks complete generation/review coverage, frozen hashes, prompt hashes and display order, unchanged raw answers and ratings, and observed tool activity.

The judge, model alias, and reasoning setting are unchanged; this run [references](calibration-reference.json) the initial 10 good/bad control pairs reviewed twice. Calibration was not repeated and is not counted as new benchmark output. The two reviewer passes share the generation model family. One generation per arm, short synthetic tasks, small language groups, and no concise-only control prevent broad claims about reliability, human comprehension, translation accuracy, or other hosts/modes.
