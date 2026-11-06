# D62 — Emendas prontas para revisão: Capítulo II, Capítulo IV e ponte com requisitos

**Estado:** substituições **candidatas**, sem alterações directas à D44 Word.  
**Hierarquia obrigatória:** análise documental **principal**; entrevistas semiestruturadas **complementares**, preservadas em anexo; decisão de engenharia explícita.  
**Fundamentação:** [D62 — auditoria oficial e matriz N01–N18](D62_AUDITORIA_FONTES_DOCUMENTAIS_N01_N18.md), [D61 — apoio qualitativo selectivo](D61_MATRIZ_DOCUMENTAL_APOIO_ENTREVISTAS.md).  
**Não** reinterpretar o corpus como origem universal de requisitos nem «recolha estatisticamente representativa». Não acrescentar uma citação sem ter consultado a fonte aplicável.

## 1. Capítulo II — substituições cirúrgicas recomendadas

### §2 (abertura) — força do corpus

**Texto da D44 identificado, p.19:** «A literatura é utilizada como fonte de enquadramento e de possíveis mecanismos de solução; as necessidades específicas da população estudada são confirmadas posteriormente através do corpus empírico».

**Substituição candidata:**

> A revisão bibliográfica e a análise documental constituem a **base principal** para caracterizar o problema, identificar mecanismos de intermediação e fundamentar as decisões de especificação da aplicação. As entrevistas semiestruturadas com trabalhadores autónomos de TI e empregadores constituem **complemento qualitativo**, permitindo relacionar algumas opções de desenho com experiências relatadas e identificar divergências relevantes. O corpus não representa, por si, confirmação estatística das necessidades da população da Cidade de Maputo; a implementação e os ensaios do protótipo são avaliados separadamente.

### §2.1 — categorias de plataformas

**Manter** tipologia OIT (2021) de plataformas baseadas na web e na localização. Ajustar, quando necessário:

> A classificação distingue o **local de execução** da actividade, e não a tecnologia pela qual se acede à plataforma. Desenvolvimento de software, design, redes e manutenção constituem exemplos de actividades tecnológicas com diferentes modalidades de execução; não são dados de prevalência dos serviços de TI da Cidade de Maputo extraídos do relatório da OIT.

