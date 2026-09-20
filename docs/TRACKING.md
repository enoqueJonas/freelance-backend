# Tracker — Reconstrução Científica e Técnica da Monografia

Última actualização: 2026-09-20.

## Estado geral

| Área | Estado | Próxima acção |
|---|---|---|
| Auditoria backend AS-IS | Concluída | Reavaliar após definição dos requisitos |
| Auditoria frontend AS-IS | Concluída | Reavaliar após definição dos requisitos |
| Gap frontend/backend | Concluído | Usar na futura reconstrução técnica |
| Guião — trabalhadores | Preparado | Validar/ajustar antes da recolha real |
| Guião — empregadores | Preparado | Validar/ajustar antes da recolha real |
| Piloto sintético — 11 entrevistas | Concluído | Usar apenas para validar instrumento/método |
| Codificação do piloto | Concluída | Não tratar N01–N18 como resultados reais |
| Análise documental | **Pendente** | Executar durante a reconstrução da monografia |
| Entrevistas reais | **Pendente** | Executar e registar separadamente |
| Codificação das entrevistas reais | **Pendente** | Criar matriz com excertos/códigos/temas |
| Triangulação | **Bloqueada** | Fazer somente após entrevistas reais + análise documental |
| Regras de negócio | **Bloqueadas** | Derivar após triangulação |
| RF/RNF definitivos | **Bloqueados** | Reconstruir após RN/necessidades validadas |
| Modelação UML | **Bloqueada** | Rever após requisitos definitivos |
| Alinhamento código ↔ requisitos | **Bloqueado** | Implementar depois da modelação |
| Testes/validação do protótipo | **Bloqueados** | Definir contra requisitos implementados |
| Redacção final de resultados/conclusão | **Bloqueada** | Fazer com evidência real |

## Backlog de investigação

### P1 — Antes/durante a reconstrução da monografia
- [ ] Estabilizar definitivamente o âmbito: aplicação web, trabalhadores autónomos de TI, empregadores/clientes, Cidade de Maputo.
- [ ] Corrigir pergunta de pesquisa e objectivos para o mesmo âmbito.
- [ ] Rever metodologia para remover métodos/análises que não tenham evidência de execução.
- [ ] Resolver inconsistência da amostra presente no draft.
- [ ] Executar análise documental a partir das fontes efectivamente utilizadas na monografia.
- [ ] Para cada documento, registar evidência → interpretação → necessidade/implicação, com página/secção verificável.
- [ ] Verificar fontes bibliográficas e remover referências não verificáveis/malformadas.
- [ ] Verificar legislação moçambicana aplicável antes de afirmar requisitos legais sobre contratos electrónicos, assinatura, dados pessoais ou pagamentos.

### P2 — Recolha qualitativa
- [ ] Rever os dois guiões à luz do piloto.
- [ ] Definir identificação anonimizada dos participantes reais.
- [ ] Realizar 8 entrevistas reais com trabalhadores autónomos de TI.
- [ ] Realizar 3 entrevistas reais com empregadores/clientes.
- [ ] Registar pergunta/resposta e follow-ups sem forçar o guião.
- [ ] Separar transcrição/evidência de interpretação.
- [ ] Codificar entrevistas reais por temas.
- [ ] Registar casos negativos/divergências, não apenas convergências.

### P3 — Síntese científica
- [ ] Cruzar análise documental com entrevistas reais.
- [ ] Construir matriz de triangulação.
- [ ] Consolidar necessidades validadas.
- [ ] Identificar regras de negócio.
- [ ] Reconstruir RF e RNF com fonte/rastreabilidade.
- [ ] Comparar requisitos reconstruídos com os 32 RF existentes: manter / alterar / remover / adicionar.
- [ ] Rever hipótese de pesquisa e decidir se deve ser reformulada/removida.

### P4 — Engenharia da solução
- [ ] Rever modelo de papéis Worker/Employer e exclusividade de roles.
- [ ] Decidir modelo de verificação bilateral.
- [ ] Decidir se assessment existe, para quem e com que carácter (opcional/obrigatório).
- [ ] Modelar diferentes evidências de competência/experiência.
- [ ] Rever ciclo Offer → Proposal → Agreement/Contract, incluindo serviços sem preço inicial fechado.
- [ ] Modelar alterações ao acordo/escopo.
- [ ] Rever pagamentos e distinguir simulação de integração real.
- [ ] Rever reputação bilateral e cold-start.
- [ ] Definir papel real de disputes/mediação.
- [ ] Decidir se chat interno é necessário ou se basta rastreabilidade contextual.
- [ ] Rever localização como atributo contextual.
- [ ] Alinhar frontend e backend.
- [ ] Corrigir findings técnicos do backend já registados na auditoria.
- [ ] Remover artefactos de ambiente/segredos do repositório e reforçar configuração.
- [ ] Criar testes automatizados relevantes.

### P5 — Monografia e validação
- [ ] Actualizar capítulo de metodologia com o processo realmente executado.
- [ ] Escrever resultados qualitativos por temas, não como confirmação do protótipo.
- [ ] Integrar análise documental no enquadramento/levantamento apropriado.
- [ ] Actualizar levantamento de actores e regras de negócio.
- [ ] Actualizar tabela de RF/RNF.
- [ ] Criar/rever diagramas de casos de uso, actividades, sequência, classes/estados conforme necessário.
- [ ] Documentar arquitectura e implementação real sem sobreafirmar integrações.
- [ ] Definir casos de teste derivados dos requisitos.
- [ ] Executar e registar validação do protótipo.
- [ ] Redigir discussão, limitações, conclusão e recomendações.
- [ ] Fazer auditoria final de rastreabilidade: problema → objectivos → metodologia → evidências → necessidades → requisitos → modelação → implementação → testes → conclusão.
- [ ] Fazer revisão final de numeração, figuras, quadros, referências internas, terminologia e bibliografia.

## Gates

**Gate G1 — Evidência suficiente:** entrevistas reais e análise documental concluídas.

**Gate G2 — Necessidades validadas:** triangulação concluída.

**Gate G3 — Especificação estável:** RN + RF + RNF aprovados e rastreáveis.

**Gate G4 — Modelo estável:** UML/arquitectura alinhadas com requisitos.

**Gate G5 — Implementação verificável:** frontend/backend alinhados e funcionalidades declaradas realmente implementadas.

**Gate G6 — Validação concluída:** testes/evidências permitem responder aos objectivos da investigação.

## Regra de tracking

Uma task bloqueada por um gate não deve ser marcada como concluída apenas porque existe código ou texto no draft. A evidência de conclusão deve corresponder à etapa científica/técnica indicada.
