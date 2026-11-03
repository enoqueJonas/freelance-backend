# D57 — Revisão das conclusões e correcções transversais da D44

**Objectivo:** preparar alterações académicas defensáveis, coerentes com a revisão proposta do Capítulo V, a proveniência documental e os ensaios D50–D56. **Documento de revisão, não texto já inserido na monografia.**  
**Documento original:** `Monografia_D44_Metodologia_Proveniencia_Verificada.docx`, pp. 11–18, 31–35, 44–66 e 80–82.  
**Dependência:** [D57_CAPITULO_V_REVISAO_INTEGRAL.md](D57_CAPITULO_V_REVISAO_INTEGRAL.md) e [D57_MATRIZ_VALIDACAO_V01_V08_RNF.md](D57_MATRIZ_VALIDACAO_V01_V08_RNF.md).

## I. Substituições cirúrgicas de inconsistências verificadas

**P01 — Justificativa, §1.2, p. 13.**

Texto actual:
> Do ponto de vista científico, o estudo permite relacionar literatura sobre plataformas digitais de trabalho, confiança, reputação, contratação e intermediação com evidência empírica recolhida no contexto delimitado da investigação.

Texto candidato:
> Do ponto de vista científico, o estudo permite relacionar a literatura sobre plataformas digitais de trabalho, confiança, reputação, contratação e intermediação com documentação sobre a economia digital e com cenários exploratórios delimitados ao problema em análise. A recolha empírica independente junto de trabalhadores e empregadores da Cidade de Maputo permanece por documentar e validar; por isso, os registos de trabalho disponíveis são tratados como apoio à formulação de necessidades candidatas, sem lhes atribuir a condição de depoimentos de campo comprovados.

Motivo: o §1.6 e o §3.2.2 já reconhecem a inexistência de documentação primária independente das onze entrevistas. A formulação actual de §1.2 contradiz essa ressalva.

**P02 — Delimitação, §1.8, p. 17.**

Texto actual:
> A investigação delimita-se à análise da conexão e do processo de contratação entre trabalhadores autónomos da área de Tecnologias de Informação e empregadores ou clientes na Cidade de Maputo, utilizando os dados empíricos e documentais disponíveis para compreender esse contexto e orientar a concepção da solução proposta.

Texto candidato:
> A investigação delimita-se à análise da conexão e do processo de contratação entre trabalhadores autónomos de Tecnologias de Informação e empregadores ou clientes na Cidade de Maputo, apoiando-se nas fontes bibliográficas e documentais disponíveis e na análise de registos exploratórios de trabalho para orientar a concepção da solução proposta. A existência e a representatividade de dados de campo independentes não são pressupostas sem documentação de proveniência.

**P03 — Técnica documental, §3.2.1, p. 32.**

Texto actual:
> As evidências documentais foram posteriormente confrontadas com os resultados das entrevistas.

Texto candidato:
> As evidências documentais foram posteriormente comparadas com temas extraídos dos registos exploratórios de trabalho e do piloto sintético identificado no repositório. Esta comparação permitiu formular questões e necessidades candidatas, mas não constitui triangulação com entrevistas de campo independentes comprovadas.

Este é um dos trechos de maior risco científico da D44. A mera presença de guião ou codificação temática não prova entrevistas realizadas.

**P04 — Modelo de desenvolvimento, §3.5, p. 34.**

Texto actual:
> Esta estrutura procura representar a diversidade observada nas entrevistas, incluindo serviços cujo preço apenas pode ser definido após diagnóstico e alterações de escopo que exigem aceitação pelas partes.

Texto candidato:
> Esta estrutura procura representar a diversidade de situações descritas nos materiais exploratórios e nas fontes documentais, incluindo serviços cujo preço apenas pode ser definido após diagnóstico e alterações de âmbito que exigem aceitação pelas partes. A pertinência e a frequência de tais situações no público-alvo permanecem hipóteses a confirmar mediante recolha de campo verificável.

