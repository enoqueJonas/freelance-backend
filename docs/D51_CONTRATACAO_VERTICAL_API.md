# D51 — Primeiro fluxo de contratação Django, com persistência e autorização

**Estado:** protótipo técnico parcial, sujeito a CI e a revisão do domínio. **Não** é um artefacto aprovado da monografia nem representa a aplicação completa.

## Requisitos e decisões adoptadas apenas para este piloto

- RN01: uma conta pode ter Worker + Employer, mas uma mesma identidade nunca pode contratar-se a si própria.
- RN02: empregador é identificado pela relação Opportunity → Employer → User; trabalhador pela relação Proposal → Worker → User.
- D48/B1: Engagement pode nascer em PENDING_AGREEMENT com zero AgreementVersion.
- D48/ACT: ambos os intervenientes registam aceite expresso da mesma versão de condições.
- O conteúdo do acordo é associado a uma impressão digital SHA-256. Esta medida detecta alterações ao conteúdo persistido mas não substitui autenticação, assinatura digital qualificada, não-repúdio ou integridade de infraestrutura.
- Toda mutação crítica envolve atomicidade Django e restrições de unicidade. A avaliação de concorrência real em PostgreSQL permanece pendente.

## Sequência implementada

1. Conta com perfil Employer cria oportunidade DRAFT, que só o proprietário pode publicar (OPEN).
2. Conta com perfil Worker diferente do empregador submete Proposal SUBMITTED para oportunidade OPEN. Submissão duplicada é rejeitada.
3. Empregador selecciona proposta SUBMITTED; a oportunidade fecha, alternativas pendentes passam a REJECTED e nasce Engagement PENDING_AGREEMENT.
4. Uma das partes cria AgreementVersion v1 PROPOSED, definindo scope e amount positivo, ou flag price_after_diagnosis=True com amount ausente.
5. Trabalhador e empregador registam aceitação individual da versão v1. Depois de apenas um aceite, Engagement permanece PENDING_AGREEMENT.
6. Depois de duas aceitações distintas do mesmo conteúdo, AgreementVersion passa a ACCEPTED e Engagement passa a ACTIVE.

## Endpoints novos

| Verbo | URI | Segurança e resposta |
|---|---|---|
| GET/POST | /api/marketplace/opportunities/ | Requer autenticação; POST requer Employer |
| POST | /api/marketplace/opportunities/{id}/publish/ | Apenas empregador proprietário; DRAFT→OPEN |
| POST | /api/marketplace/opportunities/{id}/proposals/ | Worker de outra conta, oportunidade OPEN |
| POST | /api/marketplace/proposals/{id}/accept/ | Proprietário escolhe uma proposta; cria Engagement pendente |
| GET | /api/contracts/engagements/{id}/ | Apenas intervenientes da contratação |
| POST | /api/contracts/engagements/{id}/agreements/ | Uma das partes cria primeira versão |
| POST | /api/contracts/engagements/{id}/agreements/{version_id}/accept/ | Uma das partes aceita a versão |

## Verificação executável

- apps/contracts/test_contract_flow_d51.py: 23 testes DRF de estados, autorização, autocontratação, duplicação, preço e aceite bilateral.
- apps/accounts/test_api_d50.py: 18 testes DRF existentes de perfis/autenticação, herdados da branch D50.
- GitHub Actions em .github/workflows/d51-contract-core.yml executa verificação Django, sincronização de migrações e testes com SQLite temporário e Python 3.13.
- Reprodução local (Python 3.13 e dependências do projecto): python manage.py test apps.accounts.test_api_d50 apps.contracts.test_contract_flow_d51 -v 2
- **Até confirmação do CI**, nenhum dos 41 testes é declarado aprovado neste documento.

## Limites metodológicos e técnicos

- D51 é uma cobertura técnica parcial de RF07, RF11, RF12 e RF13, com representação inicial de RF14. Não cobre gestão completa de propostas e oportunidades.
- Não existe segunda versão de acordo, rejeição de versões, adenda, entrega, conclusão, registo de pagamento, integração PSP, reputação ou processo de conflito.
- Não há frontend React integrado, análise de usabilidade, actores reais do público-alvo, nem execução de V02/V03 integralmente.
- Configuração Django de desenvolvimento contém segredo literal e DEBUG=True; NÃO está pronta para produção.
- A arquitectura académica que recomenda PostgreSQL ainda não foi verificada neste fluxo, pois CI usa SQLite de teste.
- Os pressupostos B/B1 e aceitação explícita continuam por validar com a autora/supervisor.
- D44 canónica, índices, figuras, e 14 comentários do supervisor continuam sem alteração.

## Critérios para a etapa seguinte

- Registar logs e resultados reais do CI. Resolver diferenças entre migrações e modelos se existirem.
- Integrar o React no fluxo mínimo sem autenticação simulada nem dados fictícios, passando por JWT real.
- Implementar histórico imutável das alterações e versão v2 quando o domínio tiver sido validado.
- Depois executar V02/V03 num ambiente identificado, com entradas, saídas observadas e resultados por requisito.
- Actualizar a monografia apenas com resultados comprovados, sem confundir testes Django com validação integral do público-alvo.
