# pt-BR: all source tasks and answers

Labels below are unblinded after review. Pass requires both meaning reviews and exact checks. A flagged answer is retained unchanged.

## modes-pt-BR-001 · numbers

Source task:

> Reescreva o relatório para a gerente de produção. Destaque a mudança medida e os limites da comparação, sem sugerir medidas novas.
> 
> Em setembro de 2028, a equipe pesou as sobras de tecido de 90 lotes produzidos com o molde antigo. Em outubro, pesou as sobras de outros 90 lotes feitos com o molde novo. A média caiu de 1,5 kg para 1,2 kg por lote, uma redução de 20%. Os lotes incluídos tinham 50 peças cada. A comparação não mede a sobra total da fábrica, pois outros produtos continuaram usando moldes diferentes. O relatório considera apenas os lotes cujo registro de pesagem estava completo; seis lotes de setembro e quatro de outubro ficaram de fora.
> 
> A composição dos grupos também mudou. Em setembro, 60 lotes foram feitos de algodão e 30 de tecido misto. Em outubro, foram 45 de cada tipo. O supervisor acredita que essa diferença pode influenciar a sobra, mas não calculou seu efeito. A máquina de corte foi regulada no fim de setembro, antes de iniciar os lotes com o novo molde. Não há um grupo com molde antigo depois dessa regulagem. Assim, os registros não permitem separar o efeito do molde, da regulagem e da mistura de tecidos.
> 
> A nota comercial diz que o novo molde “elimina um quinto do desperdício da empresa”. Essa frase amplia o alcance da medição. O que foi observado é uma queda de 20% na média de sobras por lote entre os grupos registrados, em uma linha de corte e nesses dois meses. Não foram medidos consumo de energia, defeitos nas peças, horas de trabalho nem sobras em outras linhas. O número de peças de cada lote não mudou, mas não há análise da espessura ou da qualidade do tecido.
> 
> A gerente pediu uma versão que permita entender o resultado sem confundi-lo com prova de causalidade. Não foi aprovada a troca de todos os moldes. Nenhum responsável ou prazo para essa troca foi indicado. Preserve a diferença entre uma mudança observada na amostra de lotes e uma redução comprovada no desperdício de toda a empresa.

### baseline: pass

```text
Relatório à gerente de produção

Nos lotes registrados, a média de sobras de tecido caiu de 1,5 kg por lote, em setembro de 2028, para 1,2 kg, em outubro: redução de 0,3 kg por lote, ou 20%. Foram comparados 90 lotes com o molde antigo e outros 90 com o novo, todos com 50 peças, em uma linha de corte. Apenas lotes com pesagem completa entraram na análise; seis de setembro e quatro de outubro foram excluídos.

Os grupos também diferiam na composição dos tecidos: setembro teve 60 lotes de algodão e 30 de tecido misto; outubro teve 45 de cada tipo. O supervisor considera que essa diferença pode influenciar as sobras, mas seu efeito não foi calculado. Além disso, a máquina de corte foi regulada no fim de setembro, antes dos lotes com o molde novo. Não há grupo com o molde antigo após a regulagem. Portanto, os registros não permitem separar os efeitos do molde, da regulagem e da composição dos tecidos, nem atribuir a queda exclusivamente ao novo molde.

A medição não representa o desperdício total da empresa: outros produtos continuaram com moldes diferentes, e as sobras de outras linhas não foram medidas. Também não foram avaliados consumo de energia, defeitos, horas de trabalho, espessura ou qualidade do tecido. Assim, a afirmação comercial de que o novo molde “elimina um quinto do desperdício da empresa” excede o alcance dos dados. O resultado observado é uma redução de 20% na média de sobras dos lotes registrados, nessa linha e nesses dois meses, não uma redução comprovada no desperdício de toda a empresa.

A troca de todos os moldes não foi aprovada, e não há responsável ou prazo indicado para essa troca.
```

### lite: pass

```text
Em setembro e outubro de 2028, a média de sobras de tecido caiu de 1,5 kg para 1,2 kg por lote, uma redução observada de 20%. Em setembro, foram pesados 90 lotes produzidos com o molde antigo; em outubro, outros 90 lotes feitos com o molde novo. Cada lote tinha 50 peças. A comparação considera apenas os lotes com registro de pesagem completo: seis lotes de setembro e quatro de outubro ficaram de fora. Não mede a sobra total da fábrica, pois outros produtos continuaram usando moldes diferentes.

A composição dos grupos também mudou. Em setembro, 60 lotes eram de algodão e 30 de tecido misto; em outubro, eram 45 de cada tipo. O supervisor acredita que essa diferença pode influenciar a sobra, mas não calculou seu efeito. A máquina de corte foi regulada no fim de setembro, antes dos lotes com o novo molde. Não há um grupo com o molde antigo após essa regulagem. Por isso, os registros não permitem separar os efeitos do molde, da regulagem e da mistura de tecidos.

A afirmação comercial de que o novo molde “elimina um quinto do desperdício da empresa” amplia o alcance da medição. O resultado observado foi uma queda de 20% na média de sobras por lote entre os grupos registrados, em uma linha de corte e nesses dois meses. Não foram medidos consumo de energia, defeitos nas peças, horas de trabalho nem sobras em outras linhas. O número de peças por lote não mudou, mas não há análise da espessura ou da qualidade do tecido.

O resultado mostra uma mudança na amostra de lotes, não prova que o novo molde causou essa queda nem que o desperdício de toda a empresa diminuiu 20%. A troca de todos os moldes não foi aprovada, e não foram indicados responsável ou prazo para essa troca.
```

### full: pass

```text
A média de sobras de tecido caiu 20% entre os grupos registrados: de 1,5 kg por lote em setembro de 2028, com o molde antigo, para 1,2 kg em outubro, com o molde novo. A equipe pesou 90 lotes em cada mês, todos com 50 peças, em uma linha de corte. Essa mudança observada não comprova que o novo molde reduziu o desperdício de toda a empresa.

Limites da comparação:
- Foram considerados apenas lotes com registros de pesagem completos. Seis lotes de setembro e quatro de outubro ficaram de fora.
- A composição dos grupos mudou: setembro teve 60 lotes de algodão e 30 de tecido misto; outubro teve 45 de cada tipo. O supervisor acredita que isso pode influenciar as sobras, mas não calculou o efeito.
- A máquina de corte foi regulada no fim de setembro, antes dos lotes com o novo molde. Não há grupo com o molde antigo após a regulagem. Portanto, os registros não permitem separar os efeitos do molde, da regulagem e da mistura de tecidos.
- A comparação não mede as sobras totais da fábrica: outros produtos continuaram usando moldes diferentes. Também não foram medidos consumo de energia, defeitos, horas de trabalho ou sobras em outras linhas. Embora o número de peças por lote não tenha mudado, não há análise da espessura ou da qualidade dos tecidos.

A afirmação comercial de que o novo molde “elimina um quinto do desperdício da empresa” amplia indevidamente o alcance da medição. O resultado é uma queda de 20% na média de sobras por lote entre os grupos registrados, nessa linha e nesses dois meses, sem prova de causalidade.

A troca de todos os moldes não foi aprovada. Não foram indicados responsável ou prazo para essa troca.
```

### ultra: pass

```text
A média de sobras caiu de 1,5 kg para 1,2 kg por lote: redução observada de 20% entre os grupos registrados em uma linha de corte. Foram comparados 90 lotes com molde antigo, em setembro de 2028, e outros 90 com molde novo, em outubro. Todos tinham 50 peças. Só entraram registros de pesagem completos; seis lotes de setembro e quatro de outubro foram excluídos.

A comparação não prova que o molde causou a queda. Em setembro, havia 60 lotes de algodão e 30 de tecido misto; em outubro, 45 de cada. O supervisor acredita que essa composição pode influenciar as sobras, mas não calculou o efeito. A máquina foi regulada no fim de setembro, antes dos lotes com molde novo, e não há grupo com molde antigo após a regulagem. Portanto, os registros não separam os efeitos do molde, da regulagem e da mistura de tecidos.

A afirmação comercial de que o novo molde “elimina um quinto do desperdício da empresa” amplia indevidamente o resultado. A medição abrange apenas a média de sobras dos lotes registrados nessa linha e nesses dois meses, não o desperdício total da fábrica. Outros produtos continuaram usando moldes diferentes. Não foram medidos energia, defeitos, horas de trabalho ou sobras em outras linhas, nem analisadas espessura ou qualidade do tecido.

A troca de todos os moldes não foi aprovada; não há responsável nem prazo indicado para ela.
```

### off: pass

```text
### Resultado observado

A média de sobras de tecido caiu de 1,5 kg para 1,2 kg por lote, uma redução de 20%, entre os grupos registrados em setembro e outubro de 2028. Em setembro, foram avaliados 90 lotes produzidos com o molde antigo; em outubro, outros 90 lotes com o molde novo. Cada lote tinha 50 peças.

O relatório inclui apenas lotes com registro de pesagem completo. Seis lotes de setembro e quatro de outubro ficaram de fora. A medição abrange uma linha de corte nesses dois meses, não a sobra total da fábrica: outros produtos continuaram usando moldes diferentes.

### Limites da comparação

A composição dos grupos mudou: setembro teve 60 lotes de algodão e 30 de tecido misto; outubro teve 45 de cada tipo. O supervisor acredita que essa diferença pode influenciar a sobra, mas seu efeito não foi calculado.

Além disso, a máquina de corte foi regulada no fim de setembro, antes dos lotes com o novo molde. Não há um grupo produzido com o molde antigo depois dessa regulagem. Portanto, os registros não permitem separar os efeitos do molde, da regulagem e da mistura de tecidos. A queda observada não comprova que o novo molde causou a redução.

Não foram medidos consumo de energia, defeitos nas peças, horas de trabalho ou sobras em outras linhas. Embora o número de peças por lote tenha permanecido igual, não há análise da espessura ou da qualidade do tecido.

### Alcance da conclusão

A afirmação comercial de que o novo molde “elimina um quinto do desperdício da empresa” amplia indevidamente o alcance da medição. O resultado registrado é uma queda de 20% na média de sobras por lote entre os dois grupos analisados, e não uma redução comprovada no desperdício de toda a empresa.

A troca de todos os moldes não foi aprovada. Não foram indicados responsável ou prazo para essa troca.
```

## modes-pt-BR-002 · conditions

Source task:

> Simplifique este regulamento fictício de um centro cultural para o público. Preserve as obrigações e as exceções. Não acrescente orientação jurídica.
> 
> O visitante pode levar água em garrafa com tampa às salas de exposição. O consumo de outras bebidas e de alimentos não é permitido nessas salas. Essa regra não se aplica à área do café, onde o consumo é autorizado. Crianças com menos de 10 anos devem permanecer acompanhadas por uma pessoa adulta. Crianças de 10 a 13 anos podem participar de uma oficina sem acompanhante apenas se a inscrição incluir autorização por escrito. A autorização para a oficina não permite circular sem acompanhante em outras áreas sujeitas à regra de acompanhamento.
> 
> O acesso à sala de cerâmica exige calçado fechado e inscrição confirmada. As duas condições são necessárias. Uma pessoa que tenha calçado fechado, mas esteja apenas na lista de espera, não pode entrar para participar da atividade. A coordenação pode abrir uma vaga extra quando houver materiais e um segundo instrutor disponível. A existência de materiais, sozinha, não garante a abertura da vaga. A decisão é opcional para a coordenação mesmo quando as duas condições estão presentes.
> 
> Fotografias sem flash são permitidas, exceto nas obras identificadas com o símbolo de proibição. A permissão não inclui filmar participantes das oficinas. Quem quiser usar tripé deve pedir autorização à recepção antes de montá-lo. Não basta avisar depois. Pessoas que precisam de equipamento de mobilidade não estão sujeitas à exigência de autorização para tripé; esse equipamento não deve ser tratado como acessório fotográfico.
> 
> Em caso de dano a uma peça, a atividade deve ser interrompida e a recepção deve ser avisada. Um registro do ocorrido precisa ser feito antes de a peça seguir para avaliação. O regulamento não determina quem causou o dano nem quem escreverá o registro. A coordenação recebe o registro e decide se a atividade pode recomeçar. Isso não significa que a coordenação tenha causado o dano ou realizado a avaliação da peça.

### baseline: pass

```text
Regras do centro cultural

Alimentos e bebidas
- Você pode levar água em garrafa com tampa às salas de exposição. Não é permitido consumir outras bebidas nem alimentos nessas salas.
- Na área do café, o consumo de alimentos e bebidas é permitido.

Crianças
- Crianças menores de 10 anos devem permanecer acompanhadas por uma pessoa adulta.
- Crianças de 10 a 13 anos podem participar de uma oficina sem acompanhante somente se a inscrição incluir autorização por escrito. Essa autorização não permite circular sem acompanhante em outras áreas onde o acompanhamento seja exigido.

Sala de cerâmica
- Para participar, é necessário ter calçado fechado e inscrição confirmada. Quem está apenas na lista de espera não pode entrar para a atividade, mesmo com calçado fechado.
- A coordenação pode abrir uma vaga extra se houver materiais e um segundo instrutor disponível. Ter apenas materiais não basta. Mesmo com as duas condições atendidas, a coordenação não é obrigada a abrir a vaga.

Fotografias e equipamentos
- Fotografias sem flash são permitidas, exceto nas obras com símbolo de proibição. Essa permissão não inclui filmar participantes das oficinas.
- Para usar tripé, peça autorização à recepção antes de montá-lo. Avisar depois não é suficiente.
- Equipamentos de mobilidade não são acessórios fotográficos e não precisam da autorização exigida para tripés.

Danos a peças
- Se uma peça for danificada, a atividade deve ser interrompida e a recepção deve ser avisada.
- É obrigatório fazer um registro do ocorrido antes de encaminhar a peça para avaliação.
- A coordenação recebe o registro e decide se a atividade pode recomeçar.
- O regulamento não define quem causou o dano nem quem fará o registro. Receber o registro e decidir sobre a retomada não significa que a coordenação tenha causado o dano ou avaliado a peça.
```

### lite: pass

```text
O visitante pode levar água em garrafa com tampa às salas de exposição. Nessas salas, não é permitido consumir outras bebidas ou alimentos. Na área do café, esse consumo é autorizado. Crianças com menos de 10 anos devem permanecer acompanhadas por uma pessoa adulta. Crianças de 10 a 13 anos podem participar de uma oficina sem acompanhante somente se a inscrição incluir autorização por escrito. Essa autorização não permite circular sem acompanhante em outras áreas sujeitas à regra de acompanhamento.

Para participar da atividade na sala de cerâmica, é necessário ter calçado fechado e inscrição confirmada. Quem estiver apenas na lista de espera não pode entrar para participar, mesmo com calçado fechado. A coordenação pode abrir uma vaga extra se houver materiais e um segundo instrutor disponível. Apenas ter materiais não basta. Mesmo com as duas condições atendidas, a coordenação não é obrigada a abrir a vaga.

Fotografias sem flash são permitidas, exceto nas obras identificadas com o símbolo de proibição. Essa permissão não inclui filmar participantes das oficinas. Para usar tripé, é preciso pedir autorização à recepção antes de montá-lo; não basta avisar depois. Equipamentos de mobilidade usados por quem precisa deles não estão sujeitos a essa exigência e não devem ser tratados como acessórios fotográficos.

Se uma peça for danificada, a atividade deve ser interrompida e a recepção deve ser avisada. Um registro do ocorrido deve ser feito antes de a peça seguir para avaliação. O regulamento não determina quem causou o dano nem quem fará o registro. A coordenação recebe o registro e decide se a atividade pode recomeçar. Isso não significa que tenha causado o dano ou realizado a avaliação da peça.
```

### full: pass

```text
### Bebidas, alimentos e acompanhamento
Você pode levar água em garrafa com tampa às salas de exposição. Nessas salas, não é permitido consumir outras bebidas ou alimentos. Na área do café, esse consumo é permitido.

Crianças com menos de 10 anos devem permanecer acompanhadas por uma pessoa adulta. Crianças de 10 a 13 anos podem participar de uma oficina sem acompanhante somente se a inscrição incluir autorização por escrito. Essa autorização não permite circular sem acompanhante em outras áreas sujeitas à regra de acompanhamento.

### Sala de cerâmica
Para participar da atividade, é necessário ter calçado fechado e inscrição confirmada. Quem está apenas na lista de espera não pode entrar para participar, mesmo com calçado fechado.

A coordenação pode abrir uma vaga extra se houver materiais e um segundo instrutor disponível. As duas condições são necessárias, mas a abertura da vaga continua sendo opcional para a coordenação.

### Fotografias e equipamentos
Fotografias sem flash são permitidas, exceto nas obras com símbolo de proibição. Essa permissão não inclui filmar participantes das oficinas.

Para usar tripé, peça autorização à recepção antes de montá-lo. Avisar depois não basta. Equipamentos de mobilidade não são acessórios fotográficos e não estão sujeitos a essa exigência de autorização.

### Dano a uma peça
Se uma peça for danificada, a atividade deve ser interrompida e a recepção deve ser avisada. Um registro do ocorrido deve ser feito antes de a peça seguir para avaliação.

A coordenação recebe o registro e decide se a atividade pode recomeçar. O regulamento não determina quem causou o dano nem quem escreverá o registro. Também não atribui à coordenação a causa do dano ou a avaliação da peça.
```

### ultra: pass

```text
**Bebidas, alimentos e acompanhamento**
Você pode levar água em garrafa com tampa às salas de exposição. Nessas salas, é proibido consumir outras bebidas ou alimentos. No café, esse consumo é permitido.

Crianças menores de 10 anos devem ficar acompanhadas por uma pessoa adulta. Crianças de 10 a 13 anos só podem participar de uma oficina sem acompanhante se a inscrição incluir autorização por escrito. Essa autorização não permite circular sem acompanhante em outras áreas sujeitas à regra de acompanhamento.

**Sala de cerâmica**
Para participar, é necessário ter calçado fechado e inscrição confirmada. Estar na lista de espera não permite entrar, mesmo com calçado fechado.

A coordenação pode abrir uma vaga extra se houver materiais e um segundo instrutor disponível. Materiais, sozinhos, não bastam. Mesmo com as duas condições atendidas, abrir a vaga é opcional.

**Fotografias e equipamentos**
Fotos sem flash são permitidas, exceto de obras com símbolo de proibição. Essa permissão não inclui filmar participantes das oficinas.

Para usar tripé, peça autorização à recepção antes de montá-lo; avisar depois não basta. Equipamentos de mobilidade não são acessórios fotográficos e não exigem essa autorização.

**Danos a peças**
Se uma peça for danificada, a atividade deve ser interrompida e a recepção avisada. Um registro do ocorrido deve ser feito antes de a peça seguir para avaliação. O regulamento não identifica quem causou o dano nem quem fará o registro.

A coordenação recebe o registro e decide se a atividade pode recomeçar. Isso não significa que tenha causado o dano ou avaliado a peça.
```

### off: pass

```text
### Bebidas, alimentos e acompanhamento

Você pode levar água em garrafa com tampa às salas de exposição. Nessas salas, não é permitido consumir outras bebidas nem alimentos. Na área do café, esse consumo é autorizado.

Crianças menores de 10 anos devem permanecer acompanhadas por uma pessoa adulta. Crianças de 10 a 13 anos podem participar de uma oficina sem acompanhante somente se a inscrição incluir autorização por escrito. Essa autorização vale apenas para a oficina: não permite circular sem acompanhante em outras áreas sujeitas à regra de acompanhamento.

### Sala de cerâmica

Para participar da atividade, é necessário ter calçado fechado e inscrição confirmada. As duas condições são obrigatórias. Quem estiver apenas na lista de espera não pode entrar para participar, mesmo com calçado fechado.

A coordenação pode abrir uma vaga extra se houver materiais e um segundo instrutor disponível. Ter apenas os materiais não basta. Mesmo com as duas condições atendidas, a coordenação não é obrigada a abrir a vaga.

### Fotografias e equipamentos

Fotografias sem flash são permitidas, exceto nas obras marcadas com o símbolo de proibição. Essa permissão não inclui filmar participantes das oficinas.

Para usar tripé, é preciso pedir autorização à recepção antes de montá-lo. Avisar depois não basta.

Equipamentos de mobilidade usados por pessoas que precisam deles não estão sujeitos à autorização exigida para tripés e não devem ser tratados como acessórios fotográficos.

### Danos a peças

Se uma peça sofrer dano, a atividade deve ser interrompida e a recepção deve ser avisada. É obrigatório fazer um registro do ocorrido antes de encaminhar a peça para avaliação.

O regulamento não define quem causou o dano nem quem escreverá o registro. A coordenação recebe o registro e decide se a atividade pode recomeçar. Isso não significa que ela tenha causado o dano ou realizado a avaliação da peça.
```

## modes-pt-BR-003 · technical

Source task:

> Transforme as notas abaixo em uma passagem de turno clara, com os problemas pendentes ao final. Use apenas o conteúdo fornecido.
> 
> O serviço de entregas recebe arquivos pelo diretório /entrada/pedidos. Um arquivo só é marcado como processado depois que todos os itens válidos são gravados e a transação é confirmada. Linhas com quantidade negativa são rejeitadas e registradas em uma tabela de erros. A rejeição de uma linha não impede que outras linhas válidas do mesmo arquivo sejam gravadas. O processamento não pode ser descrito como “tudo ou nada” para o arquivo inteiro. Essa propriedade vale apenas para cada transação de gravação, cujo limite é um grupo de até 100 linhas válidas.
> 
> O identificador externo pedido_id é usado para evitar que o mesmo pedido seja gravado duas vezes. O nome do cliente não é a chave de deduplicação. Um arquivo reenviado pode conter novos pedidos e pedidos já presentes. O relatório diferencia “já existente” de “rejeitado por erro”. A equipe de atendimento às vezes chama ambos de “não importado”, mas esse rótulo não altera os estados registrados. O reenvio, por si só, não prova duplicação na base.
> 
> Às 07:20 UTC de 18 de outubro de 2028, um arquivo com 230 linhas foi processado. Foram gravadas 210 linhas, 12 foram reconhecidas como pedidos já existentes e 8 foram rejeitadas por quantidade negativa. A soma cobre as 230 linhas do arquivo. O painel exibiu 198 novas linhas por alguns minutos porque a atualização do painel pode atrasar até 5 minutos. Ainda não foi verificado se os valores atuais do painel coincidem com o banco. O atraso não é evidência de perda de dados.
> 
> A próxima pessoa de plantão deve comparar o painel atualizado com a tabela de processamento. As notas não atribuem a ela a correção das oito linhas rejeitadas; isso depende de informações que devem vir do remetente, mas não há responsável nominal ou prazo. Não há autorização para alterar as quantidades negativas, apagar os pedidos existentes ou mudar a janela de atualização do painel. Preserve os estados e a ordem de gravação, confirmação e marcação do arquivo.

### baseline: pass

```text
Passagem de turno — serviço de entregas

Funcionamento
- Os arquivos chegam pelo diretório /entrada/pedidos.
- As linhas válidas são gravadas em transações de até 100 linhas. Primeiro ocorre a gravação, depois a confirmação da transação. O arquivo só é marcado como processado depois que todos os itens válidos foram gravados e as respectivas transações confirmadas.
- Linhas com quantidade negativa são rejeitadas e registradas na tabela de erros, sem impedir a gravação das outras linhas válidas. O processamento é “tudo ou nada” apenas dentro de cada transação, não para o arquivo inteiro.
- A deduplicação usa pedido_id, não o nome do cliente. Um reenvio pode conter pedidos novos e já existentes; reenviar, por si só, não prova duplicação na base.
- “Já existente” e “rejeitado por erro” são estados distintos. O rótulo “não importado”, usado às vezes pelo atendimento para ambos, não altera esses estados.

Último processamento
Às 07:20 UTC de 18 de outubro de 2028, foi processado um arquivo de 230 linhas:
- 210 linhas gravadas;
- 12 reconhecidas como pedidos já existentes;
- 8 rejeitadas por quantidade negativa.
Total: 210 + 12 + 8 = 230 linhas.

O painel mostrou 198 novas linhas por alguns minutos. Sua atualização pode atrasar até 5 minutos; esse atraso não é evidência de perda de dados.

Problemas pendentes
- Ainda não foi verificado se os valores atuais do painel coincidem com o banco. A próxima pessoa de plantão deve comparar o painel atualizado com a tabela de processamento.
- A correção das oito linhas rejeitadas depende de informações do remetente. Não há responsável nominal nem prazo, e essa correção não foi atribuída à próxima pessoa de plantão.
- Não há autorização para alterar as quantidades negativas, apagar pedidos existentes ou mudar a janela de atualização do painel.
```

### lite: pass

```text
Passagem de turno

O serviço de entregas recebe arquivos pelo diretório /entrada/pedidos. Os itens válidos são gravados em transações de até 100 linhas válidas. A propriedade “tudo ou nada” vale para cada transação de gravação, não para o arquivo inteiro. Linhas com quantidade negativa são rejeitadas e registradas em uma tabela de erros, sem impedir a gravação das outras linhas válidas. O arquivo só é marcado como processado depois que todos os itens válidos são gravados e a transação é confirmada.

A deduplicação usa o identificador externo pedido_id, não o nome do cliente. Um arquivo reenviado pode conter pedidos novos e pedidos já presentes. O relatório distingue “já existente” de “rejeitado por erro”. O atendimento às vezes chama ambos de “não importado”, mas esse rótulo não altera os estados registrados. O reenvio, por si só, não prova duplicação na base.

Às 07:20 UTC de 18 de outubro de 2028, foi processado um arquivo com 230 linhas:
- 210 linhas foram gravadas;
- 12 foram reconhecidas como pedidos já existentes;
- 8 foram rejeitadas por quantidade negativa.

Os três estados somam as 230 linhas do arquivo. O painel exibiu 198 novas linhas por alguns minutos. Sua atualização pode atrasar até 5 minutos, e esse atraso não é evidência de perda de dados.

Problemas pendentes

Ainda não foi verificado se os valores atuais do painel coincidem com o banco. A próxima pessoa de plantão deve comparar o painel atualizado com a tabela de processamento.

A correção das oito linhas rejeitadas depende de informações do remetente. As notas não atribuem essa correção à próxima pessoa de plantão e não indicam responsável nominal ou prazo. Não há autorização para alterar as quantidades negativas, apagar os pedidos existentes ou mudar a janela de atualização do painel.
```

### full: pass