**P05 — Procedimento de validação, §3.7, p. 35.**

Texto actual, no essencial:
> A definição de passos e oráculos constitui planeamento, não execução: os cenários V01–V08 permanecem classificados como «Não executado» enquanto não existirem registos reproduzíveis.

Texto candidato para substituir o parágrafo de estado:
> Os cenários V01–V08 constituem o protocolo integral de aceitação derivado dos requisitos. A elaboração inicial dos passos e critérios constituiu planeamento. Posteriormente, ensaios técnicos automatizados em branches de desenvolvimento produziram registos reproduzíveis de subconjuntos de V01–V03, incluindo testes de API Django e browser Chromium integrado com o frontend React. Tais execuções permitem classificar esses três cenários como parcialmente exercitados, não como totalmente aprovados, visto que continuam por satisfazer critérios específicos do protocolo. V04–V08 permanecem não executados como cenários integrais. Os resultados, identificadores de execução e limitações são documentados no Capítulo V e no Apêndice A actualizado, sem confundir verificação técnica com avaliação de usabilidade realizada junto dos intervenientes reais.

**Condição:** incorporar apenas depois de confirmar que a revisão técnica D50–D56 faz efectivamente parte da amostra de software submetida no trabalho; caso contrário, manter a descrição histórica da D44 e documentar a evolução em anexo datado.

**P06 — Actores, §5.1, p. 44.**

Texto actual:
> Esta sequência permite relacionar os resultados empíricos do Capítulo IV com a especificação e os artefactos de engenharia da solução proposta.

Texto candidato:
> Esta sequência permite relacionar as hipóteses de necessidades e os cenários exploratórios sistematizados no Capítulo IV com a especificação e os artefactos de engenharia da solução proposta, sem pressupor a validação empírica independente das categorias temáticas.

**P07 — Baseline, §5.2.1, p. 46.**

Texto actual:
> Os Quadros 5.3 e 5.4 apresentam, respectivamente, os 28 requisitos funcionais e os sete requisitos não funcionais que compõem a baseline aprovada.

Texto candidato:
> Os Quadros 5.3 e 5.4 apresentam, respectivamente, os 28 requisitos funcionais e os sete requisitos não funcionais que compõem a especificação de referência adoptada nesta versão conceptual. A aprovação formal pela autora e pela supervisão deve ser documentada antes de se designar o conjunto como baseline aprovada.

A auditoria D45/D46 identificou um documento histórico com 31 requisitos RF001–RF031, sem prova de uma decisão formal que ratifique a substituição pelos 28 requisitos da D44. **«Adoptada como referência» não é «formalmente aprovada».**

**P08 — UC13, Quadro 5.5, p. 49: estados conceptuais «aprovados».**

Texto actual, na fonte da tabela:
> Fonte: Elaboração própria, com base na análise documental, RN05–RN09 e no modelo de estados conceptual aprovado.

Texto candidato:
> Fonte: Elaboração própria, com base na análise documental, RN05–RN09 e no modelo de estados conceptual especificado neste trabalho.

Na sequência do caso de uso, clarificar que **uma parte propõe a versão e ambas registam aceitação explícita da mesma versão** no fluxo implementado D51–D56. O facto de o proponente criar uma versão não deve ser interpretado como aceitação automática. O quadro também prevê que, após diagnóstico, as partes completem o preço antes da aceitação final quando necessário; **o backend actual permite a flag `price_after_diagnosis` sem implementar essa fase de conclusão de preço**, pelo que o caso ainda não está integralmente validado.

**P09 — UC14, Quadro 5.6, pp. 49–50: formalização da alteração.**

A redacção actual refere apenas a contraparte a aceitar vN+1. A versão técnica D52 exige aceitações explícitas de **ambos** os intervenientes e, em caso de rejeição, conserva o acordo vigente. Texto candidato para o fluxo principal:

