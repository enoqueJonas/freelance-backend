# Matriz de Análise Documental

## Objectivo

Registar de forma rastreável as evidências extraídas do corpus documental que podem ajudar a compreender o contexto, identificar problemas/necessidades e fundamentar decisões futuras da solução ServiPlus.

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
| DOC-01-E01 | CTX | O INFOR 2021/22 caracteriza o sector informal moçambicano e recolhe dados sobre emprego, actividades e receitas. O estudo possui 12.534 casos e 710 variáveis. | A informalidade é um fenómeno suficientemente relevante para enquadramento empírico nacional. | Usar para caracterização do contexto; não inferir automaticamente necessidades específicas de freelancers de TI em Maputo. | Confirmado |
| DOC-01-E02 | CTX | O INFOR contém variáveis sobre emprego e actividade informal, incluindo informação geográfica e área de residência. | O contexto local pode ser analisado com dados oficiais em vez de afirmações genéricas sobre informalidade. | Seleccionar apenas indicadores directamente pertinentes à população/área do estudo e explicitar população, ano e geografia. | A aprofundar |
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
| DOC-06-E02 | REG/NEC | O relatório enquadra inclusão financeira como acesso e uso efectivo de serviços de instituições reguladas e define interoperabilidade como comunicação segura entre sistemas/plataformas financeiras. | Integração financeira exige atenção a provedores regulados, segurança e interoperabilidade. | Se houver integração real, especificar limites da plataforma e integração com provedores autorizados; não representar a ServiPlus como prestador financeiro. | Candidato; requer análise regulatória específica |
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
