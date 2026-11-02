# D47 — Verificação visual de diagramas UML da D44: inconsistências confirmadas e critérios de correcção

**Documento canónico:** `Monografia_D44_Metodologia_Proveniencia_Verificada.docx`, páginas 48, 50, 52, 54, 57, 58, 68–71, 73–71? [corrigir: 73–79].  
**Tipo de evidência:** **imagem renderizada da página do documento original**, recuperada pelo leitor da Library (não é mera extracção textual).  
**Estado:** **auditoria visual efectivamente realizada** dos diagramas enumerados abaixo. O documento Word canónico continua **não alterado**, pois os seus bytes editáveis não estão disponíveis. O painel **A.4(A), p. 72** não pôde ser inspeccionado visualmente nesta execução devido a falha temporária de recuperação da imagem. Não declarar essa figura verificada.

## 1. Matriz de cobertura da inspecção visual

| Figura / diagrama | Página da D44 | Resultado |
|---|---:|---|
| 5.1 — Casos de uso | 48 | Inspecção visual concluída; amostra de casos centrais, não catálogo completo |
| 5.2 — Classes conceptuais | 50 | Inspecção visual concluída; ver inconsistência potencial de multiplicidade |
| 5.3 — Actividades DA01 | 52 | Inspecção visual concluída; hand-off para DA02 coerente no fluxo aceite |
| 5.4 — Actividades DA02 | 54 | Inspecção visual concluída; aceitação da parte proponente implícita, requer explicitação |
| 5.11 — Estados do Engagement | 57 | Inspecção visual concluída; **saídas de IN_DISPUTE não desenhadas** |
| 5.12 — Arquitectura | 58 | Inspecção visual concluída; modelo-alvo expressamente rotulado |
| A.1 — Actividade DA03 | 68 | Inspecção visual concluída; PaymentRecord reportado/confirmado/contestado é separado da conclusão do serviço |
| A.2 — Actividade DA04 | 69 | Inspecção visual concluída; fonte inclui RF26/RF27 sem actividades correspondentes |
| A.3(A), A.3(B), A.3(C) — DS01 | 70–71 | Inspecção visual concluída; os três painéis existem e distinguem proposta aceite de contrato activo |
| A.4(A) — DS02 | 72 | **Não verificado visualmente**, falha temporária de recuperação da página |
| A.4(B) — DS02 | 73 | Inspecção visual concluída; guarda versão anterior se vN+1 for rejeitada |
| A.5(A), A.5(B), A.5(C) — DS03 | 74–76 | Inspecção visual concluída; serviço/estado financeiro/integrador externo separados |
| A.6(A), A.6(B), A.6(C) — DS04 | 77–79 | Inspecção visual concluída; conflitos, análise e encerramento representados em três painéis |
| 5.13–5.19 — ecrãs de protótipo | 61–62 | **Continuam marcadores textuais**, sem capturas autenticadas; não os substituir por imagens inventadas |

**Ajuste a auditorias anteriores:** já não é correcto dizer que **todas** as figuras são inacessíveis para inspeção visual. A Library permite recuperar representações renderizadas das páginas. A limitação restante refere-se aos **bytes DOCX**, a preservação de estilos/campos/comentários e as figuras não recuperadas.

## 2. UML-V01 [P0] — O estado IN_DISPUTE não possui saídas formais na Figura 5.11

**Evidência visual p. 57:** o desenho apresenta os estados `PENDING_AGREEMENT → ACTIVE → DELIVERED → COMPLETED`, com ramificações de `PENDING_AGREEMENT` e `ACTIVE` para `CANCELLED`. Os estados `ACTIVE` e `DELIVERED` possuem setas para `IN_DISPUTE`.

O elemento à direita de `IN_DISPUTE` é uma **anotação textual**, aproximadamente: «Após acompanhamento: retoma estado válido ACTIVE / DELIVERED / COMPLETED / CANCELLED». **Não existem transições dirigidas desenhadas** que saiam de `IN_DISPUTE` para esses estados.

**Efeito:** o diagrama fica estruturalmente incompleto como máquina de estados; a nota não permite identificar eventos, decisões/guardas nem quem autoriza cada saída.

**Correcção do modelo:** explicitar transições `IN_DISPUTE → estado_operacional_valido`, com evento e guarda, ou modelar a disputa como entidade independente `DisputeCase` e conservar `Engagement.status_operational` em paralelo. Se conservar `IN_DISPUTE` no Engagement, persistir `previous_operational_status` e explicitar quando um encerramento **não** significa concluir automaticamente o serviço.

**Questões em aberto:** (a) que eventos permitem retomar `ACTIVE` ou `DELIVERED`? (b) em que condições se aceita `COMPLETED` após o acompanhamento? (c) disputa pode ser aberta depois de `COMPLETED` e `CANCELLED`? O desenho só contém setas de entrada a partir de ACTIVE e DELIVERED; a anotação menciona estados terminais.

