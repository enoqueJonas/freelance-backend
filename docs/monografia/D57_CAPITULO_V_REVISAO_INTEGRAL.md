# D57 — Proposta de revisão integral do Capítulo V, com estado técnico actualizado

**Natureza:** substituição textual candidata e controlada dos §§5.3–5.5 da D44, além de orientações para Quadros 5.3–5.4, Figuras 5.13–5.19 e Apêndice A. **Não aplicada ao DOCX original.**  
**Referência canónica:** `Monografia_D44_Metodologia_Proveniencia_Verificada.docx`, Capítulo V pp. 44–63 e Apêndice A pp. 80–82.  
**Estado de referência técnica:** 03-11-2026, PRs **draft e não integrados na branch principal**: backend #3–#7; frontend #1, #2, #4, #5.  
**Fonte verificável dos ensaios:** [D55 backend 80/80](https://github.com/enoqueJonas/freelance-backend/actions/runs/41603523124); [D56 Chromium 2/2](https://github.com/enoqueJonas/freelance-frontend/actions/runs/41612082795); [D56 frontend 8/8 e build](https://github.com/enoqueJonas/freelance-frontend/actions/runs/41612082848).  
**Matriz de resultados canónicos:** [D57_MATRIZ_VALIDACAO_V01_V08_RNF.md](D57_MATRIZ_VALIDACAO_V01_V08_RNF.md).

> **DIRECTIVA D59 — método corrigido:** a recolha de dados foi realizada por **entrevistas semiestruturadas**, conforme esclarecimento expresso do responsável pela revisão. Os questionários, percentagens e gráficos do draft histórico ficam **fora do desenho metodológico e dos resultados da monografia**. A auditoria histórica D58 é apenas arquivo. A pendência activa é conferir **os registos originais das entrevistas** e a sua correspondência com os onze perfis textuais T01–T08/E01–E03 da D44. Ver [decisão D59](D59_DECISAO_METODOLOGICA_ENTREVISTAS_SEMIESTRUTURADAS.md). A confirmação da técnica não é prova documental automática de cada depoimento.


> **Actualização D60:** o responsável confirmou que o DOCX de 21 páginas agora entregue contém as **onze transcrições literais originais não editadas**, identificadas como T01–T08/E01–E03. A descrição anterior de ausência de registos primários textuais está ultrapassada. Prossegue a análise temática, a conferência das condições de produção/consentimento e a correspondência com a D44; gravações áudio não são obrigatórias. Ver [D60](D60_CONFIRMACAO_TRANSCRICOES_LITERAIS.md).

## Directriz de inserção editorial

Este capítulo precisa de **duas perspectivas temporais** em vez de substituir retroactivamente a descrição que existia quando a D44 foi produzida:

1. **Base inicial auditada:** frontend legado baseado em `mockApi/localStorage`, backend apenas com accounts/JWT e vários módulos de domínio vazios. Isto descrevia a versão inicial.
2. **Evolução técnica subsequente:** branches D50–D56 desenvolveram módulos reais de oportunidade, proposta, contratação e acordo versionado, rotas React dedicadas, testes de API e um percurso real no browser. Estas alterações **não estão no ramo principal** e não demonstram cobertura integral.

A autora deve confirmar qual revisão faz parte do protótipo adoptado para a monografia, indicar data, commit e ambiente. Não há autorização para introduzir evidência posterior numa capa datada de Setembro de 2025 sem resolver a cronologia institucional.

---

## 5.3 Telas e estado de implementação do protótipo — redacção candidata

O estado da implementação foi examinado mediante comparação entre a especificação funcional e o código dos repositórios React e Django. Para evitar que os diagramas de arquitectura sejam interpretados como prova de execução, importa distinguir os componentes **concebidos**, o **protótipo demonstrativo inicial**, as funcionalidades implementadas em **branches técnicas de desenvolvimento** e as capacidades **efectivamente ensaiadas**. A plataforma não estava publicada em produção e o estado aqui descrito corresponde às revisões identificadas na documentação de testes de 3 de Novembro de 2026.

### 5.3.1 Protótipo frontend

A interface utiliza React, TypeScript, Vite e Tailwind CSS. Na versão inicial, as páginas de autenticação, registo, pesquisa, dashboard, propostas, contratos e avaliações interagiam com `mockApi` e dados mantidos no armazenamento local do browser. Estes fluxos constituem **demonstrações de interface**, não operações de contratação persistidas na API Django. Essa distinção permanece necessária: os módulos legados não foram integralmente substituídos e vários continuam a apresentar comportamento simulado.

Na evolução técnica posterior foi implementada uma rota dedicada, `/#/real`, desacoplada do contexto de autenticação demonstrativo. Esta rota realiza autenticação com credenciais e JWT emitido pelo backend, criação de perfis de trabalhador e empregador, publicação de oportunidades, submissão e consulta de propostas, selecção de propostas e gestão das versões de um acordo. O cliente HTTP consulta os endpoints Django e não substitui erros de rede por respostas fictícias. O token de acesso é mantido na memória da aplicação e perde-se com o recarregamento, opção adequada ao ensaio, mas insuficiente como estratégia completa de sessão para produção.

Após as auditorias de interface, a gestão dos perfis foi reorganizada: as opções de trabalhador e empregador apresentam-se inicialmente sem os formulários abertos, e cada formulário é exibido quando solicitado. A conta pode possuir ambos os perfis, sem que isso elimine a restrição que impede a mesma identidade de ocupar os dois lados da mesma contratação. O estado das propostas próprias passou a ser consultado na API, incluindo para oportunidades encerradas, evitando a apresentação de um botão de submissão duplicada após uma proposta já registada. Estas correcções foram exercitadas por testes automatizados de interface; **não constituem avaliação formal de usabilidade com participantes**.

A interface real de contratação não implementa, nesta fase, os processos completos de entrega de serviços, liquidação de pagamentos, avaliação/reputação, contestação, disputa ou moderação previstos no modelo-alvo. Capturas de módulos legados não devem ser apresentadas como demonstração da execução dessas capacidades no backend.

### 5.3.2 Implementação backend

O backend foi desenvolvido em Django/Django REST Framework, com modelos de utilizadores e perfis e autenticação JWT. A versão inicial auditada continha principalmente as entidades `User`, `Worker` e `Employer` e não materializava o núcleo conceptual da contratação. Posteriormente, numa sequência de branches de desenvolvimento D50–D55, foi construído e submetido a testes um primeiro corte funcional da aplicação.

Esse corte introduziu as entidades `Opportunity`, `Proposal`, `Engagement`, `AgreementVersion` e `AgreementAcceptance`, com migrações e restrições de integridade. O ciclo implementado permite que um empregador crie e publique uma oportunidade, que um trabalhador distinto submeta uma proposta e que o empregador a seleccione. A selecção encerra a oportunidade e cria uma contratação em `PENDING_AGREEMENT`. A contratação apenas passa a `ACTIVE` quando as duas partes aceitam explicitamente a mesma versão das condições do acordo.

A implementação posterior de alterações ao acordo permite propor uma versão vN+1 sem substituir de imediato a versão vigente. A aceitação bilateral passa a nova versão para `ACCEPTED` e a anterior para `SUPERSEDED`; a rejeição de uma proposta preserva o acordo vigente, guardando a identidade, a data e o motivo da decisão. A API utiliza uma impressão digital SHA-256 do conteúdo nas operações de aceitação e rejeição. Este mecanismo constitui um controlo técnico de correspondência do conteúdo, **não uma assinatura electrónica juridicamente qualificada** nem garantia de imutabilidade perante acessos privilegiados à base de dados.

Foram ainda criadas listagens autorizadas de propostas por oportunidade para o empregador proprietário, de contratações para as respectivas partes e de propostas próprias para o trabalhador. A autorização é verificada com base na identidade e na relação com o recurso, preservando o princípio de que a mesma conta pode desempenhar ambos os perfis, mas não contratar-se a si própria.

O backend **não implementa ainda**, neste corte, registos completos de execução e entrega (`ExecutionRecord`), registo e confirmação de pagamentos, integração com prestador financeiro, reputação e contestação, gestão estruturada de conflitos ou moderação final. A persistência verificada pela pipeline ocorre numa base de dados SQLite temporária; a arquitectura de referência prevê PostgreSQL, mas a execução concorrente nesse sistema não foi comprovada.

As funcionalidades descritas são resultados de branches técnicas **ainda não integradas no ramo principal**. A sua verificação foi documentada por testes automatizados e não comprova disponibilidade operacional, qualidade em produção ou adequação empírica à população da Cidade de Maputo.

### 5.3.3 Diferenças entre o protótipo e o modelo concebido

**Quadro 5.x — Correspondência entre modelo-alvo e estados da implementação, com data de referência de 03-11-2026.** Substituir a tabela actual da D44 depois de confirmar a revisão final adoptada. Não assumir que as 28 RF se tornaram todas implementadas.

| Área | Modelo-alvo | Estado verificado no corte técnico D50–D56 | Limitações |
|---|---|---|---|
| Perfis acumuláveis | Conta Worker, Employer ou ambos | Implementado e exercitado em API e Chromium | Gestão integral de dados e evidências profissionais incompleta |
| Autenticação | Credenciais reais, JWT e autorização por relação | Implementada na rota React isolada e em contas Django | Renovação de sessão, segurança de produção e recuperação de conta não verificadas |
| Oportunidades | Publicar, consultar, pesquisar e gerir ciclo | Criar/publicar/fechar implementado e testado | Filtros avançados, edição e pesquisa trabalhadores incompletos |
| Propostas | Submeter, consultar, avaliar e gerir | Submissão/consulta/aceitação implementadas; estado persistente próprio verificado | Retirada/edição pelo trabalhador e todas as alternativas não implementadas |
| Formalização | Acordo inicial com condições aceites | v1 e duas aceitações implementadas/testadas | Não representa assinatura jurídica avançada; faltam prazos/entregáveis completos |
| Versionamento | Alterações, rejeição e histórico | v2/v3, `ACCEPTED`, `SUPERSEDED`, `REJECTED` implementados/testados | Auditoria imutável independente e concorrência PostgreSQL não demonstradas |
| Execução/entrega | Registar serviço, evidências, conclusão | **Não implementado no domínio real testado** | RF15–RF17 / V04 pendentes |
| Pagamentos | Condições, declaração, confirmação e PSP opcional | Valor e preço pós-diagnóstico no acordo; sem operações de pagamento | RF19–RF20 / V05 pendentes; sem custódia de fundos |
| Reputação | Avaliação bilateral contextual e contestação | Somente UI legada demonstrativa | RF21–RF23 / V06 pendentes |
| Conflitos | Reporte, evidências, acompanhamento sem arbitragem | Rejeição de acordo, que não equivale a `DisputeCase` | RF24–RF25 / V07 pendentes |
| Verificação/moderação | Verificação e acções administrativas controladas | Algumas permissões de lista de utilizadores testadas | RF06/RF26–RF28 / V08 pendentes |
| Notificações/mensagens | Comunicação contextual e rastreabilidade | UI legada utiliza dados de demonstração | Não testado como registo de domínio |
| Persistência | PostgreSQL e arquitectura desacoplada | Django ORM, migrações e SQLite em CI | PostgreSQL e simultaneidade não testados |

**Nota das Figuras 5.13–5.19:** as capturas D54–D56 de React com Django e dados sintéticos podem sustentar **partes** da interface de activação de perfis (5.13), oportunidade/proposta (5.16) e acordo/histórico (5.17). A Figura 5.13 continua a necessitar de uma captura de autenticação e de análise da legenda composta. As Figuras 5.14 (pesquisa e filtros completos), 5.15 (evidências de competência), 5.18 (reputação) e 5.19 (conflitos) **não possuem prova equivalente de funcionamento integrado**. Não substituir placeholders com capturas do `mockApi` descritas como funcionalidades reais.

Os resultados de browser foram produzidos com contas sintéticas, sem participação de trabalhadores ou empregadores recrutados para o estudo. A forma de apresentação e a numeração das figuras dependem das normas institucionais e da revisão do ficheiro Word original.

---

## 5.4 Validação do protótipo — redacção candidata

A validação foi organizada em dois níveis complementares. O primeiro diz respeito à **verificação técnica** de funcionalidades implementadas em branches de desenvolvimento; o segundo corresponde à **avaliação integral** dos cenários V01–V08 definidos na especificação da investigação. A passagem num ensaio técnico não implica, por si, o cumprimento de todos os critérios do cenário de aceitação da monografia.

No primeiro nível, as suites de API Django/Django REST Framework foram progressivamente ampliadas até **80 testes aprovados** no CI D55. Estes testes incidiram sobre autenticação, perfis acumuláveis, controlo de acesso, oportunidades, propostas, estados de contratação, aceitação bilateral, alteração de acordos, autorização das consultas e histórico de versões. Uma suite independente de cliente HTTP React obteve **oito testes aprovados**, e os processos de verificação de tipos e compilação foram concluídos no CI D56.

No segundo nível de integração, o Playwright executou **dois cenários aprovados em Chromium real** com a interface React, o servidor Django e uma base de dados SQLite temporária. O primeiro percorreu a criação de duas identidades distintas, a publicação de uma oportunidade, a submissão e selecção de uma proposta, a formalização do acordo inicial e as alterações versionadas subsequentes. O segundo verificou o comportamento da gestão contextual dos perfis numa dimensão móvel de 390 × 844 pixels, incluindo a abertura e o encerramento de formulários por teclado. Os resultados foram acompanhados por capturas reais da interface geradas no ambiente de CI.

Estes ensaios confirmam a execução de **subconjuntos dos casos V01–V03**, mas não satisfazem integralmente os critérios previstos no Quadro A.2. Nomeadamente, V01 continua a exigir a associação de portfólio ou certificação como evidência profissional; V02 prevê pesquisa com filtros e testes complementares de elegibilidade; V03 requer, entre outros aspectos, alterações de prazo/valor e a comparação de rejeição e aceitação da versão nova em casos separados. A automação exercitou cenários de acordo próximos do objectivo de V03, mas a rejeição no browser ocorreu para uma terceira versão, não exactamente para v2 num caso independente.

Os cenários V04–V08 **não foram executados como casos completos**: execução e entrega do serviço (V04), gestão de pagamentos (V05), reputação e contestação (V06), conflitos (V07) e verificação/moderação (V08). A presença de uma interface demonstrativa não altera esta classificação. A rejeição de uma proposta de acordo também não constitui um conflito administrativo, e o armazenamento de valor no acordo não equivale à confirmação de um pagamento.

**Quadro 5.y — Síntese do estado dos cenários V01–V08, com correspondência ao Quadro A.2 original.**

| Caso | Cenário e requisitos | Estado após D56 | Fundamentação resumida |
|---|---|---|---|
| V01 | Registo e perfis — RF01–RF05 | **Parcialmente exercitado** | Registo, perfis acumuláveis e sessão testados; evidência de competência não verificada |
| V02 | Oportunidades, pesquisa e propostas — RF07–RF12 | **Parcialmente exercitado** | Publicação, proposta e selecção testadas; filtros e consultas completos pendentes |
| V03 | Formalização e alterações — RF13–RF14, RF18 | **Parcialmente exercitado** | Aceites e versões testados; cenário canónico completo não reproduzido |
| V04 | Execução, entrega e histórico — RF15–RF17 | **Não executado** | Falta `ExecutionRecord`, entrega e conclusão |
| V05 | Pagamentos — RF18–RF20 | **Não executado** | Não há registo de estado de pagamento ou PSP real |
| V06 | Reputação e contestação — RF21–RF23 | **Não executado** | Sem domínio real |
| V07 | Conflitos — RF24–RF25 | **Não executado** | Sem `DisputeCase` real |
| V08 | Governação e verificação — RF06, RF26–RF28 | **Não executado** | Permissões parciais não cumprem o cenário de moderação |

A documentação de evidência associa os resultados a **runs, commits, data e ambiente**. Todos os ensaios mencionados ocorreram em **branches de desenvolvimento ainda em revisão**, não na branch principal de produção. A classificação constitui uma actualização candidata à matriz da versão D44, sujeita a aceitação e reconciliação com o roteiro canónico antes da entrega final.

### 5.4.1 Validação dos requisitos não funcionais — redacção candidata

A verificação não funcional não se considera concluída apenas porque os testes funcionais e de integração passaram. Os requisitos RNF01–RNF07 possuem procedimentos próprios de avaliação previstos no Quadro A.3 e devem receber resultados proporcionais às evidências recolhidas.

**Quadro 5.z — Estado das verificações não funcionais.**

| RNF | Estado | Evidência e pendência |
|---|---|---|
| RNF01 — Usabilidade | **Não executado conforme protocolo** | Playwright verificou interacção automatizada, mas não tarefas realizadas por participantes observados |
| RNF02 — Segurança/autorização | **Parcialmente verificado tecnicamente** | Testes de autenticação, propriedade e relação com recursos; sem avaliação de segurança integral |
| RNF03 — Privacidade | **Parcialmente verificado tecnicamente** | Consulta própria de propostas, restrição de listagens e limpeza de sessão; sem inventário integral de campos e retenção |
| RNF04 — Integridade/rastreabilidade | **Parcialmente verificado tecnicamente** | Versões, impressão digital, aceitação, autor e motivo de rejeição; sem trilho imutável e ensaio de concorrência completo |
| RNF05 — Responsividade | **Parcialmente verificado tecnicamente** | Ensaio de perfis em 390 × 844; outras tarefas e desktop 1365 × 900 ainda requerem matriz completa |
| RNF06 — Manutenibilidade | **Não executado conforme protocolo específico** | Arquitectura modular visível, mas sem auditoria sistemática de dependências |
| RNF07 — Interoperabilidade | **Não executado** | Nenhum adaptador PSP implementado/ensaiado |

Os testes acima não incluem estudos de desempenho sob carga, pentest completo, auditoria de acessibilidade WCAG, comparação com dispositivos físicos ou avaliação de utilizadores. O backend mantém configurações de desenvolvimento inadequadas para exposição pública, pelo que não se deve associar o resultado de CI à prontidão para produção.

---

## 5.5 Discussão dos resultados e limitações — redacção candidata

A investigação adoptou **entrevistas semiestruturadas** como técnica de recolha qualitativa, complementada por fontes bibliográficas e documentais. O DOCX de 21 páginas contém agora onze transcrições literais confirmadas pelo responsável, permitindo localizar excertos para relacionar as entrevistas com as necessidades e requisitos; a correspondência entre o corpus e a codificação da D44 ainda deve ser conferida, mantendo separado o piloto sintético. A concepção técnica produziu uma **especificação conceptual** e um **protótipo parcialmente implementado**. A correspondência entre o modelo proposto e o comportamento do software aumentou com a introdução de oportunidades, propostas e acordos versionados no backend e com a ligação de uma rota React à API real. Contudo, a cobertura dos requisitos permanece incompleta e o grau de suporte empírico de cada necessidade depende da conferência individual dos registos das entrevistas.

As verificações automatizadas demonstraram, num ambiente de teste isolado, a viabilidade de **distinguir a aceitação de uma proposta da activação contratual**: uma proposta escolhida gera uma contratação pendente, e a contratação só passa a activa após as aceitações das condições pela identidade do trabalhador e do empregador. Demonstraram também a preservação da versão vigente quando uma alteração ainda não foi aceite ou foi rejeitada. Esses resultados oferecem evidência de comportamento do software e de coerência com as regras de negócio escolhidas, mas não demonstram que tal mecanismo, por si só, reduza fraudes, litígios ou custos de transacção reais.

A hipótese específica **HE1** recebe sustentação de modelação e cobertura técnica parcial: a oportunidade pode ser publicada e o trabalhador pode apresentar proposta, mas a pesquisa avançada de profissionais e a comprovação de competências ainda não foram integralmente implementadas e validadas. A hipótese **HE2** possui um núcleo técnico mais desenvolvido, com formalização bilateral e alterações versionadas ensaiadas, embora persistam lacunas quanto a prazos, entregáveis e validação com utilizadores. A hipótese **HE3** permanece sobretudo conceptual: os módulos de reputação contextual, contestação e acompanhamento estruturado de conflitos não foram implementados no fluxo real. A hipótese **HE4** foi representada na especificação e parcialmente nas condições de valor/preço do acordo; **não** foi verificada por registo real, confirmação de pagamento ou integração com prestador financeiro. Consequentemente, a hipótese geral **HG** não pode ser considerada empiricamente confirmada quanto à facilitação efectiva da conexão entre trabalhadores e empregadores de Maputo.

A implementação permite responder a uma parte da pergunta de pesquisa **no plano da engenharia**: é possível reunir numa aplicação web perfis, oportunidades, propostas e aceitação versionada de condições acordadas. No plano da investigação social, não foi demonstrado que os mecanismos correspondam, em importância e utilização, às práticas reais do público-alvo. A interpretação das entrevistas semiestruturadas requer registos primários rastreáveis para distinguir relatos efectivos de interpretações de concepção; a execução de testes automatizados da aplicação não substitui essa conferência nem a avaliação de usabilidade com pessoas representativas.

A avaliação apresenta limitações adicionais. O backend foi exercitado em SQLite temporário, não em PostgreSQL com concorrência. Os testes de browser cobrem um número reduzido de caminhos e utilizam contas sintéticas. A autenticação e a configuração do servidor não foram submetidas a um processo completo de endurecimento para produção. As páginas legadas mantêm dados fictícios, e módulos relevantes para execução do serviço, pagamentos, reputação, conflitos e governação continuam sem correspondência funcional no backend testado.

Estas limitações impedem equiparar **teste técnico aprovado**, **requisito integralmente aceite**, **hipótese empiricamente confirmada** e **aplicação pronta para produção**. O contributo verificável desta fase consiste na especificação rastreável de um modelo de solução e na demonstração técnica parcial de alguns dos seus fluxos. As restantes funcionalidades e a validação junto do público-alvo constituem actividades futuras claramente delimitadas.

---

## Verificações editoriais a efectuar quando houver DOCX original

1. **Quadros:** manter numeração original quando possível; se introduzir um novo Quadro 5.x para cobertura técnica, recalcular a sequência de quadros e actualizar lista de quadros e referências. Alternativamente, substituir os quadros existentes em §5.3.3 e §5.4 sem introduzir número novo.
2. **Figuras:** não inserir imagens geradas por IA em substituição de capturas de execução; usar capturas genuínas com dados de teste e fonte apropriada. A D54 fornece originais, D55 corrige o estado da proposta, D56 acrescenta três vistas dos perfis.
3. **Casos V01–V08:** `V04` pertence exclusivamente a execução/entrega/histórico. Não associar à alteração de acordos.
4. **Estados:** não apresentar nenhum dos oito casos como integralmente «Passou», nem os sete RNF como totalmente satisfeitos.
5. **Data e ramo:** confirmar data de capa e que a autora adoptou as revisões técnicas ainda em PRs draft; evitar atribuir resultados de 2026 a uma versão originalmente datada de 2025.
6. **Comentários:** não apagar, resolver ou reescrever comentários do supervisor sem confirmar cada solicitação na fonte Word.
7. **Proveniência:** a técnica de recolha foi confirmada como entrevistas semiestruturadas; conferir a relação entre cada entrevista efectiva e os perfis T/E da D44, preservando a separação do piloto sintético. Não extrapolar que originais não localizados significam entrevistas inexistentes.
8. **Arquitectura e operações reais:** PostgreSQL e integração PSP permanecem objectivos previstos; não confundir modelos UML com implementação.
