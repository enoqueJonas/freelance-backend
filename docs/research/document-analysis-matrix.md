# Matriz de Análise Documental

## Objectivo

Registar de forma rastreável as evidências extraídas do corpus documental que podem ajudar a compreender o contexto, identificar problemas/necessidades e fundamentar decisões futuras da solução ConecTA.

Esta matriz **não converte automaticamente evidências em requisitos**. A cadeia adoptada é:

`Documento → Evidência → Problema/Necessidade → Implicação → Entrevistas/triangulação → RN/RF/RNF candidato`.

Os requisitos definitivos serão consolidados somente depois da análise das entrevistas e do cruzamento com benchmark, regras de negócio e baseline técnica.

## Classificação

- **CTX** — contextualização do problema/mercado;
- **NEC** — necessidade ou risco relevante para utilizadores;
- **BEN** — benchmark/padrão observado em plataforma existente;
- **REG** — enquadramento legal/regulatório;
- **TEC** — implicação técnica/arquitectural.

## Corpus principal

| ID | Documento | Instituição/Fonte | Papel |
|---|---|---|---|
| DOC-01 | Inquérito ao Sector Informal — INFOR 2021/22 | Instituto Nacional de Estatística (INE), Moçambique | Contexto do sector informal e trabalho por conta própria |
| DOC-02 | Mozambique Digital Economy Diagnostic | World Bank | Contexto da economia digital, pagamentos, identidade, confiança e infraestrutura em Moçambique |
| DOC-03 | Digital Labour Platforms and the Future of Work | International Labour Organization (ILO) | Funcionamento, riscos e governação das plataformas digitais de trabalho |
| DOC-04 | World Employment and Social Outlook 2021 — The role of digital labour platforms in transforming the world of work | International Labour Organization (ILO) | Matching, reputação, comunicação, pagamentos e resolução de disputas em plataformas |
| DOC-05 | Digital Labour Platforms in Kenya | International Labour Organization (ILO) | Evidência africana sobre trabalho em plataformas, freelancing e pagamentos digitais |
| DOC-06 | Relatório de Inclusão Financeira 2025 | Banco de Moçambique | Contexto actual de inclusão financeira, pagamentos digitais e protecção do consumidor |
| DOC-07 | A Freelancer's Guide to Upwork | Upwork | Benchmark funcional do ciclo de contratação numa plataforma de freelancing |

> Nota: o corpus permanece aberto a documentos adicionais. Um documento só deve ser citado na monografia para uma afirmação que ele efectivamente suporte.

## Matriz de evidências

