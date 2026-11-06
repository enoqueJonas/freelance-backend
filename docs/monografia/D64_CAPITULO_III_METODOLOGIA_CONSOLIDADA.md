# D64 — Capítulo III integral: metodologia documental principal, entrevistas subsidiárias e validação técnica

**Estatuto:** proposta integral de substituição do Capítulo III da D44, **não aplicada ao ficheiro DOCX canónico**; sujeita a revisão da autora e da supervisão.  
**Estrutura preservada:** `3.1, 3.1.1–3.1.4, 3.2, 3.2.1–3.2.2, 3.3, 3.3.1, 3.4, 3.5, 3.6 e 3.7`.  
**Fontes de trabalho:** `Monografia_D44_Metodologia_Proveniencia_Verificada.docx`, pp. físicas 31–35; `Estudo_de_Mercado_Entrevistas_e_Inquerito_TI_Maputo(1).docx`, pp. físicas 1–21, **apenas transcrições nas pp. 5–21**; [D59](D59_DECISAO_METODOLOGICA_ENTREVISTAS_SEMIESTRUTURADAS.md), [D60](D60_CONFIRMACAO_TRANSCRICOES_LITERAIS.md), [D61](D61_MATRIZ_DOCUMENTAL_APOIO_ENTREVISTAS.md), [D62](D62_AUDITORIA_FONTES_DOCUMENTAIS_N01_N18.md), [D63](D63_CAPITULO_IV_CONSOLIDADO_DOCUMENTAL.md), [D57 matriz V/RNF](D57_MATRIZ_VALIDACAO_V01_V08_RNF.md).  
**Decisão explícita de orientação:** replicar a função relativa das fontes na monografia de Blockchain/Xitique, sem transferir dados ou requisitos: **análise bibliográfica/documental fundamenta principalmente o sistema; entrevistas semiestruturadas contextualizam alguns requisitos e serão apresentadas em anexo**. A documentação de testes do software constitui um terceiro eixo, de verificação técnica, sem substituir os dois anteriores.

---

# 3 METODOLOGIA, MATERIAL E MÉTODOS

## 3.1 Tipo de pesquisa

A investigação procura compreender e estruturar o processo de conexão e contratação entre trabalhadores autónomos da área de Tecnologias de Informação e empregadores na Cidade de Maputo, com a finalidade de conceber e desenvolver um protótipo de aplicação web. A metodologia articula **levantamento bibliográfico e análise documental**, utilizados como **fundamentação principal das necessidades e dos requisitos da aplicação**, com **entrevistas semiestruturadas de carácter complementar** e actividades de especificação, modelação, desenvolvimento e verificação técnica do protótipo.

A classificação da pesquisa é apresentada segundo natureza, abordagem do problema, objectivos e procedimentos. A diversidade dessas componentes não deve ser confundida com um inquérito quantitativo, nem com a demonstração de eficácia da aplicação entre utilizadores reais.

### 3.1.1 Quanto à natureza

A investigação é de **natureza aplicada**, pois procura utilizar conhecimento bibliográfico, documental e técnico para responder a um problema de concepção e materializar uma solução informática. A finalidade prática traduz-se na especificação de regras de negócio e requisitos, elaboração de modelos de software e desenvolvimento de um protótipo que represente, de forma verificável, etapas seleccionadas de um processo de contratação de serviços de TI.

A classificação como pesquisa aplicada não implica que a plataforma esteja publicada em produção ou que os seus efeitos económicos e sociais tenham sido medidos. A capacidade de execução de determinadas funcionalidades e o alcance da validação são descritos separadamente no Capítulo V.

### 3.1.2 Quanto à abordagem

A abordagem é **predominantemente qualitativa**, centrada na interpretação de fontes bibliográficas e documentos institucionais e técnicos. A revisão documental desempenha o papel principal na identificação dos mecanismos relevantes — intermediação, informação profissional, condições de contratação, pagamentos, reputação e governação — e na fundamentação de alternativas de solução.

