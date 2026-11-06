# D54 — Auditoria visual das capturas reais e correspondência com as Figuras 5.13–5.19

**Documento de referência:** `Monografia_D44_Metodologia_Proveniencia_Verificada.docx`, §§5.3–5.4, pp. 59–62.  
**Origem dos screenshots:** [GitHub Actions #41600019575](https://github.com/enoqueJonas/freelance-frontend/actions/runs/41600019575), [ZIP original do Chromium](https://github.com/enoqueJonas/freelance-frontend/actions/runs/41600019575/artifacts/13213853540), 03-11-2026.  
**Procedimento de auditoria visual:** as **seis imagens PNG foram recuperadas do ZIP original e inspeccionadas directamente**, verificando conteúdo, estados, legibilidade e correspondência de cada fase com o teste. Foram produzidos **recortes rectangulares sem alteração de texto, de objectos, de cores ou de estados**, para facilitar a inserção no Word. Este relatório não certifica que os recortes tenham sido inseridos no documento canónico.

## 1. Lista real de capturas

| PNG original | Passo visível | Uso |
|---|---|---|
| 01-oportunidade-publicada.png | Oportunidade «Portal institucional D54» em OPEN, associada ao empregador | Demonstra criação/publicação |
| 02-proposta-submetida.png | Mensagem de sucesso de submissão, oportunidade e formulário do trabalhador | Demonstra submissão; o recorte isolado do formulário não prova o sucesso |
| 03-contratacao-pendente.png | Engagement PENDING_AGREEMENT após proposta aceite, com formulário de primeiro acordo | Demonstra separação entre selecção e activação |
| 04-acordo-v1-activo.png | Engagement ACTIVE, v1 ACCEPTED/Vigente e aceites 2/2 | Demonstra aceitação bilateral da primeira versão |
| 05-versao-v2-vigente.png | v1 SUPERSEDED e v2 ACCEPTED/Vigente; Engagement ACTIVE | Demonstra substituição versionada |
| 06-versao-v3-rejeitada.png | v1 SUPERSEDED, v2 ACCEPTED/Vigente e v3 REJECTED com motivo | Demonstra rejeição sem perder versão vigente |

**Qualidade:** os textos de estados são legíveis nos PNG originais de 1280 pixels de largura. Os recortes académicos concentram-se nas áreas de oportunidade, proposta e contratação, removendo zonas periféricas que não interessam à legenda. Os recortes **não acrescentam nenhuma informação que não esteja no original**. O tamanho final no Word deve ser validado visualmente na impressão A4.

**Limitações visuais:** algumas capturas integrais incluem formulários de activação de perfil secundário e aviso explícito de «Protótipo técnico, não produção». Estes avisos são verdadeiros e não devem ser removidos de modo a induzir aparência de prontidão de produção. O recorte que mostra somente o formulário de submissão de proposta não apresenta a mensagem de sucesso; neste caso, **usar o PNG original** ou descrever a ligação à execução de CI na legenda.

## 2. Correspondência exacta com os placeholders D44

A D44 identifica os seguintes espaços reservados:

| Figura na D44 | Conteúdo previsto | Evidência D54 disponível | Decisão editorial |
|---|---|---|---|
| 5.13 | Autenticação e activação de perfis | D54 executa registo e JWT, mas não arquivou imagem do formulário inicial | **Não substituir** apenas com capturas de perfil secundário |
| 5.14 | Pesquisa e filtragem de oportunidades | D54 mostra lista de oportunidades abertas, **sem interface de filtros** | **Não declarar filtro validado**; recolher imagem adequada ou mudar legenda após aprovação |
| 5.15 | Perfil profissional e evidências de competência | D54 só permite criar Worker com competências e experiência | **Sem captura que represente evidências de competência** |
| 5.16 | Oportunidade e submissão de proposta | 01 e 02, com estados reais da API | **Candidato forte** para figura/collage editorial fiel, com indicação de dados de teste |
| 5.17 | Acordo/contratação e histórico de alterações | 03, 04, 05 e 06 com estados reais | **Candidato forte** para figura ou sequência de dois painéis, mantendo proveniência |
| 5.18 | Avaliação e reputação | Módulo legado é demonstrativo e não foi testado no D54 | **Sem evidência real de API/E2E**; manter pendente |
| 5.19 | Reporte e acompanhamento de conflito | D54 só testa rejeição de acordo; **não** é um processo DisputeCase | **Sem evidência real de conflito**; não usar v3 REJECTED para fingir DisputeCase |

**Nota decisiva:** seis screenshots de etapas NÃO resolvem automaticamente os **sete placeholders** existentes. Só as Figuras 5.16 e 5.17 dispõem agora de capturas directamente alinhadas com a sua descrição. Para o documento final, os restantes placeholders devem ser substituídos por evidência de implementação real devidamente identificada, por ilustrações expressamente conceptuais com título correcto, ou removidos com renumeração aprovada.

## 3. Legendas académicas candidatas

- **Figura 5.16 — Interface de oportunidade publicada e submissão de proposta no protótipo em teste.** Fonte: Elaboração própria (2026), capturas da execução automatizada D54 com dados sintéticos. O primeiro ecrã representa a perspectiva do empregador, o segundo a perspectiva do trabalhador.
- **Figura 5.17 — Estados de contratação e histórico de versões do acordo no protótipo em teste.** Fonte: Elaboração própria (2026), capturas da execução automatizada D54 com dados sintéticos; v1 aceite, v2 substituta e v3 rejeitada.

Estas legendas são **propostas**, não alterações aplicadas. Rever norma institucional da USTM quanto a fontes de figuras, datas, referências e painéis compostos.

## 4. Falha UX observada e prioridade técnica

**UX-01 — Submissão da proposta mantém a acção «Propor» visível após sucesso.** No screenshot integral 02 existe uma notificação verde de «Proposta submetida ao empregador», mas o formulário continua preenchido e o botão permanece disponível. O backend rejeita duplicações; no entanto, a interface não distingue adequadamente a proposta já enviada, podendo induzir tentativas repetidas e erros HTTP 409 evitáveis.

**Critério para correção:** a conta do trabalhador deve obter o estado da própria proposta por endpoint autorizado (sem expor propostas de terceiros), actualizar a UI para «Proposta submetida»/estado actual, bloquear submissão duplicada enquanto a oportunidade estiver aberta e testar o comportamento após recarregamento/autenticação. Não resolver apenas ocultando o botão sem consultar estado persistido.

**UX-02 — Formulários de activação de perfil alternativo aparecem mesmo sem serem relevantes para a tarefa actual.** O suporte a dois perfis na mesma conta é requisito legítimo, mas os formulários devem ter prioridade visual inferior ou ficar numa secção de gestão de conta, para que o percurso da contratação seja imediatamente compreensível.

**Critério:** manter a possibilidade de perfis acumuláveis sem distrair o utilizador no momento de concluir contratos. Rever com teste de usabilidade, não por pressuposto do auditor.

## 5. Proveniência e limites

- A aplicação utiliza um backend Django real e um browser Chromium com base de dados temporária SQLite, comprovados nos logs D54.
- As contas «Empregador D54» e «Trabalhador D54», as oportunidades e os valores apresentados são **dados de teste**, sem relação com indivíduos reais entrevistados.
- Não se efectuou teste com utilizadores, recolha em Maputo, avaliação jurídica do acordo, liquidação de pagamento nem ensaios de qualidade de serviços.
- Não foram modificados o Word canónico, os seus índices/campos ou os comentários do supervisor.
- Evitar designar estas capturas como «entrevistas», «resultados do mercado» ou «validação final da aplicação».
- O ZIP original GitHub expira em 03-12-2026; preservar o arquivo local e o rasto de commit/run antes de qualquer submissão académica.

## 6. Critérios de fecho da auditoria visual

- [x] Recuperar seis screenshots originais da execução E2E e verificar conteúdos.
- [x] Validar visualmente estados e produzir seis recortes rectangulares fiéis.
- [x] Identificar exactamente quais placeholders 5.13–5.19 têm evidência compatível.
- [x] Documentar falha UX-01: ausência de estado da proposta após submissão.
- [ ] Corrigir UX-01 e repetir E2E.
- [ ] Recolher capturas reais de autenticação, pesquisa, perfil, reputação e conflito, ou ajustar a descrição da D44 ao que foi efectivamente implementado.
- [ ] Inspecionar impressão das imagens no DOCX A4 e verificar legendas/numeração.
- [ ] Inserir imagens e corrigir referências cruzadas no Word canónico preservando comentários; não reconstruir o Word a partir de texto extraído.

**Estado:** auditoria visual finalizada para seis imagens D54; **integração no DOCX não executada**.