| Evidência | Tipo | Achado suportado pelo documento | Problema/Necessidade | Implicação para a investigação/solução | Estado |
|---|---|---|---|---|---|
| DOC-01-E01 | CTX | O INFOR 2021/22 é um inquérito por amostragem aos agregados familiares, de cobertura nacional, destinado a caracterizar o sector informal, recolhendo informação sobre emprego, actividades e receitas. A documentação disponibilizada identifica indivíduos e estabelecimentos como unidades de análise e informa que os dados permitem desagregação nacional, provincial, urbano/rural e por grupos de actividade. | Existe uma fonte oficial para contextualizar emprego e actividade informal em Moçambique, mas a sua população não equivale automaticamente a trabalhadores autónomos de TI. | Usar apenas indicadores cuja definição, população, geografia e período sejam compatíveis com a afirmação pretendida. | Verificado na documentação do INFOR |
| DOC-01-E02 | CTX | A documentação do INFOR regista recolha entre Outubro e Dezembro de 2021 e cobertura nacional, com estimativas previstas para domínios provincial, urbano/rural, regional e nacional. | Afirmações sobre Maputo ou sobre um subconjunto profissional exigem extracção específica; totais nacionais não devem ser apresentados como se representassem trabalhadores autónomos de TI da Cidade de Maputo. | Procurar indicadores específicos antes de usar o INFOR para sustentar magnitude, prevalência ou perfil do fenómeno no Capítulo I. | Verificado; indicadores específicos ainda a extrair |
| DOC-02-E01 | CTX | O diagnóstico identifica infraestrutura digital, plataformas, serviços financeiros digitais, empreendedorismo e competências como componentes da economia digital de Moçambique. | A solução depende de um ecossistema digital e financeiro que apresenta oportunidades e limitações próprias. | Fundamentar a viabilidade/contexto da plataforma, sem usar o documento como prova de funcionalidades específicas. | Confirmado |
| DOC-02-E02 | NEC | O documento reporta crescimento do mobile money e simultaneamente limitações de confiança, aceitação de pagamentos digitais, interoperabilidade e identificação/KYC. | Pagamentos digitais trazem conveniência, mas também riscos de confiança, acesso e conformidade. | Investigar nas entrevistas métodos usados, dificuldades e percepção de segurança; evitar assumir que pagamento integrado é obrigatório. | Confirmado |
| DOC-02-E03 | REG/TEC | O diagnóstico destaca identidade, reputação, privacidade, protecção do consumidor e ambiente legal para transacções digitais, incluindo e-signature/e-contracts. | Identidade e transacções digitais exigem controlos e enquadramento além da UI. | Caso contratos/verificação/pagamentos sejam mantidos, avaliar legislação actual e requisitos de segurança/privacidade antes de especificar implementação. | Confirmado; legislação actual a verificar |
| DOC-02-E04 | TEC | O documento defende infraestrutura de pagamentos fiável, transparente e interoperável e discute integração entre sistemas através de APIs. | Uma eventual integração de pagamentos não deve ficar acoplada a um único meio sem análise. | Se pagamentos forem requisito validado, privilegiar arquitectura extensível por providers/APIs. | Candidato técnico |
| DOC-03-E01 | NEC | Plataformas digitais de trabalho apresentam problemas ligados a condições de trabalho, pagamento e protecção do trabalhador. | A mediação digital não elimina riscos de não pagamento ou desequilíbrio entre as partes. | Explorar pagamento, entrega, rejeição e conflitos nas entrevistas. | Confirmado |
| DOC-03-E02 | NEC | O relatório discute mecanismos de protecção e contestação quando trabalho é rejeitado/não pago. | Trabalhadores podem precisar de processo claro para contestar decisões/conflitos. | Investigar experiência local antes de decidir por dispute management/admin intervention. | Confirmado |
| DOC-04-E01 | NEC/BEN | O modelo de plataformas inclui recrutamento/matching, preço, comunicação, monitoria do trabalho, ratings/feedback/reviews, pagamentos e resolução de disputas. | O ciclo de uma plataforma de trabalho envolve mais do que descoberta de profissionais. | Usar como estrutura analítica e benchmark; cada capacidade continua sujeita à validação local. | Confirmado |
| DOC-04-E02 | BEN | Entre indicadores usados no matching aparecem reviews de clientes, ratings, perfil do trabalhador, histórico/portfólio e preço proposto. | Clientes precisam de sinais para avaliar adequação e confiança antes da contratação. | Perguntar como empregadores avaliam trabalhadores e como trabalhadores demonstram capacidade; não impor mecanismo específico. | Confirmado |
| DOC-04-E03 | NEC | Regras de governação de plataformas incluem aceitação/rejeição de trabalho, desactivação de contas, resolução de disputas e uso de dados. | Governação e moderação tornam-se parte do domínio quando a plataforma intermedeia relações. | Identificar regras de negócio e direitos/responsabilidades somente após entrevistas e análise normativa. | A validar |
| DOC-05-E01 | CTX | O estudo do Quénia identifica plataformas de freelancing com tarefas como desenvolvimento web, design, criação de conteúdo e marketing. | Existe evidência africana de mediação digital de trabalho compatível com actividades de TI/digitais. | Utilizar como referência regional, deixando claro que evidência do Quénia não representa directamente Maputo. | Confirmado |
| DOC-05-E02 | NEC | Plataformas financeiras como M-PESA permitem receber/pagar trabalho mediado por plataformas e simplificam pagamentos no contexto queniano. | Mobile money pode ser relevante para plataformas de trabalho em contexto africano. | Triangular com dados moçambicanos do BdM e entrevistas; não extrapolar preferência queniana para Moçambique. | Confirmado |
| DOC-06-E01 | CTX | A ENIF 2025–2031 e o relatório de 2025 tratam pagamentos digitais, educação financeira e protecção do consumidor como áreas de trabalho da inclusão financeira. | Pagamentos digitais são uma componente actual da política/ecossistema financeiro moçambicano. | Fundamentar contexto actual e perguntas sobre meios de pagamento/segurança. | Confirmado |
| DOC-06-E02 | REG/NEC | O relatório enquadra inclusão financeira como acesso e uso efectivo de serviços de instituições reguladas e define interoperabilidade como comunicação segura entre sistemas/plataformas financeiras. | Integração financeira exige atenção a provedores regulados, segurança e interoperabilidade. | Se houver integração real, especificar limites da plataforma e integração com provedores autorizados; não representar a ConecTA como prestador financeiro. | Candidato; requer análise regulatória específica |
| DOC-07-E01 | BEN | Upwork permite pesquisa de projectos por skills e filtros. | Matching pode beneficiar de informação estruturada e mecanismos de pesquisa. | Comparar com a necessidade local de descoberta; pode fundamentar desenho de pesquisa/filtros após entrevistas. | Confirmado |
| DOC-07-E02 | BEN | A proposta inclui preço/taxa, apresentação, informação solicitada pelo cliente e exemplos relevantes; o cliente analisa propostas e pode entrevistar antes da oferta. | Contratação pode exigir comparação estruturada de candidatos/propostas. | Investigar como clientes de Maputo recebem/comparam propostas actualmente. | Confirmado |
| DOC-07-E03 | BEN | Em contratos fixed-price, o guia usa milestones, financiamento prévio e escrow, entrega pela plataforma e libertação do pagamento. | Existem mecanismos para reduzir risco de não pagamento e de entrega. | Tratar escrow/milestones como alternativas de benchmark, não como requisitos já aprovados; verificar viabilidade legal/técnica local. | Benchmark |
| DOC-07-E04 | BEN | O guia recomenda confirmar termos de pagamento e método de pagamento verificado antes de iniciar o trabalho. | Clareza das condições e confiança no pagamento são elementos relevantes do processo. | Explorar formalização de preço, prazo, entregáveis e momento de pagamento nas entrevistas. | Confirmado |