**Complementarmente**, foram consideradas entrevistas semiestruturadas realizadas a trabalhadores autónomos de TI e empregadores ou contratantes. As respostas foram utilizadas para contextualizar situações específicas, explorar diferenças entre especialidades e questionar algumas escolhas de concepção. Os depoimentos não foram usados como fonte exclusiva das regras e requisitos, nem para produzir estimativas estatísticas sobre a população de Maputo.

A execução de testes automatizados do protótipo corresponde à **verificação técnica do software**, com objectos, dados e critérios distintos dos utilizados na análise qualitativa. Resultados de API e de browser não equivalem a entrevistas nem a observação do comportamento dos utilizadores do mercado.

### 3.1.3 Quanto aos objectivos

Quanto aos objectivos, a pesquisa apresenta carácter **exploratório e descritivo**. O carácter exploratório decorre da necessidade de relacionar conhecimento existente sobre plataformas digitais de trabalho com um modelo de contratação de serviços de TI adequado ao problema delimitado. O carácter descritivo corresponde à sistematização de modalidades de prestação, possíveis dificuldades de contratação, actores, processos e necessidades da solução.

O componente descritivo não consiste numa medição de frequência de problemas entre todos os trabalhadores autónomos de TI de Maputo. As fontes nacionais e internacionais oferecem enquadramento sobre sectores e contextos diferentes, enquanto as entrevistas permitem discutir experiências dos participantes entrevistados sem pretensão de representatividade estatística.

### 3.1.4 Quanto aos procedimentos

Os procedimentos foram organizados em **três componentes complementares**.

A primeira compreendeu **pesquisa bibliográfica e análise documental** de estudos científicos, relatórios institucionais, documentos normativos pertinentes, guias técnicos e referências de plataformas digitais. Essa componente constituiu a **base principal** para identificar problemas, ponderar alternativas e derivar uma especificação de necessidades, regras e requisitos. Os limites das fontes foram considerados na análise: uma conclusão sobre um grupo de trabalhadores de outro país ou sobre o sector informal nacional não é automaticamente aplicável aos profissionais de TI entrevistados na Cidade de Maputo.

A segunda consistiu na utilização de **entrevistas semiestruturadas de carácter exploratório**, cujo guião temático e as transcrições literais são previstos nos anexos. As entrevistas foram consideradas **subsidiariamente**, quando os relatos ilustram uma necessidade previamente enquadrada, introduzem uma condição prática ou apresentam um ponto de vista divergente. O método não procura derivar cada requisito directamente de uma resposta nem comprovar que todos os participantes desejam a mesma funcionalidade.

A terceira compreendeu **especificação e modelação da solução, prototipagem incremental e verificação técnica**, separando o domínio proposto das capacidades realmente implementadas. Diagramas e requisitos correspondem a artefactos de engenharia; apenas ensaios com resultados registados sustentam afirmações sobre execução de funcionalidades.

## 3.2 Técnicas de recolha de dados

### 3.2.1 Pesquisa bibliográfica e análise documental

A pesquisa bibliográfica contemplou literatura sobre trabalho autónomo mediado por plataformas digitais, descoberta de oportunidades, gestão algorítmica, competência profissional, confiança, remuneração, reputação, governação e fundamentos de engenharia de software. A análise documental considerou fontes institucionais e técnicas relacionadas com o contexto moçambicano e com a especificação de requisitos, incluindo publicações da Organização Internacional do Trabalho, do Banco Mundial, do Instituto Nacional de Estatística e do Banco de Moçambique, assim como documentação de sistemas comparáveis e referências técnicas pertinentes.

A consulta orientou-se pelo **problema de investigação** e procurou distinguir quatro classes de informação: **(i)** contexto e mecanismos descritos pelas fontes; **(ii)** riscos, limitações e alternativas relevantes para o modelo; **(iii)** opções de concepção e requisitos candidatos, formulados pela investigadora; e **(iv)** aspectos que necessitam de validação posterior por implementação, teste ou avaliação com pessoas.