```text
### Resultado do processamento
Às 07:20 UTC de 18 de outubro de 2028, foi processado um arquivo com 230 linhas:
- 210 linhas gravadas;
- 12 reconhecidas como pedidos já existentes;
- 8 rejeitadas por quantidade negativa.

Os três estados somam as 230 linhas. O painel mostrou 198 novas linhas por alguns minutos. Sua atualização pode atrasar até 5 minutos; esse atraso não é evidência de perda de dados.

### Regras de processamento
O serviço recebe arquivos em /entrada/pedidos. Os itens válidos são gravados, a transação é confirmada e só depois o arquivo é marcado como processado, quando todos os itens válidos tiverem sido gravados.

Linhas com quantidade negativa são rejeitadas e registradas em uma tabela de erros. Isso não impede a gravação das demais linhas válidas do arquivo. O processamento não é “tudo ou nada” para o arquivo inteiro: essa propriedade vale apenas para cada transação de gravação, limitada a um grupo de até 100 linhas válidas.

A deduplicação usa pedido_id, não o nome do cliente. Um arquivo reenviado pode conter pedidos novos e pedidos já presentes; o reenvio, sozinho, não prova duplicação na base. O relatório distingue “já existente” de “rejeitado por erro”. O rótulo “não importado”, usado às vezes pelo atendimento para ambos, não muda os estados registrados.

Não há autorização para alterar quantidades negativas, apagar pedidos existentes ou mudar a janela de atualização do painel.

### Pendências
- A próxima pessoa de plantão deve comparar o painel atualizado com a tabela de processamento. Ainda não foi verificado se os valores atuais do painel coincidem com o banco.
- A correção das oito linhas rejeitadas depende de informações do remetente. As notas não atribuem essa correção à próxima pessoa de plantão e não indicam responsável nominal ou prazo.
```

### ultra: pass

```text
**Passagem de turno**
O serviço recebe arquivos em `/entrada/pedidos`. O arquivo só é marcado como processado após a gravação de todos os itens válidos e a confirmação da transação. Cada transação abrange até 100 linhas válidas; o processamento é “tudo ou nada” por transação, não por arquivo. Linhas com quantidade negativa são rejeitadas e registradas na tabela de erros, sem impedir a gravação das demais linhas válidas.

A deduplicação usa `pedido_id`, não o nome do cliente. Um reenvio pode conter pedidos novos e já existentes; reenviar não prova duplicação na base. O relatório distingue “já existente” de “rejeitado por erro”. O rótulo “não importado”, usado às vezes pelo atendimento para ambos, não altera esses estados.

Às 07:20 UTC de 18 de outubro de 2028, foi processado um arquivo de 230 linhas: 210 gravadas, 12 reconhecidas como pedidos já existentes e 8 rejeitadas por quantidade negativa. Esses estados totalizam as 230 linhas. O painel mostrou 198 novas linhas por alguns minutos; sua atualização pode atrasar até 5 minutos. Esse atraso não é evidência de perda de dados.

**Pendências e limites**
- A próxima pessoa de plantão deve comparar o painel atualizado com a tabela de processamento. Ainda não foi verificado se os valores atuais do painel coincidem com o banco.
- A correção das oito linhas rejeitadas depende de informações do remetente. Não foi atribuída à próxima pessoa de plantão, e não há responsável nominal nem prazo.
- Não há autorização para alterar quantidades negativas, apagar pedidos existentes ou mudar a janela de atualização do painel.
```

### off: pass

```text
## Passagem de turno

### Funcionamento do processamento

O serviço de entregas recebe arquivos pelo diretório /entrada/pedidos. As linhas válidas são gravadas em transações com grupos de até 100 linhas válidas. O arquivo só é marcado como processado depois que todos os itens válidos são gravados e a transação é confirmada. A ordem é: gravação, confirmação e marcação do arquivo.

Linhas com quantidade negativa são rejeitadas e registradas em uma tabela de erros. Isso não impede a gravação das demais linhas válidas do mesmo arquivo. O processamento não é “tudo ou nada” para o arquivo inteiro; essa propriedade vale apenas para cada transação de gravação.

A deduplicação usa o identificador externo pedido_id, não o nome do cliente. Um arquivo reenviado pode conter tanto pedidos novos quanto pedidos já presentes. O relatório distingue “já existente” de “rejeitado por erro”. O atendimento às vezes chama ambos de “não importado”, mas esse rótulo não muda os estados registrados. O reenvio, por si só, não comprova duplicação na base.

### Último processamento registrado

Às 07:20 UTC de 18 de outubro de 2028, foi processado um arquivo com 230 linhas:

- 210 linhas gravadas;
- 12 reconhecidas como pedidos já existentes;
- 8 rejeitadas por quantidade negativa.

A soma dos três estados corresponde às 230 linhas do arquivo.

O painel exibiu 198 novas linhas por alguns minutos. A atualização pode atrasar até 5 minutos; esse atraso não é evidência de perda de dados.

### Problemas pendentes

- Ainda não foi verificado se os valores atuais do painel coincidem com o banco. A próxima pessoa de plantão deve comparar o painel atualizado com a tabela de processamento.
- A correção das oito linhas rejeitadas depende de informações do remetente. Não há responsável nominal nem prazo, e essa correção não foi atribuída à próxima pessoa de plantão.
- Não há autorização para alterar as quantidades negativas, apagar pedidos existentes ou mudar a janela de atualização do painel.
```

## modes-pt-BR-004 · summary

Source task:

> Resuma o levantamento para a diretora de uma escola, em até dois parágrafos. Preserve as limitações que mudam a interpretação.
> 
> O questionário foi enviado por mensagem às 360 famílias com telefone atualizado no cadastro. A escola recebeu 126 respostas completas. As famílias sem telefone atualizado não receberam o convite. A participação foi voluntária, e o formulário estava disponível apenas em português. O levantamento não foi uma amostra aleatória das famílias. A equipe não verificou se as pessoas que responderam diferiam das que não responderam. Não há informação suficiente para calcular quantas mensagens foram efetivamente lidas.
> 
> Entre as 126 respostas, 84 indicaram preferência por reunião às 19h, 28 por reunião às 14h e 14 não escolheram um horário. A preferência por 19h corresponde a dois terços das pessoas que responderam, não a dois terços de todas as famílias da escola. A pergunta tratou de uma reunião específica no próximo bimestre. Não perguntou se esse horário seria adequado para todas as reuniões do ano. Também não verificou disponibilidade de transporte, necessidade de cuidado com crianças ou jornada de trabalho.
> 
> A coordenação propôs testar o horário das 19h em uma reunião. A proposta ainda depende da disponibilidade da equipe e da autorização da direção. Nenhuma data foi definida. Uma versão inicial do comunicado dizia que as reuniões “passarão a ser sempre à noite”; essa decisão não consta dos registros e não deve aparecer no resumo. A proposta não garante que a participação presencial aumentará. A preferência declarada não é uma medida de presença futura.
> 
> Um campo opcional recebeu comentários de 39 famílias. Dezessete mencionaram trabalho, nove mencionaram deslocamento e seis mencionaram cuidar de outras crianças. Um comentário podia abordar mais de um assunto. Esses números não devem ser somados como grupos exclusivos nem apresentados como proporções de todas as famílias. As observações ajudam a descrever as respostas, mas o levantamento não mede o efeito de mudar o horário sobre a presença ou a aprendizagem.

### baseline: flagged

```text
O questionário foi enviado às 360 famílias com telefone atualizado e recebeu 126 respostas completas: 84 preferiram a reunião às 19h, 28 às 14h e 14 não escolheram horário. A preferência por 19h representa dois terços das pessoas que responderam, não de todas as famílias da escola, e diz respeito a uma reunião específica no próximo bimestre, não a todas as reuniões do ano. A participação foi voluntária, o formulário estava apenas em português e famílias sem telefone atualizado não receberam convite. Não houve amostragem aleatória nem comparação entre respondentes e não respondentes; também não se sabe quantas mensagens foram lidas. Não foram verificadas condições de transporte, cuidado com crianças ou jornada de trabalho.

A coordenação propôs testar as 19h em uma reunião, ainda sem data e dependendo da disponibilidade da equipe e da autorização da direção. Não há decisão de tornar todas as reuniões noturnas nem garantia de maior presença: preferência declarada não mede participação futura. Das 39 famílias que comentaram, 17 mencionaram trabalho, nove deslocamento e seis cuidado com outras crianças. Como um comentário podia abordar vários assuntos, esses números não são grupos exclusivos, não devem ser somados como tal nem representam proporções de todas as famílias. O levantamento descreve as respostas, mas não mede o efeito da mudança de horário sobre presença ou aprendizagem.
```

Review notes: Dois parágrafos preservam os denominadores, limitações de seleção, comentários e caráter condicional da proposta. / Resumo fiel nas limitações materiais; omite apenas o caráter opcional do campo, mantendo participação voluntária e base dos comentários.

### lite: pass

```text
Das 126 respostas completas, 84 indicaram preferência por reunião às 19h, 28 por reunião às 14h e 14 não escolheram horário. A preferência por 19h representa dois terços de quem respondeu, não de todas as famílias da escola. O questionário foi enviado por mensagem às 360 famílias com telefone atualizado; as demais não receberam o convite. A participação foi voluntária, o formulário estava apenas em português e a amostra não foi aleatória. Não se verificou se quem respondeu diferia de quem não respondeu, nem há informação suficiente para calcular quantas mensagens foram lidas. A pergunta tratava de uma reunião específica no próximo bimestre, não de todas as reuniões do ano, e não verificou transporte, necessidade de cuidado com crianças ou jornada de trabalho.

A coordenação propôs testar as 19h em uma reunião, mas isso depende da disponibilidade da equipe e da autorização da direção; não há data definida. Não foi decidido que as reuniões serão sempre à noite. A preferência declarada não mede presença futura nem garante aumento da participação presencial. No campo opcional, 39 famílias comentaram: 17 mencionaram trabalho, nove deslocamento e seis cuidado com outras crianças. Um comentário podia abordar mais de um assunto; esses números não são grupos exclusivos e não representam proporções de todas as famílias. Os comentários descrevem as respostas, mas o levantamento não mede o efeito da mudança de horário sobre presença ou aprendizagem.
```

### full: pass

```text
Entre as 126 respostas completas, 84 preferiram uma reunião às 19h, 28 às 14h e 14 não escolheram horário. A preferência pelas 19h representa dois terços das pessoas que responderam, não de todas as famílias da escola, e se refere a uma reunião específica no próximo bimestre, não a todas as reuniões do ano. O convite foi enviado por mensagem às 360 famílias com telefone atualizado; as demais não foram convidadas. A participação foi voluntária, o formulário estava disponível apenas em português e a amostra não foi aleatória. Não se verificaram diferenças entre quem respondeu e quem não respondeu, nem há informação suficiente para saber quantas mensagens foram lidas. Também não foram verificadas disponibilidade de transporte, necessidade de cuidado com crianças ou jornada de trabalho.

A coordenação propôs testar as 19h em uma reunião, dependendo da disponibilidade da equipe e da autorização da direção, sem data definida. Não há decisão de realizar sempre as reuniões à noite. A preferência declarada não mede presença futura nem garante aumento da participação presencial. No campo opcional, 39 famílias comentaram: 17 mencionaram trabalho, nove deslocamento e seis cuidado de outras crianças. Um comentário podia abordar vários assuntos; esses números não são grupos exclusivos e não representam proporções de todas as famílias. Os comentários ajudam a descrever as respostas, mas o levantamento não mede o efeito da mudança de horário sobre a presença ou a aprendizagem.
```

### ultra: pass

```text
Das 126 respostas completas, 84 preferiram reunião às 19h, 28 às 14h e 14 não escolheram horário. Os dois terços favoráveis às 19h representam quem respondeu, não todas as famílias. O convite foi enviado por mensagem às 360 famílias com telefone atualizado; as demais não o receberam. A participação foi voluntária, o formulário estava apenas em português e a amostra não foi aleatória. Não se verificaram diferenças entre respondentes e não respondentes, nem há dados suficientes para calcular quantas mensagens foram lidas. A pergunta tratava de uma reunião no próximo bimestre, não de todas as reuniões do ano, e não verificava transporte, cuidado com crianças ou jornada de trabalho.

A coordenação propôs testar as 19h em uma reunião, dependendo da disponibilidade da equipe e da autorização da direção; não há data definida nem decisão de realizar sempre as reuniões à noite. A preferência declarada não mede presença futura nem garante aumento de participação. No campo opcional, 39 famílias comentaram: 17 mencionaram trabalho, nove deslocamento e seis cuidado com outras crianças. Um comentário podia abordar vários assuntos; os números não são grupos exclusivos nem proporções de todas as famílias. Esses comentários descrevem as respostas, mas o levantamento não mede o efeito da mudança de horário sobre presença ou aprendizagem.
```

### off: pass

```text
Entre as 126 respostas completas, 84 indicaram preferência por uma reunião às 19h, 28 às 14h e 14 não escolheram horário. A preferência pelas 19h representa dois terços dos respondentes, não de todas as famílias da escola. O questionário foi enviado por mensagem às 360 famílias com telefone atualizado; as demais não receberam o convite. A participação foi voluntária, o formulário estava disponível apenas em português e a amostra não foi aleatória. Não se verificou se respondentes e não respondentes diferiam, nem há informação suficiente para saber quantas mensagens foram lidas. A pergunta tratava de uma reunião específica no próximo bimestre, não de todas as reuniões do ano, e não avaliou transporte, cuidado com crianças ou jornada de trabalho. No campo opcional, 39 famílias comentaram: 17 mencionaram trabalho, nove deslocamento e seis cuidado com outras crianças. Um comentário podia tratar de mais de um assunto; esses números não são grupos exclusivos nem proporções de todas as famílias.

A coordenação propôs testar o horário das 19h em uma reunião, condicionado à disponibilidade da equipe e à autorização da direção. Nenhuma data foi definida, e não há decisão registrada de que as reuniões serão sempre à noite. A preferência declarada não mede presença futura nem garante aumento da participação presencial. Os comentários ajudam a descrever as respostas, mas o levantamento não mede o efeito da mudança de horário sobre a presença ou a aprendizagem.
```

## modes-pt-BR-005 · analysis

Source task:

> Responda à pergunta da associação: o caixa disponível cobre o aluguel do salão e todas as despesas confirmadas do encontro? Mostre a conta e trate separadamente a despesa possível. Não recomende como arrecadar mais.
> 
> O saldo disponível no caixa operacional é de R$ 9.800. Há também uma reserva de R$ 3.000, que não deve ser usada nesta comparação. O saldo operacional já inclui as inscrições recebidas até ontem. Não some esse dinheiro de novo. As despesas confirmadas ainda não pagas são: R$ 3.200 de aluguel do salão, R$ 1.450 de som, R$ 780 de limpeza e R$ 620 de materiais. O aluguel será pago em duas parcelas de R$ 1.600; elas compõem os R$ 3.200, não são valores adicionais.
> 
> O serviço de transporte foi confirmado por R$ 1.900. Um segundo veículo custaria R$ 700, mas só seria contratado se as inscrições ultrapassassem 100 pessoas. Até agora há 86 pessoas inscritas, e a contratação do segundo veículo não está confirmada. A nota não informa se novas inscrições serão abertas. Também não há contrato assinado para a doação de R$ 1.500 que uma empresa mencionou por telefone. Essa possível doação não é um recebimento garantido.
> 
> O responsável pelo caixa quer saber se o encontro já confirmado cabe no saldo. Ele não perguntou qual serviço deve ser cortado e não pediu para considerar equipamentos extras. Uma lista antiga inclui R$ 400 para decoração, mas a comissão retirou esse item antes de confirmar o orçamento. O texto final deve usar a lista confirmada acima, não a lista antiga. Os participantes poderão levar alimentos, mas não há estimativa de valor dessas contribuições e elas não reduzem as despesas informadas.
> 
> A comparação correta precisa somar as cinco despesas confirmadas, manter as parcelas do aluguel dentro do total do aluguel e distinguir a situação atual da hipótese do veículo extra. O registro não traz data de pagamento ou autorização para movimentar a reserva. Não crie um prazo, uma decisão de contratação ou uma promessa de doação. Explique somente o resultado que os números sustentam.

### baseline: pass

```text
Sim. O caixa operacional disponível de R$ 9.800 cobre o aluguel e todas as despesas confirmadas ainda não pagas:

- Aluguel: R$ 3.200, composto por duas parcelas de R$ 1.600;
- Som: R$ 1.450;
- Limpeza: R$ 780;
- Materiais: R$ 620;
- Transporte confirmado: R$ 1.900.

Total: R$ 3.200 + R$ 1.450 + R$ 780 + R$ 620 + R$ 1.900 = R$ 7.950.
Saldo após essas despesas: R$ 9.800 − R$ 7.950 = R$ 1.850.

Despesa possível: o segundo veículo custaria R$ 700 e só seria contratado se as inscrições ultrapassassem 100 pessoas. Há 86 inscritos, e a contratação não está confirmada. Se essa despesa fosse confirmada, o total seria R$ 8.650, ainda coberto pelo caixa, com saldo de R$ 1.150. Não há informação sobre abertura de novas inscrições.

A conta não usa a reserva de R$ 3.000 nem soma novamente as inscrições, já incluídas no saldo operacional. Também não considera a possível doação de R$ 1.500, que não tem contrato assinado, a decoração de R$ 400, retirada do orçamento, ou contribuições de alimentos, sem valor estimado e que não reduzem as despesas informadas. O registro não informa datas de pagamento nem autoriza movimentar a reserva.
```

### lite: pass

```text
Sim. O caixa operacional de R$ 9.800 cobre o aluguel e todas as cinco despesas confirmadas ainda não pagas:

- Aluguel do salão: R$ 3.200, em duas parcelas de R$ 1.600 já incluídas nesse total.
- Som: R$ 1.450.
- Limpeza: R$ 780.
- Materiais: R$ 620.
- Transporte confirmado: R$ 1.900.

Total: R$ 3.200 + R$ 1.450 + R$ 780 + R$ 620 + R$ 1.900 = R$ 7.950.
Saldo após essas despesas: R$ 9.800 − R$ 7.950 = R$ 1.850.

Despesa possível: o segundo veículo custaria R$ 700 e só seria contratado se as inscrições ultrapassassem 100 pessoas. Há 86 pessoas inscritas, e essa contratação não está confirmada. Se o veículo extra fosse contratado, o total seria R$ 8.650 e ainda restariam R$ 1.150 no caixa operacional. A nota não informa se novas inscrições serão abertas.

A conta não usa a reserva de R$ 3.000 nem soma novamente as inscrições recebidas até ontem, já incluídas no saldo operacional. Também não considera a possível doação de R$ 1.500, que não tem contrato assinado e não é garantida, nem os R$ 400 de decoração retirados do orçamento. As contribuições de alimentos não têm valor estimado e não reduzem as despesas informadas. O registro não informa datas de pagamento nem autoriza movimentar a reserva.
```

### full: pass

```text
Sim. O caixa operacional de R$ 9.800 cobre o aluguel e todas as despesas confirmadas ainda não pagas, com saldo de R$ 1.850 após esses pagamentos.

| Despesa confirmada | Valor |
| --- | ---: |
| Aluguel do salão | R$ 3.200 |
| Som | R$ 1.450 |
| Limpeza | R$ 780 |
| Materiais | R$ 620 |
| Transporte | R$ 1.900 |
| **Total** | **R$ 7.950** |

**Conta:** R$ 9.800 − R$ 7.950 = **R$ 1.850**.

As duas parcelas de R$ 1.600 do aluguel já compõem os R$ 3.200. O saldo operacional já inclui as inscrições recebidas até ontem; esse dinheiro não foi somado novamente. A reserva de R$ 3.000 ficou fora da comparação.

**Despesa possível:** o segundo veículo custaria R$ 700 e só seria contratado se as inscrições ultrapassassem 100 pessoas. Há 86 inscritas, e a contratação não está confirmada. Se essa despesa se confirmar, o total será de R$ 8.650 e ainda caberá no saldo atual, restando R$ 1.150. Não há informação sobre a abertura de novas inscrições.

A possível doação de R$ 1.500, mencionada por telefone e sem contrato assinado, não foi contabilizada como recebimento garantido. Os R$ 400 de decoração foram retirados do orçamento e não entram na conta. As contribuições de alimentos não têm valor estimado e não reduzem as despesas informadas. O registro não informa datas de pagamento nem autorização para movimentar a reserva.
```

### ultra: pass

```text
Sim. O caixa operacional de R$ 9.800 cobre as cinco despesas confirmadas ainda não pagas:

- Aluguel: R$ 3.200, em duas parcelas de R$ 1.600 já incluídas nesse total.
- Som: R$ 1.450.
- Limpeza: R$ 780.
- Materiais: R$ 620.
- Transporte confirmado: R$ 1.900.

Total: R$ 3.200 + R$ 1.450 + R$ 780 + R$ 620 + R$ 1.900 = R$ 7.950.
Saldo após essas despesas: R$ 9.800 − R$ 7.950 = R$ 1.850.

**Despesa possível:** o segundo veículo custaria R$ 700 e só seria contratado se as inscrições ultrapassassem 100 pessoas. Há 86 inscritas; a contratação não está confirmada e não se sabe se novas inscrições serão abertas. Se essa despesa fosse confirmada, o total seria R$ 8.650 e ainda sobrariam R$ 1.150.

A conta exclui a reserva de R$ 3.000 e não soma novamente as inscrições, já incluídas no caixa operacional. Também exclui a possível doação de R$ 1.500, mencionada por telefone e sem contrato assinado, e os R$ 400 de decoração retirados do orçamento. Os alimentos que participantes poderão levar não têm valor estimado e não reduzem as despesas informadas. Não há datas de pagamento nem autorização para movimentar a reserva.
```

### off: pass

```text
Sim. O caixa operacional de R$ 9.800 cobre o aluguel do salão e todas as despesas confirmadas ainda não pagas.

A conta é:

- Aluguel do salão: R$ 3.200;
- Som: R$ 1.450;
- Limpeza: R$ 780;
- Materiais: R$ 620;
- Transporte confirmado: R$ 1.900.

Total confirmado: R$ 3.200 + R$ 1.450 + R$ 780 + R$ 620 + R$ 1.900 = **R$ 7.950**.

Saldo após essas despesas: R$ 9.800 − R$ 7.950 = **R$ 1.850**.

As duas parcelas de R$ 1.600 já compõem os R$ 3.200 do aluguel. As inscrições recebidas até ontem já estão no saldo operacional e não foram somadas novamente. A reserva de R$ 3.000 não entra na comparação.

**Despesa possível:** o segundo veículo custaria R$ 700 e só seria contratado se as inscrições ultrapassassem 100 pessoas. Há 86 inscritas, a contratação não está confirmada e não se sabe se novas inscrições serão abertas. Caso essa despesa seja confirmada, o total seria R$ 8.650 e ainda restariam R$ 1.150 do saldo operacional atual.

A possível doação de R$ 1.500, mencionada por telefone e sem contrato assinado, não foi contabilizada como recebimento garantido. Os R$ 400 de decoração foram retirados do orçamento e não entram na soma. As contribuições de alimentos não têm valor estimado e não reduzem as despesas informadas.
```

## modes-pt-BR-006 · exact-format

Source task:

> Devolva apenas um objeto JSON com as chaves "route_id", "capacity", "active" e "note". Copie exatamente os valores fixos do registro final. A nota deve estar em português do Brasil e explicar o estado confirmado.
> 
> Histórico: A proposta inicial previa o veículo "Circular-8" com capacidade de 24 pessoas. Esse número veio de uma estimativa feita antes da vistoria e não foi aprovado. A equipe discutiu trocar os bancos, mas nenhuma troca foi realizada. A vistoria posterior contou 20 lugares utilizáveis. Dois bancos foram bloqueados para reparo, e os outros lugares mencionados na proposta inicial não estavam instalados no veículo vistoriado. Não trate a proposta de 24 lugares como capacidade atual.
> 
> O coordenador registrou que a rota ficaria inativa até a liberação da vistoria elétrica. A vistoria de assentos não substitui a elétrica. O relatório de assentos foi assinado, mas o elétrico ainda não chegou. A existência de uma rota no sistema de horários não significa que ela esteja ativa. O sistema permite cadastrar rotas antes da liberação. Uma planilha de divulgação usou a palavra “pronta”; essa palavra não foi confirmada pelo coordenador e não faz parte do registro final.
> 
> Registro final: route_id = "Circular-8"; capacity = 20; active = false. A equipe sabe que há 20 lugares utilizáveis no veículo, mas a rota continua inativa à espera da liberação elétrica. Não foi marcada data de início. A discussão sobre bancos extras permanece sem decisão e não deve aparecer como uma ação já autorizada. O objeto JSON representa o registro final, não um resumo de todas as versões anteriores.
> 
> Na chave note, explique em uma frase ou duas que a capacidade registrada é de 20 pessoas e a rota permanece inativa porque a liberação elétrica está pendente. Não diga que a rota foi cancelada definitivamente ou que já está pronta para operar. capacity deve ser número e active deve ser booleano, não texto. As chaves são parte de uma interface técnica e devem permanecer em inglês. Não use bloco de código nem comentário fora do objeto.

### baseline: pass

```text
{"route_id":"Circular-8","capacity":20,"active":false,"note":"A capacidade registrada é de 20 pessoas, e a rota permanece inativa porque a liberação elétrica está pendente."}
```

### lite: pass

```text
{"route_id":"Circular-8","capacity":20,"active":false,"note":"A capacidade registrada é de 20 pessoas. A rota permanece inativa porque a liberação elétrica está pendente."}
```

### full: pass

```text
{"route_id":"Circular-8","capacity":20,"active":false,"note":"A capacidade registrada é de 20 pessoas. A rota permanece inativa porque a liberação elétrica está pendente."}
```

### ultra: pass

```text
{"route_id":"Circular-8","capacity":20,"active":false,"note":"A capacidade registrada é de 20 pessoas. A rota permanece inativa porque a liberação elétrica está pendente."}
```

### off: pass

```text
{"route_id":"Circular-8","capacity":20,"active":false,"note":"A capacidade registrada é de 20 pessoas, e a rota permanece inativa porque a liberação elétrica está pendente."}
```

## modes-pt-BR-007 · voice

Source task:

> Edite este relato em primeira pessoa para deixá-lo mais fluido. Preserve o humor discreto e os limites do que a narradora sabe. Não transforme o relato em propaganda.
> 
> Entrei na sala de costura com uma fita métrica e uma confiança que não cabia no bolso. A primeira gaveta continha onze carretéis e nenhum fio da cor pedida. A segunda continha botões suficientes para iniciar uma pequena assembleia. Minha tarefa era contar os carretéis, não decidir o destino político dos botões. Contei onze e registrei esse número. Não sei se todos ainda têm linha utilizável; não abri cada carretel nem fiz um teste de resistência.
> 
> A equipe espera retomar as oficinas em janeiro. A palavra “espera” não é um erro de revisão: o telhado ainda está sendo avaliado e duas máquinas aguardam manutenção. Bia aprovou o texto da chamada para inscrições, mas essa aprovação não libera o espaço nem confirma a data. As inscrições ainda não foram abertas. Seria elegante terminar este parágrafo com uma data exata, mas o registro não oferece uma e minha fita métrica não mede futuro.
> 
> Uma antiga participante disse que os botões vieram de uma doação feita em 1998. Na ficha do acervo, a origem aparece como “não confirmada”. Não há recibo de doação anexado. Registrei a lembrança da participante ao lado da ficha, sem substituir a descrição existente. A lembrança pode ajudar uma investigação, mas não vira documento só porque é mais simpática que o campo vazio. Também não sabemos quem organizou os botões por tamanho.
> 
> Ao sair, devolvi os onze carretéis à primeira gaveta. A equipe ainda não transferiu os materiais para a sala nova. Se essa transferência acontecer, será necessário atualizar a localização no cadastro. Por enquanto, a única melhoria que posso garantir é que a gaveta fecha quando deixamos a fita métrica do lado de fora. Mantenha esse final prático. Não acrescente promessa sobre vagas, qualidade das oficinas ou a experiência dos futuros participantes.

