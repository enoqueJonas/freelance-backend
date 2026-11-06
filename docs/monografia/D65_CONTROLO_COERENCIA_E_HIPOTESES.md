# D65 — Controlo de alterações e portas de aceitação da discussão e conclusão

**Documento principal:** [D65 — discussão HG/HE1–HE4, §5.5 e Capítulo VI](D65_DISCUSSÃO_HIPOTESES_CAPITULOS_V_VI.md).  
**Origem auditada:** D44 `Monografia_D44_Metodologia_Proveniencia_Verificada.docx`, §§5.1, 5.2.8, 5.3–5.5 (pp. físicas 44, 58–63) e Capítulo VI (pp. 64–66).  
**Fundamentação:** [D57 matriz V01–V08/RNF](D57_MATRIZ_VALIDACAO_V01_V08_RNF.md), [D57 implementação e teste](D57_CAPITULO_V_REVISAO_INTEGRAL.md), [D60 transcrições](D60_CONFIRMACAO_TRANSCRICOES_LITERAIS.md), [D61 matriz DOC/ENT](D61_MATRIZ_DOCUMENTAL_APOIO_ENTREVISTAS.md), [D62 fontes](D62_AUDITORIA_FONTES_DOCUMENTAIS_N01_N18.md), [D63 Capítulo IV](D63_CAPITULO_IV_CONSOLIDADO_DOCUMENTAL.md) e [D64 Capítulo III](D64_CAPITULO_III_METODOLOGIA_CONSOLIDADA.md).

## 1. Mapa das correcções e respectiva situação

| Posição D44 | Inconsistência anterior | Material D65 | Estado |
|---|---|---|---|
| §5.1 p.44 | «resultados empíricos» como fonte directa geral da especificação | Requisitos principalmente documentais/engenharia; T/E como apoio selectivo | **Texto candidato** |
| §5.2.8 p.58 | Exclusão de funcionalidades justificada genericamente por «evidência recolhida» | Delimitações são decisões de engenharia, nem sempre consensuais nos relatos; N18 ≠ RF | **Texto candidato** |
| §§5.3.1–5.3.3 pp.59–61 | Toda a implementação descrita como `mockApi` + Django apenas accounts | D57 apresenta duas perspectivas datadas; ramos D50–D56 têm domínio parcial e React `/#/real` | **Não substituir §5.3 integral apenas por D65**: usar também D57 |
| Fig. 5.13–5.19 pp.61–62 | Sete placeholders e telas simuladas | D54–D56 têm capturas verdadeiras somente para partes de 5.13, 5.16, 5.17 | **Ainda não integradas nem renumeradas** |
| §5.4 pp.62–63 | V01–V08 = «Não executado» para todos, base inicial | D57/D65 V01–V03 **parcial**, V04–V08 **não executados como casos canónicos**; RNF02–05 parcial técnico | **Quadros da D44 ainda necessitam substituição controlada** |
| §5.5 pp.62–63 | Não há domínio backend; só simulação; sem entrevistas comprovadas | Quatro níveis DOC/ENT/ENG/TECH, teste parcial, discussão explícita HG/HE1–HE4 | **Redacção integral candidata** |
| §6.1 pp.64–65 | Entrevistas consideradas não realizadas e ciclo técnico sem backend | Onze transcrições literais, documental principal, protótipo D50–D56 parcial por branch, limites e hipóteses | **Redacção integral candidata** |
| §6.2 pp.65–66 | Recomenda «começar a integrar React/Django», apesar de corte D53–56 | Consolidar PRs reais, completar lacunas de execução/pagamento/reputação/conflitos e casos de aceitação | **Redacção integral candidata** |
| §§1.6–1.7; 3; 4 | Outras passagens contraditórias | D64 e D63 já contêm emendas coordenadas | **Ainda não aplicadas na D44** |

## 2. Matriz de conclusão das hipóteses: discriminar tipos de evidência

