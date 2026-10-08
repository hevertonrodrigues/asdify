# Multilingual rewrites and translations

These are **illustrative editorial examples**, not measured model results. Wording can vary; the meaning must survive. See [language coverage and support](../docs/LANGUAGES.md) for review limits.

## Translate without changing the recommendation

Copy this complete prompt. Change `Italian (it)` to another target from the table.

```text
Use asdify full. Translate into Italian (it).
Return only the translation. Preserve the recommendation, actor,
identifiers, and sequence.

If the API returns HTTP 429, the client should wait for the interval in
Retry-After before retrying. This is a recommendation, not a requirement.
```

| Target | Illustrative wording |
| --- | --- |
| English (`en`, source) | If the API returns HTTP 429, the client should wait for the interval in Retry-After before retrying. This is a recommendation, not a requirement. |
| Brazilian Portuguese (`pt-BR`) | Se a API retornar HTTP 429, recomenda-se que o cliente aguarde o intervalo indicado em Retry-After antes de tentar novamente. É uma recomendação, não uma obrigação. |
| Spanish (`es`) | Si la API devuelve HTTP 429, se recomienda que el cliente espere el intervalo indicado en Retry-After antes de volver a intentarlo. Es una recomendación, no una obligación. |
| French (`fr`) | Si l'API renvoie HTTP 429, il est recommandé au client d'attendre le délai indiqué dans Retry-After avant de réessayer. Il s'agit d'une recommandation, pas d'une obligation. |
| German (`de`) | Wenn die API HTTP 429 zurückgibt, wird dem Client empfohlen, vor einem erneuten Versuch das in Retry-After angegebene Intervall abzuwarten. Dies ist eine Empfehlung, keine Pflicht. |
| Japanese (`ja`) | APIがHTTP 429を返した場合、クライアントには、再試行する前にRetry-Afterに示された時間だけ待つことが推奨されます。これは推奨であり、義務ではありません。 |
| Simplified Chinese (`zh-CN`) | 如果API返回HTTP 429，建议客户端在重试前等待Retry-After中指定的时间。这是建议，不是强制要求。 |
| Italian (`it`) | Se l'API restituisce HTTP 429, si raccomanda al client di attendere l'intervallo indicato in Retry-After prima di riprovare. È una raccomandazione, non un obbligo. |
| Russian (`ru`) | Если API возвращает HTTP 429, клиенту рекомендуется выждать интервал, указанный в Retry-After, прежде чем повторить попытку. Это рекомендация, а не обязанность. |

Check all five points: the trigger is conditional; the client acts; both identifiers are exact; waiting precedes retrying; the guidance remains a recommendation. A fluent translation that makes waiting mandatory fails.

## Keep protected tokens and output format

```text
Use asdify lite. Translate only the human-language string values into Japanese.
Keep JSON keys, identifiers, URLs, and placeholders exact.
Return only valid JSON, without a code fence or explanation.

{"message":"Do not delete {file} unless both tests pass and {{owner}} approves.","url":"https://example.invalid/help","code":"HTTP 429"}
```

Illustrative output:

```json
{"message":"両方のテストが成功し、かつ{{owner}}が承認するまでは、{file}を削除しないでください。","url":"https://example.invalid/help","code":"HTTP 429"}
```

The keys, URL, `HTTP 429`, `{file}`, and `{{owner}}` remain exact. Both tests must pass and the owner must approve; deletion is prohibited until these prerequisites are met.

## Preserve the source language for a rewrite

```text
Use asdify lite. Reescreva apenas se necessário.
Preserve a mistura intencional de idiomas. Retorne somente o texto.

O deployment está em staging. Keep the feature flag off até a aprovação de Ana.
```

The source is already clear for a reader familiar with the terms. Keep its language mixing, staging status, flag state, and approval condition. An English instruction to use `lite` is not itself a request to translate Portuguese.

## Keep an ambiguous date unresolved

```text
Use asdify full. Translate into German without guessing the date convention.

The deadline is 03/04. No date convention was provided.
```

Illustrative translation:

> Die Frist ist 03/04. Es wurde kein Datumsformat angegeben.

Do not silently choose 3 April or 4 March. If the requested output requires an unambiguous calendar date, ask which interpretation is intended.

The [regression inputs](../benchmarks/cases.jsonl) include rewrites for every documented locale and translations in both directions with English. The [evaluation protocol](../benchmarks/README.md) explains how bilingual reviewers can assess actual outputs.
