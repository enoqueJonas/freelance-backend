# Actores e Casos de Uso — ConecTA

## 1. Regra de modelação

Os casos de uso são derivados da baseline final de requisitos. Não se cria um caso de uso apenas porque existe uma página ou componente no protótipo.

O mesmo **Utilizador** pode acumular os perfis **Trabalhador** e **Empregador**. Trabalhador e Empregador são especializações contextuais do utilizador autenticado, não contas mutuamente exclusivas.

## 2. Actores

### Visitante
Pessoa ainda não autenticada.
Responsabilidades/interacções principais:
- Registar utilizador;
- Autenticar-se.

### Utilizador autenticado
Actor geral que representa capacidades comuns.
- Gerir dados básicos da conta/sessão;
- Consultar informação permitida;
- activar/manter os perfis aplicáveis.

### Trabalhador
Utilizador que possui WorkerProfile e actua como prestador numa determinada oportunidade/contratação.
- gerir perfil profissional e evidências;
- pesquisar oportunidades;
- submeter/gerir propostas;
- participar na formalização/alteração do acordo;
- registar execução/entrega;
- acompanhar pagamentos;
- avaliar empregador;
- reportar/acompanhar conflito.

### Empregador
Utilizador que possui EmployerProfile e actua como contratante.
- gerir perfil de empregador;
- pesquisar trabalhadores;
- gerir oportunidades;
- avaliar propostas;
- participar na formalização/alteração do acordo;
- acompanhar execução/entrega;
- gerir/acompanhar estado de pagamento;
- avaliar trabalhador;
- reportar/acompanhar conflito.

### Administrador
Utilizador autorizado para governação da plataforma.
- gerir utilizadores segundo política;
- moderar oportunidades reportadas;
- analisar verificação quando aplicável;
- acompanhar processos de contestação/conflito dentro dos limites administrativos.

### Prestador Externo de Pagamento
Actor externo opcional, apenas se RF20 for implementado.
- processar/devolver estado de transacção iniciada/facilitada pela plataforma.

Não é actor obrigatório do protótipo base.

## 3. Casos de uso principais

| ID | Caso de uso | Actor principal | RF |
|---|---|---|---|
| UC01 | Registar utilizador | Visitante | RF01 |
| UC02 | Autenticar utilizador | Visitante/Utilizador | RF02 |
| UC03 | Gerir perfil profissional | Trabalhador | RF03 |
| UC04 | Gerir perfil de empregador | Empregador | RF04 |
| UC05 | Gerir evidências de competência | Trabalhador | RF05 |
| UC06 | Gerir verificação de perfil/identidade | Utilizador / Administrador | RF06, RF28 |
| UC07 | Gerir oportunidade | Empregador | RF07 |
| UC08 | Pesquisar oportunidades | Trabalhador | RF08 |
| UC09 | Pesquisar trabalhadores | Empregador | RF09 |
| UC10 | Consultar perfil | Trabalhador/Empregador | RF10 |
| UC11 | Gerir proposta própria | Trabalhador | RF11 |
| UC12 | Avaliar proposta | Empregador | RF12 |
| UC13 | Formalizar condições acordadas | Trabalhador + Empregador | RF13 |
| UC14 | Gerir alteração ao acordo | Trabalhador + Empregador | RF14 |
| UC15 | Registar actualização da execução | Trabalhador/Empregador | RF15 |
| UC16 | Registar entrega/conclusão | Trabalhador/Empregador | RF16 |
| UC17 | Consultar histórico da contratação | Trabalhador/Empregador | RF17 |
| UC18 | Gerir condições de pagamento | Trabalhador + Empregador | RF18 |
| UC19 | Gerir estado de pagamento | Trabalhador/Empregador | RF19 |
| UC20 | Facilitar pagamento externo | Trabalhador/Empregador + PSP | RF20 |
| UC21 | Avaliar contraparte | Trabalhador/Empregador | RF21 |
| UC22 | Consultar reputação | Trabalhador/Empregador | RF22 |
| UC23 | Contestar avaliação | Trabalhador/Empregador | RF23 |
| UC24 | Reportar conflito | Trabalhador/Empregador | RF24 |
| UC25 | Acompanhar conflito | Trabalhador/Empregador/Admin | RF25 |
| UC26 | Gerir utilizadores | Administrador | RF26 |
| UC27 | Moderar oportunidade reportada | Administrador | RF27 |

