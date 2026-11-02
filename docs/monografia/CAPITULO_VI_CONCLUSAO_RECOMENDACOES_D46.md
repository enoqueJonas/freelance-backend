# Proposta D46 — Capítulo VI: Conclusão e recomendações

**Documento-base:** `Monografia_D44_Metodologia_Proveniencia_Verificada.docx`, pp. 64–66.  
**Acompanhamento obrigatório:** `SECCAO_5_5_DISCUSSAO_RESULTADOS_D46.md` e `CAPITULO_IV_REVISAO_INTEGRAL_D46.md`.  
**Estatuto:** texto completo **para revisão e integração controlada**, não aplicado ao DOCX canónico. Preserva os subtítulos §6.1 e §6.2, não introduz factos, entrevistas ou ensaios não comprovados.

---

# 6 CONCLUSÃO E RECOMENDAÇÕES

## 6.1 Conclusão

A presente investigação teve como objectivo desenvolver um protótipo de aplicação web destinado a apoiar a conexão e a contratação entre trabalhadores autónomos da área de Tecnologias de Informação e empregadores na Cidade de Maputo. Para esse efeito, articulou uma revisão bibliográfica e documental, a exploração de cenários textuais associados ao processo de contratação, a especificação de requisitos e a modelação de uma solução tecnológica, complementadas pela análise estática do código de um protótipo demonstrativo.

A revisão da literatura permitiu identificar aspectos relevantes para a concepção de plataformas de intermediação de serviços, designadamente descoberta de oportunidades, demonstração de competência, negociação, condições contratuais, pagamentos, reputação e gestão de conflitos. No entanto, o material qualitativo disponível apresenta uma limitação metodológica determinante: embora tenham sido organizados onze registos textuais, correspondentes a oito perfis de trabalhadores e três de empregadores, não foram identificadas evidências primárias independentes suficientes para confirmar a origem desses registos como entrevistas de campo efectivamente realizadas. Por essa razão, as categorias analisadas foram utilizadas como hipóteses de necessidades e cenários de desenho, e não como resultados empíricos comprovados sobre o público-alvo da Cidade de Maputo.

No domínio da especificação, a investigação organizou dezoito hipóteses de necessidades, dezasseis regras de negócio, vinte e oito requisitos funcionais e sete requisitos não funcionais. Estes elementos foram associados a actores, casos de uso, modelos de classes, diagramas de actividades, sequências, estados e arquitectura lógica. A contribuição central desta etapa é a definição de um modelo que distingue a descoberta de oportunidades, a apreciação de propostas, a formalização e o versionamento de condições, a execução do serviço, o registo de pagamentos e os mecanismos de reputação e conflitos. A formulação dessas relações constitui uma contribuição de concepção, mas não comprova que todas as necessidades tenham sido validadas junto dos utilizadores.

A análise técnica identificou uma implementação demonstrativa parcial. O frontend React/TypeScript representa diversos percursos por meio de operações e dados simulados, enquanto o backend Django/DRF possui funcionalidades limitadas de contas, perfis e autenticação. A arquitectura-alvo de contratação não se encontra integralmente materializada no código e não foi demonstrada uma integração operacional completa entre frontend e backend. Entre as diferenças relevantes destacam-se a ausência de versionamento integral dos acordos, a simplificação das transições contratuais, a inexistência de confirmação real de pagamentos e o tratamento de conflitos que não corresponde plenamente às regras do modelo concebido.

A avaliação dos objectivos evidencia, portanto, graus distintos de realização. A análise do contexto e das necessidades foi desenvolvida de forma documental e exploratória, mas não estabelece um diagnóstico empírico comprovado do processo real de contratação em Maputo. A especificação de requisitos e a modelação conceptual foram produzidas, embora ainda sujeitas a confirmação das suas bases e decisões. O desenvolvimento do protótipo foi parcial em relação ao domínio final previsto. Por fim, a definição de um protocolo de testes e a inspecção estática da implementação não substituem a validação funcional e não funcional: os ensaios V01–V08 e RNF01–RNF07 não possuem resultados de execução documentados nesta versão.

Quanto à pergunta de pesquisa — *Como uma aplicação web pode facilitar a conexão entre trabalhadores autónomos da área de Tecnologias de Informação e empregadores na Cidade de Maputo?* — o trabalho oferece uma **resposta de concepção**. Uma aplicação pode organizar a apresentação e procura de oportunidades, apoiar a avaliação de perfis, permitir o registo de propostas e condições aceites, conservar alterações e entregas e documentar estados de pagamento, avaliações e conflitos. A articulação desses mecanismos foi especificada de forma conceptual; a afirmação de que efectivamente facilitam o processo para trabalhadores e empregadores reais depende de implementação e avaliação posteriores.

Consequentemente, a hipótese geral e as hipóteses específicas encontram graus diferentes de **sustentação conceptual e representação técnica**, mas não foram confirmadas empiricamente. A HE1 possui representação parcial de pesquisa e perfis na interface demonstrativa; a HE2 é fundamentada sobretudo pelo modelo de acordos versionados; a HE3 foi concebida para reputação e conflitos, com simulação limitada; e a HE4 foi especificada para condições e estados de pagamento sem custódia própria, ainda sem comprovação de operações financeiras reais. Estas distinções impedem tratar hipóteses formuladas como possibilidades de solução como conclusões sobre eficácia, confiança ou redução de riscos no mercado.

