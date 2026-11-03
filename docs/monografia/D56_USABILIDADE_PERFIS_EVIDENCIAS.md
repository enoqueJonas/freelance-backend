# D56 — Gestão contextual dos perfis: revisão de UX com critérios verificáveis

**Data:** 03-11-2026.  
**Documento académico de referência:** `Monografia_D44_Metodologia_Proveniencia_Verificada.docx`, não modificada.  
**Código:** [PR frontend D56 #5](https://github.com/enoqueJonas/freelance-frontend/pull/5), dependente do [PR D55 #4](https://github.com/enoqueJonas/freelance-frontend/pull/4).  
**Backend de ensaio:** revisão D55 `3752c14e3cfef7bfd20a4de7a70f762fcf51ea08`, [PR backend #7](https://github.com/enoqueJonas/freelance-backend/pull/7).

## 1. Problema que motivou a alteração

A auditoria visual D54–D55 revelou que a página `/#/real` apresentava dois grandes formulários de activação de perfil (trabalhador e empregador) mesmo quando a pessoa tinha iniciado uma tarefa diferente. No ecrã móvel, a área dos formulários ocupava parte desproporcionada do espaço disponível. A presença de secções vazias para funções não activadas e a sequência numerada «2, 3, 4» numa conta sem perfil também prejudicavam a orientação.

**Estas são observações do auditor sobre a interface capturada**, não resultados de entrevistas ou medições com utilizadores representativos.

## 2. Alterações implementadas na UI

- A página mostra dois cartões compactos «Trabalhador» e «Empregador» com estado `Activo` ou `Não activado`.
- Os formulários ficam fechados até à acção «Adicionar perfil…»; apenas um formulário pode estar aberto de cada vez.
- `aria-expanded`, `aria-controls` e nomes acessíveis foram adicionados, permitindo testar a navegação pelo teclado.
- Depois de uma criação confirmada pela API, o respectivo formulário fecha e o cartão mostra o estado actualizado; uma falha não deve apresentar sucesso artificial.
- O segundo perfil continua **opcional** e pode ser activado na mesma conta, preservando a regra RN01; a proibição de contratar a si próprio mantém-se no backend (RN02).
- A visão de «Minhas oportunidades e propostas» só aparece para contas com Employer. A área de acordos só aparece quando existe pelo menos um perfil activado. Foram removidos números rígidos dos títulos, que deixavam de corresponder à navegação personalizada.
- O logout continua a eliminar campos temporários de sessão, incluindo dados de perfil de outra conta.

**Não foi alterada a implementação de pagamentos, avaliações, conflitos ou assinaturas electrónicas.**

## 3. Matriz de critérios e evidência

| Critério | Evidência técnica solicitada | Limites científicos |
|---|---|---|
| UX-02.1 — Nenhum formulário aberto inicialmente | Teste de browser de ambas as opções fechadas e screenshot | Observação técnica, não teste de compreensão humana |
| UX-02.2 — Apenas um formulário de cada vez | Abrir Worker e depois Employer, verificando o fecho do primeiro | Não estabelece preferências da população-alvo |
| UX-02.3 — Perfis acumuláveis | Criar segundo perfil na mesma conta **depois** de executar contratação e conservar o histórico | Não altera a necessidade de autorização de recursos |
| UX-02.4 — Painéis por papel | Empregador vê oportunidades próprias; trabalhador sem Employer não vê painel de gestão de empregador | É desenho contextual, não teste da melhor experiência para participantes |
| UX-02.5 — Teclado e viewport móvel | Enter para abrir Worker, alternar para Employer, fechar, com 390×844 px | Não é auditoria WCAG nem teste com dispositivos físicos |
| UX-02.6 — Fluxo de contratação não regrediu | Playwright repete oportunidade → proposta → acordo v1/v2 → rejeição v3 com Django real | Não cobre todas as transições, concorrência nem pagamentos |

A execução anterior, antes do refinamento final dos painéis, foi aprovada em [D56 CI #41611095291](https://github.com/enoqueJonas/freelance-frontend/actions/runs/41611095291): **2/2 cenários Chromium**, além do typecheck e build. Produziu [nove PNG autênticos](https://github.com/enoqueJonas/freelance-frontend/actions/runs/41611095291/artifacts/13219206876), com vencimento previsto para 03-12-2026. Os PNG 07–09 foram recuperados e inspeccionados visualmente; a revisão visual revelou a necessidade de esconder os painéis não aplicáveis e retirar a numeração rígida.

**O refinamento final está sujeito à reexecução do CI na revisão mais recente.** Não reutilizar o resultado anterior como prova de alterações posteriores até confirmar os logs da última execução.

## 4. Consequências para a monografia

**RN01:** a interface mantém a possibilidade de acumular ambos os perfis.  
**RN02:** a API mantém a proibição de autocontratação; a activação do perfil secundário não altera essa guarda.  
**RF03/RF04:** criação de perfis e confirmação de estado na UI, sem afirmar edição/eliminação completa.  
**RNF de usabilidade:** existem melhorias observáveis na interface e testes técnicos de navegação; não há evidência de melhoria estatística da usabilidade junto de participantes reais.

**Redacção académica candidata, não inserida na D44:**

> Na revisão do protótipo, a activação dos perfis de trabalhador e empregador foi reorganizada de modo a apresentar inicialmente apenas as opções disponíveis, abrindo-se o formulário correspondente após escolha explícita. A implementação conserva a possibilidade de uma conta acumular ambos os perfis, embora não permita que a mesma identidade constitua as duas partes de uma contratação. A revisão foi submetida a verificações automatizadas de interface e de integração, incluindo navegação por teclado em uma dimensão de ecrã móvel. Esses ensaios documentam comportamentos técnicos da interface, não constituindo uma avaliação de usabilidade com participantes do estudo.

A autora deve decidir se este nível de implementação compõe efectivamente a versão do protótipo apresentada no trabalho, identificar commit e data, e seguir o manual institucional para descrição de figuras e evidências. Não declarar hipóteses HG/HE1–HE4 comprovadas por este resultado.

## 5. Pendências e critérios de fecho

- [x] Refactor dos formulários para gestão contextual e acessível.
- [x] Suporte dual Worker+Employer na mesma conta, sem atalhos de autenticação fictícia.
- [x] Testes novos de mobile/teclado e preservação do histórico de propostas/contratações.
- [x] Nove capturas obtidas na primeira execução D56 do Chromium.
- [ ] Confirmar **última** execução do CI após remover painéis não pertinentes e números de secção.
- [ ] Inspeccionar a última captura móvel e verificar rótulos, alinhamentos e legibilidade.
- [ ] Recolher opiniões de utilizadores representativos; não presumir ganhos de produtividade ou satisfação.
- [ ] Integrar no **DOCX D44 original** somente o conteúdo aceite pela autora/supervisão, preservando comentários, imagens, campos e margens.

**O Word canónico e os comentários do supervisor permanecem inalterados.**
