# D54 — Primeiro ensaio de browser ponta a ponta (React + Django) com duas identidades

**Data da execução:** 03-11-2026.  
**Base documental:** `Monografia_D44_Metodologia_Proveniencia_Verificada.docx` (82 páginas; não editada).  
**Frontend de teste:** [PR técnico D54 #2](https://github.com/enoqueJonas/freelance-frontend/pull/2), branch `test/d54-real-browser-e2e`, dependente de [frontend PR D53 #1](https://github.com/enoqueJonas/freelance-frontend/pull/1).  
**Backend:** revisão D53 `ced54117d2db0db9e049086fcc975dd4f36807e0`, [PR #6](https://github.com/enoqueJonas/freelance-backend/pull/6), dependente dos PR #5, #4 e #3.

## 1. Evidência técnica confirmada

A execução [D54 GitHub Actions #41599698482](https://github.com/enoqueJonas/freelance-frontend/actions/runs/41599698482) completou com **1/1 ensaio Playwright aprovado em Chromium real**. O workflow instalou Python 3.13, Django e Node, aplicou migrações da base de teste SQLite, iniciou **servidor Django real na porta 8000** e **Vite/React na porta 3000**, compilou frontend e abriu o browser para percorrer a aplicação `/#/real`.

Log de execução: `Running 1 test using 1 worker`; `D54: two JWT users, real opportunity, proposal, v1 and v2 agreements`; `1 passed`. O tempo reportado pelo Playwright foi aproximadamente 10,8 s para o job de teste de browser (não é métrica de desempenho de negócio).

Uma primeira pipeline falhou **antes de iniciar o browser** porque Playwright 1.56.1 não é compatível com o runner `ubuntu26.04-x64`. A execução foi reproduzida com Ubuntu 24.04, suportado pelo runner seleccionado. As falhas de infra-estrutura estão distintas de defeitos da aplicação.

A revisão posterior ao primeiro ensaio acrescentou **seis capturas automáticas em pontos definidos**, com dados de teste sintéticos, e imobilizou o SHA do backend no workflow. A nova execução [D54 GitHub Actions #41600019575](https://github.com/enoqueJonas/freelance-frontend/actions/runs/41600019575) terminou com **1/1 teste Playwright aprovado**, verificações de TypeScript e build concluídas, e o artefacto visual foi **efectivamente publicado** no GitHub Actions. O backend foi fixado em `ced54117d2db0db9e049086fcc975dd4f36807e0`, evitando alterações silenciosas da branch entre ensaios.

## 2. Percurso executado no browser

| Ordem | Interacção efectivamente executada | Evidência funcional |
|---:|---|---|
| 1 | Registar uma conta de empregador com username e password | Autenticação JWT através da API real |
| 2 | Criar perfil Employer, oportunidade DRAFT e publicar OPEN | Django persiste oportunidade e apresenta-a na UI |
| 3 | Encerrar sessão; registar uma conta Worker de identidade distinta | Não depende de `mockApi`, passwords reais no formulário |
| 4 | Criar Worker e submeter proposta à oportunidade publicada | Proposta SUBMITTED é obtida do backend |
| 5 | Voltar ao empregador e seleccionar proposta | Engagement criado em PENDING_AGREEMENT |
| 6 | Empregador propõe v1 e regista o seu aceite | Contratação continua pendente |
| 7 | Trabalhador autentica e aceita a mesma v1 | Engagement passa a ACTIVE |
| 8 | Trabalhador propõe v2, mantendo v1 vigente; regista primeiro aceite | Nova versão não substitui o acordo anterior unilateralmente |
| 9 | Empregador aceita v2 | v1 SUPERSEDED, v2 ACCEPTED |
| 10 | Empregador propõe v3; trabalhador rejeita com motivo | v3 REJECTED; v2 mantém-se vigente |

**Nível da prova:** cada passo foi executado via acções reais de browser e pedidos a um Django com persistência de ensaio. O cenário foi aprovado de ponta a ponta no contexto de integração restrito acima. Nenhuma destas contas pertence a um participante do estudo; são identidades sintéticas criadas exclusivamente para testes.

## 3. Artefactos visuais planeados para a execução final

| Ficheiro de captura previsto | Ponto documentado | Uso académico permitido |
|---|---|---|
| `01-oportunidade-publicada.png` | Publicação da oportunidade | Ilustrar ecrã do protótipo em teste |
| `02-proposta-submetida.png` | Submissão pelo trabalhador | Evidenciar interface de proposta |
| `03-contratacao-pendente.png` | Engagement PENDING_AGREEMENT | Mostrar separação aceite de proposta / aceitação de condições |
| `04-acordo-v1-activo.png` | Aceitação bilateral inicial | Evidenciar estado ACTIVE na interface |
| `05-versao-v2-vigente.png` | Substituição por nova versão | Evidenciar SUPERSEDED/ACCEPTED |
| `06-versao-v3-rejeitada.png` | Rejeição fundamentada | Evidenciar preservação do acordo vigente |

**Artefacto confirmado:** [d54-real-browser-screenshots (ZIP, GitHub Actions)](https://github.com/enoqueJonas/freelance-frontend/actions/runs/41600019575/artifacts/13213853540), ID `13213853540`, 570 409 bytes, gerado em **03-11-2026 08:01 UTC**, com expiração agendada para **03-12-2026 08:01 UTC**. São seis imagens capturadas em passos do teste, conforme código Playwright. O conteúdo visual ainda carece de inspecção editorial de resolução, margens e legibilidade antes da integração no Word.

**Cautela:** capturas de um browser automatizado com dados fictícios são evidências visuais legítimas do estado do protótipo, **não** fotografias de utilizadores reais nem resultados de entrevistas ou medições de usabilidade. As legendas devem indicar «interface do protótipo — execução automatizada com dados de teste». Não usar para fundamentar estatísticas do mercado.

## 4. Rastreamento com requisitos e hipóteses

| RF/RN da D44 | Cobertura relevante de D54 | Limite |
|---|---|---|
| RN01/RN02 | Utilizadores separados com dois perfis e autocontratação previamente recusada pela suite backend | O browser executou dois actores diferentes, não todos os ataques possíveis |
| RF07 | Criar e publicar oportunidade | Não exercitou todos os estados do ciclo |
| RF11/RF12 | Submeter e seleccionar proposta | Sem múltiplas propostas no ensaio de browser |
| RF13 | Acordo inicial aceite pelas duas partes | Não equivale a assinatura jurídica qualificada |
| RF14/RN06 | Propor, aceitar, rejeitar v2/v3 e preservar versão vigente | Um cenário específico, sem teste de concorrência PostgreSQL |
| RF18 | Preço positivo associado à versão do acordo | Sem meios de pagamento, etapas ou liquidação |
| RNF02/03/04 | Testes de API anteriores comprovam algumas guardas; D54 mostra fluxo UI integrado | Não constitui ensaio completo de segurança, privacidade ou performance |
| V02–V04 | **Uma trajectória integrada foi executada com sucesso** | Não declarar casos académicos integrais «Aprovados» sem confronto de todos os critérios de aceitação |

## 5. Formulação académica proposta (não aplicada à D44)

> A componente demonstrativa de contratação foi submetida a um ensaio automatizado de integração que executou o frontend React num browser Chromium e interagiu com a API Django e uma base de dados relacional de teste. Foram utilizadas duas contas sintéticas, uma de trabalhador autónomo e outra de empregador, para reproduzir a publicação de uma oportunidade, a submissão e selecção de uma proposta, a formalização bilateral da primeira versão de um acordo e a aceitação ou rejeição de alterações posteriores. No cenário ensaiado, a contratação só passou para o estado activo após o segundo aceite e as alterações rejeitadas não substituíram o acordo vigente. O ensaio constitui evidência de funcionamento integrado da sequência implementada, dentro do ambiente de teste. Não comprova usabilidade com o público-alvo, adequação do modelo às práticas reais de contratação em Maputo nem cobertura integral de todos os requisitos funcionais e não funcionais.

A redacção requer revisão da autora e da supervisão, confirmação da versão do protótipo realmente adoptada pela investigação e sincronização com figuras, índices e §5.5. Não inserir notas do auditor ou logs no corpo académico.

## 6. Limitações materiais e critérios de fecho

- [x] Executar Playwright contra **React e Django reais**, com duas contas distintas.
- [x] Confirmar um cenário integrado completo com v1 aceite, v2 substituída e v3 rejeitada.
- [x] Confirmar capturas na última execução e disponibilizar o artefacto visual: [CI #41600019575](https://github.com/enoqueJonas/freelance-frontend/actions/runs/41600019575), [ZIP das seis capturas](https://github.com/enoqueJonas/freelance-frontend/actions/runs/41600019575/artifacts/13213853540).
- [ ] Inspeccionar visualmente cada imagem antes de decidir se substitui os placeholders 5.13–5.19; seis capturas não equivalem automaticamente a sete figuras previstas.
- [ ] Testar multiplos cenários de browser negativos, navegação em outras resoluções e erros de sessão/servidor.
- [ ] Executar os mesmos fluxos sobre PostgreSQL com concorrência, não só SQLite.
- [ ] Corrigir configurações inseguras de desenvolvimento antes de qualquer publicação.
- [ ] Alinhar hipóteses de engenharia B/B1, aceitação bilateral e rejeição com supervisão.
- [ ] Executar avaliação de usabilidade com participantes reais e tratar proveniência das 11 entrevistas não comprovadas.
- [ ] Integrar as figuras e o texto comprovados no **DOCX D44 original**, preservando comentários, estrutura, margens e campos automáticos.

**Não declarar este ensaio como validação científica das hipóteses HG/HE1–HE4, nem como conclusão integral da monografia.**
