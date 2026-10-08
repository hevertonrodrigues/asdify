# ASDify: blueprint do projeto open source

## 1. Visão

Construir uma Skill aberta, portátil e fácil de instalar que torne as respostas de agentes de IA mais claras, menos ambíguas e mais fáceis de revisar, **sem perda de significado**.

**Nome aprovado:** ASDify  
**Tagline:** Less fluff. More signal. No lost meaning.  
**Categoria:** Agent skill / prompt-level communication quality.  
**Público:** profissionais, gestores, desenvolvedores, pesquisadores e equipes que usam IA para relatórios, análises, respostas, documentação e comunicações diárias.  
**Idiomas prioritários:** inglês e português do Brasil.

## 2. Problema

O crescimento do volume de conteúdo gerado por IA aumenta o tempo necessário para ler, entender, conferir fatos e tomar decisões. Muitas respostas parecem sofisticadas, mas incluem linguagem vaga, repetições ou informações mal organizadas. Pedidos como "seja breve" podem remover ressalvas, datas e números importantes.

## 3. Promessa e limites

**Promessa de produto:** reduzir o esforço do leitor mantendo informações materiais, intenções e grau de certeza.

**Não prometer:** melhora quantificada sem benchmark, acesso universal a todas as plataformas, conformidade com ASD-STE100, precisão factual que depende de pesquisa externa, ou garantia de ranking orgânico no GitHub.

## 4. Regras nucleares

- Começar pela resposta/conclusão quando o contexto permitir.
- Identificar o leitor, o objetivo e os elementos que não podem ser alterados.
- Escolher a **menor edição completa**, em vez da resposta mais curta a qualquer custo.
- Preservar quantidades, períodos, unidades, condições, obrigações, incertezas e citações.
- Não transformar "pode" em "deve", "até" em "a partir de", nem percentuais em pontos percentuais.
- Evitar sinônimos desnecessários para um mesmo conceito.
- Evitar floreios, introduções ceremoniais, generalidades e adjetivos vazios.
- Usar listas, tabelas e títulos **só quando ajudam**.
- Não inventar recomendações, prazos ou próximos passos ao editar um texto alheio.
- Em resposta analítica, distinguir evidência, interpretação e sugestão.

## 5. Clarity ladder inspirada na lógica de simplificação do Ponytail

1. O pedido já foi respondido? Dizer somente o necessário.
2. O texto já está claro? Preservar.
3. Uma substituição local resolve? Fazer só ela.
4. Uma frase mais simples resolve? Preferir verbos concretos, voz ativa e uma ideia central por frase.
5. A estrutura atrapalha? Reorganizar: resposta, evidência, limitação e próximo passo quando fizer sentido.
6. O tema exige complexidade? Explicar por camadas e preservar todas as ressalvas.

## 6. Modos

| Modo | Regra | Exemplo de uso |
| --- | --- | --- |
| `lite` | Mudanças pequenas; preservar tom e ordem | Ajustar e-mail sem mudar estilo |
| `full` | Padrão; reorganizar apenas quando útil | Resumo para gestor |
| `ultra` | Cortar seções desnecessárias e questionar excesso de contexto | Revisar relatório longo |
| `off` | Desativar o workflow opcional conforme suporte do host | Texto criativo que exige outro estilo |

**Guardrail:** nenhum nível permite apagar qualificações relevantes para economizar palavras.

## 7. Arquitetura do repositório

```
asdify/
├── skills/asdify/
│   ├── SKILL.md
│   └── references/
│       ├── quality-rubric.md
│       └── edge-cases.md
├── AGENTS.md
├── README.md
├── README.pt-BR.md
├── INSTALL.md
├── CONTRIBUTING.md
├── LICENSE
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── examples/before-after.md
├── benchmarks/README.md
├── benchmarks/cases.jsonl
├── benchmarks/ratings-template.csv
├── scripts/install.sh
├── scripts/validate.py
├── scripts/score_ratings.py
├── tests/test_project.py
├── integrations/cursor-rule.mdc
├── .claude-plugin/
├── .github/
└── docs/LAUNCH.md
```

O diretório acima está incluído de forma editável em `./` neste pacote.

## 8. Qualidade e evidência

Medir separadamente: **fidelidade de significado** (condição eliminatória), clareza, densidade informativa, organização, calibração da certeza e adequação ao público. Usar comparação cega entre saída baseline e saída com Skill. Publicar entradas, saídas anonimizadas, modelos, configurações, datas, critérios e limitações.

Nenhum número de ganho é declarado sem execução de benchmark real. Menos tokens não é proxy suficiente de comunicação melhor.

## 9. Diferenciação

Ao contrário de um mero prompt "be concise", a Skill inclui:

- Preservação explícita de fatos, modalizadores e condições.
- Estratégia da edição mínima suficiente.
- Três intensidades.
- Formato aberto reutilizável entre agentes.
- Benchmarks de fidelidade com falhas eliminatórias.
- Referências para assuntos jurídicos, financeiros, técnicos e de segurança.
- Documentação bilingue e exemplos verificáveis.

## 10. Referências de inspiração

- [Ponytail](https://github.com/DietrichGebert/ponytail): modo de pensar, critérios de escopo mínimo, estrutura de Skill, instaladores e visibilidade de benchmarks.
- [Agent Skills](https://agentskills.io/specification): formato do pacote.
- [ASD-STE100](https://www.asd-ste100.org/): princípios públicos de linguagem controlada e redução de ambiguidade. **Sem afiliação, certificação ou reprodução do material oficial.**

## 11. Propriedade e licença

O repositório candidato está sob licença MIT. A inspiração na arquitetura do Ponytail não implica copiar seu texto, marca ou ativos. A identidade final, nome de organização e eventuais domínios precisam de verificação.