Esta separação é necessária porque a literatura não determina automaticamente o desenho de uma aplicação específica. Por exemplo, a identificação de efeitos de rede e de mecanismos de avaliação na literatura sobre plataformas digitais justifica considerar descoberta e reputação na especificação, mas **não impõe selecção algorítmica obrigatória, avaliação unilateral ou testes técnicos universais**. Do mesmo modo, as publicações de inclusão financeira contextualizam pagamentos digitais, sem estabelecer por si só que o protótipo possa custodiar fundos.

A **rastreabilidade principal** é expressa como `fonte documental → problema/alternativa → necessidade N → decisão de especificação → RN/RF/RNF`. As referências das entrevistas constituem uma coluna **facultativa de apoio ou contraste**, não a origem necessariamente exclusiva desses elementos. A identificação bibliográfica e o alcance das fontes foram auditados por tema na matriz documental, ficando a página exacta de algumas edições sujeita a conferência final.

### 3.2.2 Entrevistas semiestruturadas e corpus qualitativo complementar

A investigação utilizou **entrevistas semiestruturadas** para obter perspectivas de trabalhadores autónomos de TI e empregadores ou contratantes acerca do contacto entre as partes, demonstração de competências, negociação e formalização, pagamentos e mecanismos de confiança. O instrumento tinha **cinco blocos orientadores**, permitindo perguntas abertas e de aprofundamento relacionadas com a experiência do participante. O guião e as transcrições serão apresentados nos anexos da monografia, não reproduzidos integralmente no corpo dos capítulos.

O documento de recolha disponibilizado contém **onze transcrições com perguntas e respostas**, identificadas como **T01–T08** (oito trabalhadores autónomos de TI) e **E01–E03** (três empregadores ou contratantes). A ficha do documento identifica **Julho a Setembro de 2024** como período de realização, em **modalidade presencial**, na área de Maputo. A mesma ficha caracteriza a selecção como de **conveniência e intencional** e inclui diferentes perfis profissionais e de contratação; a descrição dos critérios e canais concretos de recrutamento deve limitar-se ao que foi efectivamente documentado, sem converter a diversidade dos perfis em representatividade estatística.

O responsável pela revisão confirmou que o ficheiro entregue constitui a **versão não editada das transcrições literais**. Assim, as perguntas e respostas aí registadas são a fonte textual primária disponibilizada para a análise. Esta confirmação não deve ser alargada para alegar que as transcrições foram conferidas com gravações áudio, que houve consentimento escrito ou que todas as decisões de codificação foram verificadas por avaliador externo, pois esses procedimentos não estão comprovados no material consultado.

A documentação histórica contém também um ficheiro denominado **«Piloto de Entrevistas — Dados Sintéticos»**. Esse material não é considerado entrevista efectivamente realizada nem utilizado como evidência de depoimentos humanos; a análise e o anexo devem utilizar exclusivamente o **corpus de transcrições literais** confirmado, com os seus códigos T/E.

A ficha inicial do documento recebido inclui uma secção intitulada **«Inquérito Estruturado»**. Por decisão metodológica expressa da revisão, **não se utilizam questionários nesta investigação**. Essa secção histórica fica excluída da descrição do procedimento realizado, dos resultados e dos anexos da versão final. Não se apresentam percentagens, conclusões estatísticas nem uma alegada validação quantitativa baseada nesse instrumento.

## 3.3 Técnicas de análise de dados

O tratamento das fontes documentais foi orientado para identificar conceitos, mecanismos, riscos e alternativas que fundamentam a concepção da solução. As necessidades e requisitos foram organizados através da análise do conteúdo pertinente das fontes e de decisões de engenharia explicitadas na especificação, com rastreabilidade entre a fundamentação, os elementos de domínio e os critérios de verificação.

