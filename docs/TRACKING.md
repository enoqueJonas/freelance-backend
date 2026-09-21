# Tracker — Reconstrução Científica e Técnica da Monografia

Última actualização: 2026-09-20.

## Plano da auditoria — 7 fases

| Fase | Objectivo | Estado |
|---|---|---|
| **1. Auditoria estrutural** | Diagnosticar estrutura, coerência, lacunas, inconsistências e estado real do protótipo/código | **Concluída** |
| **2. Espinha dorsal científica** | Alinhar problema, pergunta de pesquisa, objectivos, hipótese, âmbito e delimitação | **Pendente** |
| **3. Reconciliação do estudo empírico** | Consolidar metodologia, amostra, instrumentos, registos de entrevistas, análise documental, análise temática e triangulação | **Parcialmente preparada** |
| **4. Engenharia da solução** | Derivar necessidades → RN → RF/RNF → actores → modelação → arquitectura e reconciliar com frontend/backend | **Bloqueada por G2** |
| **5. Validação** | Definir e executar validação/testes contra requisitos e objectivos | **Bloqueada** |
| **6. Resultados e conclusão** | Discussão, resposta à pergunta, cumprimento dos objectivos, limitações, conclusão e recomendações | **Bloqueada** |
| **7. Auditoria final** | Rastreabilidade, coerência, terminologia, referências, figuras/quadros, numeração e qualidade final | **Pendente no fim** |

## Estado dos artefactos

| Área | Estado | Próxima acção |
|---|---|---|
| Auditoria backend AS-IS | Concluída | Reavaliar após requisitos |
| Auditoria frontend AS-IS | Concluída | Reavaliar após requisitos |
| Gap frontend/backend | Concluído | Usar na Fase 4 |
| Guião — trabalhadores | Preparado | Usar como referência do instrumento |
| Guião — empregadores | Preparado | Usar como referência do instrumento |
| Entrevistas efectivamente realizadas | Realizadas parcialmente / notas existentes | Consolidar apenas o que foi efectivamente recolhido |
| Simulação de 11 entrevistas | Concluída | Usar como piloto metodológico; não substituir respostas não recolhidas |
| Codificação da simulação | Concluída | N01–N18 são hipóteses/necessidades candidatas até confronto com evidência real/documental |
| Análise documental | **Pendente** | Executar durante a Fase 3 ao reconstruir a monografia |
| Triangulação | **Bloqueada** | Requer corpus empírico documentado + análise documental |
| Regras de negócio | **Bloqueadas** | Derivar após triangulação |
| RF/RNF definitivos | **Bloqueados** | Reconstruir após RN/necessidades validadas |
| Modelação UML | **Bloqueada** | Rever após requisitos definitivos |
| Alinhamento código ↔ requisitos | **Bloqueado** | Executar na Fase 4 |
| Testes/validação | **Bloqueados** | Fase 5 |
| Resultados/conclusão | **Bloqueados** | Fase 6 |

## Fase 1 — Critérios de fecho

- [x] Auditoria estrutural do draft.
- [x] Auditoria AS-IS do backend.
- [x] Auditoria AS-IS do frontend.
- [x] Gap analysis frontend/backend.
- [x] Identificação de inconsistências de âmbito, metodologia, amostra, resultados, requisitos e referências.
- [x] Registo dos principais riscos de sobreafirmação da implementação.
- [x] Preparação dos guiões de entrevista.
- [x] Piloto do instrumento e análise temática exploratória.
- [x] Registar formalmente o resumo de fecho da Fase 1 e handoff para a Fase 2.

## Fase 2 — Espinha dorsal científica

- [x] Estabilizar o âmbito: aplicação web, trabalhadores autónomos de TI, empregadores/clientes e Cidade de Maputo.
- [x] Definir baseline para reconstrução do problema de pesquisa.
- [x] Reescrever/alinha a pergunta de pesquisa.
- [x] Rever objectivo geral.
- [x] Rever objectivos específicos e estabelecer cadeia de rastreabilidade.
- [x] Verificar exigência institucional e manter hipótese em formulação compatível com o desenho do estudo.
- [x] Fechar delimitação do tema em espaço, tempo e contexto temático; intervalo documental concreto será consolidado na Fase 3.
- [x] Verificar coerência Problema → Pergunta → Objectivos → Metodologia (auditoria vertical aprovada com pendência temporal).

## Fase 3 — Reconciliação do estudo empírico

