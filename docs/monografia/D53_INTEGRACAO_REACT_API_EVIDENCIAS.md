# D53 — Integração React e API Django: implementação, evidência e limites

**Data:** 02-11-2026  
**Monografia de referência:** `Monografia_D44_Metodologia_Proveniencia_Verificada.docx` (82 páginas); **DOCX canónico não alterado**.  
**Repositórios e PRs:** [frontend PR #1](https://github.com/enoqueJonas/freelance-frontend/pull/1) e [backend PR #6](https://github.com/enoqueJonas/freelance-backend/pull/6), este último dependente de PR #5 → #4 → #3.

## 1. O que foi efectivamente implementado

Na aplicação React foi acrescentado um percurso independente, `/#/real`, **sem `mockApi`** e fora do contexto de autenticação fictícia da interface antiga. O cliente `src/services/realApi.ts` executa pedidos HTTP dirigidos à API real Django, identifica os erros de rede e os códigos 401/403/409 e utiliza JWT emitido por `/api/auth/login/` após autenticação com `username` e `password`.

O ecrã D53 permite, por acções explícitas do utilizador:

1. Registar uma conta com dados de perfil e telefone moçambicano, autenticar e criar um ou ambos os perfis Worker/Employer;
2. Criar oportunidade em DRAFT e publicar em OPEN como empregador titular;
3. Consultar oportunidades abertas de terceiros e submeter proposta, como trabalhador distinto;
4. Consultar propostas recebidas como proprietário e seleccionar uma proposta, criando Engagement PENDING_AGREEMENT;
5. Consultar a contratação como uma das partes e propor a primeira versão do acordo;
6. Aceitar ou rejeitar versões de condições, com fingerprint SHA-256 do conteúdo consultado; após duas aceitações, Engagement passa a ACTIVE;
7. Propor alteração posterior, mantendo a versão vigente enquanto a nova está pendente e preservando o histórico das rejeições.

No backend, foram acrescentadas duas **listagens restritas por autorização**: `GET /api/marketplace/opportunities/{id}/proposals/` para o empregador titular e `GET /api/contracts/engagements/` para qualquer uma das partes numa contratação. Sem esses endpoints a interface dependeria de IDs arbitrários ou exposição indevida de informações de terceiros.

## 2. Evidência de verificação — resultados que podemos afirmar

| Ensaio | Objecto efectivamente testado | Resultado verificável | O que NÃO demonstra |
|---|---|---|---|
| [CI backend D53 #41484092825](https://github.com/enoqueJonas/freelance-backend/actions/runs/41484092825) | Django/DRF com SQLite temporário, testes D50–D53 | **71/71 testes aprovados**; `manage.py check` sem problemas, `makemigrations --check --dry-run` sem alterações | Não prova que React enviou pedidos nem que UI é usável |
| [CI frontend D53 #41486079214](https://github.com/enoqueJonas/freelance-frontend/actions/runs/41486079214) | Cliente HTTP com `fetch` simulado, TypeScript e compilação | **6/6 testes do cliente aprovados**, `npm run lint` e `npm run build` concluídos na revisão mais recente | Não é teste com browser real nem Django em execução |
| Revisão estrutural do código | Rota React isolada e cliente sem dependência de mock | Percurso programado e ligado aos endpoints identificados | Sem captura real de browser nem execução por participante |
| V02/V03 da monografia | Publicação/proposta e acordo versionado | **Ainda não executados integralmente nesta etapa** | V04 corresponde a execução/entrega, não a acordos |

A última revisão frontend inclui a correcção de retorno ao formulário de login após terminar a sessão e a substituição do README genérico. O CI [#41486079214](https://github.com/enoqueJonas/freelance-frontend/actions/runs/41486079214) verificou **6/6 testes do cliente, TypeScript e build**, todos com resultado positivo.

## 3. Decisões e mitigação de risco

- **Separação de modos:** a rota `/real` não monta o `AuthProvider` de demonstração. Páginas antigas como `/login`, `/dashboard`, `/offers`, `/profile` continuam baseadas em `mockApi` e **não devem ser apresentadas como operações ligadas ao Django**.
- **Autenticação:** username + password emitindo JWT real; token de acesso apenas em memória React, sem persistência no browser. Isto reduz persistência de credenciais, mas faz perder a sessão no refresh e **não** constitui desenho completo de autenticação para produção.
- **Acordos:** conteúdo é consultado antes de aceitar e a fingerprint acompanha o pedido; assinatura electrónica qualificada e não-repúdio **não foram implementados**.
- **API e servidores:** Vite encaminha `/api` para Django via proxy local. Produção requer TLS, reverse proxy same-origin e endurecimento das configurações Django; neste estado `DEBUG=True`, segredo estático e SQLite não devem ser expostos publicamente.
- **Dados do corpus da monografia:** a integração técnica não comprova entrevistas reais, eficácia no mercado de Maputo nem aceitação por utilizadores. Não alterar conclusão HG/HE1–HE4 para «confirmadas».

## 4. Plano de execução E2E real que permanece pendente

**Ambiente:** backend branch `feat/d53-ui-api-read-models` no porto 8000, frontend `feat/d53-real-django-flow` no porto 3000; migrations aplicadas a base de ensaio isolada; duas contas criadas pelo próprio fluxo `/#/real`, sem reutilizar contas pessoais.

**Cenário V02 (parcial):** empregador publica oportunidade, trabalhador de outra conta encontra-a e submete proposta, empregador recebe e aceita. Validar estados e autorização de terceiros.

**Cenário V03 (parcial):** contratação inicia PENDING_AGREEMENT; uma parte propõe v1, ambas aceitam a mesma versão e passam a ACTIVE; criar v2, rejeitar e verificar persistência de v1; propor v3 e aceitar bilateralmente para validar estado SUPERSEDED/ACCEPTED. **V04 exige ExecutionRecord, entrega e conclusão, e não é exercitado por este fluxo.**

**Evidência necessária:** identificadores de revisão do software, timestamps de execução, vídeo/capturas do browser, registos de requests/responses sem segredos, estados persistidos no backend e resultado por passo. Não incluir tokens JWT em capturas ou documentação.

**Testes adicionais obrigatórios:** sessão expirada, erro de proxy, privilégios de terceiro, falha de backend, duplicação de pedidos, recarga do browser, compatibilidade entre navegadores e concorrência de duas contas.

## 5. Correspondência restrita com RF/RN da D44

| Área | Estado até D53 |
|---|---|
| RN01/RN02 | Perfis acumuláveis, proibição de autocontratação, com provas de API |
| RF01–RF04 | Registo/autenticação e criação de perfis ligados à rota real; verificação de API parcial |
| RF07/RF11/RF12 | Criar/publicar, propor e seleccionar, com API testada e componentes React programados |
| RF13/RF14/RN06 | Aceitação inicial e versionamento no backend; interface React adicionada; sem browser E2E comprovado |
| RNF02/RNF03/RNF04 | Controlo básico de acesso e histórico de versões; **não** segurança/conformidade integral |
| V02/V03 | **Fluxos ainda não executados na sua íntegra** |
| V04 — execução/entrega | **Não executado** |

## 6. Critérios de fecho

- [x] Criar rota React D53 sem autenticação fictícia.
- [x] Configurar proxy de desenvolvimento e cliente API com tipagem.
- [x] Implementar listagens Django autorizadas para propostas/contratações.
- [x] Confirmar 71/71 testes backend no GitHub Actions.
- [x] Confirmar 6/6 testes de cliente, typecheck e build na primeira execução frontend D53.
- [x] Confirmar última execução CI após correcção de troca de contas e README: #41486079214, 6/6 testes, typecheck e build.
- [ ] Executar fluxo browser + Django real com duas contas e capturas/logs verificáveis.
- [ ] Substituir progressivamente páginas antigas baseadas em mock por componentes reais.
- [ ] Testar backend PostgreSQL em concorrência e preparar configuração segura.
- [ ] Obter aprovação das decisões D48/B/B1, aceite e rejeição, actualizar diagramas e inserir as evidências **no Word original**, preservando os comentários do supervisor.

**Não declarar a aplicação validada nem a monografia concluída com base em CI isolado de React e Django.**