> 1. Uma parte propõe uma alteração material; 2. A aplicação cria AgreementVersion vN+1 em PROPOSED, sem alterar a versão aceite em vigor; 3. Ambas as partes analisam o conteúdo e registam individualmente a aceitação da versão; 4. Só após as duas aceitações a versão vN+1 passa a ACCEPTED e a versão anterior a SUPERSEDED; 5. O sistema disponibiliza às partes as condições vigentes e conserva a autoria, data e decisões das versões precedentes.

**Condição:** a exigência de duas acções de aceite explícitas é uma decisão de engenharia ainda **não ratificada formalmente** pela autora/supervisão. Se o caso de uso final adoptar outra regra de consentimento, alinhar modelos, backend, testes e texto em conjunto.

**P10 — Modelo de classes, §5.2.3, p. 50.**

Texto actual:
> A representação corresponde ao modelo de domínio especificado, não à estrutura já implementada no backend.

Texto candidato:
> A representação corresponde ao modelo completo de domínio especificado. Uma parte das entidades centrais — utilizador, perfis, oportunidade, proposta, contratação e versões do acordo — recebeu implementação posterior em branches de desenvolvimento do backend, mas os restantes módulos conceptuais, nomeadamente execução, pagamentos, reputação, conflitos e moderação, não possuem correspondência funcional completa no código testado.

Não transformar a Figura 5.2 conceptual num diagrama de classes da implementação sem auditar os atributos e relacionamentos efectivos.

**P11 — Arquitectura, §5.2.7, p. 57.**

A referência a frontend React/TypeScript + Django REST + PostgreSQL é **modelo-alvo**, não prova de infraestrutura de produção. Manter a legenda da Figura 5.12 como arquitectura lógica proposta; acrescentar ressalva de que os ensaios D50–D56 usaram SQLite temporário e proxy Vite para Django local, não HTTPS/PSP/PostgreSQL de produção.

**P12 — Rastreabilidade, §5.2.8, p. 58.**

Texto actual:
> Testes técnicos obrigatórios, custódia própria de fundos, matching algorítmico obrigatório, geolocalização universal, arbitragem administrativa e chat em tempo real não foram incluídos como requisitos centrais porque a evidência recolhida não sustenta a sua imposição universal.

Texto candidato:
> Testes técnicos universais, custódia própria de fundos, correspondência algorítmica obrigatória, geolocalização universal, arbitragem administrativa e chat em tempo real não foram assumidos como requisitos centrais desta versão. A decisão resulta de uma delimitação de engenharia prudente e da análise documental e exploratória, mas a ausência de recolha de campo independente comprovada **não permite afirmar** que o público-alvo tenha rejeitado essas opções ou que estejam empiricamente excluídas.

**P13 — Data e referências institucionais.**

A capa da D44 indica **Setembro de 2025**, enquanto a bibliografia já contém publicação de **2026** e os testes D50–D56 ocorreram em **Novembro de 2026**. A decisão sobre a **data oficial da versão submetida** é da autora e deve ser compatível com as regras institucionais; não inventar data de defesa nem substituir a data de capa sem autorização. Se os ensaios posteriores forem incorporados, o texto deve explicar explicitamente a sequência temporal de execução e a revisão do protótipo.

---

## II. Capítulo VI — redacção candidata completa

### 6.1 Conclusão

O presente trabalho procurou conceber e desenvolver um protótipo de aplicação web para apoiar a conexão entre trabalhadores autónomos da área de Tecnologias de Informação e empregadores na Cidade de Maputo. Para tal, foram sistematizadas fontes bibliográficas e documentais, cenários exploratórios de contratação, hipóteses de necessidades, regras de negócio, requisitos funcionais e não funcionais e modelos da solução, complementados por uma implementação técnica parcial e por ensaios automatizados.

