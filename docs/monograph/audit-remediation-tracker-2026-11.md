# Plano de auditoria e remediação integral da monografia — 2026-11-01

## Contexto e governação

- Repositório: `enoqueJonas/freelance-backend`, ramo `docs/audit-baseline`.
- Documento de referência local da revisão: **D17 — Monografia_D17_1.8_Delimitacao_do_Tema.docx** (o ficheiro binário é entregue no chat, não está armazenado neste repositório).
- Fontes normativas obrigatórias: [especificações USTM](ustm-monograph-specifications.md) e [benchmark Blockchain](blockchain-benchmark-rules.md). Quando há conflito, prevalece o Manual USTM.
- Fontes de domínio: [plano de reconstrução](reconstruction-plan.md), [baseline de requisitos](../research/requirements-final-baseline.md), matriz documental/entrevistas e modelação aprovadas no repositório.
- **Impedimento administrativo:** tentativa de criar 14 GitHub Issues em 2026-11-01 devolveu HTTP 410: *Issues has been disabled in this repository*. Este documento é a lista de trabalho versionada substitutiva. Não declarar que as Issues foram criadas.
- **Regra de fecho:** revisão textual ≠ execução de teste ≠ validação por utilizadores. Cada tarefa exige artefacto, verificação e evidência. Nunca marcar `[x]` apenas por existir uma descrição.

## Situação auditada em D17

O documento possui 7 capítulos numerados (I–VI mais VII Referências), 8 quadros/tabelas Word, 2 imagens inline e **21 blocos literais `[PLACEHOLDER]`**: Figura 2.1, Quadro 2.2, Figuras 5.1–5.12 e Figuras 5.13–5.19. Identificada hierarquia irregular em 5.2 (5.2.1 → 5.2.1.2). A secção 1.9 ainda enumera objectivos antes de hipóteses e deve reflectir a ordem real. Há documentação de implementação parcial; não inferir testes completos. O total de páginas do ficheiro não substitui a contagem do corpo da Introdução às Referências (limite USTM: 60).

## Estado e critérios por tarefa

### P0 — ordem de execução prioritária

- [x] **M01 — Fechar 1.9 Estrutura do trabalho.** Corrigir ordem hipóteses→objectivos, descrever exactamente capítulos I–VI e referências; comparar 1.3–1.9 com os títulos reais; renderizar e inspeccionar as páginas adjacentes. **Artefacto:** nova versão controlada do DOCX.
- [ ] **M02 — Pré-textuais.** Verificar capa/folha de rosto, nomes, título, supervisor, moldura, declaração/agradecimentos quando aplicáveis, resumos PT/EN 100–200 palavras e 3–5 palavras-chave, índice e listas automáticos. **Gate:** campos actualizáveis e visual verificado.
- [ ] **M03 — Capítulo II (teoria e comparação).** Auditar precisão bibliográfica; explicar conceitos em profundidade, comparar criticamente plataformas/canais; produzir **Figura 2.1 e Quadro 2.2** com fontes verificadas, sem funcionalidades inventadas. **Gate:** suporte documental e coerência com o âmbito.
- [ ] **M04 — Capítulo III (métodos).** Reconciliar tipo de estudo, amostra intencional de 11 entrevistas T01–T08/E01–E03, análise temática, fontes documentais, triangulação, limites e desenvolvimento incremental. Não inventar consentimento, gravações, datas nem testes. **Gate:** rastreabilidade instrumentos→dados→análise.
- [ ] **M05 — Capítulo IV (dados e necessidades).** Conferir cada afirmação com evidências de entrevista e documentos, incluir convergências e divergências (T05, avaliação opcional, preço após diagnóstico, localização contextual), N01–N18; não usar percentagens populacionais. **Gate:** matriz evidência→necessidade auditável.
- [ ] **M06 — Requisitos e hierarquia do Capítulo V.** Corrigir 5.2.1/5.2.1.2; validar 16 RN, 28 RF, 7 RNF, 7 macro-requisitos, actores, quadros e referência no texto. **Gate:** necessidade→RN→RF/RNF→caso de uso→verificação.
- [ ] **M07 — 12 diagramas.** Substituir **Figuras 5.1–5.12**: casos de uso, classes, 4 actividades, 4 sequências, diagrama de estados de Engagement e arquitectura. Entregar fontes editáveis e verificar contra a baseline. **Gate:** imagens inseridas e inspeccionadas, sem fluxo inventado.
- [ ] **M08 — 7 figuras de interface.** Substituir **Figuras 5.13–5.19** por capturas reais do frontend em versão identificável; remover dados pessoais; não apresentar mock/localStorage como integração real. **Gate:** evidência executada e legendada.
- [ ] **M09 — Validação.** Rastrear V01–V08 e RNF01–RNF07; estabelecer passos, ambiente, entradas/saídas, critério e estado (passou/falhou/parcial/não executado); documentar limites. **Gate:** evidências reproduzíveis, não só apreciação narrativa.
- [ ] **M10 — Referências e fontes.** Cruzar todas as citações com a bibliografia e os PDFs, validar data/autoria/título/páginas, remover links impróprios e fontes não verificáveis; normas e legislação contextualizadas sem sobreafirmações. **Gate:** correspondência bidireccional.
- [ ] **M11 — Normalização técnica/visual global.** Legendas/cross-references e índices automáticos, margens USTM, TNR12, 1,5, títulos, paginação, tabelas, imagens, português moçambicano; eliminar placeholders, texto de trabalho, instruções internas ou de commit; render a 100% e inspecção integral. **Gate:** nenhum defeito aberto; corpo ≤60 páginas.
- [ ] **M12 — Gate científico-editorial final.** Comparar problema→pergunta→hipóteses→objectivos→metodologia→evidências→necessidades→requisitos→UML→implementação→validação→conclusão; resumos fiéis aos resultados. **Gate:** auditoria final assinada por evidências, não por presunção.