**Critério de aceitação:** cada transição válida definida em tabela de estados tem seta ou regra equivalente documentada; os caminhos inválidos estão explicitados; a alteração de `DisputeCase.status` não implica automaticamente alteração de `PaymentRecord.status` ou de um estado operacional sem justificação.

## 3. UML-V02 [P1] — Contradição potencial na cardinalidade AgreementVersion

**Evidência visual p. 50:** `Engagement` associa-se a `AgreementVersion` com multiplicidade exibida como `1..*` na extremidade das versões. `Engagement` contém estado de contratação e identificadores de trabalhador/empregador.

**Confronto:** A.3(C), p. 71, mostra `Engagement PENDING_AGREEMENT` criado depois de aceitar uma proposta. A Figura 5.4, p. 54, **posteriormente** cria «v1 PROPOSED» ao formalizar o acordo. Existe, portanto, um instante lógico em que a contratação já foi criada e ainda **não possui v1**.

**Duas opções correctas, a decidir expressamente:**
- A) permitir cardinalidade `0..*` para `AgreementVersion` até ser proposta a primeira versão, com invariante `ACTIVE ⇒ existe ≥1 versão ACCEPTED`; ou
- B) manter `1..*` e obrigar a criar a primeira versão `PROPOSED` atomicamente com o Engagement, alterando DS01 e DA02.

**Não modificar multiplicidades silenciosamente:** a escolha afecta integridade do domínio, criação transaccional, requisitos e casos V02/V03.

## 4. UML-V03 [P1] — Aceitação bilateral não totalmente explícita em DA02 (Figura 5.4)

**Evidência visual p. 54:** `Parte proponente` → «Propor condições»; `Sistema` → «Criar v1 PROPOSED, registar autor e data»; `Contraparte` → «Examinar condições propostas / Aceita?»; `Sistema` → «Registar aceitações; v1 ACCEPTED / Engagement ACTIVE».

O fluxo não mostra um passo explícito de aceitação da parte proponente distinto de «Propor condições». **Não afirmar que não houve aceitação bilateral:** propor condições **pode** ser interpretado como anuência do proponente, mas a regra não está formulada de modo inequívoco.

**Correcção proposta:** explicitar em nota/guarda que `proposeInitialConditions` regista a aceitação da própria proposta pelo proponente, **ou** introduzir aceitação expressa independente. Manter `ACTIVE` condicionado ao conjunto de aceitações exigidas (UC13, RN05, RN07, RN09) e registar actores/datas/versão.

**Teste necessário:** contraparte aceita sem anuência da parte proponente → sistema não deve activar indevidamente; um proponente altera termos depois de contraparte ver → exigir nova aceitação das condições vigentes.

## 5. UML-V04 [P1] — Referências RF26/RF27 incorrectas nos diagramas de conflito

**Figura A.2, p. 69 (DA04):** mostra «Reportar conflito», «Dispute OPEN», «Analisar caso», «Aguardar informação», «Fornecer elementos adicionais», «RESOLVED ou CLOSED». A fonte inclui `RF17 e RF24–RF27`. RF26 é «Gerir utilizadores» e RF27 é «Moderar oportunidade reportada».

**Figura A.6(B), p. 78 (DS04):** mostra análise administrativa de um `Dispute`, validação da autoridade administrativa e pedido de informação adicional. A fonte inclui `RF24, RF25 e RF26`. **Não existe operação de gestão de utilizadores desenhada**. A verificação de autorização de um administrador não equivale a RF26.

**Figura A.6(C), p. 79 (DS04):** mostra encerramento de `Dispute`, validação de permissões, persistência de resultado e restauro de estado operacional. A fonte inclui `RF25–RF27`. **Não existe moderação de oportunidade reportada desenhada**.

**Correcções de fonte recomendadas (sujeitas à revisão final do diagrama):**
- A.2: `Fonte: Elaboração própria, com base em RN13, RN14 e RN16; RF17, RF24 e RF25; RNF04.`
- A.6(B): `Fonte: Elaboração própria, com base em RF24 e RF25; RN13, RN14 e RN16; RNF02 e RNF04.` (só incluir RNF02 se autorização estiver efectivamente representada e adoptada como origem).
- A.6(C): `Fonte: Elaboração própria, com base em RF25; RN13, RN14 e RN16; RNF04.`

**Não retirar RF26/RF27 dos requisitos gerais:** são requisitos legítimos de governação; apenas não estão representados nestes diagramas de conflito.

## 6. UML-V05 [P1] — Estados financeiros e disputa operacional precisam de vocabulário inequívoco

**Figura A.1, p. 68:** após registo externo de pagamento, um `PaymentRecord` assume `REPORTED_PAID`; a contraparte pode `CONFIRMED` ou `DISPUTED`. Isto não implica conclusão do serviço.

**Figura A.5(B), p. 75:** repete de modo coerente `REPORTED_PAID → CONFIRMED ou DISPUTED` no `PaymentRecord`.

**Figura A.2, p. 69, e A.6(A), p. 77:** abrem um **`Dispute`** com estado `OPEN`, podendo sinalizar um `Engagement IN_DISPUTE`. O pedido de documentos é acompanhado em `UNDER_REVIEW` / `WAITING_INFORMATION`.