No que respeita ao primeiro objectivo específico, a revisão documental e os registos exploratórios permitiram identificar dimensões relevantes para o estudo do processo de conexão e contratação, incluindo descoberta de oportunidades, apresentação de competências, negociação, formalização de condições, pagamentos, reputação e conflitos. Todavia, a auditoria de proveniência encontrou um piloto de entrevistas explicitamente sintético e não identificou documentação primária suficiente para demonstrar que os onze registos temáticos posteriores resultam de entrevistas de campo independentes. Por esta razão, os temas identificados **não podem ser apresentados como dificuldades empiricamente confirmadas dos trabalhadores e empregadores da Cidade de Maputo**. Constituem hipóteses de necessidades que exigem investigação adicional.

Quanto ao segundo objectivo, foi elaborada uma especificação de referência com **16 regras de negócio, 28 requisitos funcionais e sete requisitos não funcionais**, organizada em torno dos processos de identidade, oportunidades, propostas, contratação, alterações ao acordo, execução, pagamentos, reputação, conflitos e governação. A modelação conceptual produziu casos de uso, diagramas de classes, actividades, sequência e estados, bem como uma arquitectura lógica baseada em frontend React e API Django. A coerência da especificação foi avaliada por rastreabilidade documental, mas a sua adequação ao público-alvo permanece dependente de confirmação empírica e das decisões finais de aprovação da autora e da supervisão.

Relativamente ao terceiro objectivo, o protótipo inicial possuía uma interface demonstrativa com estados locais simulados e um backend limitado às contas e aos perfis. Em uma evolução técnica documentada de Novembro de 2026, foram implementados, em **branches de desenvolvimento ainda não incorporadas na branch principal**, componentes reais de publicação de oportunidades, submissão e selecção de propostas, criação da contratação pendente, formalização bilateral e versionamento de acordos. Uma rota React independente das páginas de demonstração passou a utilizar a API Django real. A introdução de consulta do estado das propostas e de gestão contextual dos perfis corrigiu limitações observadas na interface. Esta evolução representa implementação parcial do modelo concebido e não equivale à disponibilização de uma plataforma operacional de contratação.

No quarto objectivo, as suites de testes automatizados demonstraram o funcionamento de partes da solução. Os testes Django de API atingiram **80 resultados aprovados** no conjunto D50–D55; o cliente HTTP React obteve **oito testes aprovados**; e dois ensaios em browser Chromium real executaram o fluxo de contratação e a navegação contextual dos perfis numa base SQLite temporária. Tais resultados constituem evidência verificável de **subconjuntos dos cenários V01–V03**, não aprovação integral destes casos. Os ensaios canónicos V04–V08, relativos a execução e entrega, pagamentos, reputação, conflitos e governação, permaneceram não executados. A avaliação de usabilidade com participantes, a verificação integral dos requisitos não funcionais e a validação de produção não foram concluídas.

À pergunta de investigação — como uma aplicação web pode facilitar a conexão entre trabalhadores autónomos de TI e empregadores na Cidade de Maputo — o trabalho oferece uma resposta **de concepção e de viabilidade técnica parcial**. O modelo proposto permite estruturar a descoberta de oportunidades, a apresentação de propostas e a formalização de acordos, e alguns desses mecanismos foram efectivamente exercitados no protótipo. Não foi demonstrado, contudo, que a solução melhore as práticas reais de contratação, diminua fraudes ou resolva problemas de confiança entre pessoas e empresas da Cidade de Maputo.

A hipótese geral recebeu suporte conceptual e demonstração técnica limitada. A hipótese HE1 foi parcialmente materializada em oportunidades, perfis e propostas, sem validação completa de pesquisa e evidências profissionais; HE2 recebeu maior cobertura técnica quanto à aceitação bilateral e ao versionamento de acordos; HE3 permaneceu sobretudo conceptual, por falta de implementação real de reputação e conflitos; e HE4 foi representada nas condições do acordo, sem implementação de registo ou confirmação de pagamentos. **Nenhuma destas hipóteses pode ser declarada empiricamente comprovada em relação à população-alvo com as evidências disponíveis.**

