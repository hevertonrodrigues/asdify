# Languages, translation, and support

ASDify has translated READMEs and public regression inputs for nine locales. Use one canonical [skill](../skills/asdify/SKILL.md) with any supported host; no language-specific installation is needed.

| Locale tag | Language | README |
| --- | --- | --- |
| `en` | English | [English](../README.md) |
| `pt-BR` | Brazilian Portuguese | [Português (Brasil)](../README.pt-BR.md) |
| `es` | Spanish | [Español](../README.es.md) |
| `fr` | French | [Français](../README.fr.md) |
| `de` | German | [Deutsch](../README.de.md) |
| `ja` | Japanese | [日本語](../README.ja.md) |
| `zh-CN` | Simplified Chinese | [简体中文](../README.zh-CN.md) |
| `it` | Italian | [Italiano](../README.it.md) |
| `ru` | Russian | [Русский](../README.ru.md) |

The [language registry](../integrations/languages.json) defines documented coverage. It does not restrict the model to these languages. Other languages can be requested, but this repository does not yet provide their READMEs or regression inputs. No live translation study or independent native-speaker review of the seven new README translations is recorded.

## Request a rewrite or translation

For a rewrite, keep the source language by default:

```text
Use asdify lite. Reescreva em português brasileiro.
Retorne apenas o texto revisado. Preserve a recomendação, os identificadores
e a sequência: Se a API retornar HTTP 429, recomenda-se aguardar o intervalo
indicado em Retry-After antes de tentar novamente.
```

For translation, specify the target language or locale:

```text
Use asdify full. Translate into Japanese (ja).
Return only the translation. Preserve the recommendation, identifiers,
and sequence: If the API returns HTTP 429, the client should wait for
the interval in Retry-After before retrying. This is a recommendation,
not a requirement.
```

The target language overrides the prompt's language. Use `pt-BR` for Brazilian Portuguese or `zh-CN` for Simplified Chinese when those variants matter. You can also write the language name in ordinary prose. Modes are editing instructions, not locale flags or guaranteed slash commands.

All modes retain material content. `lite` keeps structure and tone; `full` simplifies and organizes when useful; `ultra` removes unnecessary framing. `off` disables the optional style workflow under the host's other instructions; it does not cancel an explicit translation request.

Names, figures, obligations, uncertainty, citations, code, paths, URLs, and placeholders must survive. Grammar and register can change naturally. Dates, units, currencies, legal jurisdiction, and gender must not be guessed or converted without authorization. See the [translation reference](../skills/asdify/references/translation.md) and [copyable examples](../examples/multilingual.md).

## What the tests establish

- Each registered locale has a nonempty README with links to every other language.
- Each locale has native-language rewrite inputs and translation inputs both to and from English.
- Locale tags, translation targets, fixture fields, unique IDs, and coverage are checked by `scripts/validate.py`.
- Unit tests exercise malformed registries, missing documentation, incomplete language coverage, invalid targets, Unicode content, and installation of the translation reference.

These are package and fixture checks. They do not run a translation engine or prove semantic accuracy. In a live evaluation, reviewers need competence in both source and target languages and must check meaning and naturalness separately. Do not compare raw word counts across writing systems as a quality measure. Follow the [evaluation protocol](../benchmarks/README.md) and report results by language and direction.

## Get support

- **A rewrite or translation changes meaning:** use the [meaning-regression form](https://github.com/hevertonrodrigues/asdify/issues/new?template=meaning_regression.yml). Include the source and actual output, source and target languages, regional/script variant, requested mode, model/host versions where known, and the exact meaning that changed. Reports can use any covered language; a response in that language is not guaranteed.
- **A translated README is wrong or outdated:** use the [documentation-translation form](https://github.com/hevertonrodrigues/asdify/issues/new?template=documentation_translation.yml). Give the file, section, current wording, suggested correction, and how it compares with the English README.
- **Installation or loading fails:** use the [installation report](https://github.com/hevertonrodrigues/asdify/issues/new?template=bug_report.md) and include the command and error.
- **A language is missing:** use a [feature request](https://github.com/hevertonrodrigues/asdify/issues/new?template=feature_request.md) or follow the contribution steps below.

Remove private information before reporting. Do not label an illustrative example as observed model output. No response deadline or professional translation certification is promised.

## Add or review a language

1. Add its canonical language/script/region tag, native name, and README path to `integrations/languages.json`. The registry accepts `language[-Script][-REGION]` tags; it is not a full BCP 47 parser. English uses `README.md`; other entries use `README.<tag>.md`.
2. Translate the README's claims, prompts, limitations, and installation choices. Preserve executable commands and link destinations. Link every README to the new language and link back to every existing language. Identify guides that remain in English.
3. Add original or anonymized native-language rewrites and translation cases in both directions with English. `lang` identifies the source language; `target_lang` identifies a translation's target. Omit `target_lang` for a same-language rewrite. Describe semantic invariants rather than one exact expected sentence.
4. Obtain native-speaker review where possible and record its scope honestly. A locale entry alone is not evidence of review or model effectiveness.
5. Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`. Follow [CONTRIBUTING.md](../CONTRIBUTING.md) for the PR.

Keep the canonical skill in English to avoid conflicting installed copies. Translated READMEs are user guides; the canonical skill governs behavior.
