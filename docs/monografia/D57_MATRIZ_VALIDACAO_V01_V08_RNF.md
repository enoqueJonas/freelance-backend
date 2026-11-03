# D57 — Matriz de validação exacta V01–V08 e RNF01–RNF07

**Estado:** reconciliação académica de evidências (03-11-2026), para avaliação da autora e da supervisão. **Não foi aplicada à D44.**  
**Fonte primária da definição dos cenários:** `Monografia_D44_Metodologia_Proveniencia_Verificada.docx`, §5.4 pp. 62–63, Apêndice §8.8 pp. 81–82.  
**Fonte das execuções técnicas:** CI GitHub D50–D56, nos ramos de auditoria e desenvolvimento, **não integrados na branch principal**.

## 1. Rectificação crítica de classificação

**V03 = Formalização e alteração de acordos. V04 = Execução, entrega e histórico do serviço.** A D44 estabelece-os inequivocamente no Quadro A.2 (p. 81):

- V03: RF13–RF14, RF18; RN05–RN09; condições v1, aceitações bilaterais, alteração de prazo/preço para v2, rejeição e aceitação em casos separados.
- V04: RF15–RF17, RN14; criar contratação ACTIVE, `ExecutionRecord`, entregar evidência, solicitar conclusão, impedir conclusão sem validação e preservar histórico.

Portanto, **testes de acordo v1/v2/v3 não podem ser atribuídos a V04**, nem pode V04 receber o estado «Parcial» com base exclusivamente em D51–D56. Qualquer relatório técnico anterior que referencie «V03/V04» como ensaios de versionamento necessita desta errata.

Os casos de aceitação definidos na D44 são mais extensos do que os testes de API e do browser realizados. Esta matriz distingue:

- **Plano:** critério especificado na monografia;
- **Cobertura executada:** comportamento efectivamente exercitado por CI, com log público verificável;
- **Resultado do caso D44:** `Parcialmente exercitado` apenas quando parte substancial do cenário foi executada, `Não executado` quando nenhuma parte correspondente foi comprovada; **não usar `Passou` sem percorrer todos os critérios previstos**.

## 2. Matriz V01–V08

| Caso | Critério canónico do Quadro A.2 | Evidência real D50–D56 | Classificação técnica candidata | Bloqueador para `Passou` |
|---|---|---|---|---|
| **V01** | Criar conta sintética, perfis Worker e Employer **na mesma conta** e associar portfólio/certificação como evidência; persistência após nova sessão | D50 API para registo/JWT/perfis; D56 Chromium cria os dois perfis na mesma conta e preserva históricos | **Parcialmente exercitado** | RF05: não há associação comprovada de portfólio/certificação; testar persistência de todas as evidências e perfis após novo login |
| **V02** | Publicar oportunidade, **filtrar resultados**, submeter proposta por outra conta, impedir autocontratação, seleccionar proposta e obter `PENDING_AGREEMENT` | D51 API publica/submete/selecciona e rejeita autocontratação; D54–D56 browser com dois actores, oportunidade OPEN e Engagement pendente | **Parcialmente exercitado** | Pesquisa por filtros RF08, pesquisa trabalhadores RF09, consulta RF10; teste de autocontratação no browser e variações de elegibilidade ainda incompletos |
| **V03** | Propor v1, obter aceites, alterar **prazo/preço** para v2, rejeitar v2 e, em outro caso, aceitar v2; preservar histórico | D51/D52: v1 aceite bilateralmente, v2 rejeitada ou aceite em API; D54–D56 Chromium v1→v2 aceite→v3 rejeitada e versão vigente preservada | **Parcialmente exercitado** | Não há campos completos de prazo/entregáveis; o browser rejeitou **v3**, não **v2 em caso independente**; faltam oráculos formais de imutabilidade e casos completos por cenário |
| **V04** | Registar `ExecutionRecord` com actor/data, entrega, `DELIVERED`, conclusão validada e histórico | **Nenhum ensaio técnico identificado** que execute `ExecutionRecord`, entrega ou conclusão no Django D50–D56 | **Não executado** | Domínio de execução/entrega ainda ausente; não inferir execução de serviço a partir de `Engagement ACTIVE` |
| **V05** | Condições de pagamento antecipado/por etapa, `REPORTED_PAID` ≠ `CONFIRMED`, contestação e PSP opcional | D51/D52 permitem **valor ou preço após diagnóstico no acordo**. Não existe registo/confirmação real de pagamento | **Não executado como cenário de pagamento** | RF19 sem implementação; PSP/escrow não implementados; preço em acordo não equivale a teste de pagamento |
| **V06** | Avaliação bilateral elegível, rejeição de avaliação sem relação e contestação | Apenas UI legada com mock, sem serviço real de reputação D50–D56 | **Não executado** | RF21–RF23 ausentes no backend |
| **V07** | Dispute OPEN→UNDER_REVIEW↔WAITING_INFORMATION→RESOLVED/CLOSED, evidências, actos e fecho sem arbitragem | A rejeição de `AgreementVersion` na D52 **não é** `DisputeCase`; nenhuma transição de conflito executada | **Não executado** | RF24–RF25 e modelo de conflitos ausentes no backend |
| **V08** | Capacidade de administrador, acção não autorizada, revisão de verificação e moderação com actor/motivo/data | D50 testa acesso staff à lista de contas; **não** implementa nem verifica `VerificationCase`/moderação previstos | **Não executado como cenário de governação** | RF06/RF26–RF28 e RN15/RN16 não foram cobertos integralmente |

