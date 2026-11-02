# Auditoria D45 — Integridade dos diagramas UML, estados e referências cruzadas

**Documento de referência:** `Monografia_D44_Metodologia_Proveniencia_Verificada.docx`, pp. 44–58 e 68–82.  
**Repositórios examinados (leitura estática):**
- `enoqueJonas/freelance-frontend`, commit `f41d72e8ace6c716e799131cb46ce425a1a4c215` (27-05-2026).
- `enoqueJonas/freelance-backend`, commit `6617ddf1d6dc29ccdebef6adb91602cecafe26ab` (01-06-2026).

**Limite de prova:** o índice da Library disponibilizou o **texto extraído**, mas não os bytes DOCX nem as imagens renderizadas. Consequentemente, referências e descrições podem ser auditadas; a geometria, cardinalidades, setas e guards **dentro das figuras** permanecem `PENDENTE DE INSPECÇÃO VISUAL`. Nenhuma correcção foi integrada no DOCX.

## UML-01 — Salto na numeração das figuras do Capítulo V [P1]

Na extracção textual, as seguintes numerações são as únicas **legendas/referências do capítulo**:

| Identificador | Página do ficheiro | Identificação textual |
|---|---:|---|
| 5.1 | 48 | Casos de uso centrais |
| 5.2 | 50 | Diagrama de classes |
| 5.3 | 52 | Actividade DA01 |
| 5.4 | 54 | Actividade DA02 |
| 5.5–5.10 | — | **Não localizadas no texto extraído** |
| 5.11 | 57 | Estados da contratação (Engagement) |
| 5.12 | 58 | Arquitectura lógica |
| 5.13–5.19 | 61–62 | Sete marcadores `[PLACEHOLDER]`, sem capturas reais |

A Figura 2.1 encontra-se no Capítulo II. No Apêndice A aparecem A.1, A.2, A.3(A–C), A.4(A–B), A.5(A–C) e A.6(A–C).

**Acções:** verificar no documento renderizado se 5.5–5.10 existem realmente e se apenas as legendas não foram extraídas. Se estiverem ausentes, corrigir a sequência **em toda a obra**, incluindo legendas, remissões no texto, índice de figuras (se existir) e campos `SEQ`/`REF`. Não reservar números vazios. Não aplicar renumeração automática antes da inspecção de todas as figuras.

## UML-02 — Contrato de estados do modelo-alvo [preservar e tornar verificável]

A narrativa das pp. 49, 53–57 e o plano de teste V02–V07 (p. 81) estabelece os invariantes abaixo. A tabela descreve **condições a formalizar/testar**; não declara transições confirmadas por execução nem prova que a imagem siga todas as regras.

| Entidade / evento | Estado inicial | Próximo estado esperado | Condição de negócio / evidência necessária |
|---|---|---|---|
| Opportunity: publicação | DRAFT (a confirmar no desenho) | OPEN | Empregador autorizado, dados obrigatórios, localização quando relevante (RN02, RN04; RF07) |
| Proposal: aceitação | PENDING | ACCEPTED | Oportunidade elegível em OPEN, empregador é titular, trabalhador não é a mesma conta (RN02, RF11–RF12) |
| Engagement: proposta aceite | inexistente | PENDING_AGREEMENT | Criado a partir de uma proposta aceite sem activar automaticamente a execução |
| AgreementVersion: proposta inicial | inexistente | PROPOSED | Condições completas e atribuídas à contratação (RN05, RN07–RN09) |
| AgreementVersion: aceitação inicial | PROPOSED | ACCEPTED | Aceitações exigidas das partes, respectiva autoria e data preservadas (RN06, RN14, RNF04) |
| Engagement: activação | PENDING_AGREEMENT | ACTIVE | Só após `AgreementVersion` aceite conforme regras |
| AgreementVersion: alteração material | versão N aceite | versão N+1 PROPOSED | Preservar N como vigente até decisão da contraparte |
| AgreementVersion: rejeição | versão N+1 PROPOSED | REJECTED | Versão N mantém-se vigente, sem modificação retroactiva |
| AgreementVersion: aceitação da alteração | versão N+1 PROPOSED | ACCEPTED | Apenas nova versão aceite altera condições vigentes |
| Engagement: entrega | ACTIVE | DELIVERED | Entrega efectivamente registada e associada ao autor/data (RF15–RF17) |
| Engagement: conclusão | DELIVERED | COMPLETED | Aceitação/critério de conclusão válido e histórico preservado |
| PaymentRecord: pagamento declarado | condição de pagamento acordada | REPORTED_PAID | Declaração não equivale a confirmação; condições vinculadas à versão vigente (RN09–RN10) |
| PaymentRecord: confirmação | REPORTED_PAID | CONFIRMED | Evidência/contraparte ou prestador externo autorizados; não afirmar custódia própria |
| Dispute: submissão | inexistente | OPEN | Contratação e parte elegíveis, categoria e evidência associadas (RF24) |
| Dispute: acompanhamento | OPEN | UNDER_REVIEW / WAITING_INFORMATION | Actos administrativos autorizados e documentados |
| Dispute: encerramento | UNDER_REVIEW / WAITING_INFORMATION | RESOLVED / CLOSED | Resultado registado, sem julgamento vinculativo universal (RN13) |

