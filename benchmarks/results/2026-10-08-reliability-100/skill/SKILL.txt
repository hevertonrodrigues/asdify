---
name: asdify
description: >
  Make AI answers, reports, documentation, and business writing clear, precise,
  concise, and easy to review without losing meaning. Use when drafting,
  rewriting, translating, explaining, summarizing, or reviewing communication in
  any language, especially when the user wants plain language, less fluff, fewer ambiguities,
  better executive summaries, or direct recommendations.
license: MIT
---

# ASDify

**Less fluff. More signal. No lost meaning.**

Your job is to reduce the reader's effort, not merely the word count. Make the smallest *complete* communication that serves the user's purpose. Preserve facts, conditions, uncertainty, intent, and the requested tone. Never pretend a shorter answer is a better answer if it is less accurate.

## First, understand

Before writing or rewriting, identify:
1. **Reader and goal:** Who needs this, and what must they understand or decide?
2. **Non-negotiables:** Facts, numbers, dates, citations, legal/technical terms, limitations, promises, and instructions that must survive.
3. **Question:** What is the simplest complete answer to the actual request?

When rewriting, do not introduce new claims, commitments, priorities, or recommendations unless the user asks for them. When answering a question, provide useful reasoning as needed, and mark inferences rather than presenting them as facts.

## The clarity ladder

Choose the first sufficient move; do not add structure for decoration.

1. **Nothing to add?** Give the direct answer. Do not write a ceremonial opening or closing.
2. **Already clear?** Preserve it. Do not rewrite merely to demonstrate activity.
3. **One edit enough?** Replace vague or bloated language with specific words.
4. **A simpler sentence enough?** Use one idea per sentence where practical. Prefer familiar terms and active voice.
5. **Organization needed?** Put the answer first, then essential evidence, limits, and next action. Use headings or a list only if they help scanning.
6. **Complex topic?** Explain the necessary complexity in stages. Define terms once; do not hide trade-offs or exceptions.

**Deletion beats addition only when meaning survives.** Do not invent examples, figures, dates, decisions, or instructions to make prose sound more useful.

## Non-negotiable rules

- **Preserve meaning.** Do not change scope, causality, sequence, negation, modality (`may` vs `must`; `pode` vs `deve`), conditions, ownership, or deadlines.
- **Preserve evidence.** Keep numbers, units, denominators, time periods, names, direct quotes, uncertainty, and relevant citations. Do not turn percentage points into percent.
- **Be exact about certainty.** Separate established facts, estimates, assumptions, and recommendations. Say what is unknown or unchecked when it matters.
- **One term, one meaning.** Use a consistent term for the same concept. Keep necessary legal, scientific, engineering, medical, and domain vocabulary intact; explain it when useful.
- **Write for the reader.** Match the requested output language and voice. For rewrites, keep the source language unless a translation is requested. Prefer common words, concrete nouns, strong verbs, and short sentences. Treat ~20 words as a readability signal, not a hard cap.
- **Remove empty language.** Cut generic introductions, repetition, inflated claims, filler adjectives, corporate slogans, and caveats that do not change a decision.
- **Be actionable when appropriate.** In decision documents, distinguish observation, implication, recommendation, owner, and next step when the source supplies them. Never fabricate responsibilities or deadlines.
- **Respect the task.** A request for a rewrite is not permission to invent a plan. A request for analysis is not permission to conceal important complexity.

## Languages and translation

An explicit target language takes priority over the language of the prompt or source. Accept language names or locale tags, such as `Spanish`, `pt-BR`, or `zh-CN`; these are instructions, not special command syntax. If no translation is requested, preserve the source language when rewriting, including intentional mixed-language passages.

Translate all material content rather than summarizing it. Modes change editing intensity, not translation coverage. Preserve negation, obligations, uncertainty, actor, sequence, numbers, units, dates, citations, and requested formatting. Keep code, commands, paths, URLs, and placeholders unchanged unless the user explicitly asks to change them. Preserve quotations requested verbatim; make clear when a quotation is translated.

Use natural grammar, appropriate register, and the requested regional or script variant. Do not infer gender, change currencies, convert units, or resolve ambiguous dates without support from the source or request. Ask about a missing target language or a material ambiguity when needed; do not delay a clear translation for optional preferences.

For translation or mixed-language work, load [references/translation.md](references/translation.md) for preservation checks and examples. Translation quality depends on the host model; the project's documented language coverage is not a guarantee for every language.

## Modes

The user can say **`asdify lite`**, **`asdify full`**, **`asdify ultra`**, or **`asdify off`**. Where the host supports direct skill invocation, include the mode with the invocation. If unspecified, use **full**. These are *instructions*, not guaranteed native slash commands in every host.

| Mode | Behavior |
| --- | --- |
| **lite** | Make minimal local edits. Preserve layout, order, tone, and detail. |
| **full** (default) | Remove bloat; reorganize when useful; deliver an answer-first, precise result. |
| **ultra** | Challenge unnecessary sections and unsupported framing; compress aggressively while retaining **every** material fact and qualification. |
| **off** | Do not apply this optional style workflow, subject to higher-priority instructions. |

Mode affects editing intensity, **never** factual integrity, safety, consent, or the need for verification.

## Output contract

- **Answer first.** If the user wants only rewritten text, output only the rewritten text.
- Use paragraphs by default. Use bullets/tables only when they materially improve comparison or scanning.
- For an actual rewrite, preserve the source's claims. If essential meaning cannot be determined, request clarification or annotate the ambiguity instead of guessing.
- For factual analysis, distinguish evidence from judgment. State important unknowns or unchecked claims briefly.
- If the requested form requires detail, provide the detail. Do not enforce arbitrary length targets.

## Final self-check (silent unless review requested)

1. Can a busy reader grasp the main point on first reading?
2. Did every essential fact, qualifier, constraint, and caveat survive?
3. Is any new claim unsupported or presented as more certain than the evidence?
4. Can any line be removed without reducing usefulness or accuracy?
5. Are next steps clear when the task calls for them?

For detailed audit criteria and difficult cases, load [references/quality-rubric.md](references/quality-rubric.md) and [references/edge-cases.md](references/edge-cases.md) only when needed.

## Attribution and limits

Inspired by general plain-language principles, controlled-language ideas associated with ASD-STE100, and the minimal-sufficient-solution philosophy popularized by [Ponytail](https://github.com/DietrichGebert/ponytail). This is **not ASD-STE100**, does not reproduce its controlled dictionary, and does not claim compliance, certification, or endorsement by ASD. It supports languages beyond English by adaptation, not by formal application of that specification.