## Temas para triangulação nas entrevistas

A matriz aponta, sem antecipar requisitos, para os seguintes temas a investigar:

1. descoberta de oportunidades/profissionais e matching;
2. demonstração e avaliação de competências;
3. confiança, identidade e verificação;
4. negociação de escopo, preço, prazo e entregáveis;
5. formalização do acordo/contrato;
6. comunicação e acompanhamento da execução;
7. métodos, momento e segurança do pagamento;
8. reputação, avaliações e histórico;
9. conflitos, rejeição de trabalho e resolução de disputas;
10. barreiras de adopção da plataforma.

Estes temas já estão cobertos pelos dois guiões semiestruturados.

## Regras para derivação futura de requisitos

- Evidência contextual (CTX) não gera RF por si só.
- Benchmark (BEN) demonstra uma solução possível, não uma necessidade local.
- Evidência de necessidade (NEC) deve, sempre que possível, ser triangulada com entrevistas.
- Evidência regulatória (REG) pode originar regra de negócio ou RNF quando aplicável, mas deve ser verificada contra legislação vigente.
- Decisões técnicas (TEC) devem ser justificadas pela arquitectura e atributos de qualidade, não apresentadas como preferência do utilizador.
- O estado actual do código não é fonte de requisito.
- Cada RF/RNF futuro deverá indicar a sua fonte na tabela padrão da monografia: Macro Requisito, ID, Nome, Declaração, Fonte, Prioridade, Data e Observação.

## Pendências

- Rever indicadores específicos do INFOR relevantes a Maputo e trabalho por conta própria.
- Extrair métricas actuais do Relatório de Inclusão Financeira 2025 que sejam realmente necessárias ao texto.
- Verificar legislação moçambicana vigente aplicável a contratos electrónicos, assinaturas, privacidade/dados e serviços de pagamento antes de transformar estas matérias em requisitos.
- Acrescentar documentos que venham a ser seleccionados para o corpus.
- Após as entrevistas, criar matriz de codificação temática e cruzá-la com as evidências DOC-xx.


## Análise substantiva — ronda 1

### DOC-01 — INFOR 2021/22

**O que a fonte suporta:** fonte oficial do INE sobre sector informal, emprego, actividades e receitas; cobertura nacional; possibilidade de desagregação provincial/urbano-rural/grupos de actividade; recolha em 2021.

**O que não suporta ainda:** percentagens específicas de informalidade na Cidade de Maputo; predominância de jovens; dimensão dos trabalhadores autónomos de TI; dificuldades de conexão com clientes; preferência por plataformas digitais. Essas afirmações exigem tabelas/indicadores específicos ou outras fontes.