### baseline: pass

```text
Entrei na sala de costura com uma fita métrica e uma confiança que não cabia no bolso. Na primeira gaveta, encontrei onze carretéis e nenhum fio da cor pedida. Na segunda, havia botões suficientes para iniciar uma pequena assembleia. Minha tarefa era contar os carretéis, não decidir o destino político dos botões. Contei onze e registrei o número. Não sei se todos ainda têm linha utilizável: não abri cada carretel nem fiz um teste de resistência.

A equipe espera retomar as oficinas em janeiro. A palavra “espera” não é um erro de revisão: o telhado ainda está sendo avaliado e duas máquinas aguardam manutenção. Bia aprovou o texto da chamada para inscrições, mas isso não libera o espaço nem confirma a data. As inscrições ainda não foram abertas. Seria elegante encerrar este parágrafo com uma data exata, mas o registro não oferece uma, e minha fita métrica não mede futuro.

Uma antiga participante contou que os botões vieram de uma doação feita em 1998. Na ficha do acervo, porém, a origem consta como “não confirmada”, e não há recibo de doação anexado. Registrei a lembrança ao lado da ficha, sem substituir a descrição existente. Ela pode ajudar uma investigação, mas não vira documento só por ser mais simpática que o campo vazio. Também não sabemos quem organizou os botões por tamanho.

Ao sair, devolvi os onze carretéis à primeira gaveta. A equipe ainda não transferiu os materiais para a sala nova; se isso acontecer, será necessário atualizar a localização no cadastro. Por enquanto, a única melhoria que posso garantir é que a gaveta fecha quando deixamos a fita métrica do lado de fora.
```

### lite: pass

```text
Entrei na sala de costura com uma fita métrica e uma confiança que não cabia no bolso. A primeira gaveta continha onze carretéis e nenhum fio da cor pedida. A segunda tinha botões suficientes para iniciar uma pequena assembleia. Minha tarefa era contar os carretéis, não decidir o destino político dos botões. Contei onze e registrei esse número. Não sei se todos ainda têm linha utilizável; não abri cada carretel nem fiz um teste de resistência.

A equipe espera retomar as oficinas em janeiro. A palavra “espera” não é um erro de revisão: o telhado ainda está sendo avaliado e duas máquinas aguardam manutenção. Bia aprovou o texto da chamada para inscrições, mas essa aprovação não libera o espaço nem confirma a data. As inscrições ainda não foram abertas. Seria elegante terminar este parágrafo com uma data exata, mas o registro não oferece uma e minha fita métrica não mede futuro.

Uma antiga participante disse que os botões vieram de uma doação feita em 1998. Na ficha do acervo, a origem aparece como “não confirmada”. Não há recibo de doação anexado. Registrei a lembrança da participante ao lado da ficha, sem substituir a descrição existente. A lembrança pode ajudar uma investigação, mas não vira documento só porque é mais simpática que o campo vazio. Também não sabemos quem organizou os botões por tamanho.

Ao sair, devolvi os onze carretéis à primeira gaveta. A equipe ainda não transferiu os materiais para a sala nova. Se essa transferência acontecer, será necessário atualizar a localização no cadastro. Por enquanto, a única melhoria que posso garantir é que a gaveta fecha quando deixamos a fita métrica do lado de fora.
```

### full: pass

```text
Entrei na sala de costura com uma fita métrica e uma confiança que não cabia no bolso. Na primeira gaveta, havia onze carretéis e nenhum fio da cor pedida. Na segunda, botões suficientes para iniciar uma pequena assembleia. Minha tarefa era contar os carretéis, não decidir o destino político dos botões. Contei onze e registrei o número. Não sei se todos ainda têm linha utilizável: não abri cada carretel nem fiz um teste de resistência.

A equipe espera retomar as oficinas em janeiro. “Espera” não é um erro de revisão: o telhado ainda está sendo avaliado e duas máquinas aguardam manutenção. Bia aprovou o texto da chamada para inscrições, mas isso não libera o espaço nem confirma a data. As inscrições ainda não foram abertas. Seria elegante terminar este parágrafo com uma data exata, mas o registro não oferece uma e minha fita métrica não mede futuro.

Uma antiga participante disse que os botões vieram de uma doação feita em 1998. Na ficha do acervo, a origem consta como “não confirmada”, e não há recibo de doação anexado. Registrei a lembrança ao lado da ficha, sem substituir a descrição existente. Ela pode ajudar uma investigação, mas não vira documento só porque é mais simpática que o campo vazio. Também não sabemos quem organizou os botões por tamanho.

Ao sair, devolvi os onze carretéis à primeira gaveta. A equipe ainda não transferiu os materiais para a sala nova. Se a transferência acontecer, será necessário atualizar a localização no cadastro. Por enquanto, a única melhoria que posso garantir é que a gaveta fecha quando deixamos a fita métrica do lado de fora.
```

### ultra: pass

```text
Entrei na sala de costura com uma fita métrica e uma confiança que não cabia no bolso. Na primeira gaveta, havia onze carretéis e nenhum fio da cor pedida. Na segunda, botões suficientes para uma pequena assembleia. Minha tarefa era contar carretéis, não decidir o destino político dos botões. Contei onze e registrei o número. Não sei se todos ainda têm linha utilizável: não abri cada carretel nem testei a resistência.

A equipe espera retomar as oficinas em janeiro. “Espera” não é erro de revisão: o telhado ainda está sendo avaliado e duas máquinas aguardam manutenção. Bia aprovou o texto da chamada para inscrições, mas isso não libera o espaço nem confirma a data. As inscrições ainda não foram abertas. Seria elegante terminar com uma data exata, mas o registro não oferece uma e minha fita métrica não mede futuro.

Uma antiga participante disse que os botões vieram de uma doação de 1998. Na ficha do acervo, a origem consta como “não confirmada”, sem recibo de doação anexado. Registrei a lembrança ao lado da ficha, sem substituir a descrição. Ela pode ajudar uma investigação, mas não vira documento só por ser mais simpática que o campo vazio. Também não sabemos quem organizou os botões por tamanho.

Ao sair, devolvi os onze carretéis à primeira gaveta. A equipe ainda não transferiu os materiais para a sala nova. Se isso acontecer, será necessário atualizar a localização no cadastro. Por enquanto, a única melhoria que posso garantir é que a gaveta fecha quando deixamos a fita métrica do lado de fora.
```

### off: pass

```text
Entrei na sala de costura com uma fita métrica e uma confiança que não cabia no bolso. Na primeira gaveta, encontrei onze carretéis e nenhum fio da cor pedida. Na segunda, havia botões suficientes para iniciar uma pequena assembleia. Minha tarefa era contar os carretéis, não decidir o destino político dos botões. Contei onze e registrei o número. Não sei se todos ainda têm linha utilizável: não abri cada carretel nem fiz um teste de resistência.

A equipe espera retomar as oficinas em janeiro. A palavra “espera” não é um erro de revisão: o telhado ainda está sendo avaliado e duas máquinas aguardam manutenção. Bia aprovou o texto da chamada para inscrições, mas isso não libera o espaço nem confirma a data. As inscrições ainda não foram abertas. Seria elegante encerrar este parágrafo com uma data exata, mas o registro não oferece uma, e minha fita métrica não mede futuro.

Uma antiga participante disse que os botões vieram de uma doação feita em 1998. Na ficha do acervo, porém, a origem aparece como “não confirmada”, e não há recibo de doação anexado. Registrei a lembrança da participante ao lado da ficha, sem substituir a descrição existente. A lembrança pode ajudar uma investigação, mas não vira documento só porque é mais simpática que o campo vazio. Também não sabemos quem organizou os botões por tamanho.

Ao sair, devolvi os onze carretéis à primeira gaveta. A equipe ainda não transferiu os materiais para a sala nova. Se essa transferência acontecer, será necessário atualizar a localização no cadastro. Por enquanto, a única melhoria que posso garantir é que a gaveta fecha quando deixamos a fita métrica do lado de fora.
```

## modes-pt-BR-008 · scope

Source task:

> Com base no texto abaixo, responda apenas a esta pergunta, em até três frases: o pedido de uso da sala precisa chegar na segunda-feira, e o que acontece se chegar depois? Não resuma os outros procedimentos.
> 
> Regra vigente: Para usar a sala de ensaio na sexta-feira, o pedido deve ser recebido até as 12h de segunda-feira, no horário local. Não basta enviar o pedido antes desse horário; ele precisa chegar ao sistema. Pedidos recebidos depois entram na fila da próxima data disponível. A secretaria não garante que essa data seja a sexta-feira seguinte. A regra vale para o pedido da sala, não para a lista de participantes. A lista deve ser entregue até as 18h da véspera do uso. Um pedido recebido no prazo não dispensa a lista.
> 
> O grupo pretende ensaiar com nove pessoas e usar três estantes de partitura. A sala comporta até doze pessoas, mas o grupo ainda não confirmou o número final. Há quatro estantes no prédio; uma está reservada para outra atividade. A equipe prevê duas horas de ensaio e deseja gravar um trecho. A gravação precisa de autorização separada, que não foi solicitada. Os detalhes de capacidade e equipamento não alteram o prazo do pedido da sala.
> 
> No ano passado, uma mensagem da secretaria permitia receber pedidos até terça-feira. Essa regra pertencia a outro calendário e foi substituída pela regra vigente. Uma anotação do grupo diz “documentos na segunda”, mas a regra diferencia o pedido da sala e a lista. Não transforme todos os documentos em exigências para a segunda-feira. O texto não identifica quem levará as estantes ou quem abrirá a sala.
> 
> A pergunta trata somente do prazo e da consequência de chegar depois. Informações sobre participantes, estantes, duração, gravação e lista são contexto e podem ser omitidas. Não dê conselhos para conseguir uma exceção nem invente uma reserva confirmada. A secretaria ainda não recebeu o pedido. A resposta deve preservar a diferença entre enviar e receber e não prometer uma data para os pedidos tardios.

### baseline: pass

```text
Para usar a sala na sexta-feira, o pedido precisa chegar ao sistema até as 12h de segunda-feira, no horário local; não basta enviá-lo antes desse horário. Se for recebido depois, entra na fila da próxima data disponível, sem garantia de que seja a sexta-feira seguinte.
```

### lite: pass

```text
Para usar a sala na sexta-feira, o pedido deve chegar ao sistema até as 12h de segunda-feira, no horário local; não basta enviá-lo antes desse prazo. Se chegar depois, entra na fila da próxima data disponível. A secretaria não garante que essa data seja a sexta-feira seguinte.
```

### full: pass

```text
Para usar a sala na sexta-feira, o pedido precisa chegar ao sistema até as 12h de segunda-feira, no horário local; enviá-lo antes desse horário não basta. Se chegar depois, entra na fila da próxima data disponível, sem garantia de que seja a sexta-feira seguinte.
```

### ultra: pass

```text
Para usar a sala na sexta-feira, o pedido precisa chegar ao sistema até as 12h de segunda-feira, no horário local; não basta enviá-lo até esse horário. Se chegar depois, entra na fila da próxima data disponível, sem garantia de que seja a sexta-feira seguinte.
```

### off: pass

```text
Sim: para usar a sala na sexta-feira, o pedido precisa ser recebido pelo sistema até as 12h de segunda-feira, no horário local; não basta enviá-lo antes desse horário. Se chegar depois, entra na fila da próxima data disponível, sem garantia de que seja a sexta-feira seguinte.
```

## modes-pt-BR-009 · ambiguity

Source task:

> Reescreva a nota de manutenção para o conselho do prédio. Mantenha as lacunas e os registros em conflito, sem escolher uma versão.
> 
> O livro da portaria diz: “Em 06/07, Alex conversou com Dani depois que a válvula foi retirada.” A anotação não informa o ano nem o padrão de data. A empresa que atende o prédio usa dia/mês, mas um fornecedor estrangeiro usa mês/dia, e a frase foi copiada de uma mensagem sem identificação do remetente. Não é possível escolher entre 6 de julho e 7 de junho só com esse registro. A função de Alex e de Dani também não está indicada. O texto registra uma conversa depois da retirada, mas não identifica quem retirou a válvula.
> 
> Uma ordem de serviço tem data de 7 de junho de 2028 e referência V-21. Um recibo de entrada de material tem data de 6 de julho de 2028 e referência V-12. Nenhum deles afirma que a válvula foi retirada naquele dia. A equipe não confirmou se os dois documentos se referem à mesma peça ou à válvula mencionada no livro. Não há retificação que transforme V-21 em V-12. A proximidade das letras e dos números não autoriza corrigir um dos registros por conta própria.
> 
> O painel mostrou queda de pressão durante 40 minutos antes da anotação e valores normais nas duas horas seguintes. Não há horário registrado para a retirada física. Essa sequência não prova que retirar a válvula resolveu a queda. O técnico escreveu que havia “possível obstrução”, mas o laudo de exame da peça não foi anexado. Uma obstrução permanece hipótese. O conselho pediu comparação dos registros e ainda não determinou a causa.
> 
> Uma versão anterior dizia que “Dani retirou a válvula obstruída em 6 de julho e Alex confirmou a solução”. Essa frase acrescenta ator, data interpretada, causa e confirmação que não estão estabelecidos. A nova nota deve manter a conversa depois da retirada, a data ambígua, o vínculo não confirmado entre os documentos e a diferença entre pressão normal observada e solução permanente. Não crie recomendação de reparo, responsável pela comparação ou prazo.

### baseline: pass

```text
Nota de manutenção ao conselho

O livro da portaria registra: “Em 06/07, Alex conversou com Dani depois que a válvula foi retirada.” Não informa o ano nem o padrão da data. Como a frase foi copiada de uma mensagem sem remetente identificado, e os envolvidos usam padrões distintos, não é possível escolher entre 6 de julho e 7 de junho. As funções de Alex e Dani não estão indicadas, assim como a identidade de quem retirou a válvula.

A ordem de serviço de 7 de junho de 2028 traz a referência V-21; o recibo de entrada de material de 6 de julho de 2028 traz V-12. Nenhum documento afirma que a retirada ocorreu naquela data. Não foi confirmado se ambos tratam da mesma peça ou da válvula citada no livro. As referências permanecem distintas, sem retificação que autorize substituir uma pela outra.

O painel mostrou queda de pressão durante 40 minutos antes da anotação e valores normais nas duas horas seguintes. Não há horário registrado para a retirada física; essa sequência não comprova que a retirada resolveu a queda nem que a normalização seja permanente. O técnico mencionou “possível obstrução”, mas o laudo de exame da peça não foi anexado, de modo que a obstrução permanece hipótese.

O conselho solicitou a comparação dos registros e ainda não determinou a causa. Não estão estabelecidas as afirmações da versão anterior de que Dani retirou uma válvula obstruída em 6 de julho e Alex confirmou a solução.
```

### lite: pass

```text
O livro da portaria registra: “Em 06/07, Alex conversou com Dani depois que a válvula foi retirada.” A anotação não informa o ano nem o padrão de data. A empresa que atende o prédio usa dia/mês, mas um fornecedor estrangeiro usa mês/dia. A frase foi copiada de uma mensagem sem identificação do remetente, portanto não é possível escolher entre 6 de julho e 7 de junho com base nesse registro. As funções de Alex e Dani não estão indicadas. A conversa ocorreu depois da retirada, mas o registro não identifica quem retirou a válvula.

A ordem de serviço tem data de 7 de junho de 2028 e referência V-21. O recibo de entrada de material tem data de 6 de julho de 2028 e referência V-12. Nenhum documento afirma que a válvula foi retirada naquele dia. A equipe não confirmou se os documentos se referem à mesma peça ou à válvula mencionada no livro. Não há retificação de V-21 para V-12; a semelhança entre as referências não autoriza corrigir um dos registros.

O painel mostrou queda de pressão durante 40 minutos antes da anotação e valores normais nas duas horas seguintes. Não há horário registrado para a retirada física. Essa sequência não prova que a retirada resolveu a queda nem que a pressão normal observada representa uma solução permanente. O técnico registrou “possível obstrução”, mas o laudo de exame da peça não foi anexado. A obstrução permanece uma hipótese. O conselho pediu a comparação dos registros e ainda não determinou a causa.

A versão anterior dizia que “Dani retirou a válvula obstruída em 6 de julho e Alex confirmou a solução”. Essa frase atribui a retirada a Dani, interpreta a data e afirma obstrução e confirmação da solução, sem que esses pontos estejam estabelecidos pelos registros.
```

### full: pass

```text
Os registros não permitem determinar a data nem quem retirou a válvula, confirmar o vínculo entre os documentos ou concluir que a retirada resolveu a queda de pressão.

O livro da portaria diz: “Em 06/07, Alex conversou com Dani depois que a válvula foi retirada.” Não informa o ano, o padrão de data, as funções de Alex e Dani nem quem retirou a peça. A empresa que atende o prédio usa dia/mês; um fornecedor estrangeiro usa mês/dia. Como a frase foi copiada de uma mensagem sem remetente identificado, 06/07 pode significar 6 de julho ou 7 de junho. O registro estabelece apenas que a conversa ocorreu depois da retirada.

A ordem de serviço tem data de 7 de junho de 2028 e referência V-21. O recibo de entrada de material tem data de 6 de julho de 2028 e referência V-12. Nenhum documento afirma que a retirada ocorreu nessas datas. Não foi confirmado se ambos tratam da mesma peça ou da válvula mencionada no livro. Não há retificação de V-21 para V-12; a semelhança das referências não autoriza corrigir os registros.

O painel mostrou queda de pressão durante 40 minutos antes da anotação e valores normais nas duas horas seguintes. Não há horário registrado para a retirada física. Essa sequência não prova que a retirada resolveu a queda nem que houve solução permanente. O técnico registrou “possível obstrução”, mas o laudo de exame da peça não foi anexado: a obstrução permanece hipótese.

A versão anterior — “Dani retirou a válvula obstruída em 6 de julho e Alex confirmou a solução” — acrescentava ator, interpretação da data, causa e confirmação não estabelecidos. O conselho pediu a comparação dos registros e ainda não determinou a causa.
```

### ultra: pass

```text
O livro da portaria registra: “Em 06/07, Alex conversou com Dani depois que a válvula foi retirada.” Não informa ano, padrão de data, funções de Alex e Dani nem quem retirou a válvula. A empresa usa dia/mês e um fornecedor estrangeiro, mês/dia; a mensagem copiada não identifica o remetente. Portanto, 06/07 pode significar 6 de julho ou 7 de junho.

A ordem de serviço de 7 de junho de 2028 traz a referência V-21; o recibo de entrada de material de 6 de julho de 2028, V-12. Nenhum documento afirma que a retirada ocorreu naquela data. Não foi confirmado se tratam da mesma peça ou da válvula citada no livro. Não há retificação de V-21 para V-12; a semelhança das referências não autoriza corrigir os registros.

O painel mostrou queda de pressão nos 40 minutos anteriores à anotação e valores normais nas duas horas seguintes. Sem horário da retirada física, essa sequência não prova que retirar a válvula resolveu a queda nem que houve solução permanente. O técnico registrou “possível obstrução”, mas o laudo de exame da peça não foi anexado: a obstrução permanece hipótese.

A versão anterior — “Dani retirou a válvula obstruída em 6 de julho e Alex confirmou a solução” — atribui ator, data, causa e confirmação não estabelecidos. O conselho pediu a comparação dos registros e ainda não determinou a causa.
```

### off: pass

```text
Nota de manutenção ao conselho

O livro da portaria registra: “Em 06/07, Alex conversou com Dani depois que a válvula foi retirada.” Não há indicação do ano nem do padrão de data. A empresa que atende o prédio usa dia/mês, enquanto um fornecedor estrangeiro usa mês/dia; a frase foi copiada de uma mensagem sem identificação do remetente. Assim, o registro não permite escolher entre 6 de julho e 7 de junho. As funções de Alex e Dani não estão indicadas, e não se identifica quem retirou a válvula. Está registrada apenas a conversa posterior à retirada.

A ordem de serviço de 7 de junho de 2028 traz a referência V-21. O recibo de entrada de material de 6 de julho de 2028 traz a referência V-12. Nenhum documento afirma que a retirada ocorreu na respectiva data. Não foi confirmado se ambos se referem à mesma peça ou à válvula mencionada no livro. As referências diferentes permanecem como registradas: não há retificação que transforme V-21 em V-12, e sua semelhança não autoriza corrigir um dos registros.

O painel mostrou queda de pressão durante 40 minutos antes da anotação e valores normais nas duas horas seguintes. Não há horário registrado para a retirada física, e essa sequência não comprova que a retirada resolveu a queda nem que houve solução permanente. O técnico registrou “possível obstrução”, mas o laudo de exame da peça não foi anexado; a obstrução permanece uma hipótese.

O conselho pediu a comparação dos registros e ainda não determinou a causa. A afirmação da versão anterior — “Dani retirou a válvula obstruída em 6 de julho e Alex confirmou a solução” — não é sustentada pelos registros disponíveis: atribui a retirada a uma pessoa, interpreta a data e apresenta como confirmadas a obstrução e a solução.
```

## modes-pt-BR-010 · evidence

Source task:

> Prepare uma nota curta para a reunião de compras sobre o teste de duas tintas. Descreva o que foi observado e o que o teste não permite concluir. Não escolha uma tinta.
> 
> A fabricante aplicou a Tinta Azul e a Tinta Verde em quatro placas de madeira para cada produto. Todas as placas vieram do mesmo lote de madeira. Após 72 horas de secagem, a média de perda de massa no ensaio de abrasão foi de 0,24 g para a Tinta Azul e 0,18 g para a Tinta Verde. O relatório não fornece os valores individuais, o desvio-padrão, um intervalo de confiança ou um teste estatístico. A menor média da Tinta Verde é um resultado observado nesse ensaio; não há base para afirmar significância estatística.
> 
> As placas da Tinta Azul foram preparadas no primeiro dia e as da Tinta Verde, no segundo. A umidade do ambiente só foi registrada no primeiro dia. A espessura aplicada foi descrita como “aproximadamente igual”, sem medição por placa. O procedimento não separa o efeito da tinta de possíveis diferenças de preparação, espessura ou umidade. O ensaio foi realizado por uma funcionária da fabricante, sem observador independente identificado.
> 
> A escola que considera a compra precisa de perda de massa abaixo de 0,25 g em cada placa aceita. Uma média abaixo de 0,25 g não prova que todas as placas ficaram abaixo desse limite. Sem os resultados individuais, a conformidade de cada placa permanece desconhecida. As superfícies da escola também recebem limpeza frequente com um produto não usado no ensaio. Não foram testadas essa limpeza, a exposição ao sol ou a durabilidade depois de vários meses.
> 
> O folheto comercial chama a Tinta Verde de “ideal para ambientes intensivos”. O relatório não define nem mede esse termo. Preços, rendimento por litro e intervalos de repintura não foram fornecidos, portanto o teste não permite comparar custo ao longo do uso. A nota deve distinguir a menor média observada dos limites do desenho do teste. Não apresente garantia de conformidade na escola, verificação independente ou conclusão de que uma tinta oferece melhor custo-benefício.

### baseline: pass

```text
Nota para a reunião de compras

No ensaio da fabricante, com quatro placas do mesmo lote de madeira por tinta e 72 horas de secagem, a perda média de massa por abrasão foi de 0,24 g para a Tinta Azul e 0,18 g para a Tinta Verde. A Verde apresentou menor média nesse ensaio, mas faltam resultados individuais, medidas de dispersão e análise estatística para afirmar significância.

A preparação ocorreu em dias diferentes, a umidade só foi registrada no primeiro e a espessura não foi medida por placa. Assim, não é possível separar o efeito das tintas das diferenças de preparação, espessura ou umidade. O teste foi realizado por uma funcionária da fabricante, sem observador independente identificado.

As médias abaixo de 0,25 g não comprovam que cada placa atende ao limite exigido pela escola. Também não foram testadas a limpeza usada na escola, a exposição ao sol ou a durabilidade após vários meses. A expressão comercial “ideal para ambientes intensivos” não foi definida nem medida; sem preços, rendimento e intervalos de repintura, tampouco é possível comparar custos ao longo do uso. O ensaio não permite escolher uma tinta nem garantir sua conformidade na escola.
```

### lite: pass

```text
A fabricante testou a Tinta Azul e a Tinta Verde em quatro placas de madeira por produto, todas do mesmo lote. Após 72 horas de secagem, a perda média de massa no ensaio de abrasão foi de 0,24 g para a Azul e 0,18 g para a Verde. A Verde apresentou menor média nesse ensaio, mas o relatório não fornece resultados individuais, desvio-padrão, intervalo de confiança ou teste estatístico. Não há base para afirmar significância estatística.

As placas da Azul foram preparadas no primeiro dia e as da Verde, no segundo; a umidade só foi registrada no primeiro. A espessura foi descrita como “aproximadamente igual”, sem medição por placa. O procedimento não separa o efeito da tinta de possíveis diferenças de preparação, espessura ou umidade. Uma funcionária da fabricante realizou o ensaio, sem observador independente identificado.

A escola exige perda de massa abaixo de 0,25 g em cada placa aceita. As médias abaixo desse limite não comprovam a conformidade de todas as placas; sem os resultados individuais, ela permanece desconhecida. Não foram testadas a limpeza frequente com o produto usado na escola, a exposição ao sol ou a durabilidade após vários meses.

A expressão comercial “ideal para ambientes intensivos” não foi definida nem medida no relatório. Sem preços, rendimento por litro e intervalos de repintura, o teste também não permite comparar o custo ao longo do uso nem concluir que uma tinta oferece melhor custo-benefício.
```

### full: pass

```text
A Tinta Verde apresentou menor perda média de massa neste ensaio: 0,18 g, contra 0,24 g da Tinta Azul, após 72 horas de secagem. A fabricante testou quatro placas por produto, todas do mesmo lote de madeira. Sem resultados individuais, desvio-padrão, intervalo de confiança ou teste estatístico, não é possível afirmar significância estatística.

As placas da Tinta Azul foram preparadas no primeiro dia; as da Verde, no segundo. A umidade só foi registrada no primeiro dia, e a espessura foi descrita como “aproximadamente igual”, sem medição por placa. O desenho não separa o efeito da tinta de possíveis diferenças de preparação, espessura ou umidade. Uma funcionária da fabricante realizou o ensaio, sem observador independente identificado.

A escola exige perda inferior a 0,25 g em cada placa aceita. As médias abaixo desse limite não comprovam a conformidade de todas as placas; sem os valores individuais, ela permanece desconhecida. Não foram testadas a limpeza frequente com o produto usado na escola, a exposição ao sol nem a durabilidade após vários meses.

O termo comercial “ideal para ambientes intensivos”, aplicado à Tinta Verde, não foi definido nem medido no relatório. Sem preços, rendimento por litro e intervalos de repintura, também não é possível comparar o custo ao longo do uso. O teste não permite escolher uma tinta nem garantir seu desempenho na escola.
```