RF28 foi incorporado em UC06 porque análise administrativa é parte do fluxo de verificação, não um objectivo autónomo do utilizador.

## 4. Relações entre casos de uso

### Generalização de actores
- Trabalhador —|> Utilizador autenticado
- Empregador —|> Utilizador autenticado
- Administrador —|> Utilizador autenticado

Um mesmo User pode instanciar os contextos Trabalhador e Empregador.

### Relações funcionais recomendadas

- UC07 Gerir oportunidade inclui validação das regras de estado da Opportunity.
- UC11 Gerir proposta depende de UC08/consulta da oportunidade, mas pesquisar não é obrigatoriamente «include»: uma oportunidade pode ser acedida por ligação directa.
- UC12 Avaliar proposta pode originar UC13 quando uma proposta é aceite.
- UC13 Formalizar condições acordadas inclui definição/confirmação das condições relevantes, incluindo UC18 quando houver condições de pagamento.
- UC14 Gerir alteração ao acordo estende a contratação activa quando surge necessidade de alteração; não é obrigatório em toda contratação.
- UC16 Registar entrega/conclusão ocorre sobre contratação formalizada/activa.
- UC17 Consultar histórico é transversal aos registos da contratação.
- UC21 Avaliar contraparte só fica disponível quando a contratação cumpre a regra de elegibilidade.
- UC23 Contestar avaliação estende UC22/UC21 apenas quando existe avaliação contestável.
- UC24 Reportar conflito pode ocorrer durante estados elegíveis da contratação e cria o processo acompanhado por UC25.
- UC20 Facilitar pagamento externo é extensão opcional de UC19/RF20 e depende do Prestador Externo de Pagamento.
- UC27 Moderar oportunidade reportada só ocorre quando existe sinalização/reporte que justifique análise administrativa.

## 5. Casos de uso que NÃO serão modelados como principais

- Realizar assessment técnico;
- validar universalmente competências;
- assinar digitalmente todos os contratos;
- custodiar fundos/escrow;
- chat em tempo real;
- receber notificações;
- matching algorítmico;
- geolocalização universal;
- arbitrar disputa.

Podem existir mecanismos auxiliares no protótipo sem serem promovidos a casos de uso científicos.

## 6. Casos de uso prioritários para especificação detalhada

Não é necessário criar diagrama de actividade/sequência para todos os 27 UC. Os fluxos com maior valor de domínio e cobertura são:

1. **UC01 — Registar utilizador**
2. **UC07 — Gerir oportunidade**
3. **UC11 — Gerir proposta própria**
4. **UC13 — Formalizar condições acordadas**
5. **UC14 — Gerir alteração ao acordo**
6. **UC16 — Registar entrega/conclusão**
7. **UC19 — Gerir estado de pagamento**
8. **UC21 — Avaliar contraparte**
9. **UC24/UC25 — Reportar e acompanhar conflito**

Para UML detalhado, recomenda-se seleccionar fluxos representativos em vez de duplicar operações CRUD.

## 7. Fronteira do sistema

Dentro da ConecTA:
- identidade/conta e perfis;
- oportunidades/propostas;
- contratação e versões do acordo;
- execução/entrega;
- condições e registos de pagamento;
- reputação;
- conflitos;
- governação.

Fora da ConecTA:
- execução material do serviço de TI;
- transferência/custódia financeira real, salvo integração externa;
- decisão jurídica sobre disputas;
- validação universal da competência técnica;
- redes sociais/WhatsApp/serviços externos usados fora do protótipo.

## 8. Gate parcial de modelação

**G-MODEL-UC: PASS.**

Actores e casos de uso estão rastreados à baseline de RF. Próximo passo: modelo conceptual/classes do domínio, garantindo que cada agregado suporta estes casos de uso e os estados já definidos.