**Uso previsto na monografia:** contextualização quantitativa apenas depois de seleccionar indicadores concretos. Não é fonte directa de RF.

### DOC-02 — Mozambique Digital Economy Diagnostic (World Bank, 2019)

A revisão integral da estrutura do relatório confirma cinco pilares: infraestrutura digital, plataformas digitais, serviços financeiros digitais, empreendedorismo digital e competências digitais. O relatório enquadra conectividade como meio de reduzir assimetrias de informação, ligar cidadãos a mercados/serviços e reduzir custos de transacção. Também documenta que a economia digital em Moçambique deve ser analisada como ecossistema, não apenas como disponibilidade de uma aplicação.

**Implicação:** esta fonte é adequada para a contextualização tecnológica e para justificar a relevância de estudar uma solução digital em Moçambique. Não demonstra, por si só, que trabalhadores autónomos de TI em Maputo necessitam de chat, geolocalização, avaliações, pagamentos integrados ou qualquer outra funcionalidade.

### DOC-04 — ILO WESO 2021

O relatório define as plataformas digitais de trabalho como intermediárias entre trabalhadores que executam tarefas e clientes/empresas, e documenta oportunidades e desafios associados à mediação digital do trabalho. O próprio relatório assenta numa base internacional ampla (12.000 trabalhadores em 100 países, além de empresas, plataformas e associações), pelo que é uma fonte forte para compreender o fenómeno e construir categorias analíticas.

**Limite de validade:** é evidência internacional, não uma descrição directa da Cidade de Maputo. Os mecanismos observados no relatório devem ser tratados como categorias/benchmark a triangular com o estudo local.

### Decisão após a ronda 1

Nenhum novo requisito funcional é aprovado nesta ronda. As três fontes reforçam a cadeia:

`contexto oficial/local → enquadramento da economia digital → funcionamento internacional das plataformas → investigação empírica local → necessidades → requisitos`.

A próxima ronda deve aprofundar secções específicas do World Bank e ILO relevantes a matching, confiança/reputação, pagamentos e conflitos, e extrair apenas indicadores do INFOR que sejam realmente utilizáveis no texto.


## Análise substantiva — ronda 2: mecanismos das plataformas

### Tema A — Descoberta e matching

O WESO 2021 mostra que recrutamento e matching são elementos centrais do modelo de negócio das plataformas digitais de trabalho. Na amostra de plataformas analisada pela ILO, os sinais utilizados no matching incluem avaliações de clientes, ratings, perfil do trabalhador, histórico/portfólio e preço/taxa proposta. O mesmo relatório indica que, nas plataformas freelance estudadas, a dificuldade em encontrar clientes constitui uma limitação relevante para parte dos trabalhadores.

**Leitura para a ConecTA:** existe suporte documental para tratar descoberta, pesquisa/matching e informação de perfil como categorias do problema. Não existe ainda suporte para tornar o matching algorítmico obrigatório, nem para escolher um ranking específico.

**Triangulação esperada:** N01, N02 e N04.

### Tema B — Confiança, reputação e demonstração de capacidade

O WESO coloca construção de perfil, ratings, demonstração de capacidade e feedback dentro da experiência do trabalhador na plataforma. Contudo, ratings também integram mecanismos de avaliação e gestão algorítmica, podendo afectar acesso ao trabalho e condições de participação.

O estudo ILO Kenya 2024 reforça que contas com ratings elevados adquirem valor económico para os trabalhadores e que dificuldades de criação/manutenção de contas podem produzir comportamentos secundários, incluindo compra de contas.

**Leitura para a ConecTA:** perfil, portfólio/histórico e reputação são mecanismos documentados de redução de assimetria de informação, mas não devem ser tratados como equivalentes a “confiança garantida”. A concepção de avaliações deve considerar contestabilidade, contexto e risco de efeitos injustos.

**Triangulação esperada:** N02, N03, N11 e N12.

### Tema C — Comunicação, negociação e formalização

A ILO documenta que plataformas freelance podem manter canais oficiais de comunicação e regras sobre o conteúdo e as transacções que ocorrem nesses canais. Também documenta acompanhamento do trabalho e, em alguns modelos, monitoria digital intensa.

**Leitura para a ConecTA:** a evidência suporta a necessidade de preservar informação relevante do relacionamento e de estruturar condições do trabalho, mas não prova que um chat interno completo seja necessário. A função científica a investigar é rastreabilidade de decisões/acordos, não “chat” como solução pré-definida.

