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
- [ ] Verificar exigência institucional da hipótese e decidir se deve ser reformulada ou removida.
- [ ] Completar delimitação do estudo (espacial, temática e tecnológica definidas; temporal pendente).
- [ ] Verificar coerência Problema → Pergunta → Objectivos → Metodologia.

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