### ultra: pass

```text
Após 72 horas de secagem, a perda média de massa no ensaio de abrasão foi de 0,24 g para a Tinta Azul e 0,18 g para a Tinta Verde. A fabricante aplicou cada tinta em quatro placas, todas do mesmo lote de madeira. A Verde teve menor média nesse ensaio, mas faltam valores individuais, desvio-padrão, intervalo de confiança e teste estatístico; não há base para afirmar significância estatística.

As placas da Azul foram preparadas no primeiro dia e as da Verde, no segundo; a umidade só foi registrada no primeiro. A espessura foi descrita como “aproximadamente igual”, sem medição por placa. O procedimento não separa o efeito da tinta de possíveis diferenças de preparação, espessura ou umidade. Uma funcionária da fabricante realizou o ensaio, sem observador independente identificado.

A escola exige perda abaixo de 0,25 g em cada placa aceita. Médias abaixo desse limite não comprovam conformidade individual, que permanece desconhecida. Não foram testadas a limpeza frequente com o produto usado pela escola, a exposição ao sol ou a durabilidade após vários meses.

O relatório não define nem mede “ideal para ambientes intensivos”, expressão do folheto comercial sobre a Verde. Sem preços, rendimento por litro e intervalos de repintura, não é possível comparar custos ao longo do uso. O teste não sustenta garantia de conformidade na escola nem escolha por melhor custo-benefício.
```

### off: pass

```text
No ensaio da fabricante, foram usadas quatro placas de madeira por tinta, todas do mesmo lote. Após 72 horas de secagem, a perda média de massa por abrasão foi de 0,24 g para a Tinta Azul e 0,18 g para a Tinta Verde. A Verde apresentou menor média nesse ensaio, mas o relatório não fornece resultados individuais, desvio-padrão, intervalo de confiança ou teste estatístico; portanto, não permite afirmar significância estatística.

As placas da Azul foram preparadas no primeiro dia e as da Verde, no segundo. A umidade foi registrada apenas no primeiro dia, e a espessura foi descrita como “aproximadamente igual”, sem medição por placa. O procedimento não separa o efeito da tinta de possíveis diferenças de preparação, espessura ou umidade. O ensaio foi conduzido por uma funcionária da fabricante, sem observador independente identificado.

A escola exige perda abaixo de 0,25 g em cada placa aceita. As médias abaixo desse limite não comprovam a conformidade de todas as placas, que permanece desconhecida sem os resultados individuais. Também não foram testadas a limpeza frequente com o produto usado pela escola, a exposição ao sol ou a durabilidade após vários meses. A expressão comercial “ideal para ambientes intensivos” não foi definida nem medida. Sem preços, rendimento por litro e intervalos de repintura, não é possível comparar o custo ao longo do uso ou concluir que uma tinta oferece melhor custo-benefício.
```

## modes-pt-BR-011 · numbers

Source task:

> Reescreva: “A taxa de devolução caiu de 12% para 9%, uma queda de 3 pontos percentuais ou de 25% em relação à taxa inicial. Cada mês teve 400 pedidos entregues. Os pedidos cancelados antes da entrega não entram no cálculo.”

### baseline: pass

```text
A taxa de devolução passou de 12% para 9%: caiu 3 pontos percentuais, o equivalente a 25% da taxa inicial. Em cada mês, foram entregues 400 pedidos. Os pedidos cancelados antes da entrega ficam fora do cálculo.
```

### lite: pass

```text
A taxa de devolução caiu de 12% para 9%: uma queda de 3 pontos percentuais, ou 25% em relação à taxa inicial. Cada mês teve 400 pedidos entregues. Os pedidos cancelados antes da entrega não entram no cálculo.
```

### full: pass

```text
A taxa de devolução caiu de 12% para 9%: redução de 3 pontos percentuais, ou 25% da taxa inicial. Cada mês teve 400 pedidos entregues. Pedidos cancelados antes da entrega não entram no cálculo.
```

### ultra: pass

```text
A taxa de devolução caiu de 12% para 9%: redução de 3 pontos percentuais, ou 25% da taxa inicial. Cada mês teve 400 pedidos entregues. Pedidos cancelados antes da entrega ficam fora do cálculo.
```

### off: pass

```text
A taxa de devolução passou de 12% para 9%. Isso representa uma queda de 3 pontos percentuais, equivalente a 25% da taxa inicial. Em cada mês, foram entregues 400 pedidos. Pedidos cancelados antes da entrega não entram no cálculo.
```

## modes-pt-BR-012 · numbers

Source task:

> Quantos livros estão disponíveis para empréstimo? O acervo tem 240 livros. Há 32 emprestados e 18 separados para reparo; os grupos não se sobrepõem. Outros 25 foram comprados, mas ainda não chegaram e não estão incluídos nos 240. Responda com a conta.

### baseline: pass

```text
240 − 32 − 18 = 190 livros disponíveis para empréstimo. Os 25 comprados ainda não chegaram e não entram na conta.
```

### lite: pass

```text
240 − 32 − 18 = 190 livros disponíveis para empréstimo. Os 25 livros comprados ainda não chegaram e não entram na conta.
```

### full: pass

```text
240 − 32 − 18 = 190 livros disponíveis para empréstimo. Os grupos de emprestados e separados para reparo não se sobrepõem. Os 25 livros comprados ainda não chegaram e não estão incluídos nos 240.
```

### ultra: pass

```text
240 − 32 − 18 = 190 livros disponíveis para empréstimo. Os grupos de emprestados e separados para reparo não se sobrepõem. Os 25 comprados ainda não chegaram e não entram na conta.
```

### off: pass

```text
240 − 32 − 18 = 190 livros disponíveis para empréstimo. Os 25 livros comprados ainda não chegaram e não entram nessa conta.
```

## modes-pt-BR-013 · numbers

Source task:

> Simplifique esta nota financeira: “A receita foi de R$ 18.000 em janeiro e R$ 19.800 em fevereiro, um aumento de 10%. Os valores são brutos, antes das taxas. Fevereiro ainda pode sofrer ajuste de até R$ 600; esse ajuste não foi aplicado.”

### baseline: pass

```text
A receita bruta, antes das taxas, subiu de R$ 18.000 em janeiro para R$ 19.800 em fevereiro, um aumento de 10%. O valor de fevereiro ainda pode ter um ajuste de até R$ 600, que não foi aplicado.
```

### lite: pass

```text
A receita foi de R$ 18.000 em janeiro e R$ 19.800 em fevereiro, um aumento de 10%. Os valores são brutos, antes das taxas. O valor de fevereiro ainda pode ser ajustado em até R$ 600; esse ajuste não foi aplicado.
```

### full: pass

```text
A receita bruta, antes das taxas, passou de R$ 18.000 em janeiro para R$ 19.800 em fevereiro: aumento de 10%. O valor de fevereiro ainda pode ter um ajuste de até R$ 600, que não foi aplicado.
```

### ultra: pass

```text
A receita bruta, antes das taxas, passou de R$ 18.000 em janeiro para R$ 19.800 em fevereiro: aumento de 10%. Fevereiro ainda pode ter ajuste de até R$ 600, não aplicado.
```

### off: pass

```text
A receita bruta, antes das taxas, passou de R$ 18.000 em janeiro para R$ 19.800 em fevereiro, um aumento de 10%. O valor de fevereiro ainda pode ser ajustado em até R$ 600. Esse ajuste não foi aplicado.
```

## modes-pt-BR-014 · numbers

Source task:

> O orçamento máximo é R$ 1.150. Precisamos de seis bancos de R$ 160 cada e de um frete de R$ 90 para o pedido inteiro. A pintura extra custa R$ 25 por banco, é opcional e não foi pedida. O necessário cabe no orçamento? Dê a conclusão e a conta.

### baseline: pass

```text
Sim, o necessário cabe no orçamento: 6 × R$ 160 + R$ 90 = R$ 1.050. Sobram R$ 100 dos R$ 1.150 disponíveis. A pintura opcional não entra na conta, pois não foi pedida.
```

### lite: pass

```text
Sim, o necessário cabe no orçamento: 6 × R$ 160 + R$ 90 = R$ 1.050. Sobram R$ 100 do limite de R$ 1.150. A pintura extra de R$ 25 por banco é opcional, não foi pedida e não entra na conta.
```

### full: pass

```text
Sim. O necessário custa 6 × R$ 160 + R$ 90 de frete para o pedido inteiro = R$ 1.050. Sobram R$ 100 do orçamento máximo de R$ 1.150. A pintura extra de R$ 25 por banco é opcional, não foi pedida e não entra na conta.
```

### ultra: pass

```text
Sim. Seis bancos e o frete único custam 6 × R$ 160 + R$ 90 = R$ 1.050, deixando R$ 100 do orçamento de R$ 1.150. A pintura de R$ 25 por banco é opcional, não foi pedida e fica fora da conta.
```

### off: pass

```text
Sim, o necessário cabe no orçamento.

6 × R$ 160 + R$ 90 = R$ 1.050.
R$ 1.150 − R$ 1.050 = R$ 100 de sobra.

A pintura extra, de R$ 25 por banco, é opcional, não foi pedida e não entra na conta.
```

## modes-pt-BR-015 · numbers

Source task:

> Compare o consumo diário: o escritório usou 220 kWh em 22 dias de trabalho em março e 200 kWh em 20 dias em abril. Os dois meses tiveram média de 10 kWh por dia de trabalho. Não há registro do número de pessoas presentes. Explique a diferença entre total e média.

### baseline: pass

```text
O total foi maior em março: 220 kWh, contra 200 kWh em abril. Mas março teve mais dias de trabalho. A média diária foi igual: 220 ÷ 22 = 10 kWh em março e 200 ÷ 20 = 10 kWh em abril. O total mostra o consumo acumulado no mês; a média mostra o consumo por dia de trabalho. Sem o número de pessoas presentes, não é possível comparar o consumo por pessoa.
```

### lite: pass

```text
O consumo total foi de 220 kWh em março e 200 kWh em abril. A média por dia de trabalho foi igual: 220 ÷ 22 = 10 kWh em março e 200 ÷ 20 = 10 kWh em abril. Março teve um total maior porque teve mais dias de trabalho, não porque a média diária aumentou. Sem registro do número de pessoas presentes, não é possível comparar o consumo por pessoa.
```

### full: pass

```text
O consumo total foi maior em março: 220 kWh, contra 200 kWh em abril. Mas a média por dia de trabalho foi igual:

- Março: 220 ÷ 22 = 10 kWh por dia de trabalho.
- Abril: 200 ÷ 20 = 10 kWh por dia de trabalho.

O total soma o consumo do mês; a média divide esse total pelos dias de trabalho. Março teve dois dias de trabalho a mais, sem aumento da média diária. Como não há registro do número de pessoas presentes, não é possível comparar o consumo por pessoa.
```

### ultra: pass

```text
O total caiu de 220 kWh em março para 200 kWh em abril, mas a média diária não mudou: 220 ÷ 22 = 10 e 200 ÷ 20 = 10 kWh por dia de trabalho. Abril teve dois dias de trabalho a menos, por isso o total foi menor. Sem registro de pessoas presentes, não é possível comparar o consumo por pessoa.
```

### off: pass

```text
O consumo total foi maior em março: 220 kWh, contra 200 kWh em abril. Porém, março teve 22 dias de trabalho e abril teve 20.

A média diária foi igual nos dois meses:
Março: 220 ÷ 22 = 10 kWh por dia de trabalho.
Abril: 200 ÷ 20 = 10 kWh por dia de trabalho.

O total soma o consumo de todos os dias; a média divide esse total pelo número de dias de trabalho. Assim, abril teve um total menor, mas não uma média diária menor. Como não há registro do número de pessoas presentes, não é possível comparar o consumo por pessoa.
```

## modes-pt-BR-016 · numbers

Source task:

> Reescreva o resultado: “O tempo médio de espera foi de 18 minutos, e a mediana foi de 11 minutos. Foram observados 70 atendimentos concluídos. Três esperas superiores a uma hora estão incluídas na média. Pessoas que foram embora antes do atendimento não estão na amostra.”

### baseline: pass

```text
Nos 70 atendimentos concluídos, o tempo médio de espera foi de 18 minutos e a mediana, de 11 minutos. A média inclui três esperas superiores a uma hora. Pessoas que saíram antes de serem atendidas não fazem parte da amostra.
```

### lite: pass

```text
O tempo médio de espera foi de 18 minutos, e a mediana, de 11 minutos. Foram observados 70 atendimentos concluídos. A média inclui três esperas superiores a uma hora. Pessoas que foram embora antes do atendimento não estão na amostra.
```

### full: pass

```text
Nos 70 atendimentos concluídos observados, o tempo médio de espera foi de 18 minutos e a mediana, de 11 minutos. A média inclui três esperas superiores a uma hora. Pessoas que foram embora antes do atendimento não estão na amostra.
```

### ultra: pass

```text
Nos 70 atendimentos concluídos observados, a espera média foi de 18 minutos e a mediana, de 11 minutos. A média inclui três esperas superiores a uma hora. A amostra exclui pessoas que foram embora antes do atendimento.
```

### off: pass

```text
Nos 70 atendimentos concluídos observados, o tempo médio de espera foi de 18 minutos, e a mediana foi de 11 minutos. A média inclui três esperas superiores a uma hora. Pessoas que foram embora antes do atendimento não fazem parte da amostra.
```

## modes-pt-BR-017 · numbers

Source task:

> Responda só à comparação das taxas. No curso A, 24 de 40 inscritos concluíram. No curso B, 30 de 60 concluíram. Qual teve a maior taxa de conclusão? Não conclua qual curso é melhor.

### baseline: pass

```text
O curso A teve a maior taxa de conclusão: 60% (24 de 40), contra 50% (30 de 60) no curso B.
```

### lite: pass

```text
O curso A teve a maior taxa de conclusão: 60% (24 de 40), contra 50% no curso B (30 de 60).
```

### full: pass

```text
O curso A teve a maior taxa de conclusão: 60% (24 de 40 inscritos), contra 50% no curso B (30 de 60).
```

### ultra: pass

```text
O curso A teve a maior taxa de conclusão: 60% (24 de 40), contra 50% (30 de 60) no curso B.
```

### off: pass

```text
O curso A teve a maior taxa de conclusão: 60% (24 de 40), contra 50% no curso B (30 de 60).
```

## modes-pt-BR-018 · numbers

Source task:

> Edite para o cliente: “Estimamos de 2 a 4 horas para digitalizar cerca de 600 páginas nas condições do teste. Isso não é um prazo máximo. Páginas danificadas ou formatos diferentes não foram testados. O volume se refere a páginas, não a folhas.”

### baseline: pass

```text
Estimamos entre 2 e 4 horas para digitalizar cerca de 600 páginas nas condições do teste. Essa estimativa não representa um prazo máximo. Páginas danificadas ou de formatos diferentes não foram testadas. O volume informado corresponde a páginas, não a folhas.
```

### lite: pass

```text
Estimamos de 2 a 4 horas para digitalizar cerca de 600 páginas nas condições do teste. Essa estimativa não é um prazo máximo. Páginas danificadas ou formatos diferentes não foram testados. O volume se refere a páginas, não a folhas.
```

### full: pass

```text
Estimamos de 2 a 4 horas para digitalizar cerca de 600 páginas nas condições do teste. Essa estimativa não é um prazo máximo. Páginas danificadas ou formatos diferentes não foram testados. O volume se refere a páginas, não a folhas.
```

### ultra: pass

```text
Estimamos de 2 a 4 horas para digitalizar cerca de 600 páginas nas condições do teste; isso não é um prazo máximo. Não testamos páginas danificadas nem formatos diferentes. O volume é de páginas, não de folhas.
```

### off: pass

```text
Estimamos de 2 a 4 horas para digitalizar cerca de 600 páginas nas condições do teste. Essa estimativa não representa um prazo máximo. Não foram testadas páginas danificadas nem formatos diferentes. O volume indicado se refere a páginas, não a folhas.
```

## modes-pt-BR-019 · numbers

Source task:

> Escreva uma nota sem avaliar segurança: foi medido 1,6 mg/L de nitrato em uma única amostra retirada da torneira da cozinha às 8h. O limite de quantificação do laboratório é 0,2 mg/L. Não foi fornecido limite aplicável de segurança nem resultado de outras torneiras.

### baseline: pass

```text
Foi medida uma concentração de nitrato de 1,6 mg/L em uma única amostra coletada na torneira da cozinha às 8h. O limite de quantificação do laboratório é de 0,2 mg/L. Não foram fornecidos um limite aplicável de segurança nem resultados de outras torneiras.
```

### lite: pass

```text
Foi medido 1,6 mg/L de nitrato em uma única amostra retirada da torneira da cozinha às 8h. O limite de quantificação do laboratório é 0,2 mg/L. Não foi fornecido limite aplicável de segurança nem resultado de outras torneiras.
```

### full: pass

```text
Foi medido 1,6 mg/L de nitrato em uma única amostra retirada da torneira da cozinha às 8h. O limite de quantificação do laboratório é 0,2 mg/L. Não foram fornecidos um limite aplicável de segurança nem resultados de outras torneiras.
```

### ultra: pass

```text
Foi medido 1,6 mg/L de nitrato em uma única amostra retirada da torneira da cozinha às 8h. O limite de quantificação do laboratório é 0,2 mg/L. Não foram fornecidos limite aplicável de segurança nem resultados de outras torneiras.
```

### off: pass

```text
Foi medida uma concentração de nitrato de 1,6 mg/L em uma única amostra retirada da torneira da cozinha às 8h. O limite de quantificação do laboratório é de 0,2 mg/L. Não foram fornecidos um limite aplicável de segurança nem resultados de outras torneiras.
```

## modes-pt-BR-020 · numbers

Source task:

> Corrija a porcentagem em uma ou duas frases: “Vieram 21 dos 140 associados convidados, então a presença foi de 21%.” Todos os convidados eram associados; acompanhantes não foram contados.

### baseline: pass

```text
Compareceram 21 dos 140 associados convidados, portanto a presença foi de 15%, não de 21%. Acompanhantes não foram contados.
```

### lite: pass

```text
Vieram 21 dos 140 associados convidados, então a presença foi de 15%. Todos os convidados eram associados; acompanhantes não foram contados.
```

### full: pass

```text
Vieram 21 dos 140 associados convidados, portanto a presença foi de 15%, não 21%. Todos os convidados eram associados; acompanhantes não foram contados.
```

### ultra: pass

```text
Vieram 21 dos 140 associados convidados: a presença foi de 15%, não 21%. Todos os convidados eram associados; acompanhantes não foram contados.
```

### off: pass

```text
Compareceram 21 dos 140 associados convidados, portanto a presença foi de 15%, não 21%. Todos os convidados eram associados, e acompanhantes não foram contados.
```

## modes-pt-BR-021 · conditions

Source task:

> Reescreva a regra: “Você pode trocar o horário pelo aplicativo somente se faltarem mais de 24 horas e se houver vaga na outra turma. Se qualquer condição não for atendida, procure a secretaria. Usar o aplicativo continua sendo opcional.”

### baseline: pass

```text
A troca de horário pelo aplicativo é opcional e só pode ser feita se faltarem mais de 24 horas e houver vaga na outra turma. Se uma dessas condições não for atendida, procure a secretaria.
```

### lite: pass

```text
Você pode trocar o horário pelo aplicativo somente se faltarem mais de 24 horas e houver vaga na outra turma. Se qualquer uma dessas condições não for atendida, procure a secretaria. O uso do aplicativo continua sendo opcional.
```

### full: pass

```text
Você pode trocar o horário pelo aplicativo apenas se faltarem mais de 24 horas e houver vaga na outra turma. Se uma dessas condições não for atendida, procure a secretaria. O uso do aplicativo é opcional.
```

### ultra: pass

```text
A troca de horário pelo aplicativo é opcional e só pode ser feita se faltarem mais de 24 horas e houver vaga na outra turma. Se uma dessas condições não for atendida, procure a secretaria.
```

### off: pass

```text
Você pode trocar o horário pelo aplicativo apenas quando faltarem mais de 24 horas e houver vaga na outra turma. Se uma dessas condições não for atendida, procure a secretaria. O uso do aplicativo é opcional.
```

## modes-pt-BR-022 · conditions

Source task:

> Explique esta política fornecida, sem acrescentar direitos não citados: peças sem uso podem ser trocadas em até 10 dias corridos após o recebimento. Peças usadas só podem ser trocadas se o defeito de fabricação for confirmado. Em ambos os casos, o cliente deve pedir um código antes do envio. O frete não é automaticamente reembolsado.

### baseline: pass

```text
Peças sem uso podem ser trocadas em até 10 dias corridos após o recebimento. Para peças usadas, a troca só é permitida se o defeito de fabricação for confirmado. Nos dois casos, o cliente precisa solicitar um código antes de enviar a peça. O frete não é reembolsado automaticamente.
```

### lite: pass

```text
Peças sem uso podem ser trocadas em até 10 dias corridos após o recebimento. Peças usadas só podem ser trocadas se o defeito de fabricação for confirmado. Nos dois casos, o cliente deve pedir um código antes de enviar a peça. O frete não é reembolsado automaticamente.
```

### full: pass

```text
Peças sem uso podem ser trocadas em até 10 dias corridos após o recebimento. Peças usadas só podem ser trocadas se houver confirmação de defeito de fabricação.

Nos dois casos, o cliente deve pedir um código antes de enviar a peça. O frete não é reembolsado automaticamente.
```

### ultra: pass

```text
Peças sem uso podem ser trocadas em até 10 dias corridos após o recebimento. Peças usadas só podem ser trocadas com defeito de fabricação confirmado. Nos dois casos, o cliente deve pedir um código antes do envio. O frete não é automaticamente reembolsado.
```

### off: pass

```text
Peças sem uso podem ser trocadas em até 10 dias corridos após o recebimento. Para peças usadas, a troca só é permitida se o defeito de fabricação for confirmado. Em qualquer um dos casos, o cliente deve solicitar um código antes de enviar a peça. O frete não é reembolsado automaticamente.
```

## modes-pt-BR-023 · conditions

Source task:

> Encurte a instrução: “Não desligue o leitor enquanto o envio não tiver terminado ou a luz ainda estiver vermelha. Ele só pode ser desligado quando o envio terminar e a luz ficar verde. Você pode deixar a tela aberta depois disso.”

### baseline: pass

```text
Só desligue o leitor quando o envio terminar e a luz estiver verde. Depois disso, a tela pode ficar aberta.
```

### lite: pass

```text
Só desligue o leitor quando o envio terminar e a luz ficar verde. Depois disso, você pode deixar a tela aberta.
```

### full: pass

```text
Só desligue o leitor após o envio terminar e a luz ficar verde. Não o desligue enquanto o envio estiver em andamento ou a luz estiver vermelha. Depois disso, você pode deixar a tela aberta.
```

### ultra: pass

```text
Só desligue o leitor quando o envio terminar e a luz ficar verde; não desligue enquanto a luz estiver vermelha. Depois disso, você pode deixar a tela aberta.
```

### off: pass

```text
Só desligue o leitor quando o envio terminar e a luz ficar verde. Depois disso, você pode deixar a tela aberta.
```

## modes-pt-BR-024 · conditions

Source task:

> Organize estas regras de oficina: menores de 9 anos devem estar com um adulto. Pessoas de 9 a 14 anos podem ficar sem acompanhante apenas com autorização escrita. Pessoas de 15 anos ou mais não precisam dessa autorização. O acompanhante também precisa reservar lugar.

### baseline: pass

```text
- Menores de 9 anos: devem estar acompanhados de um adulto.
- De 9 a 14 anos: podem ficar sem acompanhante apenas com autorização escrita.
- A partir de 15 anos: não precisam dessa autorização.
- O acompanhante também deve reservar lugar.
```

### lite: pass

```text
- Menores de 9 anos devem estar com um adulto.
- Pessoas de 9 a 14 anos podem ficar sem acompanhante apenas com autorização escrita.
- Pessoas de 15 anos ou mais não precisam dessa autorização.
- O acompanhante também precisa reservar lugar.
```

### full: pass

```text
- Menores de 9 anos devem estar acompanhados de um adulto.
- Pessoas de 9 a 14 anos só podem ficar sem acompanhante com autorização escrita.
- Pessoas de 15 anos ou mais não precisam dessa autorização.
- O acompanhante também precisa reservar lugar.
```

### ultra: pass

```text
- Menores de 9 anos: devem estar com um adulto.
- De 9 a 14 anos: podem ficar sem acompanhante apenas com autorização escrita.
- A partir de 15 anos: não precisam dessa autorização.
- O acompanhante também precisa reservar lugar.
```

### off: pass

```text
- Menores de 9 anos devem estar acompanhados de um adulto.
- Pessoas de 9 a 14 anos só podem ficar sem acompanhante com autorização escrita.
- Pessoas de 15 anos ou mais não precisam dessa autorização.
- O acompanhante também deve reservar lugar.
```

## modes-pt-BR-025 · conditions

Source task:

> Reescreva para a equipe: “A escala extra pode ter até três voluntários habilitados. Quem já está escalado no turno seguinte não pode participar. A inscrição como voluntário não garante vaga, e a chefia pode decidir não abrir a escala.”

### baseline: pass

```text
A escala extra pode contar com até três voluntários habilitados. Quem já estiver escalado no turno seguinte não pode participar. A inscrição não garante vaga, e a chefia pode optar por não abrir a escala.
```

### lite: pass

```text
A escala extra pode ter até três voluntários habilitados. Quem já está escalado no turno seguinte não pode participar. A inscrição como voluntário não garante vaga, e a chefia pode decidir não abrir a escala.
```

### full: pass

```text
A escala extra pode ter até três voluntários habilitados. Quem já está escalado no turno seguinte não pode participar. A inscrição não garante vaga, e a chefia pode decidir não abrir a escala.
```

### ultra: pass

```text
A escala extra pode ter até três voluntários habilitados. Quem já está escalado no turno seguinte não pode participar. A inscrição não garante vaga, e a chefia pode decidir não abrir a escala.
```

### off: pass

```text
A escala extra pode contar com até três voluntários habilitados. Quem já estiver escalado para o turno seguinte não pode participar. A inscrição como voluntário não garante vaga, e a chefia pode decidir não abrir a escala.
```

## modes-pt-BR-026 · conditions

Source task:

> Pela regra interna fictícia, a revisão é obrigatória após qualquer mudança de posição do equipamento, exceto mudanças inferiores a 20 cm dentro da mesma área marcada. A mudança proposta é de 20 cm na mesma área. A revisão pode ser dispensada? Use o limite exato do texto.

### baseline: pass

```text
Não. A dispensa vale apenas para mudanças inferiores a 20 cm dentro da mesma área marcada. Uma mudança de exatamente 20 cm exige revisão.
```

### lite: pass

```text
Não. A exceção vale apenas para mudanças inferiores a 20 cm dentro da mesma área marcada. Como a mudança é de exatamente 20 cm, a revisão é obrigatória.
```

### full: pass

```text
Não. A exceção vale apenas para mudanças inferiores a 20 cm dentro da mesma área marcada. Uma mudança de exatamente 20 cm exige revisão.
```

### ultra: pass

```text
Não. A exceção vale apenas para mudanças inferiores a 20 cm na mesma área marcada. Uma mudança de exatamente 20 cm exige revisão.
```

### off: pass

```text
Não. A exceção vale apenas para mudanças inferiores a 20 cm dentro da mesma área marcada. Como a mudança é de exatamente 20 cm, a revisão é obrigatória.
```

## modes-pt-BR-027 · conditions

Source task:

> Reescreva: “A matrícula se confirma quando o pagamento é compensado. O comprovante enviado não confirma a matrícula por si só. Os documentos devem chegar antes da primeira aula, mas não são necessários para processar o pagamento. Se o pagamento falhar, a vaga fica reservada por mais 48 horas.”

### baseline: pass

```text
A matrícula só é confirmada quando o pagamento é compensado. Enviar o comprovante, por si só, não confirma a matrícula. Os documentos devem chegar antes da primeira aula, mas o pagamento pode ser processado sem eles. Se o pagamento falhar, a vaga continuará reservada por mais 48 horas.
```

### lite: pass

```text
A matrícula é confirmada quando o pagamento é compensado. O comprovante enviado, por si só, não confirma a matrícula. Os documentos devem chegar antes da primeira aula, mas não são necessários para processar o pagamento. Se o pagamento falhar, a vaga fica reservada por mais 48 horas.
```

### full: pass

```text
A matrícula é confirmada quando o pagamento é compensado. O envio do comprovante, por si só, não confirma a matrícula. Os documentos devem chegar antes da primeira aula, mas não são necessários para processar o pagamento. Se o pagamento falhar, a vaga fica reservada por mais 48 horas.
```

### ultra: pass

```text
A matrícula só se confirma quando o pagamento é compensado; o comprovante enviado, por si só, não a confirma. Os documentos devem chegar antes da primeira aula, mas não são necessários para processar o pagamento. Se o pagamento falhar, a vaga permanece reservada por mais 48 horas.
```

### off: pass

```text
A matrícula é confirmada quando o pagamento é compensado. O envio do comprovante, por si só, não confirma a matrícula. Os documentos devem chegar antes da primeira aula, mas não são necessários para processar o pagamento. Se o pagamento falhar, a vaga continuará reservada por mais 48 horas.
```

## modes-pt-BR-028 · conditions

Source task:

> Simplifique esta cláusula fictícia sem aconselhamento jurídico: relatórios preliminares não podem ser compartilhados fora da comissão sem autorização escrita da pessoa autora. Mesmo com autorização, os telefones pessoais devem ser retirados. Totais sem nomes podem ser enviados ao setor de planejamento.

### baseline: pass

```text
Relatórios preliminares só podem ser compartilhados fora da comissão com autorização escrita da pessoa autora. Mesmo com autorização, os telefones pessoais devem ser removidos. Totais sem nomes podem ser enviados ao setor de planejamento.
```

### lite: pass

```text
Relatórios preliminares só podem ser compartilhados fora da comissão com autorização escrita da pessoa autora. Mesmo com autorização, os telefones pessoais devem ser retirados. Totais sem nomes podem ser enviados ao setor de planejamento.
```

### full: pass

```text
Relatórios preliminares só podem ser compartilhados fora da comissão com autorização escrita da pessoa autora. Mesmo com autorização, os telefones pessoais devem ser retirados. Totais sem nomes podem ser enviados ao setor de planejamento.
```

### ultra: pass

```text
Relatórios preliminares só podem ser compartilhados fora da comissão com autorização escrita da pessoa autora. Mesmo com autorização, os telefones pessoais devem ser retirados. Totais sem nomes podem ser enviados ao setor de planejamento.
```

### off: pass

```text
Relatórios preliminares só podem ser compartilhados fora da comissão com autorização escrita da pessoa autora. Mesmo com essa autorização, os telefones pessoais devem ser retirados. Totais sem nomes podem ser enviados ao setor de planejamento.
```

## modes-pt-BR-029 · conditions

Source task:

> Reescreva o aviso: “O pedido deve ser recebido até as 16h UTC de 8 de junho de 2029. O envio antes do prazo não basta se o recebimento ocorrer depois. Os anexos podem chegar até dois dias úteis após um pedido recebido no prazo.”

### baseline: pass

```text
O pedido deve ser recebido até as 16h UTC de 8 de junho de 2029. Não basta enviá-lo antes do prazo: ele também precisa ser recebido no prazo. Se o pedido for recebido no prazo, os anexos podem chegar até dois dias úteis depois.
```

### lite: pass

```text
O pedido deve ser recebido até as 16h UTC de 8 de junho de 2029. Enviar antes do prazo não basta se o recebimento ocorrer depois. Os anexos podem chegar até dois dias úteis após um pedido recebido no prazo.
```

### full: pass

```text
O pedido deve ser recebido até as 16h UTC de 8 de junho de 2029. Não basta enviá-lo antes do prazo: ele também deve ser recebido no prazo. Os anexos podem chegar até dois dias úteis após um pedido recebido no prazo.
```

### ultra: pass

```text
O pedido deve ser recebido até as 16h UTC de 8 de junho de 2029. Enviá-lo antes do prazo não basta se ele for recebido depois. Os anexos podem chegar até dois dias úteis após o recebimento do pedido, desde que ele tenha sido recebido no prazo.
```

### off: pass

```text
O pedido deve ser recebido até as 16h UTC de 8 de junho de 2029. Não basta enviá-lo antes do prazo: ele também precisa ser recebido no prazo. Se o pedido for recebido no prazo, os anexos podem chegar até dois dias úteis depois.
```

## modes-pt-BR-030 · conditions

Source task:

> Responda somente qual entrada pode ser usada. A porta lateral pode ser usada quando o palco está vazio. A porta frontal pode ser usada a qualquer momento, exceto durante gravações. Agora o palco está vazio e há uma gravação em andamento.

### baseline: pass

```text
A porta lateral.
```

### lite: pass

```text
A porta lateral.
```

### full: pass

```text
A porta lateral.
```

### ultra: pass

```text
A porta lateral.
```

### off: pass

```text
A porta lateral.
```

## modes-pt-BR-031 · technical

Source task:

> Reescreva a nota da versão 5.1: o comando `arquivo validar --simular` verifica a configuração sem criar pacote. Uma validação bem-sucedida não confirma espaço livre no destino. O pacote real é criado com `arquivo gerar --executar`. Preserve os comandos.

### baseline: pass

```text
Na versão 5.1, `arquivo validar --simular` verifica a configuração sem criar um pacote. Uma validação bem-sucedida não confirma que há espaço livre no destino. Para criar o pacote real, use `arquivo gerar --executar`.
```

### lite: pass

```text
Na versão 5.1, o comando `arquivo validar --simular` verifica a configuração sem criar um pacote. Uma validação bem-sucedida não confirma espaço livre no destino. Para criar o pacote real, use `arquivo gerar --executar`.
```

### full: pass

```text
Versão 5.1: `arquivo validar --simular` verifica a configuração sem criar pacote. Uma validação bem-sucedida não confirma espaço livre no destino. Para criar o pacote real, use `arquivo gerar --executar`.
```

### ultra: pass

```text
Versão 5.1: `arquivo validar --simular` verifica a configuração sem criar pacote. O sucesso da validação não confirma espaço livre no destino. Para criar o pacote real, use `arquivo gerar --executar`.
```

### off: pass

```text
Na versão 5.1, o comando `arquivo validar --simular` verifica a configuração sem criar um pacote. Uma validação bem-sucedida não confirma que há espaço livre no destino. Para criar o pacote real, use `arquivo gerar --executar`.
```

## modes-pt-BR-032 · technical

Source task:

> Explique para o suporte: a tarefa só é confirmada depois que a transação é gravada. Se o processo parar antes da confirmação, a tarefa pode ser entregue novamente. A deduplicação usa tarefa_id, não o endereço do cliente. Uma nova entrega não prova gravação duplicada.

### baseline: pass

```text
A tarefa só é confirmada após a gravação da transação. Se o processo parar antes da confirmação, ela poderá ser entregue novamente. A deduplicação usa tarefa_id, não o endereço do cliente. Portanto, uma nova entrega não prova que houve gravação duplicada.
```

### lite: pass

```text
A tarefa só é confirmada depois que a transação é gravada. Se o processo parar antes da confirmação, a tarefa pode ser entregue novamente. A deduplicação usa tarefa_id, não o endereço do cliente. Uma nova entrega não prova que houve gravação duplicada.
```

### full: pass

```text
A tarefa só é confirmada depois que a transação é gravada. Se o processo parar antes da confirmação, a tarefa pode ser entregue novamente. A deduplicação usa tarefa_id, não o endereço do cliente. Uma nova entrega não prova que houve gravação duplicada.
```

### ultra: pass

```text
A tarefa só é confirmada após a gravação da transação. Se o processo parar antes da confirmação, ela pode ser entregue novamente. A deduplicação usa tarefa_id, não o endereço do cliente. Uma nova entrega não prova gravação duplicada.
```

### off: pass

```text
A tarefa só é confirmada depois que a transação é gravada. Se o processo parar antes dessa confirmação, a tarefa pode ser entregue novamente. A deduplicação usa tarefa_id, e não o endereço do cliente. Portanto, uma nova entrega não prova que houve gravação duplicada.
```

## modes-pt-BR-033 · technical

Source task:

> Encurte: “O arquivo de backup passou na verificação de checksum, mas nenhuma restauração foi feita. A verificação não prova que o sistema pode ser restaurado. O backup inclui /srv/clientes e não inclui /srv/temporarios.”

### baseline: pass

```text
O backup passou na verificação de checksum, mas não foi restaurado; isso não prova que o sistema pode ser restaurado. Inclui /srv/clientes, mas não /srv/temporarios.
```

### lite: pass

```text
O backup passou na verificação de checksum, mas não foi restaurado. A verificação não prova que o sistema pode ser restaurado. O backup inclui /srv/clientes, mas não /srv/temporarios.
```

### full: pass

```text
O backup passou na verificação de checksum, mas não foi restaurado; a verificação não prova que o sistema pode ser restaurado. Inclui /srv/clientes, mas não /srv/temporarios.
```

### ultra: pass

```text
O backup passou na verificação de checksum, mas não foi restaurado; a verificação não prova que o sistema pode ser restaurado. Inclui /srv/clientes, mas não /srv/temporarios.
```

### off: pass

```text
O backup passou na verificação de checksum, mas não foi testado por restauração; a verificação não prova que o sistema pode ser restaurado. Inclui /srv/clientes, mas não /srv/temporarios.
```

## modes-pt-BR-034 · technical

Source task:

> Calcule a taxa nominal do conteúdo, sem incluir cabeçalhos. O sensor envia uma leitura de 24 bits a cada 500 ms. A nota trata apenas dos bits das leituras; o tamanho dos cabeçalhos não foi informado.

### baseline: pass

```text
A taxa nominal do conteúdo é 24 bits ÷ 0,5 s = 48 bits/s, sem incluir cabeçalhos, cujo tamanho não foi informado.
```

### lite: pass

```text
A taxa nominal do conteúdo é 48 bits/s: 24 bits ÷ 0,5 s. Esse valor inclui apenas os bits das leituras, sem cabeçalhos, cujo tamanho não foi informado.
```

### full: pass

```text
A taxa nominal do conteúdo é 48 bits/s: 24 bits ÷ 0,5 s. O cálculo inclui apenas os bits das leituras, sem cabeçalhos, cujo tamanho não foi informado.
```

### ultra: pass

```text
A taxa nominal do conteúdo é 48 bits/s: 24 bits ÷ 0,5 s. Ela inclui apenas os bits das leituras, sem cabeçalhos, cujo tamanho não foi informado.
```

### off: pass

```text
A taxa nominal do conteúdo é 48 bits/s: 500 ms equivalem a 0,5 s, então 24 bits ÷ 0,5 s = 48 bits/s. O cálculo inclui apenas os bits das leituras, sem cabeçalhos, cujo tamanho não foi informado.
```

## modes-pt-BR-035 · technical

Source task:

> Edite sem sugerir correção: “O tempo de resposta subiu depois da atualização do cache. Os dois eventos ocorreram entre 21h e 21h15 UTC. Não houve comparação de controle. A proximidade no tempo não prova que a atualização causou a lentidão. Não foi decidida uma reversão.”

### baseline: pass

```text
O tempo de resposta aumentou após a atualização do cache. Ambos os eventos ocorreram entre 21h e 21h15 UTC. Sem comparação de controle, a proximidade temporal não prova que a atualização causou a lentidão. Não foi decidida uma reversão.
```

### lite: pass

```text
O tempo de resposta aumentou após a atualização do cache. Os dois eventos ocorreram entre 21h e 21h15 UTC. Não houve comparação de controle. A proximidade no tempo não prova que a atualização causou a lentidão. Não foi decidida uma reversão.
```

### full: pass

```text
O tempo de resposta subiu depois da atualização do cache. Ambos os eventos ocorreram entre 21h e 21h15 UTC. Sem comparação de controle, a proximidade no tempo não prova que a atualização causou a lentidão. Não foi decidida uma reversão.
```

### ultra: pass

```text
O tempo de resposta subiu após a atualização do cache; ambos os eventos ocorreram entre 21h e 21h15 UTC. Sem comparação de controle, a proximidade temporal não prova que a atualização causou a lentidão. Não foi decidida uma reversão.
```

### off: pass

```text
O tempo de resposta aumentou após a atualização do cache. Ambos os eventos ocorreram entre 21h e 21h15 UTC. Não houve comparação de controle, e a proximidade temporal não prova que a atualização causou a lentidão. Não foi decidida uma reversão.
```

## modes-pt-BR-036 · technical

Source task:

> Explique o contrato: no campo apelido, ausência do campo significa manter o valor atual; JSON null significa apagá-lo; uma string vazia é um valor de texto aceito. Essa regra não foi definida para outros campos.

### baseline: pass

```text
Para o campo `apelido`, omitir o campo mantém o valor atual; enviar `null` o apaga; enviar uma string vazia (`""`) define um valor de texto aceito. Essa regra não foi definida para outros campos.
```

### lite: pass

```text
No campo `apelido`:
- Campo ausente: mantém o valor atual.
- JSON `null`: apaga o valor atual.
- String vazia (`""`): é aceita como valor de texto.

Essa regra não foi definida para outros campos.
```

### full: pass

```text
Para o campo `apelido`:
- Campo ausente: mantém o valor atual.
- Valor JSON `null`: apaga o valor atual.
- String vazia (`""`): é aceita como valor de texto.

Essa regra não foi definida para outros campos.
```

### ultra: pass

```text
No campo `apelido`:
- Campo ausente: mantém o valor atual.
- `null` no JSON: apaga o valor.
- String vazia (`""`): é aceita como texto.

Essa regra não foi definida para outros campos.
```

### off: pass

```text
No campo `apelido`, o contrato distingue três situações:
- Campo ausente: mantém o valor atual.
- Valor JSON `null`: apaga o valor atual.
- String vazia (`""`): é aceita como valor de texto.

Essa regra não foi definida para os outros campos.
```

## modes-pt-BR-037 · technical

Source task:

> Reescreva o teste: seis processos simultâneos concluíram 900 tarefas em 60 segundos, ou 15 tarefas por segundo no conjunto. As entradas já estavam em memória. Não foram medidos desempenho de um processo isolado nem leitura inicial de disco.

### baseline: pass

```text
No teste, seis processos simultâneos concluíram 900 tarefas em 60 segundos, totalizando 15 tarefas por segundo no conjunto. As entradas já estavam em memória. Não foram medidos o desempenho de um processo isolado nem a leitura inicial de disco.
```

### lite: pass

```text
Seis processos simultâneos concluíram 900 tarefas em 60 segundos: 15 tarefas por segundo no conjunto. As entradas já estavam em memória. Não foram medidos o desempenho de um processo isolado nem a leitura inicial de disco.
```

### full: pass

```text
Seis processos simultâneos concluíram 900 tarefas em 60 segundos: 15 tarefas por segundo no conjunto. As entradas já estavam em memória. O teste não mediu o desempenho de um processo isolado nem a leitura inicial de disco.
```

### ultra: pass

```text
Seis processos simultâneos concluíram 900 tarefas em 60 segundos: 15 tarefas por segundo no conjunto. As entradas já estavam em memória. Não foram medidos o desempenho de um processo isolado nem a leitura inicial de disco.
```

### off: pass

```text
No teste, seis processos simultâneos concluíram 900 tarefas em 60 segundos, com uma taxa agregada de 15 tarefas por segundo. As entradas já estavam em memória. Não foram medidos o desempenho de um processo isolado nem a leitura inicial de disco.
```

## modes-pt-BR-038 · technical

Source task:

> Resuma a configuração: ttl_dias=0 desativa a exclusão automática, sem apagar tudo imediatamente. Um valor positivo conta dias inteiros desde a criação. A exclusão manual continua disponível. O padrão é 14 e mudanças valem só para novos registros.

### baseline: flagged

```text
O padrão de `ttl_dias` é 14. O valor 0 desativa a exclusão automática, sem apagar tudo imediatamente; valores positivos contam dias inteiros desde a criação. A exclusão manual continua disponível, e mudanças na configuração valem apenas para novos registros.
```

Review notes: Preserva o significado, mas omite a sequência literal protegida `ttl_dias=0`, separando o nome e o valor. / Preserva o significado, mas omite a forma exata do token protegido `ttl_dias=0`.

### lite: pass

```text
`ttl_dias=0` desativa a exclusão automática; não apaga tudo imediatamente. Um valor positivo conta dias inteiros desde a criação. A exclusão manual continua disponível. O padrão é 14, e mudanças valem apenas para novos registros.
```

### full: pass

```text
`ttl_dias=0` desativa a exclusão automática; não apaga tudo imediatamente. Um valor positivo conta dias inteiros desde a criação. A exclusão manual continua disponível. O padrão é 14, e mudanças valem apenas para novos registros.
```

### ultra: pass

```text
`ttl_dias=0` desativa a exclusão automática; não apaga tudo imediatamente. Um valor positivo conta dias inteiros desde a criação. A exclusão manual continua disponível. O padrão é 14, e mudanças valem apenas para novos registros.
```

### off: pass

```text
A configuração `ttl_dias` tem valor padrão de 14. Um valor positivo conta dias inteiros desde a criação do registro; `ttl_dias=0` desativa a exclusão automática, sem apagar tudo imediatamente. A exclusão manual continua disponível. Mudanças na configuração valem apenas para novos registros.
```

## modes-pt-BR-039 · technical

Source task:

> Reescreva para a gerente: o teste autenticou a conta de serviço e verificou que ela consegue conectar. Não autenticou cada usuário e não verificou a permissão de cada pessoa para consultar cada documento. Não transforme conexão bem-sucedida em aprovação dos controles de acesso.

### baseline: pass

```text
O teste autenticou a conta de serviço e confirmou que ela consegue se conectar. Não autenticou cada usuário nem verificou a permissão de cada pessoa para consultar cada documento. Portanto, a conexão bem-sucedida não representa aprovação dos controles de acesso.
```

### lite: pass

```text
O teste autenticou a conta de serviço e confirmou que ela consegue conectar. Não autenticou cada usuário nem verificou a permissão de cada pessoa para consultar cada documento. A conexão bem-sucedida não comprova a aprovação dos controles de acesso.
```

### full: pass

```text
O teste autenticou a conta de serviço e confirmou que ela consegue conectar. Não autenticou cada usuário nem verificou a permissão de cada pessoa para consultar cada documento. A conexão bem-sucedida não comprova a aprovação dos controles de acesso.
```

### ultra: pass

```text
O teste autenticou a conta de serviço e confirmou que ela consegue conectar. Não autenticou cada usuário nem verificou a permissão de cada pessoa para consultar cada documento. A conexão bem-sucedida não comprova a adequação dos controles de acesso.
```

### off: pass

```text
O teste autenticou a conta de serviço e confirmou que ela consegue se conectar. Não autenticou cada usuário nem verificou a permissão de cada pessoa para consultar cada documento. Portanto, a conexão bem-sucedida não representa aprovação dos controles de acesso.
```

## modes-pt-BR-040 · technical

Source task:

> O aviso “atraso: 120 s” prova perda de dados? Ele significa que o último evento aplicado está 120 segundos atrás do último recebido. Os eventos pendentes continuam na fila. Não foi fornecida contagem de falhas nem auditoria de eventos ausentes.

### baseline: pass

```text
Não. O aviso “atraso: 120 s” indica que o último evento aplicado está 120 segundos atrás do último recebido, e os eventos pendentes continuam na fila. Sem contagem de falhas ou auditoria de eventos ausentes, o aviso não comprova perda de dados.
```

### lite: pass

```text
Não. O aviso “atraso: 120 s” significa que o último evento aplicado está 120 segundos atrás do último recebido. Os eventos pendentes continuam na fila. Sem contagem de falhas nem auditoria de eventos ausentes, o aviso não comprova perda de dados — nem permite descartá-la.
```

### full: pass

```text
Não. O aviso “atraso: 120 s” indica que o último evento aplicado está 120 segundos atrás do último recebido. Os eventos pendentes continuam na fila. Sem contagem de falhas ou auditoria de eventos ausentes, o aviso não comprova perda de dados, mas também não permite descartá-la.
```

### ultra: pass

```text
Não. O aviso “atraso: 120 s” indica que o último evento aplicado está 120 segundos atrás do último recebido. Os eventos pendentes continuam na fila. Sem contagem de falhas nem auditoria de eventos ausentes, o aviso não comprova perda de dados nem garante sua ausência.
```

### off: pass

```text
Não. O aviso “atraso: 120 s” significa que o último evento aplicado está 120 segundos atrás do último recebido. Os eventos pendentes continuam na fila. Isso, por si só, não prova perda de dados. Como não foram fornecidas uma contagem de falhas nem uma auditoria de eventos ausentes, também não é possível concluir que não houve perda.
```

## modes-pt-BR-041 · summary

Source task:

> Resuma em três tópicos: a comissão aprovou trocar o piso, desde que a vistoria confirme a necessidade. Rejeitou a compra de cortinas neste semestre. Discutiu o ventilador, sem decidir. Nara vai solicitar orçamentos da vistoria; não há prazo registrado.

### baseline: pass

```text
- A comissão aprovou a troca do piso, condicionada à confirmação da necessidade pela vistoria.
- Rejeitou a compra de cortinas neste semestre e discutiu o ventilador, sem decidir.
- Nara solicitará orçamentos da vistoria; não há prazo registrado.
```

### lite: pass

```text
- A comissão aprovou a troca do piso, desde que a vistoria confirme a necessidade.
- Rejeitou a compra de cortinas neste semestre.
- Discutiu o ventilador, sem decidir. Nara vai solicitar orçamentos da vistoria; não há prazo registrado.
```

### full: pass

```text
- A comissão aprovou a troca do piso, desde que a vistoria confirme a necessidade. Nara solicitará orçamentos da vistoria; não há prazo registrado.
- A compra de cortinas foi rejeitada neste semestre.
- O ventilador foi discutido, mas não houve decisão.
```

### ultra: pass

```text
- A comissão aprovou trocar o piso se a vistoria confirmar a necessidade. Nara solicitará orçamentos da vistoria; não há prazo registrado.
- A compra de cortinas foi rejeitada neste semestre.
- O ventilador foi discutido, sem decisão.
```

### off: pass

```text
- A comissão aprovou a troca do piso, desde que a vistoria confirme a necessidade. Nara solicitará orçamentos da vistoria; não há prazo registrado.
- A compra de cortinas foi rejeitada neste semestre.
- O ventilador foi discutido, mas não houve decisão.
```

## modes-pt-BR-042 · summary

Source task:

> Escreva uma atualização curta para o cliente: a peça quebrada foi recebida hoje. A substituta foi separada, mas ainda não saiu do depósito. O código de rastreio será enviado após a coleta. A coleta é esperada para sexta-feira, mas não foi confirmada pela transportadora. Não foi solicitado envio de outras peças.

### baseline: pass

```text
Recebemos hoje a peça quebrada. A substituta já foi separada, mas ainda não saiu do depósito. A coleta é esperada para sexta-feira, sem confirmação da transportadora; enviaremos o código de rastreio após a coleta. Não foi solicitado o envio de outras peças.
```

### lite: pass

```text
Recebemos a peça quebrada hoje. A substituta foi separada, mas ainda não saiu do depósito. A coleta é esperada para sexta-feira, sem confirmação da transportadora. O código de rastreio será enviado após a coleta. Não foi solicitado envio de outras peças.
```

### full: pass

```text
Recebemos a peça quebrada hoje. A substituta foi separada, mas ainda não saiu do depósito. A coleta é esperada para sexta-feira, sem confirmação da transportadora. O código de rastreio será enviado após a coleta. Não foi solicitado o envio de outras peças.
```

### ultra: pass

```text
Recebemos a peça quebrada hoje. A substituta foi separada, mas ainda não saiu do depósito. A coleta é esperada para sexta-feira, sem confirmação da transportadora. Enviaremos o código de rastreio após a coleta. Não foi solicitado envio de outras peças.
```

### off: pass

```text
Recebemos a peça quebrada hoje. A substituta foi separada, mas ainda não saiu do depósito. A coleta é esperada para sexta-feira, porém ainda não foi confirmada pela transportadora. O código de rastreio será enviado após a coleta. Não foi solicitado o envio de outras peças.
```

## modes-pt-BR-043 · summary

Source task:

> Resuma a revisão: foram analisados 50 cadastros escolhidos aleatoriamente entre os recebidos em maio. Oito estavam sem data de autorização, e dois desses oito também estavam sem assinatura. Nenhum cadastro de abril ou junho foi examinado. Ausência do registro não prova ausência de autorização.

### baseline: pass

```text
A revisão analisou 50 cadastros escolhidos aleatoriamente entre os recebidos em maio. Oito não tinham data de autorização; desses, dois também não tinham assinatura. Nenhum cadastro de abril ou junho foi examinado. A ausência do registro não prova ausência de autorização.
```

### lite: pass

```text
Foram analisados 50 cadastros escolhidos aleatoriamente entre os recebidos em maio. Oito estavam sem data de autorização; dois desses oito também estavam sem assinatura. Nenhum cadastro de abril ou junho foi examinado. A ausência do registro não prova ausência de autorização.
```