Conclui-se que o trabalho produziu uma base conceptual e técnica para evoluir uma plataforma de intermediação de serviços de TI, mas **não demonstrou ainda** a implementação integral dos requisitos nem a adequação e efectividade da solução junto do público-alvo. A principal contribuição defensável nesta fase reside na especificação estruturada do domínio e na identificação explícita da distância entre a solução concebida e o protótipo disponível, estabelecendo condições concretas para a sua implementação e avaliação futura.

## 6.2 Recomendações

Como primeira prioridade, recomenda-se confirmar a proveniência dos materiais qualitativos e, quando necessário, realizar recolha empírica documentada com trabalhadores autónomos de TI e empregadores da Cidade de Maputo. O processo deverá definir critérios de selecção, instrumentos, procedimentos éticos aplicáveis, registos originais e método de análise, permitindo distinguir necessidades efectivamente expressas pelos participantes das hipóteses anteriormente construídas a partir de cenários de trabalho. A recolha deve ainda considerar opiniões divergentes, evitando pressupor que todos os profissionais enfrentam os mesmos constrangimentos ou valorizam as mesmas funcionalidades.

Em segundo lugar, recomenda-se consolidar o registo de decisões e a rastreabilidade dos requisitos. A especificação final deverá identificar, para cada necessidade, a fonte que a sustenta, as regras e requisitos derivados, os modelos em que é representada e os critérios que permitirão verificar o respectivo comportamento. As decisões de facultatividade de testes técnicos, verificação contextual de perfis, ausência de custódia financeira e não obrigatoriedade de chat devem ser justificadas como escolhas de âmbito e engenharia, sem as apresentar como preferências empiricamente comprovadas.

No plano de desenvolvimento, a prioridade deverá recair sobre a integração efectiva do frontend com a API e a implementação do domínio central da contratação. Este percurso deve abranger o ciclo oportunidade–proposta–contratação, a aceitação bilateral de condições, o versionamento de alterações, os registos de execução e entrega e o histórico consultável das operações. A autorização deve considerar a relação de cada utilizador com o recurso e permitir perfis acumuláveis sem possibilitar a representação de ambos os lados da mesma contratação.

Recomenda-se também corrigir os comportamentos demonstrativos que não correspondem à especificação final. Os registos de pagamento devem distinguir declaração, confirmação e eventual integração externa, sem produzir mensagens que façam presumir custódia de fundos ou liquidação financeira não comprovada. As avaliações devem ficar associadas a relações elegíveis e admitir contestação documentada. O acompanhamento de conflitos deve dispor de registos próprios, preservando a separação entre a situação operacional da contratação e as medidas administrativas de moderação, sem assumir competências arbitrais.

Após a implementação das capacidades prioritárias, deverá ser executado um plano de verificação com evidências observáveis. Recomenda-se aplicar os cenários funcionais V01–V08, complementados por tentativas inválidas e testes de autorização, bem como as verificações RNF01–RNF07 que forem pertinentes à versão efectivamente implementada. Para cada ensaio deverão ser registados ambiente, revisão do software, dados utilizados, passos, resultado esperado, resultado observado e evidências, distinguindo casos aprovados, reprovados e não executados. A integração com prestadores de pagamento, se não estiver presente, deverá continuar identificada como não implementada, em vez de ser considerada satisfeita por uma simulação local.

Por fim, recomenda-se realizar avaliação de usabilidade baseada em tarefas e análise posterior da adopção junto de participantes do público-alvo. Essa avaliação deverá considerar, entre outros aspectos, a facilidade de encontrar uma oportunidade ou um profissional, a compreensão das condições da prestação, a capacidade de identificar alterações e o entendimento dos estados de entrega, pagamento e reclamação. A utilidade da solução dependerá ainda da existência de participantes e oportunidades suficientes, questão que exige investigação de mercado e não pode ser resolvida apenas mediante o desenvolvimento de funcionalidades adicionais.

A concretização dessas recomendações permitirá avaliar de forma mais rigorosa se a solução proposta responde às necessidades reais do contexto estudado e em que condições os mecanismos concebidos contribuem para uma relação de contratação mais clara e rastreável.

---

## Protocolo de integração editorial — não incluir na monografia

**Coerência com os objectivos estabelecidos na D44:**
- OE1: análise documental efectuada; caracterização de campo não demonstrada.
- OE2: especificação elaborada, não empiricamente validada.
- OE3: representação parcial do protótipo, sem domínio completo integrado.
- OE4: diagnóstico de cobertura + planos de verificação; não houve validação executada.

**Coerência com §5.5 D46:** HG e HE1–HE4 avaliadas por sustentação conceptual, representação demonstrativa e ausência de prova de eficácia. Sem rótulo enganador de «comprovada» ou «parcialmente comprovada».

**Restrições:** não alterar a formulação original da pergunta, hipóteses ou objectivos sem validação da supervisão; não atribuir valor estatístico aos onze registos; não incluir notas de edição nem caminhos/nomes de ficheiros no texto académico; não declarar testes executados; não usar esta conclusão para legitimar aprovação do documento canónico.

**Após eventual integração:** actualizar o índice e os campos Word, verificar paginação, remissões e legendas e reler Resumo/Abstract, Capítulo III, Capítulo IV e §5.5 para eliminar contradições.
