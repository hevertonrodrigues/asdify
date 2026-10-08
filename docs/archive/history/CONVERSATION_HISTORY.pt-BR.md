# Histórico anotado desta conversa

> Historical record: the project was later renamed **ASDify**. Original names and quoted user messages below are preserved as written. Current instructions are in the root [README](../../../README.md).

**Período:** 8 de outubro de 2026.  
**Formato:** Mensagens do usuário são reproduzidas ou referenciadas literalmente; respostas do assistente são **resumos fiéis**, e não transcrições integrais ou export oficial do aplicativo. Este documento foi criado para preservar decisões, contexto e explicações de produto.

## Etapa 1. A ideia veio de um Reel sobre ASD-STE100

**Pedido do usuário:** "https://www.instagram.com/reel/DeNVD0wJyxM/?stkn=MXg5d2N2NmI4NjE2YQ==  como transformar isso em uma skill?"

O assistente informou que não conseguiu acessar o vídeo diretamente e solicitou a transcrição. Explicou que uma Skill completa precisaria de objetivo, workflow, critérios de execução, entradas/saídas e arquivo `SKILL.md`. Sugeriu ChatGPT, Claude e Claude Code como destinos possíveis, mas não recebeu preferência definitiva.

O usuário forneceu a transcrição integral. **Consulte `REEL_TRANSCRIPT.pt-BR.md`** para preservar as palavras originais. O vídeo defendia a aplicação de princípios de redação técnica simplificada inspirados em manuais aeronáuticos: frases curtas, vocabulário controlado, uma ideia por frase e redução de ambiguidades. Ele mencionava a utilização em `AGENTS.md` para instruções persistentes.

## Etapa 2. Primeira proposta: Clear Communication

O assistente propôs a Skill `clear-communication`, para produzir respostas, relatórios, análises e documentação empresarial claras e precisas, em português e inglês. A primeira versão conceitual do `SKILL.md` incluía:

- Estrutura: frases curtas, uma ideia principal por frase e voz ativa, quando útil.
- Vocabulário: palavras comuns, termos consistentes e explicação de jargões.
- Densidade: eliminar repetições, introduções genéricas e frases sem informação.
- Precisão: separar fatos de suposições, quantificar quando possível e preservar ressalvas.
- Organização: conclusão primeiro, listas apenas quando ajudam, recomendação separada de observação.
- Contexto empresarial: decisões, métricas, riscos e efeitos práticos.
- Autorrevisão: checar clareza, ambiguidade, redundância e omissões.

O assistente destacou que uma adaptação multilíngue não constitui conformidade integral com o ASD-STE100. Também explicou a diferença entre uma Skill instalada e instruções permanentes como `AGENTS.md`.

**Evolução importante:** A versão atual do projeto abandonou qualquer leitura rígida de "menos de 20 palavras" como obrigação. A prioridade passou a ser preservar o significado: uma frase curta que omite condições, números ou riscos não é uma melhoria.

## Etapa 3. Comparação com o Ponytail

**Pedido do usuário:** "compare com essa https://github.com/dietrichgebert/ponytail e veja se tem coisas em comum"

O assistente consultou o repositório [Ponytail](https://github.com/DietrichGebert/ponytail), incluindo README, `AGENTS.md` e `skills/ponytail/SKILL.md`. A comparação identificou o princípio comum: **eliminar complexidade sem perder a parte essencial**.

Distinção de produto:

- Ponytail: reduz código novo, abstrações desnecessárias e sobreengenharia. Prioriza soluções completas que reutilizam o código existente e preservam segurança, tratamento de erros e testes relevantes.
- Clear Communication: reduz esforço de leitura e revisão. Prioriza clareza, fidelidade às informações e preservação de condições, datas, números e incertezas.

O Ponytail possui uma "escada" que recomenda perguntar se o recurso precisa existir antes de criá-lo, reaproveitar código do projeto, usar funcionalidades da plataforma, dependências já instaladas e só depois escrever código novo. A aplicação na comunicação é uma "escada de clareza": responder diretamente, não reescrever o que já está claro, fazer a menor edição suficiente, reorganizar somente quando isso melhora compreensão e explicar complexidade inevitável.

Também foram identificadas práticas úteis: níveis `lite`, `full`, `ultra`, regras compactas em `AGENTS.md`, critérios explícitos de qualidade, exemplos antes/depois e transparência sobre limitações.

Veja a comparação consolidada em `strategy/PONYTAIL_COMPARISON.pt-BR.md`.

## Etapa 4. Transformar a Skill em projeto open source

**Pedido do usuário:** "use o ponytail como referencia e melhore a clear communication baseado nela e a estrutura do repositorio similar ao do pontail, a ideia é fazermos um opensource para ser bem rankeado no github e se popularizar tbm"

Decisão: adotar o nome de trabalho **Clear Communication**, com a tagline **"Less fluff. More signal. No lost meaning."** e um formato aberto `SKILL.md`.

Pilares definidos:

1. **Clarity:** facilitar compreensão e eliminar ambiguidades.
2. **Precision:** preservar fatos, dados, prazos, regras, condições e incertezas.
3. **Efficiency:** reduzir esforço de leitura e revisão sem descartar informação material.

O assistente preparou um repositório inicial com: README em inglês e português, Skill principal, `AGENTS.md`, instalação, exemplos antes/depois, referências de qualidade, casos de benchmark, scripts, testes, templates do GitHub, regras do Cursor, metadados para plugin do Claude Code, licença MIT e guia de lançamento.

A resposta apresentou um ZIP da v0.1 e enfatizou que o projeto ainda **não estava publicado**, o nome e a organização do GitHub ainda precisavam ser definidos, e não havia números de desempenho validados por testes com modelos.

A proposta de distribuição incluiu bons exemplos, tópicos relevantes no GitHub, testes públicos e benchmark reproduzível. A estratégia não depende de promessas de ranking, estrelas artificiais, avaliações falsas ou métricas inventadas.

## Etapa 5. Empacotar todo o contexto

**Pedido atual:** "make a zip file with all explanations, this history, the potential repo file, etc.."

Este arquivo é a resposta ao pedido: reúne o repositório candidato em forma extraída e no ZIP original, o contexto do vídeo, a comparação com o Ponytail, decisões e próximos passos.

## O que está decidido vs. o que ainda é hipótese

**Decidido:** Skill para comunicação; fidelidade antes de concisão; português e inglês; modos lite/full/ultra/off; uso do Ponytail como referência estrutural (sem copiar código ou marca); MIT; instalação e avaliação transparente; não afirmar conformidade com ASD-STE100.

**Aberto:** nome definitivo e disponibilidade; usuário/organização do GitHub; identidade visual; versão 1.0; estratégias de lançamento específicas; validação em modelos reais; resultados de benchmark; compatibilidade efetiva em versões de cada host.

## Relação com a conversa do ChatGPT

Este é um **histórico anotado** para transferência de contexto. Não contém mensagens privadas internas, nem promete ser o export integral, literal e completo do produto ChatGPT. Para arquivamento palavra por palavra de toda a interface, use a função oficial de exportação de conversas do produto.
