# D52 — Evolução dos acordos versionados: evidência real de API e limites académicos

**Referência canónica da monografia:** `Monografia_D44_Metodologia_Proveniencia_Verificada.docx`, não modificada nesta revisão.  
**Referência técnica:** [PR #5 — D52](https://github.com/enoqueJonas/freelance-backend/pull/5), dependente de [PR #4 — D51](https://github.com/enoqueJonas/freelance-backend/pull/4) e [PR #3 — D50](https://github.com/enoqueJonas/freelance-backend/pull/3).  
**Evidência primária de execução técnica:** [GitHub Actions D52 #41483135110](https://github.com/enoqueJonas/freelance-backend/actions/runs/41483135110) — **65/65 testes Django aprovados**, sendo 18 D50 + 23 D51 + 24 D52. Migração `contracts.0002_agreement_lifecycle` aplicada e `makemigrations --check --dry-run` sem diferenças.

## 1. Nova função de engenharia efectivamente verificada

O backend implementa e testa a **evolução de versões de condições acordadas**. Enquanto uma v2 está `PROPOSED`, a v1 permanece `ACCEPTED`; a aceitação explícita pelas duas partes torna v2 `ACCEPTED` e v1 `SUPERSEDED`. Uma contraparte pode rejeitar a v2, produzindo `REJECTED` com autor, data e motivo, sem perder o acordo anterior. Após uma rejeição, é possível criar v3, preservando a numeração. A API exige que quem aceita/rejeita forneça a impressão digital SHA-256 da versão consultada.

São resultados reais de código Django/DRF testado em base de dados SQLite temporária; **não são testes do protótipo React nem de participantes reais**. Os checks passaram numa branch draft, não num ambiente de produção.

## 2. Relação com os artefactos académicos da D44

| Elemento | Facto técnico D52 | Afirmação académica defensável |
|---|---|---|
| RN06 — Alterações materiais | Versão posterior requer aceite de ambas as partes para substituir vigente | «O backend implementa uma proposta de versionamento e aceitação bilateral com testes unitários de API aprovados» |
| RF14 — Versionamento | v1/v2/v3, estados e rejeição preservados | «O comportamento central de RF14 está implementado no backend de teste», **não** «RF14 integralmente validado na aplicação» |
| RN14 — Histórico | Versões anteriores e rejeições permanecem; aceitações registadas com actor/tempo | «Há registos persistidos de histórico de acordo», **não** «auditoria imutável e juridicamente suficiente» |
| §5.2.6 / Fig. 5.2 | AgreementVersion 0..* e única vigente; edição proibida pelo protocolo | Harmonizar cardinalidade e estados apenas após decisão B1 autorizada |
| Fig. 5.4 / A.4(A–B) | Aceite explícito de ambos os intervenientes, rejeição de alteração | Actualizar diagramas de actividades e sequências coerentemente, sem presumir autoria de uma única acção |
| V03/V04 | 24 novos testes D52 de API e 23 D51 cobrem subconjuntos | **V03/V04 integrais permanecem não executados** até frontend e cenários completos |

## 3. Discussão proposta para §5.5 (redacção condicional, não aplicada)

> A evolução técnica posterior da componente de contratação permitiu implementar, no backend Django/DRF, um mecanismo de versionamento de condições acordadas. Nesse mecanismo, a versão vigente não é substituída pela simples apresentação de uma proposta de alteração; a nova versão passa a vigorar apenas após aceitação expressa pelas duas partes. A rejeição preserva o conteúdo e o histórico da versão anteriormente aceite. A implementação foi submetida a testes automatizados de API num ambiente isolado, com resultados documentados no respectivo repositório. Esta evidência reforça a viabilidade técnica do mecanismo previsto na especificação, mas não comprova a sua usabilidade, a integração com o frontend, a adequação ao público-alvo ou os efeitos da solução na prevenção de conflitos reais.

**Condição de inclusão:** só incorporar se a autora decidir que os ensaios D52 fazem parte da versão de protótipo submetida e indicar versão, data, método e evidências académicas aceites. **Não** inserir o texto desta auditoria, links GitHub, mensagens internas ou notas do processo de revisão na dissertação.

## 4. Segurança e validade — limites

- O SHA-256 utilizado identifica o conteúdo da versão. Não equivale a assinatura digital legalmente qualificada, autenticação independente, prova de não-repúdio ou garantia de imutabilidade contra acesso administrativo à base de dados.
- A verificação de concorrência sobre PostgreSQL está pendente; o CI usa SQLite.
- Só se exercitaram pedidos reais de API. O React utiliza ainda `mockApi`, pelo que V03/V04 não podem ser considerados end-to-end.
- Não há prova de que o mecanismo melhora a confiança, reduz o incumprimento ou corresponde a necessidades empiricamente confirmadas em Maputo.
- As decisões B/B1, dois aceites explícitos e rejeição exclusiva pela contraparte são **hipóteses de engenharia** ainda por confirmar com a supervisão.
- Não foram editadas as figuras, comentários do supervisor, bibliografia ou o ficheiro DOCX.

## 5. Rastreabilidade e próximos passos

- [x] Confirmar implementação e 65/65 testes com logs reais.
- [x] Preservar v1 vigente enquanto v2 pendente/rejeitada.
- [x] Persistir rejeição e histórico de versões.
- [ ] Rever a representação de vN/vN+1 nos diagramas e o texto da §5.5 com decisão da supervisão.
- [ ] Integrar frontend React/JWT e avaliar fluxo completo no browser.
- [ ] Executar testes de concorrência e integridade com PostgreSQL.
- [ ] Actualizar D44 canónica sem descartar comentários, figuras nem campos, quando bytes DOCX originais estiverem acessíveis.