- [ ] Consolidar amostra efectivamente utilizada e corrigir números contraditórios do draft.
- [ ] Consolidar os registos das entrevistas efectivamente realizadas.
- [ ] Manter dados simulados claramente separados de dados efectivamente recolhidos.
- [ ] Rever metodologia para corresponder apenas aos métodos efectivamente executados.
- [ ] Executar análise documental a partir das fontes efectivamente utilizadas.
- [ ] Registar documento → evidência verificável → interpretação → necessidade/implicação.
- [ ] Incluir página/secção verificável sempre que aplicável.
- [ ] Verificar bibliografia e legislação relevante.
- [ ] Codificar o corpus empírico consolidado.
- [ ] Cruzar entrevistas/documentos numa matriz de triangulação.
- [ ] Consolidar necessidades validadas e divergências.

## Fase 4 — Engenharia da solução

- [ ] Identificar regras de negócio a partir das necessidades validadas.
- [ ] Reconstruir RF/RNF com fonte e rastreabilidade.
- [ ] Comparar os 32 RF existentes: manter / alterar / remover / adicionar.
- [ ] Rever modelo Worker/Employer e exclusividade de roles.
- [ ] Decidir modelo de verificação bilateral.
- [ ] Decidir papel do assessment.
- [ ] Modelar diferentes evidências de competência/experiência.
- [ ] Rever Offer → Proposal → Agreement/Contract e serviços sem preço inicial fechado.
- [ ] Modelar alterações ao acordo/escopo.
- [ ] Rever pagamentos e separar simulação de integração real.
- [ ] Rever reputação bilateral/cold-start.
- [ ] Definir papel de disputes/mediação.
- [ ] Decidir necessidade de chat versus rastreabilidade contextual.
- [ ] Rever localização como atributo contextual.
- [ ] Actualizar actores, casos de uso, actividades, sequências, classes/estados e arquitectura.
- [ ] Alinhar frontend/backend com o modelo aprovado.
- [ ] Corrigir findings técnicos do backend.
- [ ] Reforçar configuração/segredos/higiene do repositório.

## Fase 5 — Validação

- [ ] Derivar casos de teste dos requisitos.
- [ ] Definir critérios de aceitação.
- [ ] Criar testes automatizados relevantes.
- [ ] Executar validação funcional do protótipo.
- [ ] Registar evidências e limitações.
- [ ] Demonstrar quais requisitos foram implementados, simulados ou ficaram fora do protótipo.

## Fase 6 — Resultados e conclusão

- [ ] Escrever resultados por temas e evidências.
- [ ] Integrar resultados da triangulação.
- [ ] Discutir resultados face à literatura/documentos.
- [ ] Responder explicitamente à pergunta de pesquisa.
- [ ] Avaliar cumprimento de cada objectivo.
- [ ] Registar limitações.
- [ ] Redigir conclusão e recomendações.

## Fase 7 — Auditoria final

- [ ] Auditar problema → objectivos → metodologia → evidências → necessidades → requisitos → modelação → implementação → testes → conclusão.
- [ ] Conferir numeração e referências internas.
- [ ] Conferir figuras, quadros, legendas e índices automáticos.
- [ ] Uniformizar terminologia e variante linguística.
- [ ] Verificar referências bibliográficas e citações.
- [ ] Eliminar afirmações técnicas não demonstradas.
- [ ] Fazer leitura final de consistência científica e técnica.

## Gates

**G1 — Evidência suficiente:** corpus empírico efectivamente documentado + análise documental concluída.

**G2 — Necessidades validadas:** triangulação concluída.

**G3 — Especificação estável:** RN + RF + RNF aprovados e rastreáveis.

**G4 — Modelo estável:** UML/arquitectura alinhadas com requisitos.

**G5 — Implementação verificável:** frontend/backend alinhados e funcionalidades declaradas realmente implementadas.

**G6 — Validação concluída:** testes/evidências permitem responder aos objectivos da investigação.

## Regra de tracking

Código existente, texto do draft ou dados simulados não fecham por si só uma etapa científica. Uma task só é concluída quando existe evidência correspondente à actividade indicada.


### Marco Fase 2

- **PHASE-2-CLOSED** — espinha dorsal científica e auditoria vertical aprovadas.
- Próximo marco: **PHASE-3-EMPIRICAL-RECONCILIATION**.


### Gate documental — Fase 3

- **G-DOC: PASS** — corpus documental suficiente para iniciar triangulação temática; não para fechar requisitos.
- Próximo artefacto: matriz Evidência empírica × Evidência documental → Necessidade consolidada.
- Manter entrevistas reais separadas do piloto sintético.


### Gate de triangulação — Fase 3

- **G-TRI: PASS** — N01–N16 consolidadas (N16 condicional); N17 classificada como atributo de qualidade/adopção; N18 como condição de ecossistema.
- Divergências preservadas: assessment, chat, assinatura, integração/custódia de pagamentos, preço, localização, arbitragem e reputação.
- Próxima actividade: derivar RN/RF/RNF candidatos com rastreabilidade explícita.