**Termos DRAFT e PENDING para Opportunity/Proposal** são **propostas de normalização técnica**, não estados confirmados como presentes na Figura 5.11. A legenda da Figura 5.11 cobre especificamente o `Engagement`.

### Guards que precisam de especificação ou verificação visual

- O que acontece quando a proposta é retirada, a oportunidade expira, é fechada, ou outra proposta já foi aceite? A narrativa não fornece critério inequívoco para impedir aceitação incompatível.
- Quem tem competência para marcar a entrega como aceite? A narrativa exige confirmação válida, mas não define detalhadamente os critérios de aceitação, rejeição e retrabalho.
- A acção de propor a primeira versão de acordo conta como aceitação explícita do proponente, ou ambos confirmam separadamente? UC13 fala em aceitação bilateral mas o fluxo precisa de tornar essa evidência verificável.
- O que acontece ao `Engagement` ao abrir disputa? O ciclo operacional deve ser preservado ou suspenso segundo regra expressa; o estado de `Dispute` não deve sobrescrever silenciosamente `Engagement.status`.
- Cancelamento e término: condições, autorizações, efeitos sobre versão vigente, pagamento e possibilidade de reabertura. São citados em §5.2.6, mas precisam de guards verificáveis antes de classificar a Figura 5.11 como auditada.

Não inventar resposta a estas ambiguidades. São decisões a formalizar e depois comparar aos desenhos.

## UML-03 — Divergência entre separação de ciclos no modelo-alvo e frontend [P0]

A D44 (p. 69, descrição DA04) afirma explicitamente: **«Os estados do conflito e da contratação mantêm-se distintos»**. Em §5.2.5 (p. 56), `RESOLVED` e `CLOSED` são estados do processo administrativo, não conclusões contratuais. Em contrapartida:

- `src/types.ts`: `ContractStatus = 'pending' | 'active' | 'completed' | 'disputed'`, sem `DELIVERED`, `PENDING_AGREEMENT`, entidade `AgreementVersion` ou tipo de caso de disputa com ciclo autónomo;
- `src/services/mockApi.ts`, `contracts.dispute` (~728–750): altera `contracts[idx].status = 'disputed'` directamente;
- `src/services/mockApi.ts`, `contracts.sign` (~661–685): altera o contrato para `active` em resposta à assinatura simplificada, sem versão de acordo aceite e auditável;
- `src/services/mockApi.ts`, `contracts.complete` (~687–726): coloca directamente o estado `completed`; a função, tal como escrita, não possui parâmetro de actor ou condição explícita `DELIVERED` e não confere a transição de estado anterior.

**Consequência científica:** a D44 deve distinguir `diagrama do modelo concebido` de `estado real implementado`. Não apresentar a Figura 5.11 como state machine testada. Conservar a diferenciação entre ciclo operacional, acordo, pagamento e disputa no desenho final.

**Consequência para testes:** V03–V07 devem testar transições positivas e negativas; não podem ser considerados aprovados no frontend mock enquanto a representação de estados divergente permanecer sem implementação das regras.

## UML-04 — Autorização contextual e invariantes de papéis [P0/P1]

No modelo académico, RN01 permite acumular perfis, mas RN02 proíbe ocupar ambos os lados da mesma contratação. No frontend mock:

- `src/types.ts` mantém um único atributo `User.role` (`worker`, `employer`, `admin`);
- `contracts.createFromProposal` (~605–659) localiza proposta, oportunidade e perfil de empregador, mas a função inspeccionada não verifica explicitamente se o utilizador é o titular da oportunidade nem se a proposta foi anteriormente aceite/autorizada;
- `contracts.sign` recebe `workerUserId` mas a função não o utiliza para demonstrar que o assinante é o trabalhador associado à contratação antes de marcar `signedByWorker`;
- `contracts.complete` não recebe actor; `contracts.dispute` recebe `disputingUserId` sem o utilizar numa verificação explícita de elegibilidade.

**Nota:** estas constatações são exclusivamente de **inspecção estática de funções no simulador local**, e não alegação de exploração ou acesso indevido a dados de produção. Restringir a narrativa a insuficiência dos controlos demonstrados. O estado de autenticação JWT no backend não valida as operações do frontend, que ainda não está integrado.