**Regra de contabilização:** não converter «V01–V03 parcialmente exercitados» em «3 casos passaram». Os três requerem critérios adicionais para `Passou`; V04–V08 permanecem não executados como casos canónicos, apesar de testes unitários cobrirem capacidades auxiliares.

## 3. Matriz RNF01–RNF07

| RNF | Plano da D44 (Quadro A.3, p.82) | Evidência disponível | Estado proposto |
|---|---|---|---|
| **RNF01 Usabilidade** | Participantes definidos, conclusão de tarefas sem assistência, dificuldades e resultados | D56 automatiza navegação por teclado e layout; **sem participantes humanos nem tarefas observadas** | **Não executado conforme protocolo** |
| **RNF02 Segurança e autorização** | Sessão ausente, actor errado e recurso de terceiro, com resultados anotados | D50–D55 testam JWT, restrições de consulta, permissões por titularidade, enumeração e autocontratação | **Parcialmente verificado tecnicamente**; falta matriz integral de recursos e análise de segurança |
| **RNF03 Privacidade e minimização** | Campos públicos/privados, persistência local e exposição por actor, com matriz | D50–D55 corrigem exposição da lista de utilizadores, limitam propostas e limpam formulários no logout | **Parcialmente verificado tecnicamente**; faltam auditoria sistemática de campos, retenção, logs e dados em todos os recursos |
| **RNF04 Integridade e rastreabilidade** | Alterar acordo aceite e verificar versão nova, autor, data e histórico imutável | D52 testa fingerprint/aceitação, histórico v1/v2/v3, rejeição com autor/data; D54 demonstra pela UI | **Parcialmente verificado tecnicamente**; não há imutabilidade perante acesso privilegiado nem trilho completo de auditoria |
| **RNF05 Responsividade** | Ensaiar fluxos centrais em 390×844 móvel e 1365×900 desktop, verificar sobreposição/recorte | D56 Chromium executa **um fluxo de abertura/fecho de perfis a 390×844**; o fluxo contratual foi exercitado em viewport desktop Playwright, não exactamente 1365×900 | **Parcialmente verificado tecnicamente**; faltam todas as tarefas centrais em ambos os viewports e auditoria de sobreposição |
| **RNF06 Manutenibilidade** | Rever UI/API/domínio e dependências; verificar separação das regras | Estrutura modular React/Django visível e checks de build; sem avaliação sistemática documentada de dependências | **Não executado conforme protocolo específico** |
| **RNF07 Interoperabilidade** | Adaptador PSP com sucesso/erro e estados, quando houver PSP | Arquitectura apenas prevê adaptadores; não existe integração PSP D50–D56 | **Não executado** |

