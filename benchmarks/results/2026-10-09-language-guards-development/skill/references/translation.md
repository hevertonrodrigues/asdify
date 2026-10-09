# Translation and multilingual editing

Use these checks when the task changes languages or includes mixed-language text. The same preservation rules apply in every mode.

## Choose the output language

- Follow an explicit target, even if the instructions use another language: an English prompt asking for Japanese gets Japanese output.
- Accept ordinary requests such as `Translate into Italian` or `Use asdify lite. Translate into pt-BR.` No locale flag or extra installation is needed.
- If asked to translate without a target and context does not supply it, ask which language. If asked only to rewrite, keep the source language.
- Honor a supplied regional or script variant, such as Brazilian Portuguese or Simplified Chinese. Do not substitute a different variant silently.
- Keep deliberate language mixing during a rewrite. During a translation, translate prose into the target and retain protected tokens.

## Preserve what can change meaning

| Source feature | Translation check |
| --- | --- |
| Permission, requirement, recommendation | `may`, `must`, and `should` retain their distinct force. |
| Negation and conditions | Keep `not`, `unless`, `only after`, and whether all or any conditions are required. |
| Numbers and units | Keep value, sign, denominator, timeframe, currency, and percent versus percentage points. Localize separators only when the value stays unambiguous. |
| Dates and times | Keep the actual date and timezone. An ambiguous `03/04` needs clarification if the target requires interpreting it. |
| Technical content | Keep `HTTP 429`, `Retry-After`, code, commands, filenames, URLs, JSON keys, and placeholders such as `{name}` or `{{count}}` exact unless changes are requested. |
| Names and grammatical gender | Do not invent gender or replace a name with an unsupported spelling. Use neutral phrasing when the source does not establish gender. |
| Roles and authority | Preserve the person's occupation or function when choosing neutral wording; do not substitute an owner, manager, or institution. |
| Citations and quotations | Keep attribution and each citation with its claim. Leave a quotation verbatim when requested; label translations of quotations when the task requires that distinction. |
| Format and voice | Preserve requested Markdown, list order, markup, register, humor, and politeness. A target's grammar may require different word order. |

Do not silently convert units, exchange currencies, substitute local law, or add cultural assumptions. Preserve exact wording the user protects, even when the surrounding prose is translated.

Role distinctions also matter across languages. In German, a caretaker is not the property administration (`Hausverwaltung`). In Japanese, a baker (`パン職人`) need not own the shop (`店主`). In Portuguese, an engineer need not be responsible for the whole engineering function. Avoiding unsupported gender must not change the role.

## Illustrative example

Source:

> If the API returns HTTP 429, the client should wait for the interval in Retry-After before retrying. This is a recommendation, not a requirement.

Spanish translation:

> Si la API devuelve HTTP 429, se recomienda que el cliente espere el intervalo indicado en Retry-After antes de volver a intentarlo. Es una recomendación, no una obligación.

Preserve the client as actor, the conditional trigger, both identifiers, waiting before retrying, and recommendation rather than obligation. This is an editorial example, not recorded model output.

## Review

Compare source and translation for material meaning before polishing naturalness. A fluent translation can still fail by dropping a qualifier or changing an obligation. If the user requests only translated text, return only that text unless a material ambiguity must be resolved.

Model language ability and native-speaker review are separate from package validation. Do not claim professional certification, native-speaker approval, or ASD-STE100 compliance.