As entrevistas semiestruturadas foram utilizadas para **análise qualitativa temática complementar**. As unidades de análise correspondem a respostas ou segmentos de depoimento com significado para as dimensões consideradas na investigação. Os temas trabalhados na D44 compreendem descoberta de oportunidades, evidências de competência, confiança bilateral, condições de acordo, alterações, pagamentos, reputação, conflitos, localização e adopção. A análise procura conservar o contexto dos relatos e distinguir situações semelhantes de casos divergentes.

O exame dos depoimentos não serve para atribuir prevalência populacional aos problemas. O número de participantes referido corresponde ao corpus qualitativo disponibilizado; a repetição de um tema pode ser descrita apenas como observação interna desse corpus, não como estimativa sobre o mercado de TI em Maputo. Também não é adequado afirmar **saturação teórica, dupla codificação, software específico de análise ou validação das transcrições pelos participantes** sem documentação de que tais procedimentos ocorreram.

Para tornar o procedimento auditável, os vínculos entre **documentos, decisões e necessidades** deverão ser acompanhados, quando pertinente, por uma referência ao **código do entrevistado e à pergunta/resposta no anexo**. Uma funcionalidade mencionada por um participante não é automaticamente adoptada; e a ausência de comentário numa entrevista não invalida um requisito devidamente justificado por fonte documental, norma ou necessidade técnica do sistema.

### 3.3.1 Triangulação e derivação de necessidades e requisitos

As fontes bibliográficas e documentais foram confrontadas com os **relatos qualitativos complementares**, procurando convergências, diferenças e limites das decisões consideradas na concepção. Nesta monografia, tal confronto significa **comparar informação de natureza distinta** para melhorar a fundamentação de algumas opções de engenharia. A utilização do termo «triangulação» não implica a existência de amostras independentes representativas, de triangulação estatística ou de uma comprovação causal da eficácia do protótipo.

A **derivação principal das necessidades e requisitos** assenta na análise documental e no modelo de solução concebido. A interpretação dos relatos T/E acrescenta contexto onde existe uma relação clara: T03/T06 ilustram preço que pode depender de diagnóstico; T05/E02 esclarecem a utilidade do histórico de alterações; T05 relativiza a ideia de dificuldade universal de captação de clientes; e T02/T04/E01 apresentam interesse por **escrow**, em divergência com a opção de não custódia própria de fundos no protótipo. Os exemplos não constituem instruções de implementação nem substituem a fundamentação técnica ou normativa.

A correspondência entre necessidades N01–N18, regras RN01–RN16 e requisitos RF01–RF28 e RNF01–RNF07 representa uma **matriz de rastreabilidade da especificação**, sujeita a revisão e aprovação. Parte dos requisitos, como autenticação, controlo de acesso, segurança e auditoria administrativa, surge de exigências técnicas ou de governação, não de declarações literais de entrevistados. Os ensaios do protótipo são referidos separadamente e não alteram retroactivamente a origem dos requisitos.

## 3.4 População e amostra

A população de interesse corresponde a **trabalhadores autónomos de Tecnologias de Informação e empregadores ou contratantes na Cidade de Maputo**. A componente qualitativa complementar utiliza onze entrevistas semiestruturadas constantes do documento disponibilizado, identificadas por códigos pseudónimos: **oito trabalhadores (T01–T08)** e **três empregadores ou clientes (E01–E03)**.

A ficha metodológica caracteriza a selecção como de **conveniência e intencional** e inclui profissionais de desenvolvimento web, UI/UX, redes e suporte, desenvolvimento mobile, full-stack, hardware e manutenção e dados/automação, além de contratantes de serviços de TI. A heterogeneidade procura oferecer **exemplos de modalidades de contratação**, mas não representa amostragem probabilística nem permite estimar as preferências ou dificuldades da população de Maputo. As características e os procedimentos de selecção foram descritos até ao nível registado na ficha; não se pressupõe documentação adicional de convites, recusas ou taxas de resposta.

