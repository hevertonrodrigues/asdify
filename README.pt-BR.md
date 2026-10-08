# ASDify

![ASDify — Textos de IA mais claros. Significado preservado.](assets/readme/hero.pt-BR.svg)

[![Verificações de CI](https://github.com/hevertonrodrigues/asdify/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/hevertonrodrigues/asdify/actions/workflows/validate.yml)
[![Licença: MIT](https://img.shields.io/badge/licen%C3%A7a-MIT-18283b?style=flat-square)](LICENSE)
[![Formato: Markdown portátil](https://img.shields.io/badge/formato-Markdown%20port%C3%A1til-18283b?style=flat-square)](skills/asdify/SKILL.md)
[![Exemplos: EN e PT-BR](https://img.shields.io/badge/exemplos-EN%20%2B%20PT--BR-dba44e?style=flat-square)](examples/before-after.md)

[English](README.md) · [Experimente](#experimente-sem-instalar) · [Instalação](#instale-no-seu-agente) · [Receitas de uso](examples/recipes.md) · [Contribua](CONTRIBUTING.md)

Dê ao seu agente de IA uma rotina de revisão: identificar o ponto principal, remover excessos e conferir se os detalhes importantes foram preservados. ASDify é uma Skill pequena e portátil em Markdown para respostas, atualizações, relatórios e documentação nos agentes de programação e editores compatíveis.

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

1. Abra [SKILL.md](skills/asdify/SKILL.md), copie seu conteúdo e cole como instruções em uma conversa, por exemplo no ChatGPT ou Claude web.
2. Envie este prompt:

```text
Use asdify full. Reescreva esta atualização para a diretoria.
Retorne apenas o texto revisado. Preserve todos os fatos e ressalvas.

Gostaríamos de destacar que a receita preliminar de assinaturas cresceu 12%
ano a ano no Brasil, excluindo reembolsos. Esses números ainda não foram
auditados.
```

Compare o resultado com os detalhes mostrados acima. A redação pode variar; os fatos e as ressalvas precisam ser preservados. É um teste manual, sem instalação automática da Skill.

[Veja uma execução real no Codex](docs/demos/codex-full-2026-10-08.md), com o prompt, a resposta e a conferência dos detalhes preservados (em inglês).

## Instale no seu agente

Use a [Skills CLI](https://github.com/vercel-labs/skills) para localizar o ASDify e instalar no seu agente:

```bash
npx skills add hevertonrodrigues/asdify --list
npx skills add hevertonrodrigues/asdify --skill asdify --agent claude-code
```

Troque `claude-code` pelo [ID do seu agente](docs/HARNESSES.md), como `codex`, `cursor`, `gemini-cli` ou `opencode`. Execute a partir do projeto de destino; acrescente `--global` para instalar no escopo do usuário, quando disponível. Veja [escopos, caminhos e remoção](INSTALL.md) no guia completo.

<details>
<summary><strong>Prefere o instalador local?</strong></summary>

```bash
git clone https://github.com/hevertonrodrigues/asdify.git
cd asdify
bash scripts/install.sh --list
bash scripts/install.sh --agent claude-code --scope user
```

Escolha um ID de `--list`. O instalador copia a Skill completa e suas referências a partir do clone, sem downloads, e recusa sobrescrever arquivos existentes sem `--force`.

Para Skills nativas no Cursor, use o ID local `cursor-skill`; `cursor` preserva o adaptador anterior de regra compacta para projetos. A Skills CLI usa `cursor` para Skills nativas. [Veja as diferenças e os caminhos](INSTALL.md#cursor-native-skill-or-compact-rule).

</details>

A [tabela de agentes](docs/HARNESSES.md) cobre os destinos do registro desta versão. Testes de instalação e sessões reais são registrados separadamente em [compatibilidade](docs/COMPATIBILITY.md). Para outro agente, use o caminho de Skills documentado por ele ou o teste manual acima.

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
