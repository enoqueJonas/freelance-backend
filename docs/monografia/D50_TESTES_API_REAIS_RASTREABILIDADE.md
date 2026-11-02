# D50 — Transição de testes do modelo para testes reais da API

**Data:** 02-11-2026.  
**Fonte:** repositório `enoqueJonas/freelance-backend`, ramo `qa/d50-accounts-api-regression`; PR técnico independente: https://github.com/enoqueJonas/freelance-backend/pull/3

**Este documento distingue objectos de teste:**

| Nível | Entrega | Estado e alcance |
|---|---|---|
| D49 | 32 testes em modelo Python independente | Executados no modelo de referência; **não testam aplicação** |
| D50 | 18 testes com DRF APITestCase sobre endpoints Django reais | Testes adicionados ao repositório e workflow GitHub Actions configurado; **18/18 aprovados em execução real de CI**: [GitHub Actions D50, run #41478553838](https://github.com/enoqueJonas/freelance-backend/actions/runs/41478553838) na revisão `44c4e67097c79f31f48dd42406f3ceeb7b073722` (base de dados de teste SQLite; `python manage.py check` sem problemas) |
| Monografia V01–V08 | Aceitação dos RF01–RF28 | **Não executados** como cenários integrais; D50 só abrange subconjunto de RF01–RF04 e aspectos de RNF02/RNF03 |
| Monografia RNF01–RNF07 | Verificação não funcional integral | **Não executada**; D50 limita-se a controlo de acesso básico e privacidade da listagem, não a conformidade de segurança completa |
| Fluxo V02/V03 | Proposta aceite → PENDING_AGREEMENT → acordo → ACTIVE | **Não implementado no backend**: não existem endpoints de propostas, contratos nem AgreementVersion na configuração examinada |

## 1. Defeitos directamente identificados em código

| D50 ID | Código anterior | Problema | Correcção proposta no PR #3 |
|---|---|---|---|
| API-01 | `MyProfile` sem `permission_classes` | Endpoint de perfil privado não requer autenticação na definição da classe | `IsAuthenticated` |
| API-02 | `MyWorker` e `MyEmployer` sem `permission_classes` | Tentativa de criar/consultar perfil sem identidade autenticada; potencial erro ao guardar utilizador anónimo | `IsAuthenticated` |
| API-03 | `MyWorker.get` acede `user.worker_profile` | A OneToOne `Worker.user` não tem `related_name`; acesso inverso correcto é `user.worker` | Usar `request.user.worker` |
| API-04 | `EmployerSerializer` usa `fields=['id','name',...]` | `Employer` não possui campo `name`, mas o serializer declara `employer_name` | Devolver `employer_name` |
| API-05 | `EmployerList` usa `prefetch_related('client_documents')` | Relação não existe no modelo Employer consultado | Remover `prefetch_related` inválido |
| API-06 | `UserList` exige apenas `IsAuthenticated` | Lista emails e telefones de outros utilizadores a qualquer conta autenticada | Exigir `IsAdminUser` e documentar necessidade de política de visibilidade |
| API-07 | `RegisterSerializer.validate_phone_number` | Método não corresponde ao campo `phone`; normalização específica não é invocada | Renomear para `validate_phone` |
| API-08 | POST duplicado em `MyWorker` sem código de erro | Responde com sucesso HTTP 200 apesar de rejeitar a acção | Devolver HTTP 400 |

**Atenção:** os oito defeitos foram identificados por leitura estática e as respectivas correcções submetidas; os 18 testes de API **passaram realmente no GitHub Actions**. Isso não confirma todos os caminhos possíveis, a segurança do sistema inteiro ou quaisquer RF do domínio de contratos.

## 2. Ensaios de API adicionados

Ficheiro: `apps/accounts/test_api_d50.py`, 18 testes independentes sobre:

- Registo, normalização e rejeição de telefone inválido;
- Emissão de access/refresh JWT por credenciais reais;
- Rejeição de acesso anónimo ao perfil privado e à criação de perfis;
- Visibilidade da lista de utilizadores apenas para staff e restrição de consulta de terceiro;
- Criação/consulta de perfil Worker, rejeição de duplicação e isolamento do perfil por utilizador;
- Criação simultânea de Worker e Employer na mesma conta (RN01);
- Serialização de Employer, listagem administrativa e negação a não staff;
- Listagem de Worker protegida e filtragem por competências.

Ambiente GitHub Actions configurado: Python 3.13, dependências do `requirements.txt`, Django system check, testes DRF usando base de dados temporária SQLite. O fluxo só verifica módulo `apps.accounts`. A implantação PostgreSQL e contratos continuam fora do âmbito.

## 3. Relação com os requisitos da D44

| Requisito | Contributo D50 | Limite |
|---|---|---|
| RF01 — Registar utilizador | Registo + validação/normalização de telefone | Não avalia usabilidade, recuperação de conta nem privacidade completa |
| RF02 — Autenticar | Endpoint JWT real, tokens presentes | Sem teste completo de expiração, revogação ou integração React |
| RF03 — Gerir perfil trabalhador | Criar e consultar; protecção de conta | Não testa edição, remoção, evidências profissionais de RF05 |
| RF04 — Gerir perfil empregador | Criar e consultar; ambos os perfis na mesma conta | Ainda não há ciclo de oportunidades |
| RN01 — Perfis acumuláveis | Ambos na mesma conta e sem campo único obrigatório no backend | Frontend continua com role exclusivo |
| RNF02 — Segurança/autorização | Acesso negado a anónimo, não staff e não titular em endpoints específicos | Não é pentest; autorização de recurso no contrato não existe |
| RNF03 — Privacidade | Restringir consulta de listagem de utilizadores com email/telefone | Exige matriz de campos/actores e testes em todos os endpoints |

**Não declarar RF01–RF04 ou RNF02/RNF03 completamente satisfeitos com a suite D50:** é cobertura parcial de comportamentos seleccionados.

## 4. Próximas verificações concretas

- [x] Consultar resultado final do GitHub Actions do PR #3: 18 testes executados e aprovados em 02-11-2026, run #41478553838; `manage.py check` sem problemas; não extrapolar para o frontend.
- [ ] Testar autorização no registo e alterações de recursos segundo a relação com o utilizador, não apenas autenticação.
- [ ] Rever configurações de segurança do Django e segredos de ambiente sem publicar credenciais.
- [ ] Decidir o modelo de Engagement/AgreementVersion conforme D48/D49 antes de desenvolver endpoints.
- [ ] Implementar o primeiro corte vertical de oportunidade/proposta/acordo apenas após fixar invariantes, migrações, contratos API e plano de verificação.
- [ ] Executar V02/V03 com API real, conta trabalhador distinta do empregador, transições, histórico persistido e provas de resultado.
- [ ] Actualizar §§5.3–5.5 da D44 somente com estados reais de implementação e execução, em data/commit documentados.

**A D44 canónica e os comentários do supervisor continuam inalterados.**