**Fonte:** [OIT 2021](https://www.ilo.org/publications/summary-role-digital-labour-platforms-transforming-world-work).

### §2.2 — cinco pilares específicos da edição de Moçambique de 2019

**Verificação positiva:** o relatório [*Mozambique Digital Economy Diagnostic — Executive Summary Report*](https://pubdocs.worldbank.org/en/833211594395622030/Mozambique-DECA.pdf) identifica especificamente **Digital Infrastructure, Digital Platforms, Digital Financial Services, Digital Entrepreneurship e Digital Skills**, com secções de síntese 2.1–2.5 nas páginas impressas 16–17. **A D44 já nomeia os cinco pilares correctamente; não corrigir esta passagem para as palavras da grelha DE4A genérica contemporânea.**

**Precisão a acrescentar:**

> Os pilares deste diagnóstico contextualizam condições de conectividade, plataformas digitais, pagamentos, empreendedorismo e competências no país. Não permitem concluir, sem recolha própria, qual é a dimensão do mercado de trabalhadores autónomos de TI em Maputo nem que uma funcionalidade específica é desejada ou viável para esses trabalhadores.

**Sobre INE:** o [INFOR](https://mozdata.ine.gov.mz/index.php/catalog/89) é referência contextual ao sector informal; os [relatórios finais de 2022](https://mozdata.ine.gov.mz/index.php/catalog/89/related-materials) estão listados, mas nenhuma tabela relevante à população freelance de TI foi extraída nesta auditoria. Não inserir estatísticas novas sem universo, página, denominador e fonte.

### §2.3 — discovery, filtros e efeito de rede

> A OIT (2021) documenta efeitos de rede e o uso de dados, métricas e algoritmos na correspondência e gestão do trabalho em plataformas digitais. Estes mecanismos podem afectar a visibilidade e o acesso a oportunidades. Na ConecTA, a opção por **pesquisa manual com filtros e comparação de perfis**, sem imposição de selecção algorítmica, constitui uma **decisão de engenharia** orientada pela transparência e autonomia das partes. A existência de uma função de pesquisa não assegura, isoladamente, que haverá trabalhadores e oportunidades suficientes para que a intermediação seja útil.

**Fonte:** [OIT 2021 — network effects e algorithmic management](https://www.ilo.org/infostories/en-GB/Campaigns/WESO/World-Employment-Social-Outlook-2021).  
**Apoio subsidiário:** T04 é exemplo de preferência por escolha manual; T05 é contraexemplo à universalidade do problema de descoberta. Os depoimentos são **apenas nota selectiva**, não a origem exclusiva do RF.

### §2.4 — competência/identidade

> A literatura sobre plataformas identifica a influência de avaliações e indicadores de competência na visibilidade dos trabalhadores, mas não estabelece uma forma universal de comprovação técnica adequada a todas as especialidades de TI. A possibilidade de apresentar portfólios, repositórios, certificações, experiência e referências constitui uma decisão de modelação **plural e proporcional** ao tipo de actividade. A verificação de perfis deve ainda respeitar finalidades e dados necessários, não se confundindo com KYC financeiro.

**Fontes:** [OIT 2021](https://www.ilo.org/resource/role-digital-labour-platforms-transforming-world-work-0), [OWASP ASVS 5.0.0](https://asvs.owasp.org/) **somente** para características de segurança da aplicação.  
**Apoio subsidiário:** T01/T03/T06 mostram limitações diferentes das evidências profissionais; não provar que testes universais são ilegais ou tecnicamente impossíveis.

### §2.5 — acordos e versões

> A governação das plataformas e a clareza das condições de trabalho integram o enquadramento das relações mediadas digitalmente. Para a ConecTA, a opção por **registar uma versão das condições aceites, conservar o histórico e exigir concordância explícita em alterações materiais** é uma decisão de especificação destinada a apoiar a rastreabilidade. Não resulta de uma regra universal prescrita pela OIT nem se equipara, por si, a assinatura electrónica qualificada. A sua eficácia na prevenção de conflitos depende de uso correcto, implementação e avaliação.

**Fontes:** [OIT 2021](https://www.ilo.org/sites/default/files/wcmsp5/groups/public/%40dgreports/%40dcomm/%40publ/documents/publication/wcms_771749.pdf) para governação **geral**, [ISO/IEC/IEEE 29148](https://www.iso.org/standard/72089.html) para **processo de especificação**, nunca como fonte de obrigação contratual.  
**Apoio subsidiário:** T01/T05/T06/E02 relatam cenários de alterações.

### §2.6 — pagamento, escrow e legislação

> As fontes sobre trabalho em plataformas e a inclusão financeira demonstram a relevância do pagamento, da transparência e da protecção dos intervenientes. No protótipo, optou-se por registar **condições e estados** de pagamento e por prever eventual integração com prestador externo, **sem custódia própria de fundos**. Esta delimitação resulta de uma decisão de âmbito e de exposição operacional/regulatória a examinar; não significa que a Estratégia Nacional de Inclusão Financeira proíba escrow ou que os participantes das entrevistas tenham rejeitado esse mecanismo. **T02, T04 e E01**, pelo contrário, descreveram vantagens possíveis de custódia sob condições claras; essa divergência deve permanecer visível na discussão. O registo de um pagamento declarado não prova que uma transacção financeira ocorreu.

**Fontes:** [OIT 2018 — remuneração e condições em microtarefas](https://www.ilo.org/publications/digital-labour-platforms-and-future-work-towards-decent-work-online-world), [ENIF 2025–2031](https://www.bancomoc.mz/pt/areas-de-actuacao/inclusao-financeira/quadro-conceptual-da-inclusao-financeira/).  
**Bloqueio jurídico:** se a revisão for posterior a 2 Julho 2026, consultar integralmente a [Lei 15/2026](https://inm.gov.mz/pt-br/content/sum%C3%A1rio-br-n%C2%BA-124-de-020726-boletim-da-rep%C3%BAblica-i-serie-p%C3%A1g-1013) antes de qualquer conclusão sobre licenciamento/autorização de serviços de pagamento. Não extrair conclusões legais do sumário.

### §2.7 — avaliação e contestação

> Classificações e reputação são usadas em plataformas para apoiar a escolha e influenciar a distribuição de oportunidades. A OIT descreve também impactos desses instrumentos no acesso ao trabalho. A ConecTA propõe **avaliação bilateral, elegibilidade por relação de contratação e contextualização/contestação de avaliações** como medidas de concepção, não como efeitos comprovados nem obrigações universais estabelecidas pela literatura. Uma classificação isolada não demonstra a competência ou fiabilidade de qualquer participante.

**Apoio subsidiário:** T02 sobre avaliações potencialmente injustas; E02/E03 sobre contexto.

### §2.8 — moderação e conflitos

> A literatura descreve regras de governação e tratamento de queixas em diferentes plataformas. Na ConecTA, propõe-se um processo de **registo, organização e acompanhamento administrativo** de situações reportadas, com preservação dos elementos relevantes e controlo de acesso. A plataforma não se apresenta como árbitro universal de obrigações legais ou de qualidade técnica, cujas decisões podem exigir terceiros competentes. O mecanismo exacto de estados, permissões e retenção é uma decisão técnica da especificação e requer testes próprios.

**Apoio subsidiário:** T08/E02 sobre registo e limite de peritagem.  
**Limite:** não equiparar mecanismo conceitual a funcionalidade Django já implementada.

### §2.9 (se existir) — engenharia de requisitos, UML e segurança

> A ISO/IEC/IEEE 29148:2018 fornece orientação sobre processos e características dos requisitos; a UML 2.5.1 é uma notação formal de modelação; e o OWASP ASVS 5.0.0 é referência de requisitos verificáveis de segurança de aplicações. Estas fontes fundamentam **o método de especificação, a forma dos diagramas e os critérios técnicos**; não demonstram que as funcionalidades estejam implementadas, que a ConecTA cumpra o ASVS ou que exista validação empírica com o público-alvo.

**Fontes:** [ISO 29148](https://www.iso.org/standard/72089.html), [OMG UML 2.5.1](https://www.omg.org/spec/UML/2.5.1/About-UML), [OWASP ASVS](https://asvs.owasp.org/).

## 2. Capítulo IV — modificar a hierarquia da argumentação, não a lista de necessidades

### §4.1 — início do capítulo

> A análise do contexto da contratação entre trabalhadores autónomos de Tecnologias de Informação e empregadores na Cidade de Maputo baseia-se **principalmente na revisão bibliográfica e documental** sobre economia digital, trabalho mediado por plataformas, condições de contratação, pagamentos e governação de aplicações. A especificação traduz a interpretação dessas fontes em necessidades e regras de negócio. As **entrevistas semiestruturadas** com oito trabalhadores e três empregadores, cujas transcrições literais são apresentadas nos anexos, desempenham função **complementar**: fornecem exemplos de práticas e dificuldades, permitem contrastar certas decisões e revelar divergências. Não representam um inquérito estatístico e não comprovam que as funcionalidades do protótipo produzem efeitos no mercado.

### §4.6 — caracterização das entrevistas sem inverter o método

> O documento de recolha disponibilizado contém onze transcrições literais, codificadas T01–T08 e E01–E03. A respectiva ficha identifica entrevistas semiestruturadas presenciais realizadas entre Julho e Setembro de 2024, com participantes de diferentes especialidades e tipos de contratação. Os depoimentos foram utilizados **para contextualizar situações seleccionadas** discutidas na análise documental, não para derivar automaticamente todos os requisitos. A interpretação preserva exemplos divergentes, incluindo a situação de um profissional cuja rede já gera trabalho suficiente e as preferências de algumas partes por mecanismos de custódia de pagamento, que não foram adoptados no escopo do protótipo. A amostra qualitativa não permite determinar incidência populacional das práticas; os dados de selecção, consentimento e produção do registo textual devem reflectir o procedimento efectivamente realizado.

### §4.15 e §4.16 — precedência causal correcta

> A análise documental e a interpretação de decisões de engenharia permitiram organizar **dezoito necessidades candidatas**, N01–N18, relacionadas com a especificação da plataforma. Os relatos das entrevistas semiestruturadas foram associados **selectivamente** a necessidades para as quais ofereceram exemplos concretos, confirmação contextual ou contrapontos. N18 permanece uma condição de adopção e não uma funcionalidade implementável isoladamente. A rastreabilidade distingue `documento → necessidade → regra/requisito` de `entrevista → apoio/contraste`, sem pressupor validação universal de necessidades nem testes concluídos do protótipo.

**Nota estrutural:** manter a lista N01–N18 e a numeração de secções da D44 até ratificação da baseline. A análise das respostas completas irá para **ANEXOS**; o Capítulo IV deve conter apenas remissões curtas (por exemplo T03/T06 para preço após diagnóstico, T05 para a ressalva sobre procura, T02/T04/E01 para tensão com escrow).

## 3. Ponte ao Capítulo V, §5.2 (origem dos requisitos)

> As regras RN01–RN16 e os requisitos RF01–RF28 resultam de um processo de especificação **fundamentado principalmente na análise bibliográfica/documental e nas decisões de engenharia**. Determinadas funcionalidades recebem apoio qualitativo complementar de entrevistas semiestruturadas, conforme identificadores e transcrições no anexo. Outras, como autenticação, autorização, auditoria administrativa e segurança, são requisitos habilitadores ou de governação do sistema, e não declarações directas dos participantes. Os cenários de validação e os resultados de implementação devem ser apresentados separadamente, sem converter a existência de uma fonte ou de uma opinião num teste aprovado.

## 4. Testes de integridade antes de usar estas emendas

- [ ] Verificar contra a edição oficial citada os recortes exactos das fontes e requisitos a que são associados.
- [ ] Conferir se **todas** as afirmações documentais preservam a população e âmbito dos respectivos relatórios.
- [ ] Confirmar que a terminologia da versão Banco Mundial Moçambique 2019 está correcta (está) e não foi substituída por terminologia genérica de 2024.
- [ ] Confrontar os exemplos T/E com as transcrições literais e não aumentar artificialmente o número de entrevistados.
- [ ] Não declarar «revisão sistemática» ou processos de análise que não constem do procedimento real.
- [ ] Aplicar alterações apenas à cópia do DOCX D44 original, sem remover comentários nem diagramas e com revisão da autora/supervisão.
- [ ] Conciliar referências de 2026 e a data da capa; definir que revisão do protótipo entra na dissertação.

**Este documento é uma proposta operacional de texto. Nenhum Word foi editado ou aprovado por estes registos GitHub.**
