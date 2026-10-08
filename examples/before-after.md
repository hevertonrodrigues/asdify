# Before and after

These are **illustrative editorial transformations**, not measured model results. The examples are original and designed to show what the skill should and should not do.

## 1. Corporate filler (EN)

**Before**

> In light of the evolving landscape, we are exploring a variety of initiatives with the goal of potentially creating meaningful opportunities for greater operational excellence.

**After (full)**

> We are exploring ways to improve operations.

**Why:** names the action without inventing a decision, timeline or promise.

## 2. Numbers + qualifiers (EN)

**Before**

> Preliminary subscription revenue grew 12% year over year in Brazil, excluding refunds. The data has not yet been audited.

**After (full)**

> Unaudited, preliminary subscription revenue in Brazil grew 12% year over year, excluding refunds.

**Wrong:** `Revenue grew 12%.` Loses uncertainty, segment, geography, timeframe and exclusion.

## 3. Risk + action (PT-BR)

**Antes**

> Em relação ao projeto, gostaríamos de ressaltar que estamos enfrentando algumas dificuldades relacionadas à integração de pagamentos, de modo que o lançamento, previsto para 18 de novembro, pode sofrer um atraso de até cinco dias, a depender da homologação do fornecedor.

**Depois (full)**

> A integração de pagamentos está com problemas. O lançamento previsto para 18 de novembro pode atrasar até cinco dias, dependendo da homologação do fornecedor.

**Por quê:** preserva data, limite do atraso e condição. Não troca possibilidade por certeza.

## 4. Business writing without inventing actions (PT-BR)

**Antes**

> No contexto do atual cenário operacional, temos observado oportunidades de otimização que, se devidamente exploradas, poderiam nos ajudar a aprimorar a eficiência.

**Depois (full)**

> Observamos oportunidades que podem melhorar a eficiência operacional se forem exploradas.

**Por quê:** preserva a possibilidade e a condição sem inventar decisões ou iniciativas.

## 5. Legal modality (EN)

**Before**

> The supplier may terminate the agreement after providing written notice at least 30 days in advance, except where applicable law requires a longer period.

**After (lite)**

> The supplier may terminate the agreement with at least 30 days' written notice, unless applicable law requires a longer notice period.

**Preserve:** `may`, written notice, 30-day minimum, law exception. Formal legal use may require the original text unchanged.

## 6. Executive update (EN)

**Before**

> With respect to the migration initiative, the engineering team has successfully completed the database transfer; however, we wish to highlight that customer reports remain unavailable, and restoration is tentatively expected by Friday, subject to successful validation.

**After (full)**

> The engineering team completed the database migration. Customer reports are still unavailable. We expect to restore them by Friday if validation succeeds.

**Preserve:** status, ownership, projected date, and conditionality. `Expect` is not a guaranteed deadline.

## 7. Technical identifier (PT-BR)

**Antes**

> Caso a API venha a retornar o código HTTP 429, recomenda-se que o cliente aguarde o intervalo indicado no cabeçalho Retry-After antes de realizar uma nova requisição.

**Depois (full)**

> Se a API retornar HTTP 429, recomenda-se que o cliente espere o intervalo indicado no cabeçalho `Retry-After` antes de tentar novamente.

**Preserve:** recommendation rather than requirement, client as actor, exact protocol code and header name, and waiting before the next request.

**Wrong:** `Se a API retornar HTTP 429, o cliente deve tentar novamente imediatamente.` Changes the recommendation into an obligation and removes the wait before retrying.

## 8. Don't simplify useful nuance (EN)

**Source**

> In a cohort of 120 users, the test group retained 68% after 30 days, compared with 63% in the control group. The five-percentage-point difference was not statistically significant.

**Acceptable**

> After 30 days, retention was 68% in the test group and 63% in the control group (120 users total). The five-percentage-point gap was not statistically significant.

**Wrong:** `The experiment improved retention by 5%.` False certainty and incorrect unit.