Os códigos T/E são utilizados para **evitar expor nomes e contactos pessoais**, mas pseudonimização não equivale a anonimização completa quando a profissão, a data e o contexto permitam reconhecimento indirecto. A apresentação de depoimentos integrais nos anexos deverá ser revista quanto às condições de partilha, confidencialidade e consentimento efectivamente estabelecidas no trabalho, sem presumir aprovação ética formal ou autorização de gravação não demonstradas.

## 3.5 Modelo de desenvolvimento do sistema

O desenvolvimento do protótipo adoptou uma **abordagem incremental, orientada por requisitos**, na qual a especificação foi traduzida em modelos de domínio, casos de uso, regras de negócio, arquitectura e conjuntos verificáveis de funcionalidades. A sequência conceptual abrange identificação de actores e requisitos, modelação UML, construção do frontend/backend e testes técnicos de partes do fluxo. Esta organização permite distinguir capacidades **especificadas**, **implementadas** e **testadas**.

A concepção prevê uma aplicação web em camadas, com interface React/TypeScript e serviços Django/Django REST Framework. O domínio proposto inclui contas com perfis de trabalhador e empregador, oportunidades e propostas, relações de contratação, versões das condições acordadas, execução e entrega, condições e estados de pagamento, reputação, conflitos e governação. Nem todos os elementos do modelo conceptual foram materializados num backend funcional.

Em revisões técnicas posteriores à versão inicialmente auditada da monografia, **branches de desenvolvimento** introduziram entidades e serviços reais para oportunidades, propostas, contratações e acordos versionados, integrando-os numa rota específica do frontend. A possibilidade de acumular perfis sem permitir autocontratação, a exigência de duas aceitações expressas das condições e a preservação da versão vigente quando uma alteração é rejeitada representam **decisões de engenharia** executadas em parte do protótipo. Estas revisões permanecem identificadas por ramo/commit e não devem ser apresentadas como funcionalidades disponibilizadas na branch principal ou em produção.

As etapas de desenvolvimento e os cenários técnicos são apresentados com resultados e limitações no Capítulo V. A correspondência entre um diagrama e uma entidade de código deve ser verificada; a existência de uma figura UML não demonstra que a operação esteja implementada.

## 3.6 Tecnologias e ferramentas

O frontend foi desenvolvido com **React, TypeScript, Vite e Tailwind CSS**. O backend recorre a **Python, Django e Django REST Framework**, com autenticação JWT. Para modelação e comunicação de arquitectura foram utilizados diagramas UML, enquanto os ensaios técnicos de API e interface são registados mediante frameworks de testes associados às respectivas revisões.

A arquitectura de referência prevê uma base de dados relacional **PostgreSQL**. Contudo, os ensaios automatizados documentados para as revisões D50–D56 utilizaram **SQLite temporário**, pelo que não comprovam comportamento de concorrência, desempenho ou persistência da solução em PostgreSQL. Da mesma forma, os fluxos ainda baseados em dados simulados na interface legada não são descritos como processos reais da API Django.

As tecnologias e os frameworks constituem instrumentos de implementação; a sua mera utilização não demonstra a conformidade com requisitos de segurança, privacidade, usabilidade, qualidade em produção ou validade jurídica dos acordos.

## 3.7 Procedimento de validação

O procedimento de validação estabeleceu **oito cenários de aceitação funcional (V01–V08)** associados aos requisitos e **sete verificações não funcionais (RNF01–RNF07)**. O protocolo define passos, actores, dados e resultados esperados. A sua especificação, por si só, constitui **planeamento**, não aprovação ou execução completa dos casos.

Uma etapa técnica posterior produziu registos reproduzíveis de testes de API Django/Django REST Framework, testes do cliente HTTP React e ensaios de integração em browser Chromium com React e Django reais. Nos ramos de desenvolvimento D50–D56, os ensaios exerceram **subconjuntos de V01–V03**: registo e perfis, publicação e proposta, início de contratação, aceitação e alterações versionadas de acordo. Os **casos canónicos V01–V03 permanecem apenas parcialmente exercitados**, pois não foram cumpridos todos os critérios definidos no Quadro A.2.