As limitações centrais do estudo abrangem a proveniência não confirmada dos registos qualitativos, a ausência de avaliação com participantes recrutados, a cobertura funcional ainda incompleta, a utilização de uma base SQLite de teste em vez da infraestrutura PostgreSQL prevista, a execução de um número limitado de cenários no browser e a ausência de configuração demonstrada de segurança de produção. Por conseguinte, o contributo da investigação reside na formulação fundamentada de uma especificação e na implementação verificável de um núcleo parcial do protótipo; a sua eficácia, aceitação e evolução para serviço utilizável permanecem objecto de trabalho futuro.

### 6.2 Recomendações

Recomenda-se, em primeiro lugar, **documentar a proveniência das fontes qualitativas** antes de qualquer nova interpretação dos onze registos como entrevistas de campo. Se não existirem comprovativos primários de recrutamento, recolha, transcrição e procedimentos éticos, deverá ser realizado um estudo empírico verificável com trabalhadores autónomos de TI e empregadores da Cidade de Maputo. Os resultados devem ser utilizados para rever as necessidades candidatas e identificar divergências entre a concepção proposta e as práticas efectivamente observadas.

No plano técnico, recomenda-se consolidar e rever os PRs de desenvolvimento que implementaram o núcleo de contratação, estabelecendo uma revisão estável do protótipo. Devem ser completados os campos e regras de prazos e entregáveis dos acordos, a gestão do ciclo de execução e entrega, a manutenção de histórico de eventos, a gestão de pagamentos sem custódia própria de fundos, a reputação bilateral com possibilidade de contestação e o reporte/acompanhamento administrativo de conflitos. A integração externa com prestadores financeiros deverá permanecer facultativa, desacoplada e sujeita a validação específica.

A avaliação deverá prosseguir com a execução **integral** dos casos V01–V08, utilizando os critérios do Quadro A.2 e registando para cada execução os dados, actor, estado inicial, resultado observado, ambiente, versão, data e evidências. Devem também ser executadas as verificações RNF01–RNF07, incluindo tarefas reais de usabilidade com participantes, autorização por recurso, minimização de dados, integridade e histórico de versões, responsividade em múltiplas dimensões, análise de manutenibilidade e interoperabilidade quando existir prestador integrado.

Antes de qualquer publicação do protótipo, importa eliminar configurações inseguras de desenvolvimento, rever a gestão de sessões e segredos, realizar testes de concorrência e persistência em PostgreSQL e validar práticas adequadas de segurança e protecção de dados. Os testes CI com SQLite e contas sintéticas são úteis para regressão funcional, mas não demonstram, por si só, adequação a operações reais.

Por fim, estudos posteriores poderão ampliar a investigação a outras especialidades e regiões de Moçambique e examinar como utilizadores reais avaliam a descoberta de oportunidades, a confiança, a formalização de condições e a utilização da plataforma. A análise de eventuais melhorias na contratação deverá basear-se em indicadores e observações recolhidos de forma sistemática, não apenas na existência de funcionalidades ou em inferências a partir do protótipo.

---

## III. Apêndice A: reconciliação obrigatória antes da entrega

### Quadro A.1 — Interfaces e estado de execução

A tabela actual (§8.7, p.80) corresponde ao frontend legado `Login.tsx/OffersList.tsx/Dashboard.tsx/mockApi.ts` e afirma que **nenhuma** das interfaces foi validada no browser, o que descrevia a base inicial, mas não a evolução D54–D56. Não apagar essa informação histórica nem reescrevê-la como se todas as páginas tivessem sido migradas.

**Proposta:** manter uma coluna «Base inicial (legado com mock)» e acrescentar «Evolução D53–D56 (rota real)» e «Limitação observada», sem aumentar o número de figuras ficticiamente.

