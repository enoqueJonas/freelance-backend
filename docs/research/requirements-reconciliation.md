# Reconciliação dos Requisitos do Draft com a Baseline Derivada

## Critério

Esta análise confronta os 32 RF presentes no draft da monografia com a baseline derivada por triangulação e com o AS-IS técnico. Classificações:

- **Manter** — necessidade e comportamento continuam válidos.
- **Reformular** — intenção válida, mas declaração/regra actual é demasiado restritiva ou incorrecta.
- **Fundir** — comportamento é válido, mas deve integrar requisito mais abrangente.
- **Auxiliar** — útil para UX/operação, mas não emergiu como capacidade central.
- **Remover da baseline** — não há suporte suficiente ou contradiz decisões já tomadas.

A existência no código não constitui evidência científica.

## RF01–RF32

| Draft | Requisito actual | Decisão | Destino / fundamento |
|---|---|---|---|
| RF01 | Criar conta | **Reformular** | → novo RF01. Registo mantém-se, mas GitHub/portfólio não são obrigatórios no registo. Um User pode acumular WorkerProfile e EmployerProfile. |
| RF02 | Iniciar sessão | **Manter** | → novo RF02. Capacidade operacional necessária. |
| RF03 | Actualizar conta | **Fundir/Reformular** | Dados de conta e palavra-passe pertencem à gestão da conta; documentos/evidências pertencem aos perfis/verificação. Não misturar responsabilidades. |
| RF04 | Submeter documentos de verificação | **Reformular** | → novo RF06, se adoptado. Verificação deve ser proporcional e bilateral; não exclusiva a empregadores nem confundida com KYC. |
| RF05 | Visualizar estado de verificação | **Fundir** | Subfunção do fluxo de verificação RF06, caso este permaneça no âmbito. |
| RF06 | Restringir funcionalidades de contas não verificadas | **Remover/Reformular regra** | Evidência não sustenta verificação obrigatória como gate universal. Restrições específicas só podem existir se justificadas por risco/política. |
| RF07 | Publicar oferta | **Manter/Reformular** | → novo RF07. Não condicionar universalmente a “empregador verificado”; preço pode ser definido depois de diagnóstico. |
| RF08 | Editar oferta | **Fundir** | Integrar na gestão da oportunidade RF07; regras de edição dependem do estado da oportunidade. |
| RF09 | Pesquisar ofertas | **Manter** | → novo RF08. Fundamentado por N01/N04. |
| RF10 | Pesquisar trabalhadores | **Manter/Reformular** | → novo RF09. Filtros profissionais; localização contextual; classificação não deve ser único sinal. |
| RF11 | Submeter proposta | **Manter/Reformular** | → novo RF11. Retirar gate universal de verificação. |
| RF12 | Gerir propostas (Trabalhador) | **Manter/Fundir** | Integrar no ciclo da proposta; edição/cancelamento depende do estado e antes de aceitação. |
| RF13 | Visualizar propostas recebidas | **Manter/Fundir** | → parte de RF12 novo “Avaliar proposta”. |
| RF14 | Validar proposta | **Manter/Reformular** | → novo RF12. Usar aceitar/rejeitar; “validar” é ambíguo. |
| RF15 | Criar contrato digital | **Reformular** | → novo RF13 “Registar condições acordadas”. Não assumir contrato pesado/automático para todos os serviços. |
| RF16 | Assinar contrato digital | **Remover como obrigação** | Evidência suporta aceitação/formalização proporcional, não assinatura digital avançada universal. |
| RF17 | Visualizar contrato digital | **Reformular** | → novos RF17/RF13: consultar histórico e condições da contratação. |
| RF18 | Aceitar contrato | **Fundir/Reformular** | Aceitação das condições faz parte de RF13; deve envolver ambas as partes conforme fluxo, não apenas trabalhador. |
| RF19 | Efectuar pagamento | **Rebaixar para opcional** | → novo RF20 Could. Integração com PSP pode existir, mas não é core nem autoriza custódia. |
| RF20 | Confirmar pagamento | **Reformular** | → novo RF19 “Registar estado de pagamento”. Confirmação por API só quando integração existir. |
| RF21 | Receber pagamento | **Rebaixar/absorver** | Não tratar ConecTA como custodiante. Pagamento externo pode ser facilitado por PSP; condições/estado são core. |
| RF22 | Classificar trabalhador | **Fundir** | → novo RF21 bilateral “Avaliar contraparte”. |
| RF23 | Classificar empregador | **Fundir** | → novo RF21 bilateral “Avaliar contraparte”. |
| RF24 | Iniciar conversa privada | **Remover como RF core** | N08 é rastreabilidade. Mensagens podem ser mecanismo de implementação, mas chat não é necessidade autónoma. |
| RF25 | Enviar notificações | **Auxiliar** | Pode ser mecanismo UX para eventos importantes, mas não foi derivado como macro necessidade. Decidir após modelação de estados. |
| RF26 | Realizar avaliação de habilidades | **Remover como gate** | Evidência é divergente; diferentes especialidades exigem diferentes evidências. Pode existir futuramente como opção específica. |
| RF27 | Validar habilidades (Administrador) | **Remover** | Depende do RF26 e não há fundamento para administrador validar competência técnica de todas as especialidades. |
| RF28 | Validar documentos (Administrador) | **Reformular** | Só permanece se RF06 usar revisão documental; deve ter finalidade e critérios claros. Não é automaticamente exclusivo ao empregador. |
| RF29 | Gerir utilizadores (Administrador) | **Manter com fundamento operacional/governação** | Necessário para segurança/governação, mas suspensão/remoção devem seguir estados, motivos e regras. Candidato a RF administrativo. |
| RF30 | Gerir ofertas (Administrador) | **Reformular** | Corpus suporta publicações suspeitas/reporte. Administração pode moderar oferta segundo política; não remover arbitrariamente. |
| RF31 | Gerir propostas (Administrador) | **Não manter como RF autónomo** | Não surgiu necessidade específica de moderação manual de propostas. Abuso pode ser tratado por mecanismo geral de reporte/moderação. |
| RF32 | Gerir contratos (Administrador) | **Reformular fortemente** | → novos RF24/RF25 para reportar/acompanhar conflitos. Administração não recebe poder arbitral sobre a contratação. |

