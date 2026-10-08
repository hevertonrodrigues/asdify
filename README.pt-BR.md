# ASDify

![ASDify — Textos de IA mais claros. Significado preservado.](assets/readme/hero.pt-BR.svg)

[![Licença: MIT](https://img.shields.io/badge/licen%C3%A7a-MIT-18283b?style=flat-square)](LICENSE)
[![Formato: Markdown portátil](https://img.shields.io/badge/formato-Markdown%20port%C3%A1til-18283b?style=flat-square)](skills/asdify/SKILL.md)
[![Exemplos: EN e PT-BR](https://img.shields.io/badge/exemplos-EN%20%2B%20PT--BR-dba44e?style=flat-square)](examples/before-after.md)

[English](README.md) · [Experimente](#experimente-sem-instalar) · [Instalação](#instale-no-seu-agente) · [Receitas de uso](examples/recipes.md) · [Contribua](CONTRIBUTING.md)

Dê ao seu agente de IA uma rotina de revisão: identificar o ponto principal, remover excessos e conferir se os detalhes importantes foram preservados. ASDify é uma Skill pequena e legível para respostas, atualizações, relatórios e documentação.

## Veja a diferença

![Uma edição ilustrativa remove a introdução e preserva receita de assinaturas preliminar e não auditada, Brasil, crescimento de 12% em relação ao mesmo período do ano anterior e exclusão de reembolsos.](assets/readme/before-after.pt-BR.svg)

*Exemplo editorial ilustrativo, não um resultado medido em modelos.* [Veja mais exemplos de antes e depois →](examples/before-after.md)

<details>
<summary><strong>Copie a revisão ilustrativa</strong></summary>

```text
A receita preliminar de assinaturas no Brasil cresceu 12% ano a ano,
excluindo reembolsos. Os números ainda não foram auditados.
```

</details>

## Experimente sem instalar

1. Abra [SKILL.md](skills/asdify/SKILL.md), copie seu conteúdo e cole em uma conversa como instruções.
2. Envie este prompt:

```text
Use asdify full. Reescreva esta atualização para a diretoria.
Retorne apenas o texto revisado. Preserve todos os fatos e ressalvas.

Gostaríamos de destacar que a receita preliminar de assinaturas cresceu 12%
ano a ano no Brasil, excluindo reembolsos. Esses números ainda não foram
auditados.
```

Compare o resultado com os detalhes mostrados acima. A redação pode variar; os fatos e as ressalvas precisam ser preservados. É um teste manual, sem instalação automática da Skill.

## Instale no seu agente

Clone o projeto uma vez e escolha seu agente abaixo:

```bash
git clone https://github.com/hevertonrodrigues/asdify.git
cd asdify
```

<details>
<summary><strong>Claude Code</strong></summary>

```bash
bash scripts/install.sh --agent claude --scope user
```

Copia a Skill e suas referências para `~/.claude/skills/asdify/`.

</details>

<details>
<summary><strong>Codex</strong></summary>

```bash
bash scripts/install.sh --agent codex --scope user
```

Copia a Skill e suas referências para `~/.agents/skills/asdify/`.

</details>

<details>
<summary><strong>Cursor</strong></summary>

Execute a partir do projeto que deve receber a regra:

```bash
cd "/path/to/your-project" && \
  bash "/path/to/asdify/scripts/install.sh" --agent cursor --scope project
```

Copia uma regra compacta para `.cursor/rules/asdify.mdc`.

</details>

O instalador copia arquivos locais e recusa sobrescrever uma instalação existente, a menos que você use `--force`. Veja [caminhos, remoção e solução de problemas](INSTALL.md) e o [status de verificação por agente](docs/COMPATIBILITY.md).

Em outros agentes com suporte a Skills, copie a pasta [`skills/asdify/`](skills/asdify/) inteira para o diretório aceito pelo agente. Para instruções permanentes, incorpore as regras compactas de [`AGENTS.md`](AGENTS.md) ao arquivo de instruções existente.

## Como o ASDify revisa

![Quatro etapas: identificar o leitor, marcar os fatos que precisam ser preservados, fazer a menor edição útil e conferir se o significado permanece intacto.](assets/readme/how-it-works.pt-BR.svg)

Preserve números, datas, condições, incertezas e termos técnicos necessários. Mantenha o que já está claro. Não invente recomendações, decisões ou prazos durante uma revisão.

| Modo | Quando usar | O que muda |
| --- | --- | --- |
| `lite` | Você quer uma revisão leve | A redação; preserva estrutura, ordem e tom. |
| `full` · padrão | Você quer uma resposta mais clara | A redação e a estrutura, quando isso ajuda. |
| `ultra` | O texto tem introduções ou seções desnecessárias | Uma revisão mais intensa, com as mesmas regras de preservação. |

Peça um modo com `Use asdify lite`, `full` ou `ultra`. Use `asdify off` para interromper este fluxo opcional, respeitando as demais instruções do agente. Os modos são instruções; o suporte a comandos nativos varia por agente.

## Coloque em prática

| Tarefa | O que preservar | Copie um prompt completo |
| --- | --- | --- |
| Atualização executiva | Status, responsáveis, prazos estimados e condições | [Experimente `full` · EN](examples/recipes.md#1-executive-update-en) |
| Recomendação técnica | Identificadores, responsável, sequência e recomendação versus obrigação | [Experimente `lite` · PT-BR](examples/recipes.md#2-technical-recommendation-pt-br) |
| Texto denso para decisão | Estimativas, exclusões e aprovações necessárias | [Experimente `ultra` · EN](examples/recipes.md#3-dense-decision-brief-en) |
| Mensagem que já está clara | A redação original, quando não há edição útil | [Experimente preservar sem alterar · EN](examples/recipes.md#4-leave-clear-text-alone-en) |

## Feito para ser verificado

Uma resposta mais curta que altera um fato relevante falha na avaliação. O repositório inclui casos de regressão em português e inglês, critérios de revisão humana e um [protocolo de avaliação reproduzível](benchmarks/README.md). **Ainda não demonstramos ganhos de qualidade em modelos reais.** Veja os registros separados de [verificação do pacote](docs/VERIFICATION.md) e [compatibilidade dos agentes](docs/COMPATIBILITY.md).

Encontrou uma condição perdida, um número alterado ou uma promessa inventada? [Relate a mudança de significado](https://github.com/hevertonrodrigues/asdify/issues/new?template=meaning_regression.yml). Um pequeno exemplo anonimizado já é uma boa primeira contribuição. Veja os passos em [CONTRIBUTING.md](CONTRIBUTING.md).

[Roadmap](docs/ROADMAP.md) · [Changelog](CHANGELOG.md) · [Licença MIT](LICENSE)