**Problema:** existem **três conceitos diferentes** ligados à palavra «disputa»: (1) pagamento contestado, (2) processo administrativo `Dispute`, (3) contratação marcada como `IN_DISPUTE`. O próprio desenho distingue os elementos, mas ainda não documenta quando a contestação do pagamento obriga a criar um `DisputeCase` ou alterar o estado do Engagement.

**Correcção:** definir enumerações e transições independentes e política de propagação de eventos explícita; sem inferir automaticamente uma mudança financeira de um fecho administrativo.

## 7. UML-V06 [P2] — Fontes genéricas em DS01

As Figuras A.3(A), A.3(B) e A.3(C) (pp. 70–71) partilham a referência genérica a `RF07–RF12`. A.3(A) apenas cria/publica oportunidade; A.3(B) submete proposta; A.3(C) selecciona proposta e cria Engagement.

A fonte de cada **painel** deve identificar os RF que de facto representam, por exemplo:
- A.3(A): RF07 (ciclo de oportunidade), RN02/RN04 se as validações efectivamente cobertas;
- A.3(B): RF11 (submeter proposta), RN02 e restrição de estado OPEN, com RF07 enquanto requisito relacionado;
- A.3(C): RF12 (avaliar proposta), RF13 como processo subsequente **não executado neste painel**.

Isto não exige renumerar RF nem inventar novos UC; trata-se de tornar as remissões mais precisas.

## 8. UML-V07 [P2] — Figura 5.12 e dependência de estado-alvo

A Figura 5.12 (p. 58) está correctamente titulada **«Arquitectura lógica da solução proposta (modelo-alvo)»** e inclui nota de que a integração frontend–API e PostgreSQL **não estão demonstrados** no protótipo actual. Este é um aspecto **positivo**, a preservar. A ilustração não deve receber títulos como «arquitectura implementada» ou «solução validada».

## 9. UML-V08 [P2] — Pontos fortes que devem ser preservados

- Figura 5.3 e A.3(C): aceitar uma proposta produz `PENDING_AGREEMENT`, **não** `ACTIVE`.
- Figura 5.4 e A.4(B): a alteração é proposta como vN+1; rejeição preserva a versão vigente.
- Figura A.1 e A.5(A): `DELIVERED` e `COMPLETED` são operações separadas; conclusão depende de aceitação/validação.
- Figura A.1 e A.5(B/C): pagamentos declarados, confirmados e integração facultativa são conceitos distintos; sem custódia própria.
- Figura A.2 e A.6(A–C): os processos de reporte e acompanhamento são representados como moderação/documentação, sem declarar decisão arbitral vinculativa.

Estas decisões dão consistência ao modelo-alvo e não devem ser anuladas para corresponder à implementação simplificada do frontend.

## 10. Critérios de fecho actualizados

- [ ] Corrigir Figura 5.11 com transições e guardas formais de saída de IN_DISPUTE.
- [ ] Decidir quando nasce `AgreementVersion` face ao nascimento de `Engagement` (1..* vs 0..*).
- [ ] Explicitar a aceitação bilateral no DA02, não apenas na narrativa.
- [ ] Corrigir fontes A.2, A.6(B), A.6(C) para não atribuir RF26/RF27 a operações inexistentes.
- [ ] Definir estados e transições para `PaymentRecord`, `DisputeCase` e `Engagement`, preservando independência.
- [ ] Verificar visualmente a Figura A.4(A), p. 72, cuja recuperação falhou temporariamente.
- [ ] Inserir legendas/capturas reais para 5.13–5.19 ou remover/remapear referências sem falsificar resultados.
- [ ] Confirmar no documento final o salto 5.4→5.11 e actualizar toda a numeração, índice e campos `REF/SEQ`, se não existirem figuras intermédias.
- [ ] Verificar legibilidade no Word em páginas A4 antes de aprovação.
- [ ] Não assumir que as figuras são ensaios de execução: todas descrevem **modelo concebido**.

## 11. Segurança básica do código consultado [P1, exame estático]

O backend `backend/settings.py` contém `DEBUG = True` e uma `SECRET_KEY` definida como literal directamente no ficheiro de configuração. **Não reproduzir o segredo** neste relatório nem na monografia. O facto sugere configuração de desenvolvimento, não evidência de intrusão ou comprometimento.

**Acção:** antes de qualquer publicação de serviço, usar segredo injectado por ambiente, validar `DEBUG=False` e configuração de hosts/HTTPS, e substituir a chave se tiver sido reutilizada em ambiente persistente ou externo. No Capítulo V, não declarar conformidade RNF02 (segurança) nem prontidão de produção sem revisão de configuração e ensaios. Esta observação não altera, por si só, o tema nem a conclusão metodológica da monografia.

---

**Status auditável:** Figuras listadas na secção 1 inspeccionadas visualmente conforme coluna, uma imagem pendente, DOCX original **não editado** e nenhum teste funcional executado.