**Nota:** os 80 testes Django [D55](https://github.com/enoqueJonas/freelance-backend/actions/runs/41603523124), 8 testes HTTP React e 2 testes Chromium [D56 final](https://github.com/enoqueJonas/freelance-frontend/actions/runs/41612082795) não perfazem 90 testes de aceitação académica. São suites de níveis e objectos distintos; não os somar como uma pontuação da monografia.

## 4. Evidências de execução a referenciar (sem fabricar resultados)

| ID | Código/artefacto | Resultado confirmado | Limitação |
|---|---|---|---|
| E-D50 | [Backend CI D50](https://github.com/enoqueJonas/freelance-backend/actions/runs/41478553838) | 18/18 Django API | Contas/perfis |
| E-D51 | [Backend CI D51](https://github.com/enoqueJonas/freelance-backend/actions/runs/41481395290) | 41/41 Django API acumulados | Contrato v1 |
| E-D52 | [Backend CI D52](https://github.com/enoqueJonas/freelance-backend/actions/runs/41483135110) | 65/65 Django API acumulados | Versionamento |
| E-D53 | [Backend CI D53](https://github.com/enoqueJonas/freelance-backend/actions/runs/41484092825) | 71/71 Django API acumulados | Listagens autorizadas |
| E-D54 | [Chromium CI D54](https://github.com/enoqueJonas/freelance-frontend/actions/runs/41600019575) | 1/1 browser React + Django real | Um percurso, dados sintéticos |
| E-D55 | [Backend CI D55](https://github.com/enoqueJonas/freelance-backend/actions/runs/41603523124) | 80/80 Django API acumulados | Estado de proposta |
| E-D55-UI | [Chromium CI D55](https://github.com/enoqueJonas/freelance-frontend/actions/runs/41604340826) | 1/1 browser | Persistência do estado/limpeza de sessão |
| E-D56 | [Chromium CI D56 final](https://github.com/enoqueJonas/freelance-frontend/actions/runs/41612082795) | 2/2 browser | Contratação + perfil/mobile |
| E-D56-TS | [Frontend CI D56 final](https://github.com/enoqueJonas/freelance-frontend/actions/runs/41612082848) | 8/8 cliente HTTP, typecheck/build | Não é teste de browser |

**Todas as revisões acima são ramos/PRs draft no GitHub:** o resultado prova comportamento nessas revisões, **não** da branch principal, nem do `Monografia_D44...` no momento em que foi produzido.

## 5. Errata a publicar sobre os relatórios anteriores

Os relatórios D52–D56 que escrevem «V03/V04» associados a versionamento de acordos devem usar uma destas formulações:

- **Preferida:** «subconjunto de V03 (formalização e alteração de acordos), exercitado por testes reais da API e do browser; V04 (execução e entrega) não executado».
- **Para referência a V02:** «subconjunto de V02, incluindo publicação, proposta e início de contratação; sem validação integral de pesquisa e filtros».
- **Para referência a perfis:** «subconjunto de V01, sem avaliação de evidências profissionais/portfólio».

Não afirmar que «v3 rejeitada» satisfaz automaticamente o critério formal «v2 rejeitada num caso independente». A semântica é semelhante, mas os dados e o roteiro canónico diferem.

## 6. Texto curto candidato para §5.4

> Os cenários V01–V08 foram definidos como protocolo de aceitação. Em uma etapa técnica posterior à elaboração da versão documental inicialmente auditada, foram implementados e submetidos a ensaios automatizados subconjuntos dos fluxos V01–V03, utilizando testes de API Django e um cenário de browser Chromium com React e Django reais. Os testes demonstraram a criação e acumulação de perfis, a publicação de oportunidade, a submissão e selecção de proposta, a activação bilateral do acordo e alterações versionadas. Os casos V01–V03 permanecem **parcialmente exercitados**, pois não foram cumpridos todos os seus critérios canónicos. V04–V08 não foram executados como cenários completos de aceitação; execução e entrega, registo de pagamento, reputação, conflitos e governação continuam com lacunas técnicas. As verificações RNF02–RNF05 receberam cobertura técnica parcial, sem que isso substitua os respectivos procedimentos integrais, em particular a avaliação de usabilidade com participantes. As evidências foram produzidas em branches de desenvolvimento, num ambiente isolado, e não autorizam conclusões sobre comportamento em produção ou eficácia junto do público-alvo.

A redacção só deve ser integrada se **a autora optar por incorporar estas revisões técnicas no objecto da monografia**, com a data e revisão do protótipo identificadas. Não reutilizar a matriz D44 `Não executado` sem actualizar a metodologia, nem reescrever o histórico como se os testes tivessem sido realizados antes da data real.

## 7. Critérios de aprovação desta matriz

- [x] Confirmar definições V01–V08 e RNF01–RNF07 no Apêndice da D44.
- [x] Correlacionar resultados com execuções do GitHub Actions D50–D56.
- [x] Separar testes de API, de cliente HTTP e de browser E2E.
- [x] Corrigir a atribuição errada de V04.
- [ ] Rever com autora/supervisão, em particular critérios de aceitação V03 para preço/prazo e formalização.
- [ ] Actualizar de forma coordenada §3.7, §5.3–5.5, Capítulo VI, Quadros 5.3–5.4, Quadro A.1 e Quadro A.2 **no DOCX canónico**.
- [ ] Completar V01–V03 com ensaios exigidos na D44 e executar V04–V08, não apenas gerar novos screenshots.
- [ ] Definir e executar protocolo RNF01 com participantes reais; não inventar amostra humana.