## UML-05 — Relação das fontes das figuras com RF/RN [P1]

| Figura | Estado de verificação textual | Correcção / decisão |
|---|---|---|
| 5.1 — casos de uso | Fonte associa genericamente RN01–RN16 e RF07–RF25 | Verificar que cada associação actor→UC tem correspondente RF, e delimitar o catálogo ausente UC01–UC27; não inventar UC |
| 5.2 — classes | Texto omite várias classes de apoio para simplificar | Manter nota explícita de que é vista parcial; inspeccionar multiplicidades e dependências das versões |
| 5.3/5.4 — actividades | Texto coerente em proposta → acordo, mas guards incompletos | Conferir decisões e saídas de rejeição/cancelamento nas imagens |
| 5.11 — estados | Narrativa define PENDING_AGREEMENT/ACTIVE/DELIVERED/COMPLETED; falta verificar desenho | Auditar guards, caminhos proibidos e independência da disputa |
| 5.12 — arquitectura | É modelo-alvo, não diagrama «as built» | Legenda e texto devem preservar distinção, inclusive SQLite actual versus PostgreSQL alvo |
| A.1, A.5(A–C) — execução/pagamento | Separação pagamento/execução correcta na narrativa | RF20 aparece apenas na integração opcional; não transformar em requisito obrigatório |
| A.2 — actividade de conflito | Fonte cita RF24–RF27 | RF26 (gerir utilizadores) e RF27 (moderar oportunidade) só pertencem se a imagem demonstrar operações dessas categorias; caso contrário corrigir fonte |
| A.3(A–C) — DS01 | Texto vincula RF07–RF12 em bloco | Em cada painel, citar RF efectivamente exercidos; atenção RF09/RF10 (pesquisa e consulta de perfis) não aparecem necessariamente no fluxo descrito |
| A.4(A–B) — DS02 | Texto associa RF13,14,17,18 | Verificar dupla aceitação, preservação de versões e rastreabilidade |
| A.6(B–C) — DS04 | Fonte inclui RF26 e RF27 sem correspondência óbvia com gestão de conflitos | Conferir a figura e restringir a fonte a RF24/25, RN13/14/16, RNF04 se não houver gestão de utilizadores/oportunidades |

Não alterar a figura apenas para fazê-la parecer consistente com os requisitos; corrigir o modelo ou o texto conforme a decisão funcional efectivamente aprovada.

## UML-06 — Redacções integráveis na monografia

### Complemento para §5.2.6 (sem declarar validação)

> O diagrama representa o ciclo operacional da relação de contratação, separado dos ciclos de vida do acordo, dos registos de pagamento e dos casos de conflito. A transição para ACTIVE depende de uma versão das condições aceite pelas partes, enquanto a passagem de DELIVERED para COMPLETED depende da conclusão validada segundo as regras da relação. O reporte de conflito deve conservar o histórico e a identificação do estado operacional da contratação, sem transformar um resultado administrativo de moderação numa decisão arbitral vinculativa. A implementação destas transições ainda carece de integração e ensaios de execução.

### Complemento para §5.3.3 (diferenças do estado do frontend)

> O modelo de estados do frontend demonstrativo não corresponde integralmente ao modelo-alvo. A representação existente utiliza estados simplificados de contratação, permite classificar o contrato directamente como «disputed» e não materializa de forma independente os estados de entrega, versionamento do acordo e acompanhamento administrativo do conflito. A leitura estática da implementação indica, portanto, uma divergência que deverá ser resolvida antes de validar as regras de negócio propostas.

### Nota de prudência para referências das figuras

> As fontes e legendas de cada diagrama devem mencionar apenas os requisitos e regras efectivamente representados, distinguindo modelos conceptuais de funcionalidades implementadas. A correspondência completa deverá ser documentada numa matriz de rastreabilidade e verificada por revisão visual dos diagramas.

## Checklist para fechar este bloco

- [ ] Verificar Figuras 5.5–5.10 ausentes da extracção e corrigir numeração se realmente não existirem.
- [ ] Inspeccionar visualmente figuras 5.1–5.4, 5.11–5.12, A.1–A.6 antes de declarar correctos os elementos UML.
- [ ] Formalizar guards de aceitação, alteração, entrega, conclusão, disputa e cancelamento.
- [ ] Garantir autonomia dos ciclos `Engagement`, `AgreementVersion`, `PaymentRecord` e `DisputeCase`.
- [ ] Rever remissões DS04/DA04 para RF26–RF27.
- [ ] Actualizar matriz de requisitos e V01–V08 em consonância com transições e tentativas inválidas.
- [ ] Sem alteração do DOCX original, sem testes executados, sem presumir que diagrama e código são equivalentes.
