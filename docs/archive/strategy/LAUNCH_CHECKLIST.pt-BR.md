# Checklist de publicação no GitHub

## Antes de tornar público

- [x] Definir nome e owner: `hevertonrodrigues/asdify`.
- [ ] Verificar conflitos relevantes de marca/nome e definir domínio apenas se necessário.
- [x] Usar `https://github.com/hevertonrodrigues/asdify` nas instruções.
- [ ] Definir maintainers e política de resposta a issues.
- [ ] Revisar licença MIT, autoria e créditos.
- [ ] Confirmar que nenhum arquivo contém segredo, dado pessoal, token ou conteúdo de terceiros não autorizado.
- [ ] Rodar `python3 scripts/validate.py`.
- [ ] Rodar `python3 -m unittest discover -s tests -v`.
- [ ] Testar instalação em diretórios temporários e depois em Claude Code, Codex e Cursor reais.
- [ ] Verificar todas as instruções de ativação nas versões oficiais atuais.
- [ ] Conferir README em inglês e português, incluindo links relativos e exemplos.
- [ ] Criar capa opcional apenas se contribuir com clareza visual, sem copiar a identidade Ponytail.

## Lançamento

- [x] Posicionar o produto na raiz do repositório.
- [ ] Publicar o repositório público no GitHub.
- [ ] Configurar descrição curta, topics e branch protection.
- [ ] Habilitar GitHub Actions e verificar execução verde.
- [ ] Publicar release `v0.1.0` com changelog e limitações conhecidas.
- [ ] Abrir issues de roadmap e label `good first issue` para tarefas reais.
- [ ] Divulgar com demonstrações verificáveis, não com promessas sem dados.

## Depois do lançamento

- [ ] Executar protocolo A/B real, cego e reprodutível.
- [ ] Publicar outputs brutos, métricas de fidelidade e falhas relevantes.
- [ ] Consertar regressões antes de dizer que o método melhora qualidade.
- [ ] Manter CHANGELOG e lista de compatibilidade por host.

Consulte `./docs/LAUNCH.md` para o plano mais detalhado existente na primeira versão.