| Figura | Legado D44 | Revisão testada | Actualização responsável |
|---|---|---|---|
| 5.13 — Autenticação e perfis | `Login.tsx/Register.tsx/AuthContext.tsx` com perfil exclusivo e mock | `/#/real`: registo/JWT real e perfis acumuláveis; D56 gerou capturas reais de activação contextual | Só mostrar captura de login após recolhê-la; perfil contextual é evidência parcial |
| 5.14 — Pesquisa e filtros | `OffersList.tsx` com mock | `/#/real` lista oportunidades abertas, não cobre filtros avançados | Sem evidência de filtro real |
| 5.15 — Perfil profissional/evidências | `ProfileDetail.tsx/WorkersList.tsx` com mock | Criar perfil básico Worker real | Portfólio/certificação não demonstrados |
| 5.16 — Oportunidade e proposta | `OffersList.tsx` com mock | D54–D56 publicou e submeteu proposta em Django, D55 corrigiu submissão duplicada | Candidato a screenshot real de execução |
| 5.17 — Acordos e histórico | `Dashboard.tsx/mockApi.ts` com contrato simulado | D54–D56 demonstram v1 aceite, v2 aceite, v3 rejeitada e preservação de versão | Candidato a screenshots reais de estados |
| 5.18 — Avaliação e reputação | Simulação de estrelas/comentários | Não implementado/testado na API real | Não apresentar como funcionalidade concluída |
| 5.19 — Conflitos e acompanhamento | Simulação de arbitragem | A rejeição de uma AgreementVersion não é DisputeCase | Não apresentar como funcionalidade concluída |

### Quadro A.2 — Casos V01–V08

O Quadro A.2 é um **plano formal prospectivo** na D44, com nota «Estado de execução dos oito cenários: não executado». Depois de incluir as revisões D50–D56, preservar as **definições, passos e critérios canónicos**, mas alterar a nota geral para:

> Estado após os ensaios técnicos D50–D56: V01, V02 e V03 parcialmente exercitados em subconjuntos verificáveis; V04–V08 não executados como cenários de aceitação. A matriz de resultados e as evidências de API/browser encontram-se no Capítulo V. Não foram conduzidas avaliações com participantes reais.

Não alterar a definição V04: é **execução, entrega e histórico**, não acordo versionado.

### Quadro A.3 — RNF01–RNF07

Preservar os procedimentos e evidências previstos como **critérios planeados**. Evitar substituí-los por «teste passou» apenas com base em typecheck/build/Playwright. Acrescentar, se aceite editorialmente, uma coluna ou nota que reporte a classificação exacta da [matriz D57](D57_MATRIZ_VALIDACAO_V01_V08_RNF.md): RNF02–RNF05 parcial técnico; RNF01, RNF06 e RNF07 sem execução do protocolo específico.

---

## IV. Decisões ainda pendentes de autoria e supervisão

- **D-01:** confirmar se a pesquisa conservará uma componente empírica sobre pessoas reais ou assumirá explicitamente abordagem documental + prototipagem, com reformulação de objectivos/hipóteses adequada às exigências da USTM.
- **D-02:** verificar proveniência das onze entrevistas e, na ausência de evidências, **não inventar entrevistas, consentimentos, datas ou resultados**.
- **D-03:** decidir a baseline RF01–RF28 e registar eventual aprovação; não presumir a aprovação pela existência de uma versão de tabela.
- **D-04:** aprovar a semântica técnica de `PENDING_AGREEMENT`, duas aceitações expressas e versão `SUPERSEDED`, sem criar contradição entre UML e código.
- **D-05:** decidir se os resultados de Novembro de 2026 integrarão a monografia, qual será a data formal do manuscrito e que revisão técnica será citada.
- **D-06:** obter/identificar o **ficheiro Word canónico em bytes originais**, não apenas texto indexado; só assim preservar estilos, margens, imagens, campos e comentários do supervisor em revisões automáticas.
- **D-07:** decidir o tratamento das Figuras 5.13–5.19 que não têm evidência visual correspondente. Não colocar imagens genéricas que aparentem funcionalidades executadas quando não o foram.

**Regra de fecho:** uma auditoria textual não substitui aprovação da autora, revisão da supervisão, validação de campo nem controlo de qualidade do Word original. O DOCX D44 não foi modificado por este conjunto D57.