**Triangulação esperada:** N05, N06, N07 e N08.

### Tema D — Pagamentos e protecção bilateral

A literatura distingue método de pagamento, momento de pagamento, taxas, aceitação/rejeição do trabalho e mecanismos de protecção. O WESO documenta escrow em algumas plataformas freelance, enquanto o estudo do Quénia mostra que trabalhadores valorizam sistemas seguros de pagamento, mas também podem sentir-se limitados pelos métodos disponibilizados. No estudo queniano, a maioria dos freelancers online pesquisados utilizava sistemas de pagamento online, com outros a recorrerem a transferência bancária ou métodos móveis.

**Leitura para a ConecTA:** existe forte fundamento para investigar e especificar clareza sobre valor, método, momento e condições de pagamento. Não existe fundamento para concluir que a ConecTA deve custodiar dinheiro, operar escrow ou integrar um meio específico. Escrow permanece benchmark e dependeria de viabilidade técnica/regulatória.

**Triangulação esperada:** N09 e N10.

### Tema E — Rejeição, conflitos e governação

A ILO trata rejeição de trabalho, withholding/non-payment, account deactivation, feedback e dispute resolution como pontos relevantes da experiência do trabalhador e das regras de governação das plataformas. A literatura também mostra que regras unilaterais da plataforma podem criar desequilíbrios.

**Leitura para a ConecTA:** há suporte documental para que conflitos e preservação de evidência sejam investigados como parte do domínio. Não há suporte suficiente para transformar automaticamente a ConecTA num árbitro de disputas ou para assumir decisão administrativa sobre conflitos técnicos.

**Triangulação esperada:** N12, N13 e N14.

### Tema F — Diversidade dos serviços de TI e localização

O WESO distingue plataformas online web-based, nas quais o trabalho pode ser executado remotamente, de plataformas location-based. Software development aparece entre os trabalhos que podem ser mediados online. O corpus africano também mostra diversidade entre serviços mediados digitalmente.

**Leitura para a ConecTA:** o domínio de TI não deve assumir que todos os serviços são remotos. A localização pode ser relevante para serviços presenciais, mas não deve funcionar como requisito universal de matching.

**Triangulação esperada:** N15 e N16.

## Resultado da ronda 2 — estatuto das funcionalidades actualmente visíveis no protótipo

| Capacidade | Suporte documental | Decisão nesta fase |
|---|---|---|
| Pesquisa/descoberta de trabalhadores/ofertas | Forte | Manter como capacidade candidata; triangular localmente |
| Perfil profissional | Forte | Manter como capacidade candidata |
| Portfólio/histórico | Forte | Manter como mecanismo candidato de demonstração de capacidade |
| Ratings/reviews | Forte como padrão de plataforma; riscos também documentados | Candidato, desenho ainda não definido |
| Propostas | Moderado/forte no modelo freelance | Candidato; triangular forma local de negociação |
| Registo de condições/acordo | Forte como necessidade de clareza | Candidato; forma de formalização ainda aberta |
| Chat interno | Fraco como requisito autónomo | Não derivar directamente; investigar rastreabilidade |
| Notificações | Não estabelecido como necessidade central nesta ronda | Não derivar ainda |
| Pagamentos integrados | Parcial | Não aprovar integração; necessidade é clareza/protecção do pagamento |
| Escrow | Benchmark | Não aprovar como requisito |
| Assinatura electrónica | Não estabelecida nesta ronda | Não aprovar |
| Verificação documental | Parcial/indirecto | Requer triangulação local e análise normativa |
| Teste/assessment de competências | Não estabelecido como necessidade universal | Não aprovar |
| Avaliação bilateral | Plausível; reputação é forte, bilateralidade precisa triangulação | Candidato |
| Gestão administrativa de disputas | Conflitos são suportados; arbitragem pela plataforma não | Não aprovar como desenho |
| Localização | Contextual | Usar apenas quando o tipo de serviço a torna relevante |

### Conclusão da ronda 2

A análise documental começa a separar claramente **necessidades do domínio** de **soluções de interface/produto**. O corpus suporta descoberta, informação profissional, clareza das condições, pagamento/protecção, reputação e tratamento de conflitos como temas relevantes. Não suporta ainda a adopção automática de chat, escrow, assinatura electrónica, assessments, geolocalização universal ou arbitragem administrativa.

Nenhum RF é fechado apenas com esta ronda.