## Requisitos derivados que não estavam adequadamente representados no draft

1. **RF03 — Gerir perfil profissional** com múltiplos tipos de evidência.
2. **RF04 — Gerir perfil de empregador** acumulável com WorkerProfile.
3. **RF10 — Consultar perfil** como capacidade explícita.
4. **RF14 — Registar alteração ao acordo** — consequência directa de scope creep/mudanças.
5. **RF15 — Registar actualizações relevantes à execução**.
6. **RF16 — Registar entrega/conclusão**.
7. **RF17 — Consultar histórico da contratação**.
8. **RF18 — Definir condições de pagamento**, não apenas executar API.
9. **RF22 — Reputação contextualizada**.
10. **RF23 — Contestar avaliação**.
11. **RF24/RF25 — Reportar e acompanhar conflito**, sem arbitragem.

## Capacidades administrativas a acrescentar à baseline

O confronto mostra que a baseline derivada focou correctamente o domínio principal, mas deixou governação operacional demasiado implícita. Acrescentam-se como candidatos:

- **RF26 — Gerir utilizadores:** permitir ao administrador consultar e aplicar medidas administrativas a contas segundo regras/políticas e motivo registado.
- **RF27 — Moderar oportunidade reportada:** permitir ao administrador analisar uma oportunidade reportada e aplicar a acção prevista pela política.
- **RF28 — Analisar verificação:** caso a verificação documental permaneça no protótipo, permitir a utilizador autorizado analisar evidências/documentos e registar decisão/estado.

Estes RF são de governação; não autorizam arbitragem de conflitos contratuais nem validação universal de competências.

## Resultado quantitativo da reconciliação

A baseline passa de **25 RF para 28 RF candidatos**, porque três capacidades administrativas justificáveis foram recuperadas do draft.

Isto não significa preservar 28 dos 32 RF antigos. Grande parte dos RF antigos foi fundida ou reformulada. A nova numeração deve ser aplicada apenas após fechar estados e atomicidade.

## Impacto no AS-IS técnico

- **Frontend:** papel singular `worker | employer | admin` deve ser substituído por capacidades/perfis acumuláveis; contratos/assinaturas e pagamentos simulados precisam de alinhamento com a nova semântica.
- **Backend:** relações Worker/Employer independentes são melhor ponto de partida, mas modelos de marketplace, messaging, payments, reviews e notifications estão incompletos.
- **Assessment:** não deve orientar o domínio.
- **Verification:** manter apenas depois de definir finalidade e fluxo proporcional.
- **Contract:** deve evoluir semanticamente para contratação/acordo com versões/alterações.
- **Payment:** separar PaymentTerms/PaymentStatus de PaymentProvider/Transaction.
- **Review:** associar a contratação e perspectiva da parte.
- **Dispute:** representar reporte/estado/evidência, não decisão arbitral.
- **Messages/Notifications:** mecanismos auxiliares; não devem dominar o modelo.

## Gate

**G-REQ-RECONCILIATION: PASS.**

Pendências antes de **G-REQ final**:
1. definir estados e transições das entidades centrais;
2. rever atomicidade dos 28 RF;
3. consolidar as 14 RN com as novas capacidades administrativas;
4. definir critérios verificáveis dos RNF;
5. gerar matriz final de rastreabilidade Necessidade → RN → RF/RNF → futuro teste.