Os cenários **V04–V08 não foram executados integralmente como casos de aceitação**: V04 refere-se a **execução, entrega e histórico do serviço**, não a versionamento de acordos; V05 abrange pagamentos; V06 reputação; V07 conflitos; e V08 verificação e governação. A presença de elementos de interface simulados, a activação de um acordo ou testes isolados de permissões não autorizam classificar esses cenários como aprovados.

Nas verificações não funcionais, há cobertura técnica **parcial** de autorização, privacidade, integridade e responsividade (RNF02–RNF05), mas não execução integral de todos os respectivos protocolos. O RNF01, que exige usabilidade avaliada com participantes, não foi executado conforme o critério da D44; o mesmo se aplica às verificações específicas RNF06 e RNF07. Testes automatizados de navegação e visualização não substituem observação de pessoas reais.

Os resultados reportados são circunscritos às **revisões de código em branches de desenvolvimento**, com contas sintéticas e ambiente de teste; não descrevem um sistema publicado, o cumprimento integral de normas de segurança ou a eficácia da aplicação no mercado. A validação técnica demonstra apenas comportamentos efectivamente observados nos ensaios realizados. A avaliação científica das hipóteses distingue, por isso, **fundamentação documental**, **apoio qualitativo das entrevistas**, **requisito especificado**, **funcionalidade executada** e **resultado de aceitação**, sem os tratar como equivalentes.

---

## Notas de integração editorial (NÃO inserir no corpo final)

1. **Estrutura:** manter IDs de todas as secções da D44 (3.1–3.7, subsecções originais). Títulos foram conservados em termos gerais; não criar uma nova técnica de recolha não prevista.
2. **Anexo:** guião e onze transcrições literais **ainda não constam da D44 original**; remissões devem ser verificadas depois da inserção. Ver [D61 plano](D61_PLANO_ANEXOS_TRANSCRICOES.md).
3. **Método:** não dizer que as entrevistas foram «editadas/reorganizadas» ou «perdidas», pois o responsável rectificou esses pressupostos e confirmou transcrições literais não editadas ([D60](D60_CONFIRMACAO_TRANSCRICOES_LITERAIS.md)).
4. **Registos históricos:** o ficheiro inicial de 21 páginas ainda contém **questionário** nas pp. 1–5; **excluir** do instrumento e dos resultados adoptados, conforme D59, sem eliminar involuntariamente o início da entrevista T01 na p.5.
5. **Amostragem:** o documento declara «conveniência e intencional» e «presencial»; não afirmar que os procedimentos de recrutamento, consentimento ou gravação estão independentemente comprovados. Diversidade de especialidades **não significa representatividade**.
6. **Triangulação:** manter numeração §3.3.1 e explicar o sentido restrito de confronto documental/qualitativo; não declarar validação independente ou saturação sem fonte.
7. **Cap. I:** §§1.6–1.7 da D44 ainda dizem que não foram encontradas entrevistas reais. **Exigem correcção coordenada** antes da integração do Capítulo III; ver mapa D64.
8. **Cap. V:** V01–V03 parcial e V04–V08 não executados; basear-se na [matriz D57](D57_MATRIZ_VALIDACAO_V01_V08_RNF.md), não no estado de validação inicialmente descrito em 2025.
9. **Cronologia:** a D44 apresenta capa de Setembro de 2025, ao passo que o projecto inclui referências e ensaios técnicos de 2026. Resolver o histórico de revisão; não atribuir testes de 2026 à execução de 2025.
10. **Fonte documental:** citações bibliográficas exactas e páginas precisam de reconciliação final conforme [D62](D62_AUDITORIA_FONTES_DOCUMENTAIS_N01_N18.md), sem criar fontes normativas adicionais que não foram consultadas.
11. **Word:** texto Markdown apenas; o DOCX canónico permanece inacessível em bytes originais e não foi editado, renderizado nem entregue como versão consolidada.