| Elemento | Evidência conceptual/documental | Depoimentos | Evidência técnica | Efeito em população-alvo | Linguagem conclusiva permitida |
|---|---|---|---|---|---|
| HG | Sim | Apoio pontual, não representativo | Parcial, fluxo contratação | **Não medido** | Suporte conceptual e demonstração técnica parcial |
| HE1 | Sim | Exemplos/contraexemplo T05 | Perfis, oportunidades, propostas parcialmente | **Não medido** | Parcialmente exercitada tecnicamente, V01/V02 incompletos |
| HE2 | Sim | T03/T06, T05/E02 | v1/v2/v3 acordos com aceites/rejeição | **Não medido** | Demonstração técnica parcial; V03 canónico não integral |
| HE3 | Sim | Reputação/contestação/queixas | Sem módulos reais completos | **Não medido** | Fundamentação conceptual, sem execução integral |
| HE4 | Sim | Algumas preferências a favor de escrow (contraste RN10) | Condições/valor, **não** pagamento realizado | **Não medido** | Fundamentação conceptual, V05 não executado |

**Proibição editorial:** «comprovada», «validada empiricamente» ou «reduziu fraudes» só quando se indicar protocolo e evidência que demonstrem o alcance exacto; nenhum dos ensaios automatizados D50–D56 responde a essa medição.

## 3. Verificações efectivamente feitas

- [x] Confrontados os textos da D44 em §§5.1, 5.2.8, 5.3–5.5 e §§6.1–6.2.
- [x] Inserida, no texto candidato D65, a mesma precedência das fontes que D63 e D64.
- [x] HG e **HE1–HE4** aparecem tanto no texto interpretativo como na matriz.
- [x] O estado de **V03** não foi confundido com V04.
- [x] Os resultados documentados D55/D56 mantêm valores separados: 80 testes API Django, 8 HTTP React, 2 Chromium; sem soma como testes académicos de aceitação.
- [x] Mantida a separação entre UI legada simulação e interface real `/#/real` em ramos de desenvolvimento.
- [x] Preservada a divergência entre **RN10 sem custódia própria** e preferências por escrow T02/T04/E01.
- [x] Mantida distinção entre transcrições literais declaradas e procedimentos de consentimento/registo não documentados.
- [x] Conclusão do quarto objectivo não chama «Aprovado» a V01–V03.
- [x] D65 publicada e conferida no ramo de auditoria.
- [ ] Aprovação formal da autora/supervisão e ratificação da baseline.
- [ ] Substituição controlada de figuras, quadros, §§5.3–5.4 e anexos **no DOCX**, não apenas em Markdown.
- [ ] Auditoria das páginas das fontes D62, ética/confidencialidade e cronologia.
- [ ] Renderização e revisão completa do Word/PDF original com comentários preservados.
- [ ] Resultados adicionais V01–V08/RNF, sem extrapolar da suíte já existente.

## 4. Dependências ainda bloqueadoras para declarar «monografia finalizada»

**P0 — Documento:** D44 original de 82 páginas tem texto indexado, mas nenhum fluxo de edição de bytes originais foi autorizado/verificado no Project. Não reconstruir .docx a partir de extracção.

**P0 — Cronologia:** a capa D44 diz «Setembro de 2025», enquanto pelo menos um relatório institucional e os ensaios técnicos são de 2026. A autora/supervisão devem seleccionar revisão e data institucional coerentes.

**P0 — Ética e transcrições:** antes de publicar os onze depoimentos completos como anexo, conferir procedimentos reais de recolha e consentimento e risco de reidentificação; não apresentar ausência de áudio como perda de registos, pois foi entregue um DOCX de transcrições literais.

**P1 — Aceitação:** V01–V03 são incompletos, V04–V08 não executados integralmente; RNF01/usabilidade com pessoas continua não executado. As hipóteses não ficam empiricamente demonstradas por testes automatizados.

## 5. Próximo passo de maior impacto

Passar **da redacção em relatórios para o manuscrito único**, se e quando houver bytes originais D44 acessíveis: preservar comentários/estilos/capa/quadros, aplicar D62–D65 de forma coordenada, anexar o guião e os onze depoimentos, resolver referências temporais, actualizar índices e renderizar DOCX/PDF. Caso ainda não seja possível editar a D44, a melhor actividade seguinte é validar fontes exactas e obter a decisão de autoria/supervisão sobre a **baseline**; outra ronda abstracta de reescrita não elimina estes bloqueios.

**Este controlo não é prova de que o manuscrito Word foi alterado.**
