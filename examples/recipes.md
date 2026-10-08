# Recipes

Install the skill using [INSTALL.md](../INSTALL.md), or paste the [canonical skill](../skills/asdify/SKILL.md) into a chat as instructions for a manual trial. Then send a prompt below. These are original practice inputs with review criteria, **not measured model results**. Modes change editing intensity; all modes must preserve meaning.

## 1. Executive update (EN)

Use **full** when a reader needs the status and condition for a projected deadline quickly.

```text
Use asdify full. Rewrite this update for the project sponsor.
Return only the update. Preserve facts, ownership, uncertainty, and conditions.

With regard to the database migration, the engineering team has completed
the transfer. Customer reports remain unavailable. The team tentatively
expects to restore them by Friday, provided validation succeeds.
No customer data loss has been detected, but the investigation is ongoing.
```

**Check:** engineering completed the transfer; reports remain unavailable; Friday is tentative and depends on successful validation; no loss has been detected; the investigation is ongoing. “No data was lost” overstates the evidence. Do not add a new owner or action plan.

## 2. Technical recommendation (PT-BR)

Use **lite** for a local wording edit that preserves the instruction's force and technical identifiers.

```text
Use asdify lite. Simplifique o texto abaixo mantendo o tom
de recomendação, o responsável e a ordem das ações. Retorne apenas o texto.

Caso a API venha a retornar o código HTTP 429, recomenda-se que o cliente
aguarde o intervalo indicado no cabeçalho Retry-After antes de realizar
uma nova requisição.
```

**Confira:** continua sendo uma recomendação; o cliente é o responsável; `HTTP 429` e `Retry-After` permanecem exatos; a espera ocorre antes da nova requisição. Não invente um intervalo em segundos.

## 3. Dense decision brief (EN)

Use **ultra** to remove repeated framing from a draft with several material constraints.

```text
Use asdify ultra. Edit this decision brief for a busy reader.
Keep every material fact and condition. Return only the edited brief.

For the purpose of supporting our upcoming discussion, we would like to
provide an overview of the pilot. The pilot involves 24 stores in Brazil
and ends on 30 November. Its estimated cost is R$48,000, excluding tax.
As previously noted, this remains an estimate. The supplier has not yet
confirmed the final price. A rollout requires finance approval and an
error rate below 1% during the pilot. No rollout decision has been made.
```

**Check:** 24 stores, Brazil, 30 November, estimated R$48,000 excluding tax, supplier price unconfirmed, finance approval **and** error rate below 1%, no rollout decision. Compress repeated uncertainty without turning an estimate into an agreed price. Do not propose a rollout date.

## 4. Leave clear text alone (EN)

Use **full** to review clarity without forcing an edit. A useful result may be identical to the input.

```text
Use asdify full. Review the message below for clarity.
If it is already clear and complete, return it unchanged.
Return only the message.

The deployment is paused until the security review is complete.
```

**Expected:** `The deployment is paused until the security review is complete.` No invented completion date, new advice, or extra explanation is needed.

If an output changes material meaning, report it using the **Meaning changed** GitHub issue form. See [CONTRIBUTING.md](../CONTRIBUTING.md) for the details needed to reproduce it.