### Engenharia de requisitos — baseline candidata

- **G-REQ-CANDIDATE: PASS** — derivadas 14 RN, 25 RF e 7 RNF candidatos a partir da triangulação.
- Fora do âmbito nesta baseline: assessment obrigatório, assinatura digital avançada obrigatória, escrow/custódia, matching algorítmico obrigatório, geolocalização universal, arbitragem administrativa e chat como requisito autónomo.
- Próximo passo: confrontar esta baseline com os 32 RF do draft e com o AS-IS técnico, resolver papéis e estados do domínio, e só depois fechar G-REQ.


### Reconciliação dos requisitos do draft

- **G-REQ-RECONCILIATION: PASS** — os 32 RF do draft foram confrontados com a baseline derivada e o AS-IS técnico.
- Recuperadas três capacidades administrativas justificáveis: gestão de utilizadores, moderação de oportunidades reportadas e análise de verificação (condicional ao fluxo de verificação), elevando a baseline para 28 RF candidatos.
- Assessment obrigatório, assinatura digital universal, chat como core, custódia/escrow e arbitragem administrativa permanecem fora da baseline.
- Próximo passo: definir estados/transições, rever atomicidade e fechar a matriz final de rastreabilidade antes de G-REQ.


### Modelo de estados do domínio

- **G-DOMAIN-STATES: PASS** — definidos estados/transições de Opportunity, Proposal, Engagement/Agreement, Payment, Dispute e Review.
- Contract evolui conceptualmente para Engagement + AgreementVersion; alterações preservam histórico.
- PaymentTerms, PaymentRecord e PaymentTransaction foram separados; ConecTA não assume custódia.
- Próximo: atomicidade final + RN/RNF verificáveis + matriz de rastreabilidade para fechar G-REQ.


### Baseline final de requisitos

- **G-REQ: PASS** — baseline fechada após triangulação, reconciliação do draft e modelação de estados.
- Resultado: **16 RN, 28 RF, 7 RNF e 7 Macro Requisitos**.
- Matriz de rastreabilidade N01–N18 → RN → RF/RNF → critério de validação criada; N18 permanece condição de adopção, não requisito.
- Próximo gate: **G-MODEL** — actores/casos de uso, classes/domínio, actividades, sequências, estados e arquitectura.


### Modelação — actores e casos de uso

- **G-MODEL-UC: PASS** — definidos Visitante, Utilizador autenticado, Trabalhador, Empregador, Administrador e PSP opcional.
- 27 casos de uso derivados dos 28 RF; RF28 foi absorvido no fluxo UC06 de verificação.
- Trabalhador/Empregador são capacidades acumuláveis do mesmo User, não contas exclusivas.
- Próximo: modelo conceptual/classes do domínio.


### Modelação — modelo conceptual/classes

- **G-MODEL-CLASS: PASS** — definidos agregados, classes, cardinalidades e invariantes do domínio-alvo.
- AS-IS confrontado: Worker/Employer OneToOne são boa base; Document exclusivo de Employer e Assessment >=50 conflitam com a baseline; Contract/Signature evoluem para Engagement/AgreementVersion.
- Próximo: diagramas de actividade dos fluxos representativos e sequências.


### Modelação — fluxos de actividade

- **G-MODEL-ACTIVITY: PASS** — quatro fluxos representativos definidos: oportunidade/proposta; formalização/alteração; execução/entrega/pagamento; conflito.
- Evitada duplicação de CRUD; estados e decisões de negócio são explícitos.
- Próximo: diagramas de sequência correspondentes, com fronteiras de aplicação e domínio.


### Modelação — sequências

- **G-MODEL-SEQUENCE: PASS** — sequências derivadas dos quatro fluxos de actividade.
- Fronteiras lógicas: UI/API → Application Service → Domain → ORM/Repository; PSP via Adapter opcional.
- Repositories são abstrações UML e não obrigam repository pattern artificial em Django.
- Próximo: representação UML dos estados + arquitectura lógica/física + auditoria cruzada para fechar G-MODEL.


### Modelação — estados, arquitectura e fecho

- **G-MODEL-STATE-UML: PASS** — máquinas de estado consolidadas; Engagement recomendado como diagrama principal na monografia.
- **G-MODEL-ARCH: PASS** — arquitectura-alvo definida: React → Django/DRF → domínio/ORM → PostgreSQL; integrações externas desacopladas.
- **G-MODEL: PASS** — auditoria cruzada RF ↔ UC ↔ classes ↔ actividades ↔ sequências ↔ estados ↔ arquitectura concluída sem lacunas bloqueantes.
- Próximo: plano AS-IS → TO-BE e implementação/refactor incremental do protótipo antes da validação.