### full: pass

```text
Foram analisados 50 cadastros escolhidos aleatoriamente entre os recebidos em maio. Oito não tinham data de autorização; dois desses oito também não tinham assinatura. Nenhum cadastro de abril ou junho foi examinado. A ausência do registro não prova ausência de autorização.
```

### ultra: pass

```text
Foram analisados 50 cadastros escolhidos aleatoriamente entre os recebidos em maio. Oito não tinham data de autorização; desses, dois também não tinham assinatura. Nenhum cadastro de abril ou junho foi examinado. A ausência do registro não prova ausência de autorização.
```

### off: pass

```text
Foram analisados 50 cadastros escolhidos aleatoriamente entre os recebidos em maio. Oito não tinham data de autorização; dois desses oito também não tinham assinatura. Nenhum cadastro de abril ou junho foi examinado. A ausência do registro não prova ausência de autorização.
```

## modes-pt-BR-044 · summary

Source task:

> Faça um comunicado curto e completo: o viveiro abre em 17 de agosto de 2029 se a vistoria da passarela for aprovada. Se não for, uma nova data será anunciada; ainda não há alternativa. A entrada é gratuita, visitas guiadas exigem reserva e a loja ficará fechada no primeiro dia.

### baseline: pass

```text
O viveiro abrirá em 17 de agosto de 2029 se a vistoria da passarela for aprovada. Caso contrário, uma nova data será anunciada; ainda não há alternativa definida. A entrada é gratuita, as visitas guiadas exigem reserva e a loja ficará fechada no primeiro dia.
```

### lite: pass

```text
O viveiro abre em 17 de agosto de 2029 se a vistoria da passarela for aprovada. Caso contrário, uma nova data será anunciada; ainda não há data alternativa. A entrada é gratuita. Visitas guiadas exigem reserva, e a loja ficará fechada no primeiro dia.
```

### full: pass

```text
O viveiro abrirá em 17 de agosto de 2029 se a vistoria da passarela for aprovada. Caso contrário, uma nova data será anunciada; ainda não há data alternativa. A entrada é gratuita, as visitas guiadas exigem reserva e a loja ficará fechada no primeiro dia.
```

### ultra: pass

```text
O viveiro abre em 17 de agosto de 2029 se a vistoria da passarela for aprovada. Caso contrário, uma nova data será anunciada; ainda não há data alternativa. A entrada é gratuita, visitas guiadas exigem reserva e a loja ficará fechada no primeiro dia.
```

### off: pass

```text
O viveiro abrirá em 17 de agosto de 2029 se a vistoria da passarela for aprovada. Caso não seja, uma nova data será anunciada; ainda não há data alternativa. A entrada é gratuita, as visitas guiadas exigem reserva e a loja ficará fechada no primeiro dia.
```

## modes-pt-BR-045 · summary

Source task:

> Resuma apenas o resultado da auditoria: foram revisadas notas acima de R$ 800 do último trimestre, sem incluir reembolsos de viagem. Sete das 84 notas não tinham código de aprovação. Não se verificou se houve aprovação verbal. A responsável por compras vai conferir os códigos.

### baseline: flagged

```text
Das 84 notas acima de R$ 800 do último trimestre revisadas, excluídos os reembolsos de viagem, sete não tinham código de aprovação. Não se verificou se houve aprovação verbal. A responsável por compras conferirá os códigos.
```

Review notes: Fiel aos fatos e invariantes, mas inclui encaminhamento futuro apesar do pedido de resumir apenas o resultado. / Preserva os invariantes, mas inclui uma ação futura além do escopo explícito de resumir apenas o resultado.

### lite: flagged

```text
Das 84 notas acima de R$ 800 do último trimestre revisadas, sete não tinham código de aprovação. Reembolsos de viagem não foram incluídos. Não se verificou se houve aprovação verbal.
```

Review notes: Preserva escopo, contagem e limite da auditoria. A ação futura omitida não integra o resultado estritamente solicitado. / Omite a ação futura do invariante 3, mas ela não integra o resultado solicitado; o escopo autoritativo pede apenas o resultado.

### full: flagged

```text
Das 84 notas acima de R$ 800 do último trimestre revisadas, excluindo reembolsos de viagem, sete não tinham código de aprovação. Não se verificou se houve aprovação verbal.
```

Review notes: Preserva integralmente o resultado solicitado. O encaminhamento omitido está fora do escopo autoritativo de resumir apenas o resultado. / Resume apenas o resultado, como solicitado; a parte ausente do invariante 3 é uma ação futura.

### ultra: flagged

```text
Das 84 notas acima de R$ 800 do último trimestre revisadas, excluindo reembolsos de viagem, sete não tinham código de aprovação. Não se verificou se houve aprovação verbal.
```

Review notes: Mantém todos os achados pertinentes ao resultado; a omissão do encaminhamento respeita o escopo restrito solicitado. / A ação futura do invariante 3 está ausente, conforme o escopo autoritativo limitado ao resultado.

### off: flagged

```text
Das 84 notas acima de R$ 800 do último trimestre revisadas, excluindo reembolsos de viagem, sete não tinham código de aprovação. Não se verificou se houve aprovação verbal.
```

Review notes: Resumo fiel apenas do resultado. A parte ausente do terceiro invariante é uma ação futura, excluída pelo escopo pedido. / Preserva integralmente o resultado solicitado; a ação futura ausente está fora desse escopo.

## modes-pt-BR-046 · analysis

Source task:

> Compare somente o custo mensal informado para 18 usuários. O plano Lago custa R$ 22 por usuário, sem mínimo. O plano Serra custa R$ 350 por mês para até 20 usuários. Os dois têm os recursos necessários. Não há dados de qualidade. Qual custa menos para esse grupo?

### baseline: pass

```text
O plano Serra custa menos: R$ 350 por mês para 18 usuários. O Lago custa 18 × R$ 22 = R$ 396 por mês. A economia com o Serra é de R$ 46 mensais.
```

### lite: pass

```text
O plano Serra custa menos para 18 usuários: R$ 350 por mês, contra R$ 396 do Lago (18 × R$ 22). A diferença é de R$ 46 por mês.
```

### full: pass

```text
O plano Serra custa menos para 18 usuários: R$ 350 por mês, contra R$ 396 do Lago (18 × R$ 22). A economia mensal é de R$ 46.
```

### ultra: pass

```text
O Serra custa menos: R$ 350 por mês para 18 usuários. O Lago custa 18 × R$ 22 = R$ 396. A diferença é de R$ 46 por mês.
```

### off: pass

```text
O plano Serra custa menos para 18 usuários: R$ 350 por mês, contra R$ 396 do Lago (18 × R$ 22). A diferença é de R$ 46 por mês.
```

## modes-pt-BR-047 · analysis

Source task:

> A gerente atribui a queda de erros a um curso opcional: 25 participantes cometeram 5 erros, e 25 não participantes cometeram 11. Cada pessoa decidiu se faria o curso; a experiência anterior não foi medida. Explique o que a comparação mostra e por que não prova a causa.

### baseline: pass

```text
A comparação mostra menos erros entre os participantes: 5, contra 11 entre os não participantes, em grupos de 25 pessoas. Isso indica uma associação, mas não prova que o curso causou a diferença. Como cada pessoa decidiu participar e a experiência anterior não foi medida, os grupos podem ter diferenças prévias que expliquem o resultado.
```

### lite: pass

```text
Os 25 participantes cometeram 5 erros, enquanto os 25 não participantes cometeram 11. A comparação mostra menos erros entre os participantes, mas não prova que o curso causou a diferença. Cada pessoa decidiu se faria o curso, e a experiência anterior não foi medida. Assim, os grupos podem ter diferenças que expliquem o resultado.
```

### full: flagged

```text
Os 25 participantes cometeram 5 erros, contra 11 entre os 25 não participantes. A comparação mostra menos erros no grupo que fez o curso, mas não prova que o curso causou essa diferença.

Cada pessoa decidiu se participaria, e a experiência anterior não foi medida. Assim, os grupos podem ter diferenças prévias que expliquem o resultado. Também não há uma medida anterior de erros para demonstrar uma queda.
```

Review notes: Explica corretamente a associação e os limites causais, mas acrescenta uma ausência de medição não estabelecida pela fonte. / Preserva os invariantes, mas acrescenta ausência de medição anterior como fato não estabelecido.

### ultra: pass

```text
Os 25 participantes cometeram 5 erros, contra 11 dos 25 não participantes. A comparação mostra menos erros entre participantes, mas não prova que o curso causou a diferença: a participação foi voluntária e a experiência anterior não foi medida. Os grupos podem ter diferenças que expliquem o resultado.
```

### off: pass

```text
Os 25 participantes cometeram 5 erros, enquanto os 25 não participantes cometeram 11. A comparação mostra menos erros no grupo que participou, mas não prova que o curso causou essa diferença. Cada pessoa decidiu se faria o curso, portanto os grupos podem ter diferenças anteriores à participação. Como a experiência anterior não foi medida, ela também pode ajudar a explicar o resultado.
```

## modes-pt-BR-048 · analysis

Source task:

> Os pedidos confirmados exigem 120 embalagens. Há 50 utilizáveis em estoque. A chefia permite até 15 de reserva extra, mas não exige essa reserva. Não há pedido mínimo do fornecedor informado. O texto sustenta comprar 150 hoje? Separe necessidade confirmada e reserva opcional.

### baseline: pass

```text
Não. A necessidade confirmada de compra é de 70 embalagens: 120 exigidas menos 50 utilizáveis em estoque. A reserva opcional permite comprar até 15 adicionais, totalizando até 85. Sem pedido mínimo informado, o texto não sustenta comprar 150 hoje.
```

### lite: pass

```text
Não. A necessidade confirmada é comprar 70 embalagens: os pedidos exigem 120, e há 50 utilizáveis em estoque. A reserva opcional permite comprar até 15 adicionais, totalizando até 85. Ela não é obrigatória. Sem pedido mínimo informado, o texto não sustenta comprar 150 hoje.
```

### full: pass

```text
Não. A necessidade confirmada é comprar 70 embalagens: 120 exigidas pelos pedidos menos 50 utilizáveis em estoque.

A reserva é opcional, de até 15 embalagens extras. Portanto, a compra pode chegar a 85 se essa reserva for escolhida, mas ela não é obrigatória. Sem pedido mínimo informado, o texto não sustenta comprar 150 hoje.
```

### ultra: pass

```text
Não. A necessidade confirmada é comprar 70 embalagens: 120 exigidas menos 50 utilizáveis em estoque. A reserva opcional permite acrescentar até 15, totalizando até 85 na compra. Sem pedido mínimo informado, o texto não sustenta comprar 150 hoje.
```

### off: pass

```text
Não. A necessidade confirmada é comprar 70 embalagens: os pedidos exigem 120 e há 50 utilizáveis em estoque. A reserva extra é opcional, de até 15 embalagens, permitindo uma compra de até 85 se a chefia optar pela reserva máxima. Não há pedido mínimo informado que justifique comprar 150 hoje.
```

## modes-pt-BR-049 · analysis

Source task:

> Explique a divergência sem decidir quem tem razão: o cronograma estima 4 semanas de montagem se as peças chegarem até 3 de setembro. Compras estima chegada entre 8 e 15 de setembro. Nenhuma estimativa é compromisso. Não há duração revisada para chegada depois do dia 3.

### baseline: pass

```text
O cronograma estima 4 semanas de montagem sob a condição de as peças chegarem até 3 de setembro. Compras estima chegada entre 8 e 15 de setembro, fora dessa condição. A divergência está nas datas consideradas; nenhuma estimativa é compromisso. Como não há duração revisada para uma chegada após o dia 3, não é possível determinar o prazo de montagem nesse cenário.
```

### lite: pass

```text
O cronograma estima 4 semanas de montagem se as peças chegarem até 3 de setembro. Compras estima que elas chegarão entre 8 e 15 de setembro, depois dessa data. A divergência está na condição de chegada usada pelo cronograma. Nenhuma estimativa é compromisso, e não há duração revisada para uma chegada depois do dia 3.
```

### full: pass

```text
As estimativas usam condições diferentes: o cronograma prevê 4 semanas de montagem se as peças chegarem até 3 de setembro; Compras estima a chegada entre 8 e 15 de setembro, depois desse limite.

Assim, a previsão de Compras não atende à condição da estimativa de montagem. Nenhuma das estimativas é compromisso, e não há duração revisada para chegada após o dia 3. Os dados não permitem decidir quem tem razão nem calcular um novo prazo de montagem.
```

### ultra: pass

```text
A estimativa de 4 semanas de montagem depende da chegada das peças até 3 de setembro. Compras estima chegada entre 8 e 15 de setembro, fora dessa condição. Nenhuma estimativa é compromisso, e não há duração revisada para chegada após o dia 3; portanto, não se pode determinar o prazo de montagem nesse cenário.
```

### off: pass

```text
A estimativa de 4 semanas de montagem depende de as peças chegarem até 3 de setembro. Compras estima a chegada entre 8 e 15 de setembro, depois dessa data. A divergência está nessa condição: a previsão de chegada não atende ao prazo pressuposto pelo cronograma. Nenhuma estimativa é compromisso, e não há duração revisada para uma chegada depois do dia 3; portanto, não é possível estabelecer um novo prazo de montagem com esses dados.
```

## modes-pt-BR-050 · analysis

Source task:

> O teste permite afirmar que o aplicativo funciona sem internet? Foram abertas quatro telas após desligar o Wi-Fi, mas todas estavam no cache. O estado dos dados móveis não foi registrado. Nenhuma tela nova foi aberta e os registros de requisições não foram analisados. Use apenas esses fatos.

### baseline: pass

```text
Não. O teste mostra apenas que quatro telas em cache foram abertas após desligar o Wi-Fi. Como o estado dos dados móveis não foi registrado, não se sabe se o aplicativo estava sem internet. Além disso, nenhuma tela nova foi aberta e os registros de requisições não foram analisados. Esses fatos não permitem afirmar que o aplicativo funciona sem internet.
```

### lite: pass

```text
Não. O teste mostra apenas que quatro telas já armazenadas no cache foram abertas após desligar o Wi-Fi. Como o estado dos dados móveis não foi registrado, não se sabe se o aplicativo estava sem internet. Nenhuma tela nova foi aberta e os registros de requisições não foram analisados. Esses fatos não permitem afirmar que o aplicativo funciona sem internet.
```

### full: pass

```text
Não. O teste mostra apenas que quatro telas já armazenadas no cache foram abertas após desligar o Wi-Fi.

Como o estado dos dados móveis não foi registrado, não se sabe se o aparelho estava sem internet. Nenhuma tela nova foi aberta e os registros de requisições não foram analisados. Portanto, o teste não permite afirmar que o aplicativo funciona sem internet.
```

### ultra: pass

```text
Não. O teste mostra apenas que quatro telas já no cache abriram após desligar o Wi-Fi. Como o estado dos dados móveis não foi registrado, nenhuma tela nova foi aberta e os registros de requisições não foram analisados, não é possível afirmar que o aplicativo funciona sem internet.
```

### off: pass

```text
Não. O teste mostrou apenas que quatro telas já presentes no cache foram abertas após desligar o Wi-Fi. Como o estado dos dados móveis não foi registrado, não ficou demonstrado que o aparelho estava sem internet. Além disso, nenhuma tela nova foi aberta e os registros de requisições não foram analisados. Esses fatos não permitem afirmar que o aplicativo funciona sem internet.
```

## modes-pt-BR-051 · exact-format

Source task:

> Devolva exatamente a mensagem já clara, sem título, explicação ou aspas: A biblioteca fecha às 18h.

### baseline: pass

```text
A biblioteca fecha às 18h.
```

### lite: pass

```text
A biblioteca fecha às 18h.
```

### full: pass

```text
A biblioteca fecha às 18h.
```

### ultra: pass

```text
A biblioteca fecha às 18h.
```

### off: pass

```text
A biblioteca fecha às 18h.
```

## modes-pt-BR-052 · exact-format

Source task:

> Reescreva em exatamente dois itens numerados, mantendo os marcadores: “1. {visitante}, sua entrada está liberada depois das 14h. 2. Se chegar depois das 21h, ligue para {{telefone_portaria}} antes de entrar.” Não acrescente saudação ou assinatura.

### baseline: pass

```text
1. {visitante}, você pode entrar depois das 14h.
2. Se chegar depois das 21h, ligue para {{telefone_portaria}} antes de entrar.
```

### lite: pass

```text
1. {visitante}, sua entrada está liberada depois das 14h.
2. Se chegar depois das 21h, ligue para {{telefone_portaria}} antes de entrar.
```

### full: pass

```text
1. {visitante}, sua entrada está liberada depois das 14h.
2. Se chegar depois das 21h, ligue para {{telefone_portaria}} antes de entrar.
```

### ultra: pass

```text
1. {visitante}, sua entrada está liberada depois das 14h.
2. Se chegar depois das 21h, ligue para {{telefone_portaria}} antes de entrar.
```

### off: pass

```text
1. {visitante}, sua entrada está liberada depois das 14h.
2. Se chegar depois das 21h, ligue para {{telefone_portaria}} antes de entrar.
```

## modes-pt-BR-053 · exact-format

Source task:

> Devolva um objeto JSON somente com "request_id", "level" e "message". Use request_id "P-631", level 3 e uma mensagem em português do Brasil informando que a análise começou, mas não tem data de conclusão. Não use bloco de código.

### baseline: pass

```text
{"request_id":"P-631","level":3,"message":"A análise começou, mas não tem data de conclusão."}
```

### lite: pass

```text
{"request_id":"P-631","level":3,"message":"A análise começou, mas não tem data de conclusão."}
```

### full: pass

```text
{"request_id":"P-631","level":3,"message":"A análise começou, mas não tem data de conclusão."}
```

### ultra: pass

```text
{"request_id":"P-631","level":3,"message":"A análise começou, mas não tem data de conclusão."}
```

### off: pass

```text
{"request_id":"P-631","level":3,"message":"A análise começou, mas não tem data de conclusão."}
```

## modes-pt-BR-054 · exact-format

Source task:

