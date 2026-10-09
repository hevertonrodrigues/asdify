# Edge cases and preservation checklist

- **Numbers:** Keep base, timeframe, currency, units, significant digits, percent vs percentage points, `at least`/`up to` qualifiers, and ranges.
- **Legal and compliance:** Do not weaken obligations, exemptions, defined terms, or jurisdiction. Do not summarize away exceptions. Keep verbatim clauses when exact wording matters.
- **Safety and medicine:** Keep warnings, contraindications, steps, and uncertainty. Do not prioritize readability over safe meaning.
- **Engineering/API:** Keep identifiers, signatures, error codes, file paths, and protocols exact. Explain jargon, don't rename interfaces.
- **Scientific reporting:** Preserve association vs causation, sample size, estimates, confidence intervals, and limitations. Keep population and selection details such as voluntary participation, nonresponse, and exclusions; naming respondents alone does not preserve a self-selection caveat.
- **Instructions:** Preserve sequence, prerequisites, responsible parties, and optional vs mandatory steps. Combining clauses must not attach an unnamed action to a named actor: "The technician found damage. A replacement was ordered" does not establish that the technician placed the order.
- **Marketing:** Persuasive tone is allowed. Do not create unsupported superlatives, statistics, testimonials, or guarantees.
- **Executive summaries:** Prioritize decisions, metrics, risks, and actions only when supported by the source.
- **Creative writing and branding:** Follow requested style; do not flatten intentional rhythm, voice, idioms, or humor.
- **Multilingual:** Keep the source language unless translation is requested. Follow the explicit target language, locale, script, and register; preserve intentional language mixing. See [translation.md](translation.md) for translation checks. Controlled vocabulary from ASD-STE100 applies to English only; this project does not enforce it.
- **Conflicting inputs:** Do not silently reconcile inconsistent facts. Flag a material conflict if required to complete the task.
- **Extremely short requests:** Reply directly; no headings or manufactured "next steps."

Three anti-patterns:

1. **Overcompression:** `Revenue grew` loses `Revenue grew 12% year over year in Brazil, excluding refunds.`
2. **False precision:** `There may be delays` must not become `Delivery will take 3 days.`
3. **Unasked advice:** A request to rewrite a paragraph must not be changed into a business plan.
