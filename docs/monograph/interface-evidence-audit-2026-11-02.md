# M08 — Auditoria das interfaces e protocolo de evidência (02/11/2026)

## Escopo e fonte
- Manuscrito: D39 — `Monografia_D39_Auditoria_Interfaces_Implementacao.docx`.
- Frontend auditado: [freelance-frontend](https://github.com/enoqueJonas/freelance-frontend), ramo `master`, revisão **f41d72e8ace6c716e799131cb46ce425a1a4c215**.
- Referência: [requisitos finais](../research/requirements-final-baseline.md), [modelo do domínio](../modeling/domain-class-model.md) e [arquitectura aprovada](../modeling/solution-architecture.md).
- Método realmente executado: análise estática dos componentes `src/App.tsx`, `src/pages/*`, `src/context/AuthContext.tsx`, `src/services/mockApi.ts` e `src/types.ts` através do repositório ligado; inspeção dos anexos disponíveis. **Não foram executados o frontend nem testes de aceitação**. As imagens anexadas disponíveis são de documentos Word, não de interfaces da aplicação. Não há capturas autenticadas para inserir.
- Limite técnico da execução nesta sessão: o clone HTTP no container não foi possível por indisponibilidade de DNS para github.com; o conector de GitHub permitiu analisar o código, mas não executar a aplicação. Isto não permite atestar a apresentação gráfica real.

## Achados de compatibilidade que impedem afirmações de conformidade

1. **Identidade comercial:** a aplicação mostra «ServiPlus» nos componentes (incluindo `src/App.tsx` e `src/pages/Login.tsx`), enquanto o nome da solução na monografia é «ConecTA».
2. **Autenticação:** `Login.tsx` permite acesso de demonstração por email, sem palavra-passe, usando `mockApi.auth.login`; `AuthContext.tsx` mantém sessão em `localStorage`. Logo, uma captura da tela de login não demonstra autenticação backend/JWT.
3. **Perfis:** `Register.tsx` e `types.ts` usam `role: 'worker'|'employer'` exclusivo. Isso não representa perfis acumuláveis / autorização contextual da baseline.
4. **Oportunidades/propostas:** `OffersList.tsx` filtra e submete dados via `mockApi`. A submissão exige `documentStatus === 'approved'`, um gate universal não fundamentado na especificação final.
5. **Contratação:** `Dashboard.tsx` cria e assina contratos via `mockApi.contracts`; não comprova `Engagement + AgreementVersion` com aceitação versionada/histórico imutável.
6. **Pagamento:** o código contém criação de pagamento simulado e linguagem de custódia/escrow. A baseline proíbe que a aplicação custodie fundos.
7. **Conflitos:** o dashboard usa disputa/decisão administrativa simulada e linguagem de mediação técnica; não demonstra `DisputeEvidence` nem processo `UNDER_REVIEW/WAITING_INFORMATION` com poderes limitados de acompanhamento.

## Matriz de correspondência para as figuras

| Figura | Interface existente / rota candidata | O que a captura efectivamente pode mostrar | O que **não** se pode inferir |
|---|---|---|---|
| 5.13 | `#/login`, `#/register` | Formulários de demonstração e escolha de role | JWT real, activação de perfis acumuláveis |
| 5.14 | `#/offers` | Lista e filtros simulados | Pesquisa persistida em backend |
| 5.15 | `#/profile/1`, `#/workers` | Bio, competências, ligações e reputação simulada | Verificação formal de evidências / diversidade do modelo final |
| 5.16 | `#/offers/1` como modal/drawer | Detalhe de oportunidade e formulário de proposta com conta demo | Regra RN02/RN04 integral ou backend integrado |
| 5.17 | `#/dashboard` contratante/trabalhador | Contrato simplificado e respectiva interacção simulada | Versionamento de `AgreementVersion` / histórico de alterações; **não há ecrã equivalente comprovado** |
| 5.18 | `#/profile/1` e dashboard | Avaliações simuladas e formulário em condições específicas | Elegibilidade bilateral e contestação prevista |
| 5.19 | `#/dashboard` contratante / admin | Acção simplificada de disputa e estado correspondente | Gestão de evidências/espera de informação e limite de autoridade do modelo; **não há ecrã equivalente comprovado** |

## Protocolo de captura reproduzível (pendente de execução)

1. Obter os ficheiros **originais** do frontend e fixar a revisão acima: `git clone https://github.com/enoqueJonas/freelance-frontend.git`, `git checkout f41d72e8ace6c716e799131cb46ce425a1a4c215`, `npm ci`, `npm run dev`. Anotar sucesso/erros do build e porta Vite (configurada para 3000 por omissão no package.json).
2. Usar instância limpa do navegador, viewport desktop consistente (ex.: 1365 × 900). A aplicação utiliza `HashRouter`; abrir rotas com `/#/...` e não presumir servidor de rotas tradicionais.
3. Registar, para cada figura, rota, passos, actor demo, versão commit, data, viewport, estado dos dados locais, resultado real, e imagem PNG original. Nunca utilizar dados pessoais, tokens ou documentos reais.
4. Para 5.13, capturar login e registo por tipo de perfil; indicar expressamente a limitação de role único. A conta de demonstração não prova autenticação.
5. Para 5.14 e 5.15, capturar filtros e perfil com dados de demonstração, verificando se a pesquisa e a renderização efectivamente funcionam. Não usar os resultados simulados como dados recolhidos na pesquisa científica.
6. Para 5.16, usar trabalhador de demonstração elegível e abrir detalhe de oportunidade. Registar submissão como **simulação local** e evidenciar a validação documental restritiva.
7. Para 5.17 e 5.19, não encenar os ecrãs inexistentes de versionamento e gestão estruturada de conflito. É aceitável demonstrar apenas as interacções **que existam**, com legenda explicitamente limitada; se a figura exigir a função final, manter não demonstrada até implementação.
8. Para 5.18, capturar avaliações apresentadas e, se possível, formulário de avaliação; distinguir mock de vínculo real a contrato concluído.
9. Reconciliar cada captura com o resultado observável no código e com um cenário reproduzível, recolher evidência de testes e só depois inserir no DOCX.
10. Na inserção final, manter o corpo da Introdução às Referências ≤ 60 páginas. D39 ocupa **59**: privilegiar apêndices para ecrãs complementares e corrigir numeração, legendas e índice automático.

## Estado e fecho
- **M08: ABERTA**. `7/7` figuras de interfaces por capturar e validar, sem inventar ecrãs.
- **M07: concluída apenas quanto à modelação**, não atesta conformidade funcional.
- D39 contém o **Quadro A.1** de correspondência estática e uma distinção textual no Capítulo V; os sete placeholders continuam explícitos na versão de trabalho.
- Critério de fecho: cada figura deve mostrar um **ecrã realmente renderizado** da revisão identificada, com origem, cenário, limites da funcionalidade e ausência de conteúdo fictício.

## 02/11/2026 — Instrumentação de recolha preparada (execução ainda pendente)

- Implementado [script de captura M08](scripts/capture_frontend_m08.py) no repositório de auditoria. Foi também produzido um kit ZIP autónomo nesta conversa, com versão Python mais detalhada e guia de execução. Ambos fixam a revisão `f41d72e8ace6c716e799131cb46ce425a1a4c215`.
- O instrumento automatiza acesso às rotas reais com `HashRouter`, autenticação simulada por contas demo, isolamento do armazenamento por cenário, viewport 1365 × 900, PNG e manifesto JSON com data, SHA do código, contexto da imagem, estado e SHA-256 do ficheiro. As capturas **5.17 e 5.19 são explicitamente marcadas como simulação não equivalente ao modelo-alvo**.
- QA efectuada ao kit local: `py_compile`, `--help`, leitura do ZIP e lançamento bem-sucedido de Chromium por Playwright num documento HTML de teste. **Este teste de ferramenta não é teste da aplicação**. O acesso directo ao clone GitHub continua indisponível no container por falha de DNS; **0/7 evidências do frontend real validadas nesta sessão**.
- **Risco textual concreto:** `src/pages/OffersList.tsx` contém o selo «Ativo • Custódia Garantida», em contradição com RN10. `src/pages/Dashboard.tsx` atribui a obrigatoriedade de BI/NUIT a «políticas do Ministério da Ciência e Tecnologia em Moçambique», sem documentação normativa verificada na baseline. Não reproduzir tal alegação como facto académico ou jurídico.
- O frontend possui `INITIAL_CONTRACTS = []` (em `mockApi.ts`): uma captura de `#/dashboard` pode apenas mostrar estado vazio sem que o contrato versionado esteja presente. Uma captura não é evidência de um cenário não executado.
- **Próximo gate concreto:** executar o instrumento na revisão indicada, inspeccionar PNGs e manifesto, observar resultados de runtime e só então decidir se alguma imagem pode entrar como *captura do protótipo simulado*, com legenda fiel. Capturas de AgreementVersion e DisputeEvidence exigem implementação funcional e não devem ser encenadas.
