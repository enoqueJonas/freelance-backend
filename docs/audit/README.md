# Baseline de Auditoria — ServiPlus

Este directório regista a auditoria AS-IS realizada antes da reconstrução dos requisitos e antes de alterações funcionais ao protótipo.

## Princípios

1. O código descreve o estado actual da implementação, não a origem científica dos requisitos.
2. Requisitos serão posteriormente derivados e justificados por entrevistas semiestruturadas, análise documental e benchmark de soluções existentes.
3. Deve distinguir-se entre solução concebida, protótipo interactivo e implementação técnica.
4. Funcionalidades simuladas não serão descritas como integrações reais.
5. As decisões futuras devem manter rastreabilidade: evidência → necessidade/regra → requisito → modelação → implementação → teste.

## Documentos

- `backend-as-is.md` — estado actual do backend Django.
- `frontend-as-is.md` — estado actual do protótipo React.
- `prototype-gap-analysis.md` — comparação entre as duas camadas e gaps.
- `../research/interview-guide-workers.md` — guião para trabalhadores autónomos de TI.
- `../research/interview-guide-employers.md` — guião para empregadores/clientes.

## Baseline

Backend oficial: `enoqueJonas/freelance-backend`, branch `master`, commit auditado `6617ddf1d6dc29ccdebef6adb91602cecafe26ab`.

Frontend oficial: `enoqueJonas/freelance-frontend`.

Esta baseline não altera código funcional.