> Simplifique a frase e mantenha o link Markdown exatamente: “Seria recomendável ler [Guia de acesso](https://example.invalid/guia?ed=3#salas) antes de enviar o formulário, pois ele apresenta as opções de acesso.” Devolva uma frase só.

### baseline: flagged

```text
Leia [Guia de acesso](https://example.invalid/guia?ed=3#salas) antes de enviar o formulário para conhecer as opções de acesso.
```

Review notes: Timing, link, and purpose remain, but the recommendation becomes a directive. / Preserves the link and timing but materially strengthens the recommendation into a directive.

### lite: pass

```text
Recomenda-se ler [Guia de acesso](https://example.invalid/guia?ed=3#salas) antes de enviar o formulário, pois o guia apresenta as opções de acesso.
```

### full: pass

```text
É recomendável ler [Guia de acesso](https://example.invalid/guia?ed=3#salas) antes de enviar o formulário, pois o guia apresenta as opções de acesso.
```

### ultra: pass

```text
É recomendável ler [Guia de acesso](https://example.invalid/guia?ed=3#salas) antes de enviar o formulário, pois o guia apresenta as opções de acesso.
```

### off: pass

```text
É recomendável ler [Guia de acesso](https://example.invalid/guia?ed=3#salas) antes de enviar o formulário, pois o guia apresenta as opções de acesso.
```

## modes-pt-BR-055 · exact-format

Source task:

> Produza JSON com exatamente "lot", "units", "cleared" e "reason". lot é "LT/8-B", units é 0 e cleared é false. A razão, em português, deve informar que nenhuma unidade foi liberada porque a inspeção está incompleta. Mantenha os tipos JSON.

### baseline: pass

```text
{"lot":"LT/8-B","units":0,"cleared":false,"reason":"Nenhuma unidade foi liberada porque a inspeção está incompleta."}
```

### lite: pass

```text
{"lot":"LT/8-B","units":0,"cleared":false,"reason":"Nenhuma unidade foi liberada porque a inspeção está incompleta."}
```

### full: pass

```text
{"lot":"LT/8-B","units":0,"cleared":false,"reason":"Nenhuma unidade foi liberada porque a inspeção está incompleta."}
```

### ultra: pass

```text
{"lot":"LT/8-B","units":0,"cleared":false,"reason":"Nenhuma unidade foi liberada porque a inspeção está incompleta."}
```

### off: pass

```text
{"lot":"LT/8-B","units":0,"cleared":false,"reason":"Nenhuma unidade foi liberada porque a inspeção está incompleta."}
```

## modes-pt-BR-056 · exact-format

Source task:

> Edite só a prosa, mantendo o comando literal: “Para poder consultar a fila sem fazer alterações, execute `fila listar --somente-leitura`. Esse comando não remove itens.” Preserve explicitamente a informação de que não há remoção.

### baseline: pass

```text
Para consultar a fila sem fazer alterações, execute `fila listar --somente-leitura`. Esse comando não remove itens.
```

### lite: pass

```text
Para consultar a fila sem fazer alterações, execute `fila listar --somente-leitura`. Esse comando não remove itens.
```

### full: pass

```text
Para consultar a fila sem fazer alterações, execute `fila listar --somente-leitura`. Esse comando não remove itens.
```

### ultra: pass

```text
Para consultar a fila sem alterações, execute `fila listar --somente-leitura`. O comando não remove itens.
```

### off: pass

```text
Para consultar a fila sem fazer alterações, execute `fila listar --somente-leitura`. Esse comando não remove itens.
```

## modes-pt-BR-057 · exact-format

Source task:

> Devolva exatamente três tópicos sem título. Informe que a linha L-23 está suspensa em 12 de dezembro, a L-24 continua operando e o reembolso depende de pedido opcional, não de pagamento automático. Preserve os códigos.

### baseline: pass

```text
- A linha L-23 está suspensa em 12 de dezembro.
- A linha L-24 continua operando.
- O reembolso depende de um pedido opcional; não há pagamento automático.
```

### lite: pass

```text
- A linha L-23 está suspensa em 12 de dezembro.
- A linha L-24 continua operando.
- O reembolso depende de um pedido opcional; o pagamento não é automático.
```

### full: pass

```text
- A linha L-23 está suspensa em 12 de dezembro.
- A linha L-24 continua operando.
- O reembolso depende de um pedido opcional; não há pagamento automático.
```

### ultra: pass

```text
- A linha L-23 está suspensa em 12 de dezembro.
- A linha L-24 continua operando.
- O reembolso depende de pedido opcional; não há pagamento automático.
```

### off: pass

```text
- A linha L-23 está suspensa em 12 de dezembro.
- A linha L-24 continua operando.
- O reembolso depende de um pedido opcional; o pagamento não é automático.
```

## modes-pt-BR-058 · exact-format

Source task:

> Devolva apenas esta linha, sem qualquer alteração de pontuação ou espaços: REV-6 | aguardando | 0/15 verificados

### baseline: pass

```text
REV-6 | aguardando | 0/15 verificados
```

### lite: pass

```text
REV-6 | aguardando | 0/15 verificados
```

### full: pass

```text
REV-6 | aguardando | 0/15 verificados
```

### ultra: pass

```text
REV-6 | aguardando | 0/15 verificados
```

### off: pass

```text
REV-6 | aguardando | 0/15 verificados
```

## modes-pt-BR-059 · exact-format

Source task:

> Reescreva em um parágrafo, mantendo caminho e variável: salve o rascunho em /relatorios/2029/nota_final.md. Mantenha APROVADO=false até a editora aprovar. Salvar o arquivo não significa obter aprovação.

### baseline: pass

```text
Salve o rascunho em /relatorios/2029/nota_final.md e mantenha APROVADO=false até a editora aprovar. Salvar o arquivo não significa obter aprovação.
```

### lite: pass

```text
Salve o rascunho em /relatorios/2029/nota_final.md. Mantenha APROVADO=false até a editora aprovar. Salvar o arquivo não significa obter aprovação.
```

### full: pass

```text
Salve o rascunho em /relatorios/2029/nota_final.md. Mantenha APROVADO=false até a editora aprovar. Salvar o arquivo não significa obter aprovação.
```

### ultra: pass

```text
Salve o rascunho em /relatorios/2029/nota_final.md. Mantenha APROVADO=false até a editora aprovar. Salvar o arquivo não significa obter aprovação.
```

### off: pass

```text
Salve o rascunho em /relatorios/2029/nota_final.md e mantenha APROVADO=false até a editora aprovar. Salvar o arquivo não significa obter aprovação.
```

## modes-pt-BR-060 · exact-format

Source task:

> Devolva somente um objeto JSON com "code", "wait_seconds" e "description". code deve ser "PAUSA_9" e wait_seconds deve ser 60. A descrição em português precisa dizer que esperar 60 segundos é uma recomendação, não uma obrigação.

### baseline: pass

```text
{"code":"PAUSA_9","wait_seconds":60,"description":"Esperar 60 segundos é uma recomendação, não uma obrigação."}
```

### lite: pass

```text
{"code":"PAUSA_9","wait_seconds":60,"description":"Esperar 60 segundos é uma recomendação, não uma obrigação."}
```

### full: pass

```text
{"code":"PAUSA_9","wait_seconds":60,"description":"Esperar 60 segundos é uma recomendação, não uma obrigação."}
```

### ultra: pass

```text
{"code":"PAUSA_9","wait_seconds":60,"description":"Esperar 60 segundos é uma recomendação, não uma obrigação."}
```

### off: pass

```text
{"code":"PAUSA_9","wait_seconds":60,"description":"Esperar 60 segundos é uma recomendação, não uma obrigação."}
```

## modes-pt-BR-061 · voice

Source task:

> Melhore esta mensagem acolhedora sem prometer o resultado: “Obrigada por avisar sobre a cadeira instável, Lia. Pedimos à oficina que examine a cadeira. Ainda não sabemos se ela pode ser consertada, mas avisaremos quando o resultado da avaliação chegar.”

### baseline: pass

```text
Obrigada por nos avisar sobre a cadeira instável, Lia. Pedimos à oficina que a examine. Ainda não sabemos se será possível consertá-la, mas avisaremos você assim que recebermos o resultado da avaliação.
```

### lite: pass

```text
Obrigada por avisar sobre a cadeira instável, Lia. Pedimos à oficina que examine a cadeira. Ainda não sabemos se ela pode ser consertada, mas avisaremos assim que recebermos o resultado da avaliação.
```

### full: pass

```text
Obrigada por avisar sobre a cadeira instável, Lia. Pedimos à oficina que a examine. Ainda não sabemos se há conserto, mas avisaremos assim que recebermos o resultado da avaliação.
```

### ultra: pass

```text
Obrigada por avisar sobre a cadeira instável, Lia. Pedimos à oficina que a examine. Ainda não sabemos se há conserto, mas avisaremos assim que recebermos a avaliação.
```

### off: pass

```text
Obrigada por nos avisar sobre a cadeira instável, Lia. Já pedimos à oficina que a examine. Ainda não sabemos se será possível consertá-la, mas avisaremos você assim que recebermos o resultado da avaliação.
```

## modes-pt-BR-062 · voice

Source task:

> Encurte sem perder a brincadeira: “A hortelã tomou a varanda como uma síndica de folhas. Contamos oito brotos novos nesta semana. Isso não é recorde: na semana passada ninguém contou. A taxa de condomínio continua sendo água.”

### baseline: pass

```text
A hortelã virou síndica da varanda: oito brotos novos nesta semana. Recorde? Na passada ninguém contou. O condomínio segue pago em água.
```

### lite: pass

```text
A hortelã tomou a varanda como uma síndica de folhas. Contamos oito brotos novos nesta semana. Não é recorde: na semana passada ninguém contou. O condomínio continua sendo água.
```

### full: pass

```text
A hortelã virou síndica de folhas da varanda: contamos oito brotos novos nesta semana. Recorde? Não: na semana passada ninguém contou. O condomínio continua sendo pago em água.
```

### ultra: pass

```text
A hortelã virou síndica de folhas da varanda: oito brotos novos nesta semana. Não é recorde — na passada, ninguém contou. O condomínio continua sendo pago em água.
```

### off: pass

```text
A hortelã virou síndica da varanda: oito brotos novos nesta semana. Recorde? Não sabemos: ninguém contou na semana passada. O condomínio continua sendo pago em água.
```

## modes-pt-BR-063 · voice

Source task:

> Deixe o pedido de desculpas direto: “Eu informei o número errado do apartamento. A equipe usou o endereço que passei. Perguntei ao entregador se pode corrigir a rota, mas ele ainda não respondeu. Sinto muito pelo atraso.” Não transfira culpa nem prometa a correção.

### baseline: pass

```text
Sinto muito pelo atraso. Informei o número errado do apartamento, e a equipe seguiu o endereço que passei. Perguntei ao entregador se pode corrigir a rota, mas ainda não recebi resposta.
```

### lite: pass

```text
Informei o número errado do apartamento, e a equipe usou o endereço que passei. Perguntei ao entregador se pode corrigir a rota, mas ele ainda não respondeu. Sinto muito pelo atraso.
```

### full: pass

```text
Sinto muito pelo atraso. Informei o número errado do apartamento, e a equipe usou o endereço que passei. Perguntei ao entregador se pode corrigir a rota, mas ele ainda não respondeu.
```

### ultra: pass

```text
Sinto muito pelo atraso. Informei o apartamento errado, e a equipe usou o endereço que passei. Perguntei ao entregador se pode corrigir a rota, mas ele ainda não respondeu.
```

### off: pass

```text
Sinto muito pelo atraso. Informei o número errado do apartamento, e a equipe usou o endereço que passei. Perguntei ao entregador se pode corrigir a rota, mas ele ainda não respondeu.
```

## modes-pt-BR-064 · voice

Source task:

> Reescreva com tom calmo: “Encontramos três mochilas ao lado da quadra depois do fechamento. Não sabemos quem são os donos. Elas estão na sala da zeladoria. Os donos podem procurar a recepção e descrever a mochila antes de retirá-la. Não sabemos se foram deixadas de propósito.”

### baseline: pass

```text
Encontramos três mochilas ao lado da quadra após o fechamento. Elas estão na sala da zeladoria. Ainda não sabemos quem são os donos nem se foram deixadas ali de propósito. Para retirá-las, os donos podem procurar a recepção e descrever a mochila.
```

### lite: pass

```text
Encontramos três mochilas ao lado da quadra depois do fechamento. Não sabemos quem são os donos nem se foram deixadas de propósito. Elas estão na sala da zeladoria. Os donos podem procurar a recepção e descrever a mochila antes de retirá-la.
```

### full: pass

```text
Encontramos três mochilas ao lado da quadra depois do fechamento. Elas estão na sala da zeladoria. Não sabemos quem são os donos nem se foram deixadas de propósito. Os donos podem procurar a recepção e descrever a mochila antes de retirá-la.
```

### ultra: pass

```text
Encontramos três mochilas ao lado da quadra após o fechamento. Estão na sala da zeladoria. Não sabemos quem são os donos nem se foram deixadas de propósito. Os donos podem procurar a recepção e descrever a mochila antes de retirá-la.
```

### off: pass

```text
Encontramos três mochilas ao lado da quadra depois do fechamento. Elas estão na sala da zeladoria. Não sabemos quem são os donos nem se foram deixadas ali de propósito. Os donos podem procurar a recepção e descrever a mochila antes de retirá-la.
```

## modes-pt-BR-065 · voice

Source task:

> Ajuste o diálogo, mantendo a hesitação: “Talvez eu vá no primeiro ônibus”, disse Caio, “se a reunião acabar cedo. Mas não comprei a passagem e não quero que você me espere como se estivesse tudo certo.” Não transforme em plano confirmado.

### baseline: pass

```text
— Talvez eu pegue o primeiro ônibus, se a reunião acabar cedo — disse Caio. — Mas ainda não comprei a passagem… Não quero que você fique me esperando como se já estivesse tudo certo.
```

### lite: pass

```text
“Talvez eu vá no primeiro ônibus”, disse Caio, “se a reunião acabar cedo. Mas ainda não comprei a passagem e não quero que você me espere como se estivesse tudo certo.”
```

### full: pass

```text
“Talvez eu vá no primeiro ônibus, se a reunião acabar cedo”, disse Caio. “Mas ainda não comprei a passagem. Não quero que você me espere como se estivesse tudo certo.”
```

### ultra: pass

```text
“Talvez eu vá no primeiro ônibus, se a reunião acabar cedo”, disse Caio. “Mas ainda não comprei a passagem. Não quero que você me espere como se estivesse tudo certo.”
```

### off: pass

```text
“Talvez eu pegue o primeiro ônibus”, disse Caio, “se a reunião acabar cedo. Mas ainda não comprei a passagem… Não quero que você fique me esperando como se já estivesse tudo certo.”
```

## modes-pt-BR-066 · scope

Source task:

> Responda só quem tem a próxima ação registrada: a coordenadora escreveu a proposta. O técnico deve conferir o desenho antes de ela enviar ao cliente. O cliente poderá comentar depois. Não há data para a conferência.

### baseline: pass

```text
O técnico.
```

### lite: pass

```text
O técnico.
```

### full: pass

```text
O técnico.
```

### ultra: pass

```text
O técnico.
```

### off: pass

```text
O técnico.
```

## modes-pt-BR-067 · scope

Source task:

> Altere apenas a segunda frase e devolva as três: “O parque abre às oito. É obrigatório que os visitantes mantenham os bilhetes até a saída. A loja fecha às cinco.” Preserve a primeira e a terceira exatamente.

### baseline: pass

```text
O parque abre às oito. Os visitantes devem manter os bilhetes até a saída. A loja fecha às cinco.
```

### lite: pass

```text
O parque abre às oito. Os visitantes devem manter os bilhetes até a saída. A loja fecha às cinco.
```

### full: pass

```text
O parque abre às oito. Os visitantes devem manter os bilhetes até a saída. A loja fecha às cinco.
```

### ultra: pass

```text
O parque abre às oito. Os visitantes devem manter os bilhetes até a saída. A loja fecha às cinco.
```

### off: pass

```text
O parque abre às oito. Os visitantes devem manter os bilhetes até a saída. A loja fecha às cinco.
```

## modes-pt-BR-068 · scope

Source task:

> Responda apenas se houve decisão sobre o portão: a diretoria aprovou reparar os bancos, adiou a decisão do portão até receber a vistoria e pediu amostras de tinta para a fachada. A vistoria não tem data marcada.

### baseline: pass

```text
Não. A decisão sobre o portão foi adiada até receber a vistoria.
```

### lite: pass

```text
Não. A decisão sobre o portão foi adiada até receber a vistoria, que não tem data marcada.
```

### full: pass

```text
Não. A decisão sobre o portão foi adiada até o recebimento da vistoria, que não tem data marcada.
```

### ultra: pass

```text
Não. A decisão foi adiada até receber a vistoria, que não tem data marcada.
```

### off: pass

```text
Não. A decisão sobre o portão foi adiada até o recebimento da vistoria, que ainda não tem data marcada.
```

## modes-pt-BR-069 · scope

Source task:

> Resuma apenas o problema ainda não resolvido: o cliente agradeceu a troca da tampa. A nova tampa encaixa, mas a alça substituta continua travando em dias úmidos. A equipe não testou essa condição. O cliente não pediu troca completa do aparelho.

### baseline: pass

```text
A alça substituta continua travando em dias úmidos, condição que a equipe ainda não testou.
```

### lite: pass

```text
A alça substituta continua travando em dias úmidos. A equipe não testou essa condição.
```

### full: pass

```text
A alça substituta continua travando em dias úmidos. A equipe não testou essa condição.
```

### ultra: pass

```text
A alça substituta continua travando em dias úmidos. A equipe não testou essa condição.
```

### off: pass

```text
A alça substituta continua travando em dias úmidos, condição que a equipe não testou.
```

## modes-pt-BR-070 · scope

Source task:

> Corrija só a concordância, preservando ordem e fatos: “As três caixas foi lacradas antes da impressão das etiquetas. Não sabemos quem lacrou. Ivo imprimiu as etiquetas.” Não atribua o lacre a Ivo.

### baseline: pass

```text
As três caixas foram lacradas antes da impressão das etiquetas. Não sabemos quem lacrou. Ivo imprimiu as etiquetas.
```

### lite: pass

```text
As três caixas foram lacradas antes da impressão das etiquetas. Não sabemos quem lacrou. Ivo imprimiu as etiquetas.
```

### full: pass

```text
As três caixas foram lacradas antes da impressão das etiquetas. Não sabemos quem lacrou. Ivo imprimiu as etiquetas.
```

### ultra: pass

```text
As três caixas foram lacradas antes da impressão das etiquetas. Não sabemos quem lacrou. Ivo imprimiu as etiquetas.
```

### off: pass

```text
As três caixas foram lacradas antes da impressão das etiquetas. Não sabemos quem lacrou. Ivo imprimiu as etiquetas.
```

## modes-pt-BR-071 · ambiguity

Source task:

> Torne a lacuna explícita: “Luca disse a Cris que o seu cartão tinha vencido.” A nota não esclarece a quem “seu” se refere. Reescreva sem escolher a pessoa e indique apenas a pergunta necessária.

### baseline: pass

```text
Luca disse a Cris que um cartão tinha vencido, mas a nota não esclarece de quem era o cartão.
De quem era o cartão?
```

### lite: pass

```text
Luca disse a Cris que o cartão tinha vencido. A nota não esclarece de quem era o cartão.

De quem era o cartão?
```

### full: pass

```text
Luca disse a Cris que um cartão tinha vencido, mas a nota não esclarece de quem era o cartão.

De quem era o cartão?
```

### ultra: pass

```text
Luca disse a Cris que um cartão tinha vencido, mas a nota não esclarece de quem era o cartão.
De quem era o cartão?
```

### off: pass

```text
Luca disse a Cris que um cartão tinha vencido, mas a nota não esclarece de quem era o cartão.

A quem “seu” se refere?
```

## modes-pt-BR-072 · ambiguity

Source task:

> Reescreva: “O envelope foi entregue depois que Tati telefonou ao porteiro. Não sabemos quem o entregou. O porteiro registrou o recebimento às 17h20.” Preserve quem é conhecido e quem continua desconhecido.

### baseline: pass

```text
Depois que Tati telefonou ao porteiro, o envelope foi entregue por alguém cuja identidade desconhecemos. O porteiro registrou o recebimento às 17h20.
```

### lite: pass

```text
O envelope foi entregue depois que Tati telefonou ao porteiro. Não sabemos quem entregou o envelope. O porteiro registrou o recebimento às 17h20.
```

### full: pass

```text
O envelope foi entregue depois que Tati telefonou ao porteiro. Não sabemos quem entregou o envelope. O porteiro registrou o recebimento às 17h20.
```

### ultra: pass

```text
O envelope foi entregue depois que Tati telefonou ao porteiro. Não sabemos quem o entregou. O porteiro registrou o recebimento às 17h20.
```

### off: pass

```text
O envelope foi entregue depois que Tati telefonou ao porteiro. Não sabemos quem fez a entrega. O porteiro registrou o recebimento às 17h20.
```

## modes-pt-BR-073 · ambiguity

Source task:

> O pedido diz “entregar até 09/10”, sem ano ou padrão de data. Pediram uma versão com mês por extenso. Explique brevemente o que falta antes de escrever uma data completa. Não use a data atual para preencher a lacuna.

### baseline: pass

```text
Falta confirmar o ano e o padrão da data: “09/10” pode significar 9 de outubro ou 10 de setembro. Só após essa confirmação será possível escrever uma data completa com o mês por extenso.
```

### lite: pass

```text
Falta confirmar o ano e o padrão da data: “09/10” significa 9 de outubro ou 10 de setembro? Sem essas informações, não é possível escrever a data completa com o mês por extenso.
```

### full: pass

```text
Faltam o ano e o padrão da data: “09/10” significa 9 de outubro ou 10 de setembro? É preciso confirmar ambos antes de escrever a data completa com o mês por extenso.
```

### ultra: pass

```text
Faltam o ano e o padrão da data: 09/10 pode significar 9 de outubro ou 10 de setembro. É preciso esclarecer ambos antes de escrever a data completa.
```

### off: pass

```text
Falta confirmar o ano e o padrão da data: “09/10” significa 9 de outubro ou 10 de setembro? Sem essas informações, não é possível escrever uma data completa com o mês por extenso.
```

## modes-pt-BR-074 · ambiguity

Source task:

> Faça uma atualização sem resolver o conflito: o painel diz “entregue”, e a planilha do depósito diz “aguardando saída”. Ambos foram atualizados às 13h, sem autor identificado. A confirmação do cliente ainda não chegou.

### baseline: pass

```text
O status permanece divergente: o painel indica “entregue”, enquanto a planilha do depósito indica “aguardando saída”. Ambos foram atualizados às 13h, sem identificação dos autores. A confirmação do cliente ainda não chegou.
```

### lite: pass

```text
Há um conflito: o painel indica “entregue”, mas a planilha do depósito indica “aguardando saída”. Ambos foram atualizados às 13h, sem autor identificado. A confirmação do cliente ainda não chegou.
```

### full: pass

```text
Há um conflito entre os registros: o painel indica “entregue”, enquanto a planilha do depósito indica “aguardando saída”. Ambos foram atualizados às 13h, sem autor identificado. A confirmação do cliente ainda não chegou.
```

### ultra: pass

```text
Os registros divergem: o painel indica “entregue”; a planilha do depósito, “aguardando saída”. Ambos foram atualizados às 13h, sem autor identificado. A confirmação do cliente ainda não chegou.
```

### off: pass

```text
Há um conflito de status: o painel indica “entregue”, enquanto a planilha do depósito indica “aguardando saída”. Ambos foram atualizados às 13h, sem autor identificado. A confirmação do cliente ainda não chegou.
```

## modes-pt-BR-075 · ambiguity

Source task:

> Clareie sem aumentar a certeza: “A mancha pode ter crescido durante o armazenamento, mas a foto anterior está escura demais para comparar.” O texto não diz que o armazenamento criou a mancha.

### baseline: pass

```text
É possível que a mancha tenha aumentado durante o armazenamento, mas a foto anterior está escura demais para permitir a comparação. O texto não afirma que o armazenamento tenha causado a mancha.
```

### lite: pass

```text
A mancha pode ter crescido durante o armazenamento, mas a foto anterior está escura demais para permitir a comparação.
```

### full: pass

```text
A mancha pode ter aumentado durante o armazenamento, mas a foto anterior está escura demais para permitir a comparação. Isso não significa que o armazenamento tenha criado a mancha.
```

### ultra: pass

```text
A mancha pode ter crescido durante o armazenamento, mas a foto anterior está escura demais para comparar. O texto não atribui ao armazenamento a origem da mancha.
```

### off: pass

```text
A mancha pode ter aumentado durante o armazenamento, mas a foto anterior está escura demais para permitir a comparação. O texto não afirma que o armazenamento tenha causado a mancha.
```

## modes-pt-BR-076 · evidence

Source task:

> Resuma a observação: uma voluntária contou 18 passagens de aves pela janela norte entre 6h e 6h30 em uma manhã sem chuva. A mesma ave pode ter passado várias vezes. Não houve observação de outras janelas ou dias. Não estime a população de aves.

### baseline: pass

```text
Uma voluntária registrou 18 passagens de aves pela janela norte entre 6h e 6h30, em uma manhã sem chuva. A mesma ave pode ter passado mais de uma vez. Não foram observadas outras janelas ou outros dias; o registro não permite estimar a população de aves.
```

### lite: pass

```text
Uma voluntária contou 18 passagens de aves pela janela norte entre 6h e 6h30, em uma manhã sem chuva. A mesma ave pode ter passado várias vezes. Não foram observadas outras janelas ou outros dias.
```

### full: pass

```text
Uma voluntária contou 18 passagens de aves pela janela norte, entre 6h e 6h30, em uma manhã sem chuva. A mesma ave pode ter passado várias vezes. Não foram observadas outras janelas ou outros dias.
```

### ultra: pass

```text
Uma voluntária contou 18 passagens de aves pela janela norte, entre 6h e 6h30, em uma manhã sem chuva. A mesma ave pode ter passado várias vezes. Não foram observadas outras janelas nem outros dias; a contagem não permite estimar a população de aves.
```

### off: pass

```text
Uma voluntária contou 18 passagens de aves pela janela norte, entre 6h e 6h30, em uma manhã sem chuva. A mesma ave pode ter passado várias vezes; portanto, a contagem não representa necessariamente 18 aves diferentes. Não foram observadas outras janelas ou outros dias.
```

## modes-pt-BR-077 · evidence

Source task:

> Reescreva para o laudo: “Não havia mofo visível na parte externa da caixa.” A caixa não foi aberta e não foi feita análise laboratorial. Não transforme a observação externa em conclusão sobre o interior.

### baseline: pass

```text
Não foi observado mofo visível na superfície externa da caixa. A caixa não foi aberta nem submetida a análise laboratorial, portanto não há conclusão sobre a presença de mofo em seu interior.
```

### lite: pass

```text
Não havia mofo visível na parte externa da caixa. A caixa não foi aberta e não foi realizada análise laboratorial. Essa observação não permite concluir se havia mofo no interior.
```

### full: pass

```text
Não havia mofo visível na parte externa da caixa. A caixa não foi aberta e não foi realizada análise laboratorial. A observação não permite concluir se havia mofo no interior.
```

### ultra: pass

```text
Não havia mofo visível na parte externa da caixa. A caixa não foi aberta nem submetida a análise laboratorial; a observação não permite concluir sobre seu interior.
```

### off: pass

```text
Não foi observado mofo visível na parte externa da caixa. A caixa não foi aberta e não foi realizada análise laboratorial. A observação externa não permite concluir sobre a presença ou ausência de mofo no interior.
```

## modes-pt-BR-078 · evidence

Source task:

> Explique para o conselho: 70% de 100 pessoas que voluntariamente leram um QR code pediram mais bicicletários. O cartaz estava ao lado de uma loja de bicicletas. Não houve seleção aleatória. Não apresente o número como 70% dos moradores.

### baseline: pass

```text
Das 100 pessoas que voluntariamente leram o QR code, 70% pediram mais bicicletários. O cartaz estava ao lado de uma loja de bicicletas, e não houve seleção aleatória. Assim, o resultado descreve apenas os participantes e não pode ser apresentado como a opinião de 70% dos moradores.
```

### lite: pass

```text
Das 100 pessoas que voluntariamente leram um QR code, 70% pediram mais bicicletários. O cartaz estava ao lado de uma loja de bicicletas e não houve seleção aleatória. O resultado descreve esse grupo, não 70% dos moradores.
```

### full: pass

```text
Das 100 pessoas que voluntariamente leram um QR code, 70% pediram mais bicicletários. O cartaz estava ao lado de uma loja de bicicletas e não houve seleção aleatória. O resultado descreve esse grupo de participantes, não 70% dos moradores.
```

### ultra: pass

```text
Das 100 pessoas que voluntariamente leram um QR code, 70% pediram mais bicicletários. O cartaz estava ao lado de uma loja de bicicletas, e não houve seleção aleatória. O resultado descreve esses participantes, não 70% dos moradores.
```

### off: pass

```text
Das 100 pessoas que voluntariamente leram o QR code, 70% pediram mais bicicletários. Esse percentual se refere apenas às pessoas participantes, não ao conjunto dos moradores. O cartaz estava ao lado de uma loja de bicicletas e não houve seleção aleatória, o que limita a representatividade do resultado.
```

## modes-pt-BR-079 · evidence

Source task:

> Reescreva esta nota de agendamento, sem orientação médica: a consulta das 9h foi cancelada porque a profissional não estará disponível. Não foi informado o motivo. As pessoas agendadas serão contatadas para combinar outro horário. Nenhum horário substituto foi definido.

### baseline: pass

```text
A consulta das 9h foi cancelada por indisponibilidade da profissional. O motivo da indisponibilidade não foi informado. As pessoas agendadas serão contatadas para combinar outro horário, ainda não definido.
```

### lite: pass

```text
A consulta das 9h foi cancelada porque a profissional não estará disponível. O motivo da indisponibilidade não foi informado. As pessoas agendadas serão contatadas para combinar outro horário. Nenhum horário substituto foi definido.
```

### full: pass

```text
A consulta das 9h foi cancelada porque a profissional não estará disponível. O motivo da indisponibilidade não foi informado. As pessoas agendadas serão contatadas para combinar outro horário. Nenhum horário substituto foi definido.
```

### ultra: pass

```text
A consulta das 9h foi cancelada porque a profissional não estará disponível; o motivo da indisponibilidade não foi informado. As pessoas agendadas serão contatadas para combinar outro horário. Nenhum horário substituto foi definido.
```

### off: pass

```text
A consulta das 9h foi cancelada porque a profissional não estará disponível. O motivo da indisponibilidade não foi informado. As pessoas agendadas serão contatadas para combinar outro horário. Nenhum horário substituto foi definido.
```

## modes-pt-BR-080 · evidence

Source task:

> Escreva uma nota de qualidade: a balança marcou 250 g três vezes ao pesar uma massa certificada de 250 g hoje. Apenas essa carga foi testada. Isso não demonstra a precisão para outras cargas e não é uma calibração completa.

### baseline: pass

```text
Hoje, a balança indicou 250 g em três pesagens de uma massa certificada de 250 g. Apenas essa carga foi testada. O resultado não demonstra a precisão para outras cargas e não constitui uma calibração completa.
```

### lite: pass

```text
Hoje, a balança marcou 250 g em três pesagens de uma massa certificada de 250 g. Apenas essa carga foi testada. O resultado não demonstra a precisão para outras cargas e não constitui uma calibração completa.
```

### full: pass

```text
Hoje, a balança indicou 250 g em três pesagens de uma massa certificada de 250 g. Apenas essa carga foi testada. O resultado não demonstra a precisão para outras cargas e não constitui uma calibração completa.
```

### ultra: pass

```text
Hoje, a balança marcou 250 g em três pesagens de uma massa certificada de 250 g. Apenas essa carga foi testada. O resultado não demonstra a precisão para outras cargas nem constitui uma calibração completa.
```

### off: pass

```text
Hoje, a balança indicou 250 g em três pesagens de uma massa certificada de 250 g. Apenas essa carga foi testada. O resultado não demonstra a precisão da balança para outras cargas e não constitui uma calibração completa.
```

## modes-pt-BR-081 · translation

Source task:

> Traduza o aviso inteiro para português do Brasil, mantendo o marcador: “Hello, {member}. Your renewal request has been received but has not yet been approved. You may upload a supporting document by 17:00 UTC on 11 January 2030. Uploading is optional at this stage; we will contact you if it becomes required.”

### baseline: pass

```text
Olá, {member}. Sua solicitação de renovação foi recebida, mas ainda não foi aprovada. Você pode enviar um documento comprobatório até as 17h00 UTC de 11 de janeiro de 2030. O envio é opcional nesta etapa; entraremos em contato se ele se tornar obrigatório.
```

### lite: pass

```text
Olá, {member}. Sua solicitação de renovação foi recebida, mas ainda não foi aprovada. Você pode enviar um documento de apoio até as 17:00 UTC de 11 de janeiro de 2030. O envio é opcional nesta etapa; entraremos em contato se ele se tornar obrigatório.
```

### full: pass

```text
Olá, {member}. Recebemos sua solicitação de renovação, mas ela ainda não foi aprovada. Você pode enviar um documento comprobatório até as 17:00 UTC de 11 de janeiro de 2030. O envio é opcional nesta etapa; entraremos em contato se ele se tornar obrigatório.
```

### ultra: pass

```text
Olá, {member}. Sua solicitação de renovação foi recebida, mas ainda não foi aprovada. Você pode enviar um documento comprobatório até as 17:00 UTC de 11 de janeiro de 2030. O envio é opcional nesta etapa; entraremos em contato se ele se tornar obrigatório.
```

### off: pass

```text
Olá, {member}. Sua solicitação de renovação foi recebida, mas ainda não foi aprovada. Você pode enviar um documento comprobatório até as 17:00 UTC de 11 de janeiro de 2030. O envio é opcional nesta etapa; entraremos em contato se ele se tornar obrigatório.
```

## modes-pt-BR-082 · translation

Source task:

> Traduza todo o texto para português do Brasil: “The workshop expects the repair to take 3–5 business days after the component arrives. The component has not been shipped. Ren approved the price estimate only, not replacement of the whole device. The note does not identify who removed the panel.”

### baseline: pass

```text
A oficina estima que o reparo leve de 3 a 5 dias úteis após a chegada do componente. O componente ainda não foi enviado. Ren aprovou apenas o orçamento, não a substituição de todo o aparelho. A anotação não identifica quem removeu o painel.
```

### lite: pass

```text
A oficina prevê que o reparo leve de 3 a 5 dias úteis após a chegada do componente. O componente ainda não foi enviado. Ren aprovou apenas a estimativa de preço, não a substituição do aparelho inteiro. A nota não identifica quem removeu o painel.
```

### full: pass

```text
A oficina prevê que o reparo leve de 3 a 5 dias úteis após a chegada do componente. O componente ainda não foi enviado. Ren aprovou apenas o orçamento, não a substituição do aparelho inteiro. A anotação não identifica quem removeu o painel.
```

### ultra: pass

```text
A oficina prevê que o reparo leve de 3 a 5 dias úteis após a chegada do componente. O componente ainda não foi enviado. Ren aprovou apenas o orçamento, não a substituição do aparelho inteiro. A nota não identifica quem removeu o painel.
```

### off: pass

```text
A oficina prevê que o reparo leve de 3 a 5 dias úteis após a chegada do componente. O componente ainda não foi enviado. Ren aprovou apenas o orçamento, não a substituição do aparelho inteiro. A anotação não identifica quem removeu o painel.
```

## modes-pt-BR-083 · translation

Source task:

> Traduza para português do Brasil, preservando o humor: “My shopping bag surrendered halfway up the hill. I got home with the apples, but the bread had escaped. This happened on Monday. I have not asked the shop for a refund, so I do not know whether it would offer one.”

### baseline: pass

```text
Minha sacola de compras se rendeu no meio da subida. Cheguei em casa com as maçãs, mas o pão tinha fugido. Isso aconteceu na segunda-feira. Não pedi reembolso à loja, então não sei se ela ofereceria um.
```

### lite: pass

```text
Minha sacola de compras se rendeu no meio da subida. Cheguei em casa com as maçãs, mas o pão tinha escapado. Isso aconteceu na segunda-feira. Não pedi reembolso à loja, então não sei se ela ofereceria um.
```

### full: pass

```text
Minha sacola de compras se rendeu no meio da subida. Cheguei em casa com as maçãs, mas o pão tinha escapado. Isso aconteceu na segunda-feira. Não pedi reembolso à loja, então não sei se ela ofereceria um.
```

### ultra: pass

```text
Minha sacola de compras se rendeu na metade da subida. Cheguei em casa com as maçãs, mas o pão tinha escapado. Isso aconteceu na segunda-feira. Não pedi reembolso à loja, então não sei se ela ofereceria um.
```

### off: pass

```text
Minha sacola de compras se rendeu no meio da subida. Cheguei em casa com as maçãs, mas o pão tinha escapado. Isso aconteceu na segunda-feira. Não pedi reembolso à loja, então não sei se ela ofereceria um.
```

## modes-pt-BR-084 · translation

Source task:

> Traduza integralmente para português do Brasil: “The seat is reserved only after payment is received. You may pay online or at the counter. Payments received after 22 May 2030 will be moved to the next available session; we cannot guarantee a session in the same month.”

### baseline: pass

```text
A vaga só é reservada após o recebimento do pagamento. Você pode pagar on-line ou no balcão. Os pagamentos recebidos após 22 de maio de 2030 serão transferidos para a próxima sessão disponível; não podemos garantir uma sessão no mesmo mês.
```

### lite: pass

```text
O lugar só é reservado após o recebimento do pagamento. Você pode pagar on-line ou no balcão. Pagamentos recebidos após 22 de maio de 2030 serão transferidos para a próxima sessão disponível; não podemos garantir uma sessão no mesmo mês.
```

### full: pass

```text
A vaga só fica reservada após o recebimento do pagamento. Você pode pagar online ou no balcão. Os pagamentos recebidos após 22 de maio de 2030 serão transferidos para a próxima sessão disponível; não podemos garantir uma sessão no mesmo mês.
```

### ultra: pass

```text
A vaga só é reservada após o recebimento do pagamento. Você pode pagar pela internet ou no balcão. Pagamentos recebidos após 22 de maio de 2030 serão transferidos para a próxima sessão disponível; não podemos garantir uma sessão no mesmo mês.
```

### off: pass

```text
O lugar só é reservado após o recebimento do pagamento. Você pode pagar pela internet ou no balcão. Os pagamentos recebidos após 22 de maio de 2030 serão transferidos para a próxima sessão disponível; não podemos garantir uma sessão no mesmo mês.
```

## modes-pt-BR-085 · translation

Source task:

> O idioma de destino é português do Brasil. Traduza, mantendo o comando e o caminho: “Run `report verify --offline` to check the local report. This command sends nothing to the server. The result is saved to /tmp/reports/check.log unless you specify another directory.”

### baseline: pass

```text
Execute `report verify --offline` para verificar o relatório local. Esse comando não envia nada ao servidor. O resultado é salvo em /tmp/reports/check.log, a menos que você especifique outro diretório.
```

### lite: pass

```text
Execute `report verify --offline` para verificar o relatório local. Esse comando não envia nada ao servidor. O resultado é salvo em /tmp/reports/check.log, a menos que você especifique outro diretório.
```

### full: pass

```text
Execute `report verify --offline` para verificar o relatório local. Esse comando não envia nada ao servidor. O resultado é salvo em /tmp/reports/check.log, a menos que você especifique outro diretório.
```

### ultra: pass

```text
Execute `report verify --offline` para verificar o relatório local. Esse comando não envia nada ao servidor. O resultado é salvo em /tmp/reports/check.log, a menos que você especifique outro diretório.
```

### off: pass

```text
Execute `report verify --offline` para verificar o relatório local. Esse comando não envia nada ao servidor. O resultado é salvo em /tmp/reports/check.log, a menos que você especifique outro diretório.
```

## modes-pt-BR-086 · translation

Source task:

> O idioma de destino é português do Brasil. Traduza o parágrafo inteiro: “Forty-two of the 120 email invitees responded. Invitations went only to last year's volunteers, not to a random sample. Of respondents, 60% preferred a morning event. This does not establish the preference of all residents.”

### baseline: pass

```text
Quarenta e duas das 120 pessoas convidadas por e-mail responderam. Os convites foram enviados apenas aos voluntários do ano passado, não a uma amostra aleatória. Entre os respondentes, 60% preferiam um evento pela manhã. Isso não estabelece a preferência de todos os moradores.
```

### lite: pass

```text
Quarenta e duas das 120 pessoas convidadas por e-mail responderam. Os convites foram enviados apenas aos voluntários do ano passado, não a uma amostra aleatória. Entre as pessoas que responderam, 60% preferiam um evento pela manhã. Isso não estabelece a preferência de todos os moradores.
```

### full: pass

```text
Das 120 pessoas convidadas por e-mail, 42 responderam. Os convites foram enviados apenas a quem atuou como voluntário no ano passado, não a uma amostra aleatória. Entre as pessoas que responderam, 60% preferiram um evento pela manhã. Isso não estabelece a preferência de todos os moradores.
```

### ultra: pass

```text
Das 120 pessoas convidadas por e-mail, 42 responderam. Os convites foram enviados apenas aos voluntários do ano passado, não a uma amostra aleatória. Entre os respondentes, 60% preferiram um evento pela manhã. Isso não estabelece a preferência de todos os moradores.
```

### off: pass

```text
Quarenta e duas das 120 pessoas convidadas por e-mail responderam. Os convites foram enviados apenas a quem participou como voluntário no ano passado, e não a uma amostra aleatória. Das pessoas que responderam, 60% preferiram um evento pela manhã. Isso não estabelece a preferência de todos os moradores.
```

## modes-pt-BR-087 · translation

Source task:

> Traduza para português do Brasil: “You must return the key before leaving. You may keep the paper map. If the desk is closed, put the key in the box marked KEY-5. This exception does not permit you to take the key home.”

### baseline: pass

```text
Você deve devolver a chave antes de sair. Você pode ficar com o mapa de papel. Se o balcão estiver fechado, coloque a chave na caixa identificada como KEY-5. Essa exceção não permite que você leve a chave para casa.
```

### lite: pass

```text
Você deve devolver a chave antes de sair. Você pode ficar com o mapa de papel. Se o balcão estiver fechado, coloque a chave na caixa identificada como KEY-5. Essa exceção não permite que você leve a chave para casa.
```

### full: pass

```text
Você deve devolver a chave antes de sair. Você pode ficar com o mapa de papel. Se o balcão estiver fechado, coloque a chave na caixa identificada como KEY-5. Essa exceção não permite que você leve a chave para casa.
```

### ultra: pass

```text
Você deve devolver a chave antes de sair. Pode ficar com o mapa de papel. Se o balcão estiver fechado, coloque a chave na caixa identificada como KEY-5. Essa exceção não permite levar a chave para casa.
```

### off: pass

```text
Você deve devolver a chave antes de sair. Você pode ficar com o mapa de papel. Se o balcão estiver fechado, coloque a chave na caixa identificada como KEY-5. Essa exceção não permite que você leve a chave para casa.
```

## modes-pt-BR-088 · translation

Source task:

> O idioma de destino é português do Brasil. Traduza sem trocar as unidades: “Measured output rose from 16 to 20 metres per minute, a 25% increase. The same belt was used, but the loads differed. We have not established that the new motor caused the increase.”

### baseline: pass

```text
A produção medida passou de 16 para 20 metros por minuto, um aumento de 25%. Foi utilizada a mesma correia, mas as cargas eram diferentes. Não estabelecemos que o novo motor tenha causado o aumento.
```

### lite: pass

```text
A produção medida aumentou de 16 para 20 metros por minuto, um aumento de 25%. A mesma correia foi usada, mas as cargas eram diferentes. Não estabelecemos que o novo motor tenha causado o aumento.
```

### full: pass

```text
A produção medida passou de 16 para 20 metros por minuto, um aumento de 25%. Foi usada a mesma correia, mas as cargas eram diferentes. Não estabelecemos que o novo motor tenha causado o aumento.
```

### ultra: pass

```text
A produção medida subiu de 16 para 20 metros por minuto, um aumento de 25%. Foi usada a mesma correia, mas as cargas eram diferentes. Não estabelecemos que o novo motor causou o aumento.
```

### off: pass

```text
A produção medida aumentou de 16 para 20 metros por minuto, um aumento de 25%. Foi utilizada a mesma correia, mas as cargas eram diferentes. Não estabelecemos que o novo motor tenha causado o aumento.
```

## modes-pt-BR-089 · translation

Source task:

> O idioma de destino é português do Brasil. Traduza mantendo o tom cortês: “Thank you, Morgan, for reporting the open gate. It was closed after your call, but the log does not name the person who closed it. We have requested a latch inspection; no result is available yet.”

### baseline: pass

```text
Agradecemos, Morgan, por informar que o portão estava aberto. Ele foi fechado após sua ligação, mas o registro não identifica a pessoa que o fechou. Solicitamos uma inspeção do trinco; ainda não há resultado disponível.
```

### lite: pass

```text
Agradecemos, Morgan, por informar que o portão estava aberto. Ele foi fechado após sua ligação, mas o registro não identifica a pessoa que o fechou. Solicitamos uma inspeção do trinco; ainda não há resultado disponível.
```

### full: pass

```text
Agradecemos, Morgan, por avisar que o portão estava aberto. Ele foi fechado após sua ligação, mas o registro não identifica quem o fechou. Solicitamos uma inspeção do trinco; ainda não há resultado disponível.
```

### ultra: pass

```text
Agradecemos, Morgan, por avisar que o portão estava aberto. Ele foi fechado após sua ligação, mas o registro não identifica quem o fechou. Solicitamos uma inspeção do trinco; ainda não há resultado disponível.
```

### off: pass

```text
Agradecemos, Morgan, por informar que o portão estava aberto. Ele foi fechado após sua ligação, mas o registro não identifica a pessoa que o fechou. Solicitamos uma inspeção do trinco; ainda não há resultado disponível.
```

## modes-pt-BR-090 · translation

Source task:

> O idioma de destino é português do Brasil. Traduza todo o texto: “The shipment contains six crates, not six individual pumps. Each crate holds four pumps. One crate is blocked pending inspection. The inspection is planned but has not taken place.”

### baseline: pass

```text
A remessa contém seis engradados, não seis bombas individuais. Cada engradado contém quatro bombas. Um engradado está bloqueado, aguardando inspeção. A inspeção está planejada, mas ainda não foi realizada.
```

### lite: pass

```text
A remessa contém seis caixotes, não seis bombas individuais. Cada caixote contém quatro bombas. Um caixote está bloqueado até que seja realizada a inspeção. A inspeção está planejada, mas ainda não foi realizada.
```

### full: pass

```text
A remessa contém seis caixotes, não seis bombas individuais. Cada caixote contém quatro bombas. Um caixote está bloqueado até a inspeção. A inspeção está planejada, mas ainda não foi realizada.
```

### ultra: pass

```text
A remessa contém seis engradados, não seis bombas individuais. Cada engradado contém quatro bombas. Um engradado está bloqueado até a inspeção. A inspeção está planejada, mas ainda não foi realizada.
```

### off: pass

```text
A remessa contém seis engradados, não seis bombas individuais. Cada engradado contém quatro bombas. Um engradado está bloqueado, aguardando inspeção. A inspeção está planejada, mas ainda não foi realizada.
```

## modes-pt-BR-091 · translation

Source task:

> Traduza a regra para português do Brasil: “Walk-in attendance is allowed only if places remain. Minors must still bring written consent. Adults do not need that consent. Registering in advance does not guarantee parking.”

### baseline: pass

```text
A participação sem inscrição prévia só é permitida se ainda houver vagas. Menores de idade ainda devem trazer autorização por escrito. Adultos não precisam dessa autorização. A inscrição antecipada não garante vaga no estacionamento.
```

### lite: pass

```text
A participação sem inscrição prévia é permitida somente se ainda houver vagas. Menores de idade ainda devem trazer consentimento por escrito. Adultos não precisam desse consentimento. A inscrição antecipada não garante estacionamento.
```

### full: pass

```text
A participação sem inscrição prévia só é permitida se ainda houver vagas. Menores de idade devem trazer autorização por escrito. Adultos não precisam dessa autorização. A inscrição antecipada não garante vaga de estacionamento.
```

### ultra: pass

```text
A participação sem inscrição prévia só é permitida se ainda houver vagas. Menores de idade ainda devem apresentar consentimento por escrito. Adultos não precisam desse consentimento. A inscrição antecipada não garante vaga no estacionamento.
```

### off: pass

```text
A participação sem inscrição prévia é permitida somente se ainda houver vagas. Menores de idade ainda devem trazer consentimento por escrito. Adultos não precisam desse consentimento. A inscrição antecipada não garante vaga no estacionamento.
```

## modes-pt-BR-092 · translation

Source task:

> O idioma de destino é português do Brasil. Traduza sem mudar o estado do pedido: “The record says, ‘Not yet authorized.’ That does not mean the application was rejected. Review is continuing, and no decision date has been given.”

### baseline: pass

```text
O registro diz: “Ainda não autorizado”. Isso não significa que o pedido foi rejeitado. A análise continua, e nenhuma data para a decisão foi informada.
```

### lite: pass

```text
O registro diz: “Ainda não autorizado”. Isso não significa que o pedido foi rejeitado. A análise continua, e nenhuma data para a decisão foi informada.
```

### full: pass

```text
O registro diz: “Ainda não autorizado.” Isso não significa que o pedido foi rejeitado. A análise continua, e nenhuma data para a decisão foi informada.
```

### ultra: pass

```text
O registro diz: “Ainda não autorizado”. Isso não significa que o pedido foi rejeitado. A análise continua, e nenhuma data para a decisão foi informada.
```

### off: pass

```text
O registro diz: “Ainda não autorizado.” Isso não significa que o pedido foi rejeitado. A análise continua, e nenhuma data para a decisão foi informada.
```

## modes-pt-BR-093 · translation

Source task:

> O idioma de destino é português do Brasil. Traduza todo o aviso: “Changing a booking is free, but you must contact us by noon two days before the appointment. Same-day changes are not accepted. A cancellation refund depends on the payment method and is not guaranteed.”

### baseline: pass

```text
Alterar uma reserva é gratuito, mas você deve entrar em contato conosco até o meio-dia de dois dias antes do horário agendado. Alterações no mesmo dia não são aceitas. O reembolso em caso de cancelamento depende da forma de pagamento e não é garantido.
```

### lite: pass

```text
Alterar uma reserva é gratuito, mas você deve entrar em contato conosco até o meio-dia de dois dias antes do horário agendado. Alterações no mesmo dia não são aceitas. O reembolso por cancelamento depende da forma de pagamento e não é garantido.
```

### full: pass

```text
Alterar uma reserva é gratuito, mas você deve entrar em contato conosco até o meio-dia de dois dias antes do horário agendado. Não são aceitas alterações no mesmo dia. O reembolso em caso de cancelamento depende da forma de pagamento e não é garantido.
```

### ultra: pass

```text
Alterar uma reserva é gratuito, mas você deve entrar em contato conosco até o meio-dia de dois dias antes do horário agendado. Não são aceitas alterações no mesmo dia. O reembolso em caso de cancelamento depende da forma de pagamento e não é garantido.
```

### off: pass

```text
Alterar uma reserva é gratuito, mas você deve entrar em contato conosco até o meio-dia de dois dias antes do horário agendado. Não são aceitas alterações no mesmo dia. O reembolso em caso de cancelamento depende da forma de pagamento e não é garantido.
```

## modes-pt-BR-094 · translation

Source task:

> Traduza para português do Brasil e preserve os identificadores: “Sensor T-12 read 18.7 °C once at 08:15. Afternoon temperature was not measured. The file is /data/T-12.csv. The name of the person who measured it was not recorded.”

### baseline: pass

```text
O sensor T-12 registrou 18,7 °C uma única vez, às 08:15. A temperatura da tarde não foi medida. O arquivo é /data/T-12.csv. O nome da pessoa que fez a medição não foi registrado.
```

### lite: pass

```text
O sensor T-12 registrou 18,7 °C uma única vez, às 08:15. A temperatura da tarde não foi medida. O arquivo é /data/T-12.csv. O nome da pessoa que fez a medição não foi registrado.
```

### full: pass

```text
O sensor T-12 registrou 18,7 °C uma única vez, às 08:15. A temperatura da tarde não foi medida. O arquivo é /data/T-12.csv. O nome da pessoa que fez a medição não foi registrado.
```

### ultra: pass

```text
O sensor T-12 registrou 18,7 °C uma única vez, às 08:15. A temperatura da tarde não foi medida. O arquivo é /data/T-12.csv. O nome da pessoa que fez a medição não foi registrado.
```

### off: pass

```text
O sensor T-12 registrou 18,7 °C uma única vez, às 08:15. A temperatura da tarde não foi medida. O arquivo é /data/T-12.csv. O nome da pessoa que fez a medição não foi registrado.
```

## modes-pt-BR-095 · translation

Source task:

> O idioma de destino é português do Brasil. Traduza a mensagem inteira: “The order can leave only after the supervisor approves it and the funds arrive. A payment screenshot does not show cleared funds. Collection is optional, but both conditions still apply. No dispatch date is stated.”

### baseline: pass

```text
O pedido só pode sair após a aprovação do supervisor e o recebimento dos fundos. Uma captura de tela do pagamento não comprova que os fundos foram compensados. A retirada é opcional, mas ambas as condições continuam se aplicando. Nenhuma data de envio foi informada.
```

### lite: pass

```text
O pedido só pode sair depois que o supervisor o aprovar e os fundos forem recebidos. Uma captura de tela do pagamento não comprova que os fundos foram compensados. A retirada é opcional, mas ambas as condições continuam valendo. Nenhuma data de envio é informada.
```

### full: pass

```text
O pedido só pode sair depois que o supervisor o aprovar e os fundos forem recebidos. Uma captura de tela do pagamento não comprova que os fundos foram compensados. A retirada é opcional, mas ambas as condições continuam válidas. Nenhuma data de envio foi informada.
```

### ultra: pass

```text
O pedido só pode sair após a aprovação do supervisor e o recebimento dos fundos. Uma captura de tela do pagamento não comprova que os fundos foram compensados. A retirada é opcional, mas ambas as condições continuam valendo. Nenhuma data de envio foi informada.
```

### off: pass

```text
O pedido só pode sair depois que o supervisor o aprovar e os fundos forem recebidos. Uma captura de tela do pagamento não comprova que os fundos foram compensados. A retirada é opcional, mas ambas as condições continuam se aplicando. Nenhuma data de envio foi informada.
```

## modes-pt-BR-096 · translation

Source task:

> O idioma de destino é português do Brasil. Traduza preservando o código: “The log shows ERR_63, but this does not prove that the file is damaged. The checker has not read the whole file. The engineer considers a dropped connection one possible cause; the cause is not established.”

### baseline: pass

```text
O registro mostra ERR_63, mas isso não prova que o arquivo esteja danificado. O verificador não leu o arquivo inteiro. O engenheiro considera uma queda de conexão uma possível causa; a causa não foi estabelecida.
```

### lite: flagged

```text
O log mostra ERR_63, mas isso não prova que o arquivo está danificado. O verificador não leu o arquivo inteiro. A pessoa responsável pela engenharia considera uma queda de conexão uma possível causa; a causa não foi estabelecida.
```

Review notes: Preserves the numbered invariants but changes the engineer’s role by adding responsibility for engineering. / Preserva o conteúdo material; “responsável pela engenharia” é menos preciso que a designação profissional original.

### full: pass

```text
O registro mostra ERR_63, mas isso não prova que o arquivo esteja danificado. O verificador não leu o arquivo inteiro. A pessoa que atua como engenheira considera uma queda de conexão uma possível causa; a causa não foi estabelecida.
```

### ultra: pass

```text
O log mostra ERR_63, mas isso não prova que o arquivo está danificado. O verificador ainda não leu o arquivo inteiro. A pessoa da engenharia considera uma queda de conexão uma possível causa; a causa não está estabelecida.
```

### off: pass

```text
O registro mostra ERR_63, mas isso não prova que o arquivo esteja danificado. O verificador não leu o arquivo inteiro. O profissional de engenharia considera uma queda de conexão uma possível causa; a causa não foi estabelecida.
```

## modes-pt-BR-097 · translation

Source task:

> O idioma de destino é português do Brasil. Traduza todo o parágrafo: “The parcel was placed at reception after Jo's phone call. We do not know who delivered it. Reception recorded arrival at 12:35. That time does not show when the parcel left the depot.”

### baseline: pass

```text
A encomenda foi colocada na recepção após a ligação de Jo. Não sabemos quem a entregou. A recepção registrou a chegada às 12:35. Esse horário não indica quando a encomenda saiu do depósito.
```

### lite: pass

```text
A encomenda foi colocada na recepção após a ligação de Jo. Não sabemos quem a entregou. A recepção registrou a chegada às 12:35. Esse horário não indica quando a encomenda saiu do depósito.
```

### full: pass

```text
A encomenda foi colocada na recepção após a ligação de Jo. Não sabemos quem a entregou. A recepção registrou a chegada às 12:35. Esse horário não indica quando a encomenda saiu do depósito.
```

### ultra: pass

```text
A encomenda foi colocada na recepção após a ligação de Jo. Não sabemos quem a entregou. A recepção registrou a chegada às 12:35. Esse horário não indica quando a encomenda saiu do depósito.
```

### off: pass

```text
A encomenda foi colocada na recepção após a ligação de Jo. Não sabemos quem a entregou. A recepção registrou a chegada às 12:35. Esse horário não indica quando a encomenda saiu do depósito.
```

## modes-pt-BR-098 · translation

Source task:

> O idioma de destino é português do Brasil. Traduza sem converter moeda: “The quote is US$980 including tax. Optional installation is estimated at US$120–US$170 and is not included. The product price is valid until 16 November 2030; this is not a required purchase deadline.”

### baseline: pass

```text
O valor cotado é de US$980, incluindo impostos. A instalação opcional está estimada entre US$120 e US$170 e não está incluída. O preço do produto é válido até 16 de novembro de 2030; essa data não é um prazo obrigatório para a compra.
```

### lite: pass

```text
O orçamento é de US$980, incluindo impostos. A instalação opcional está estimada entre US$120 e US$170 e não está incluída. O preço do produto é válido até 16 de novembro de 2030; essa data não é um prazo obrigatório para a compra.
```

### full: pass

```text
O valor cotado é de US$980, incluindo impostos. A instalação opcional é estimada em US$120–US$170 e não está incluída. O preço do produto é válido até 16 de novembro de 2030; essa data não é um prazo obrigatório para a compra.
```

### ultra: pass

```text
O valor do orçamento é US$980, incluindo impostos. A instalação opcional está estimada em US$120–US$170 e não está incluída. O preço do produto é válido até 16 de novembro de 2030; essa data não é um prazo obrigatório para a compra.
```

### off: pass

```text
O orçamento é de US$980, incluindo impostos. A instalação opcional está estimada em US$120–US$170 e não está incluída. O preço do produto é válido até 16 de novembro de 2030; essa data não é um prazo obrigatório para a compra.
```

## modes-pt-BR-099 · translation

Source task:

> O idioma de destino é português do Brasil. Traduza integralmente: “The reading room opens on Thursdays from 09:30 to 13:30. Visitors may photograph cleared documents but must register every requested box. Photography is optional. Restricted material requires written permission before access.”

### baseline: pass

```text
A sala de leitura abre às quintas-feiras, das 09:30 às 13:30. Os visitantes podem fotografar documentos liberados, mas devem registrar cada caixa solicitada. Fotografar é opcional. O material restrito exige autorização por escrito antes do acesso.
```

### lite: pass

```text
A sala de leitura abre às quintas-feiras, das 09:30 às 13:30. Visitantes podem fotografar documentos liberados, mas devem registrar cada caixa solicitada. Fotografar é opcional. O acesso a materiais restritos exige autorização por escrito antes do acesso.
```

### full: pass

```text
A sala de leitura abre às quintas-feiras, das 09:30 às 13:30. Visitantes podem fotografar documentos liberados, mas devem registrar cada caixa solicitada. Fotografar é opcional. O acesso a material restrito exige autorização por escrito antes do acesso.
```

### ultra: pass

```text
A sala de leitura abre às quintas-feiras, das 09:30 às 13:30. Visitantes podem fotografar documentos liberados, mas devem registrar cada caixa solicitada. Fotografar é opcional. O acesso a material restrito exige autorização prévia por escrito.
```

### off: pass

```text
A sala de leitura abre às quintas-feiras, das 09:30 às 13:30. Visitantes podem fotografar documentos liberados, mas devem registrar cada caixa solicitada. Fotografar é opcional. O material restrito exige autorização por escrito antes do acesso.
```

## modes-pt-BR-100 · translation

Source task:

> O idioma de destino é português do Brasil. Traduza o texto completo: “The survey involved 75 volunteers from one association. Forty-five supported weekend classes. Participants were not selected randomly. These figures do not show the opinion of everyone in the district.”

### baseline: pass

```text
A pesquisa envolveu 75 voluntários de uma associação. Quarenta e cinco apoiaram aulas nos fins de semana. Os participantes não foram selecionados aleatoriamente. Esses números não mostram a opinião de todos no distrito.
```

### lite: pass

```text
A pesquisa envolveu 75 voluntários de uma única associação. Quarenta e cinco apoiaram aulas nos fins de semana. Os participantes não foram selecionados aleatoriamente. Esses números não mostram a opinião de todas as pessoas do distrito.
```

### full: pass

```text
A pesquisa envolveu 75 voluntários de uma única associação. Quarenta e cinco apoiaram aulas nos fins de semana. Os participantes não foram selecionados aleatoriamente. Esses números não mostram a opinião de todas as pessoas do distrito.
```

### ultra: pass

```text
A pesquisa envolveu 75 voluntários de uma única associação. Quarenta e cinco apoiaram aulas nos fins de semana. Os participantes não foram selecionados aleatoriamente. Esses números não mostram a opinião de todas as pessoas do distrito.
```

### off: pass

```text
A pesquisa envolveu 75 voluntários de uma associação. Quarenta e cinco apoiaram aulas nos fins de semana. Os participantes não foram selecionados aleatoriamente. Esses números não mostram a opinião de todas as pessoas do distrito.
```