### Pendências adicionais identificadas na auditoria de 2026-11-01

- [ ] **M15 — Reconciliar 14 comentários do supervisor preservados no DOCX.** O pacote `word/comments.xml` contém 14 comentários, todos ainda sinalizados sem resolução formal. Rever caso a caso: delimitação temporal (não inventar datas), elementos pós-textuais, glossário, numerar figuras por capítulo, legendas/fontes de tabelas, população/amostra, identificação de actores e associações caso de uso→actor. Os comentários elogiosos/sem alteração concreta podem ser registados como informativos. **Gate:** matriz comentário→excerto actual→resposta→evidência; só retirar comentários com decisão fundamentada.
- [ ] **M16 — Retirar vestígios editoriais/metadiscursivos.** Há texto no parágrafo de abertura do Capítulo V que refere literalmente «monografia de referência», o que é inadequado ao manuscrito científico final; procurar também instruções internas, termos de commit e texto de produção. **Gate:** varrimento textual e visual sem conteúdo de processo ou notas para quem edita.

### P1 — dependentes de evidência e decisões técnicas

- [ ] **M13 — Capítulo VI.** Avaliar cada objectivo e hipótese contra evidência efectiva; evitar inferência causal de impacto; declarar limitações e recomendações rastreáveis. **Dependências:** M04–M09.
- [ ] **M14 — Reconciliar código e arquitectura, se o âmbito técnico for retomado.** Comparar commits do frontend/backend com o AS-IS documentado, perfis acumuláveis, Opportunity→Proposal→Engagement/AgreementVersion, pagamentos externos sem custódia e testes reais. **Regra:** a monografia deve descrever o código como ele está; não alterar o sistema só para legitimar afirmações. **Dependências:** requisitos e modelo aprovados.

## Marcos anteriores — estado NÃO revalidado nesta auditoria

O ciclo de edições D10–D17 actualizou, em sequência, 1.1 Contextualização, 1.2 Justificativa, 1.3 Problema, 1.4 Hipóteses, 1.5 Objectivos, 1.6 Metodologia, 1.7 Considerações éticas e 1.8 Delimitação. Estes marcos significam **texto revisto**, não aprovação automática da monografia completa nem validação empírica independente.

## Procedimento de execução de cada tarefa

1. Ler USTM, benchmark, tracker e artefactos de evidência relevantes.
2. Delimitar o bloco e registar o problema antes da alteração.
3. Alterar apenas o bloco seleccionado, preservando os demais.
4. Fazer verificações estruturais com scripts e renderizar DOCX em PNG.
5. Inspeccionar visualmente a secção e páginas limítrofes; na entrega final, **todas** as páginas.
6. Registar versão, evidência, pendências e resultado neste documento. Apenas então marcar como concluída.

## Diário de execução

- **2026-11-01:** auditoria inicial da D17 identificou 21 placeholders, salto de numeração em 5.2, inconsistência de 1.9 e lacunas de evidência de implementação. Tentativa de usar GitHub Issues bloqueada por configuração do repositório; backlog criado aqui.
- **2026-11-01 / M01:** concluída a revisão estritamente localizada da secção 1.9. Documento **D18 — Monografia_D18_1.9_Estrutura_do_Trabalho.docx**, 57 páginas. Comparação estrutural confirmou **exactamente dois parágrafos modificados**; renderizado; inspeccionadas efectivamente as páginas 16, 17 e 18. A secção descreve seis capítulos e referências, e coloca hipóteses antes de objectivos.
- **2026-11-01 / auditoria de comentários e campos:** detectados 14 comentários preexistentes e não formalmente resolvidos, `TOC` automático presente, mas **não foram encontrados campos `SEQ` para numeração automática de legendas nem bookmarks de referência**, pelo que o gate de legendas e referências cruzadas permanece aberto. A abertura do Capítulo V inclui uma menção metadiscursiva à «monografia de referência» (M16).
