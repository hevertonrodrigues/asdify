# Comparação: Ponytail e ASDify

**Referência examinada na conversa:** [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail), especialmente `README.md`, `AGENTS.md` e `skills/ponytail/SKILL.md` (repositório acessado em 8 de outubro de 2026).

## Diferença essencial

**Ponytail:** tornar a **solução implementada** menor, com o menor código novo necessário e sem abrir mão de funcionamento, testes e segurança.

**ASDify:** tornar a **comunicação** mais fácil de compreender e revisar, sem retirar informações relevantes.

| Dimensão | Ponytail | ASDify |
| --- | --- | --- |
| Domínio | Desenvolvimento de software | Escrita, relatórios, respostas e análise |
| Objetivo | Solução mínima e completa | Texto mínimo e completo |
| Pergunta inicial | Precisa construir isto? | Precisa dizer isto? |
| Reuso | Código e recursos existentes | Texto claro e terminologia existente |
| Risco a evitar | Quebras, falhas, segurança, ausência de testes | Perda de fatos, condições, ressalvas, contexto |
| Diretriz compacta | AGENTS.md | AGENTS.md |
| Skill canônica | skills/ponytail/SKILL.md | skills/asdify/SKILL.md |
| Modos | lite/full/ultra | lite/full/ultra/off |
| Exemplos | Diferentes quantidades de código para mesma tarefa | Antes/depois com preservação semântica |
| Benchmark | Código, custo, tempo, testes, revisão | Fidelidade, clareza, densidade, calibração |

## Semelhanças reais

1. Simplicidade não é superficialidade. Cortar o essencial é falhar.
2. Preferir a menor mudança que resolve o problema.
3. Questionar complexidade desnecessária antes de produzir mais conteúdo.
4. Fazer revisão de qualidade e informar limites relevantes.
5. Disponibilizar formato simples e portátil, com instruções claras de instalação.
6. Tornar resultados auditáveis por exemplos e benchmarks.

## Melhorias absorvidas da referência

- A "escada" de decisões precede a produção do texto.
- O modo `ultra` questiona se seções ou floreios precisam existir, mas não inventa novas prioridades.
- `AGENTS.md` reduz o custo de adoção quando um host não suporta Skills.
- `SKILL.md` é a fonte canônica para comportamentos mais ricos.
- Exemplos e benchmarks devem demonstrar eficácia, não prometer eficácia.

## O que NÃO copiar

Não reutilizar identidade visual, nome, personagens, ilustrações, frases promocionais, números de benchmark ou código do Ponytail. A licença MIT não elimina a necessidade de atribuição de materiais efetivamente reutilizados. A Skill é escrita para um domínio distinto.

**Atenção à compatibilidade:** instalação em múltiplos agentes deve ser verificada por versão. Não afirmar que todos suportam comandos, hooks ou mecanismos de ativação idênticos.

## Produtos complementares

Em projetos de software, usar Ponytail para reduzir sobreengenharia; usar ASDify para explicar decisões, revisar documentação e apresentar resultados. A segunda Skill não deve substituir instruções especializadas de segurança e qualidade de código.
