# D55 — Estado persistente das propostas e isolamento entre utilizadores

**Data:** 03-11-2026.  
**Contexto:** após inspecção visual das imagens D54, a Figura candidata 5.16 mostrava êxito de submissão de proposta, mas mantinha o formulário «Propor» disponível. Essa inconsistência de UX foi documentada no [issue #3](https://github.com/enoqueJonas/freelance-frontend/issues/3).

## 1. Implementação técnica

No [backend PR #7](https://github.com/enoqueJonas/freelance-backend/pull/7), foi criado `GET /api/marketplace/proposals/mine/` com `IsAuthenticated` e filtro **`Proposal.worker.user=request.user`**. A resposta contém o próprio ID da proposta, o título e estado da oportunidade, a descrição da proposta e o estado `SUBMITTED`, `ACCEPTED` ou `REJECTED`. Não devolve a identidade nem os contactos de outros candidatos. A listagem continua a incluir propostas de oportunidades CLOSED; portanto, o trabalhador não perde o histórico após a selecção pelo empregador.

No [frontend PR #4](https://github.com/enoqueJonas/freelance-frontend/pull/4), o cliente React `realApi.ts` passou a recuperar as propostas do próprio utilizador em cada autenticação e actualização. Ao identificar uma submissão para uma oportunidade, a interface substitui o formulário pelo estado «Proposta submetida · SUBMITTED»; uma secção «Minhas propostas» apresenta o histórico, inclusive oportunidades encerradas. Esta decisão assenta em **estado do backend**, não em `localStorage`, valores mock ou sinalizadores persistidos somente na interface.

Uma auditoria visual posterior das capturas D55 detectou ainda um problema distinto: ao trocar de conta, um formulário secundário mantinha o nome da empresa da sessão anterior. O método de logout foi reforçado para limpar **todos os dados transitórios dos formulários e da conta** (nome de utilizador, empresa, contactos, textos de propostas e termos de acordo), além do JWT. A mudança de utilizador deve ser testada em browser antes de dar por resolvida esta questão de privacidade da interface.

## 2. Evidências efectivamente verificadas

- **Backend:** [GitHub Actions D55 #41603523124](https://github.com/enoqueJonas/freelance-backend/actions/runs/41603523124), **80/80 testes Django/DRF aprovados**, incluindo **nove testes novos** sobre filtragem e privacidade das próprias propostas, estado depois de encerramento da oportunidade, perfis acumuláveis, acesso anónimo e método somente de leitura. `manage.py check` sem erros e `makemigrations --check --dry-run` sem alterações.
- **Frontend:** [CI frontend D55 #41603937303](https://github.com/enoqueJonas/freelance-frontend/actions/runs/41603937303), **8/8 testes HTTP aprovados**, TypeScript e build aprovados após corrigir uma inferência de tipos. Esta execução foi anterior ao reforço de limpeza de formulários.
- **Browser:** [GitHub Actions D55 #41603937276](https://github.com/enoqueJonas/freelance-frontend/actions/runs/41603937276), cenário Playwright real aprovado com backend D55 e React em Chromium. Verificou supressão do formulário após submissão, persistência do estado depois de sair/reentrar e apresentação do estado ACCEPTED após selecção do empregador. [Capturas da execução](https://github.com/enoqueJonas/freelance-frontend/actions/runs/41603937276/artifacts/13215343392) foram recuperadas e inspeccionadas: no ecrã de proposta o formulário foi substituído por «Proposta submetida · SUBMITTED».
- **Última alteração da interface:** reforço de limpeza de dados no logout e remoção de títulos de versão D53 obsoletos. Confirmar resultado do CI no commit final antes de actualizar esta linha com um número de execução.

## 3. Relação com requisitos e critérios da D44

| Elemento | Contributo D55 | Limite |
|---|---|---|
| RF11 — Submeter proposta | Interface deixa de incentivar submissão duplicada e lê estado real | Ainda não existem edição ou retirada pelo trabalhador |
| RF12 — Avaliar proposta | A conta do trabalhador vê alteração de estado para ACCEPTED | Não avalia notificações nem decisões administrativas |
| RNF02 — Autorização | O endpoint devolve apenas as próprias propostas | Não equivale a revisão completa de segurança |
| RNF03 — Privacidade | Registos de outros trabalhadores não são expostos; dados transitórios do utilizador devem ser limpos ao trocar de conta | Não demonstra protecção completa contra XSS, fuga de JWT ou tratamento legal de dados |
| V02 | Caminho browser submeteu proposta e consultou estado persistido | **Parte de V02**, não todos os critérios de aceitação nem teste com utilizadores reais |

## 4. Evidências visuais e integridade científica

A nova captura de proposta submetida poderá substituir a imagem D54 no material **candidato** à Figura 5.16. A diferença é observável: a proposta tem uma representação de estado, sem botão de submissão duplicado. A imagem deve ser identificada como «interface do protótipo — execução automatizada com dados sintéticos»; não corresponde a resultados de entrevista, avaliação de usabilidade ou aceitação por candidatos reais em Maputo.

A última D44 canónica **não foi editada**; as sete figuras 5.13–5.19 não podem ser preenchidas por inferência. Nenhum comentário do supervisor foi considerado resolvido apenas por este trabalho. Os PRs continuam em draft.

## 5. Pendências

- [x] Endpoint autenticado e isolado por trabalhador, inclusive oportunidades fechadas.
- [x] Nove testes backend D55 e CI 80/80.
- [x] Cliente HTTP e React actualizados; oito testes HTTP e build verificados.
- [x] Browser confirma estado SUBMITTED pós-envio, sobrevive ao novo login e passa a ACCEPTED.
- [ ] Confirmar CI final de limpeza de campos após logout e os screenshots correspondentes.
- [ ] Rever UX-02: perfis alternativos ocupam espaço excessivo; manter suporte a dois perfis sem distrair do fluxo principal.
- [ ] Executar testes de segurança e usabilidade adicionais, incluindo sessão expirada e dados transientes em ambientes partilhados.
- [ ] Integrar apenas as capturas aprovadas no DOCX original com fidelidade gráfica, preservação de campos e comentários.

**Conclusão restrita:** o problema UX de submissão duplicada foi corrigido e verificado no percurso de API/browser testado, não validado com público-alvo real nem em produção.
