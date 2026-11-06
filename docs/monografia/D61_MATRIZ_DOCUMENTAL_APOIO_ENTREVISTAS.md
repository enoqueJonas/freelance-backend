# D61 — Matriz de apoio qualitativo subsidiário à fundamentação documental dos requisitos

> **AUDITORIA D62 (06-11-2026):** fontes oficiais da OIT, Banco Mundial, Banco de Moçambique, INE, ISO, OMG, OWASP e Upwork foram confrontadas com os grupos N01–N18. **Não considerar um problema documentado prova de uma solução técnica obrigatória.** Ver [matriz documental verificada D62](D62_AUDITORIA_FONTES_DOCUMENTAIS_N01_N18.md) e [emendas dos capítulos II/IV](D62_EMENDAS_CAPITULOS_II_IV.md). Os vínculos de engenharia que não são prescritos pelas fontes continuam decisões da autora e necessitam de justificação específica.

**Estado:** matriz candidata de rastreabilidade e análise de conteúdo; **não integrada na D44** e não constitui aprovação dos requisitos nem teste de aceitação.  
**Decisão de autoria (06-11-2026):** reproduzir a função metodológica adoptada na monografia de Xitique/Blockchain: **análise bibliográfica/documental como fundamento principal dos requisitos**; entrevistas semiestruturadas utilizadas **subsidiariamente**, para apoiar ou problematizar decisões específicas; **transcrições no anexo**, sem transformá-las no eixo da argumentação.  
**Fonte qualitativa:** `Estudo_de_Mercado_Entrevistas_e_Inquerito_TI_Maputo(1).docx`, 21 páginas, SHA-256 `e85420e8d306c3914028fd75f24e56624d90d0df649e916ce9a49c6025a3e64f`. O responsável confirmou que os blocos T01–T08/E01–E03 constituem **transcrições literais não editadas**. Para análise: **somente a secção «Entrevistas realizadas»**, pp. 5–21. As secções de inquérito, pp. 1–5, ficam excluídas por decisão D59.  
**Fonte de requisitos:** matriz actual da D44 e [rastreabilidade D45](MATRIZ_N01_N18_RASTREABILIDADE_D45.md), a qual é **associação interpretativa do auditor**, não aprovação formal.  
**Referência de método:** monografia blockchain/Xitique canónica, Capítulo 3 §§3.1.2, 3.1.4 e 3.2.1–3.2.2 (pp. impressas 48–50), Capítulo 9 («ANEXOS»): as fontes bibliográficas/documentais orientam a especificação; fichas de entrevistas contextualizam **alguns** requisitos, sem demonstrar que todos tenham origem em entrevistas.

## 1. Hierarquia de evidências e atribuição causal

**Ordem obrigatória da narrativa académica:**

1. **Documento/literatura:** delimita o problema, os mecanismos que o abordam, riscos, normas e alternativas técnicas. Fonte primária **da fundamentação dos requisitos** — com obra, edição e **página/trecho conferido**; não basta colocar uma lista de autores na bibliografia.
2. **Decisão de engenharia e especificação:** traduz o problema em necessidade N, regra RN, requisito RF/RNF e critério de aceitação. O facto de um documento mencionar um risco não impõe uma solução única. Justificar escolhas e exclusões.
3. **Entrevista semiestruturada (complementar):** dá contexto local **a algumas decisões**, ilustra casos de utilização ou introduz divergências. Um testemunho não obriga a criar RF e não prova eficácia da solução.
4. **Protótipo e testes:** demonstram comportamento técnico, não a origem ou adequação sociológica do requisito. D50–D56 são verificações de engenharia num ambiente de ensaio.
5. **Discussão crítica:** enuncia o alcance da documentação, dos relatos e dos resultados técnicos, sem misturar amostragem qualitativa com prevalência populacional ou inferência causal sobre fraudes.

**Trilho preferido:** `Documento (autor/ano/recorte) → problema/decisão → N → RN/RF/RNF → implementação/teste`; quando existe apoio adequado, adicionar `↳ ENT Txx/Exx, pergunta/localizador, função [apoio/contexto/contraexemplo]`. Uma linha de RF sem entrevista é **legítima**. Também pode existir um achado de entrevista sem RF novo.

**Marcadores usados:** `DOC` = fundamentação documental a especificar/confirmar em fonte; `ENG` = decisão de engenharia; `ENT` = apoio qualitativo da transcrição; `TECH` = teste de software. Não trocar estes marcadores por «validado com utilizadores».

## 2. Matriz selectiva de apoio das entrevistas

As colunas `N / RN / RF` são associações **candidatas**, herdadas da D44/D45 e a confirmar com a autora. Os **localizadores são páginas físicas do ficheiro recebido**, não do Word canónico. Os resumos de conteúdo abaixo são **paráfrases analíticas**; citações literais, quando usadas no manuscrito, devem ser copiadas **exactamente** do original com identificação e devida autorização.

| Tema documental principal a ancorar | Decisão/requisito já proposto | Apoio qualitativo **selectivo** e localização | Tipo de contribuição | Limite e cuidado |
|---|---|---|---|---|
| Plataformas digitais: descoberta e transparência dos canais | N01/N04 → RF07–RF10 (pesquisa, publicação, consulta) | **T01**, pp. 5–6: referências e anúncios; **E01**, p. 17: indicações pessoais; **T05**, pp. 12–13: **não** precisa de captar novos clientes | **Contexto + caso divergente** | Não concluir que todos os freelancers têm dificuldade de encontrar trabalho; a pesquisa é opção de suporte, não garantia de novos clientes |
| Confiança e credenciais: diferentes meios de demonstrar competência | N02 → RN03 → RF03/RF05 (perfís/evidências) | **T01**, pp. 6–7: GitHub insuficiente em caso confidencial; **T03**, pp. 9–10: certificações/referências e restrição de imagens; **T06**, p. 13: experiência prática sem certificação universal; **E01**, p. 17: portfólio não verificável | **Complementaridade e diversidade de meios** | Não impor portfólio público, prova fotográfica ou certificação obrigatória a todas as especialidades; verificar protecção de dados |
| Segurança e controlo de identidade: autorização proporcional | N03 → RN15 → RF04/RF06/RF28 (perfis/verificação) | **T03**, p. 10: desconhecidos e deslocação; **T07**, p. 15: denúncias de solicitações abusivas | **Caso de risco relatado** | A verificação de identidade é uma medida proposta; não comprova eliminação de fraude e requer minimização de dados |
| Escopo/alterações: rastreabilidade e aceitação | N05/N06 → RN05/RN06/RN14 → RF13/RF14, RNF04 | **T01**, pp. 6–7: acréscimos ao website e negociações; **T05**, p. 12: aprovações dispersas; **T06**, p. 14: custo adicional de reparação só após aceitação; **E02**, p. 19: atraso após revisões informais | **Apoio forte a regra de aceitação de alterações** | A tecnologia `AgreementVersion` e a exigência de duas aceitações são **decisões de engenharia** a justificar, não palavras dos participantes |
| Condições diferenciadas por diagnóstico técnico | N05/N15 → RN08/RN09 → RF13/RF18 | **T03**, pp. 9–10: avaliação presencial antes de orçamento; **T06**, pp. 13–14: diagnóstico de equipamento e preço final posterior | **Caso concreto que afasta preço fixo universal** | A modalidade «preço após diagnóstico» precisa de dados/regras e teste de formalização final; a flag técnica não completa o processo |
| Formalização proporcional e sem assinatura universal | N07 → RN05/RN07 → RF13/RF17 | **E02**, p. 19: para trabalhos rotineiros considera suficiente aceitação digital registada; **E03**, pp. 20–21: acordo simplificado para serviços pequenos | **Delimitação de peso burocrático** | Aceitação na UI não é automaticamente assinatura qualificada nem validação jurídica |
| Risco de pagamento versus escopo real | N09/N10 → RN09/RN10 → RF18/RF19; RF20 facultativo | **T02**, p. 9, **T04**, p. 11, e **E01**, p. 18, defendem em contextos específicos **escrow/custódia**; **E02**, p. 19, explica exigências bancárias/contabilísticas | **CONTRASTE entre preferência relatada e escolha de escopo** | **RN10 sem custódia própria** é decisão de arquitectura/risco legal e operacional; não alegar que entrevistados rejeitaram escrow; sem PSP ou prova de redução de risco |
| Reputação bilateral, contexto e contestação | N11/N12 → RN11/RN12 → RF21–RF23 | **T01**, p. 7 e **E01**, p. 18: bilateralidade; **T02**, p. 9: receio de retaliação; **E02**, p. 19: comentários e contraditório; **E03**, p. 21: contexto além das estrelas | **Apoio com alerta de equidade** | Não demonstrado que avaliações realmente aumentam confiança; RF21–RF23 não executados no backend D50–D56 |
| Conflitos e prova digital sem arbitragem automática | N13/N14 → RN13/RN14 → RF24/RF25 | **T08**, pp. 16–17: preservação de evidências; **E02**, pp. 19–20: avaliação técnica pode exigir perito; **E03**, p. 21: necessidade de apoio em atrasos | **Delimitação de função administrativa** | Nunca equiparar rejeição de versão de acordo a caso de disputa nem atribuir poderes de arbitragem à aplicação |
| Simplicidade, limites de automação e condições de adesão | N17/N18 → RNF01 (N18 **sem RF**) | **T05**, pp. 12–13: rejeita notificações em excesso/taxas/burocracia; **T04**, p. 11: não quer matching que impeça escolha manual; **E03**, p. 21: custos, navegação e número de profissionais | **Contraexemplos e limites de desenho** | Nenhum desses relatos prova a usabilidade do protótipo; N18 exige participação real na plataforma, não funcionalidade fictícia |

### Decisões deliberadamente **não imputadas** às entrevistas

- **RF01/RF02 autenticação/JWT, RNF02 autorização, RNF03 privacidade, RNF04 integridade:** base principal de arquitectura, normas, riscos e governação. As entrevistas podem contextualizar confiança, mas não prescrever JWT, hashes ou estratégias de segurança.
- **RN02 prevenção de autocontratação:** regra de integridade/consistência de actores, não preferência empírica demonstrada.
- **RN10 ausência de custódia própria de pagamentos:** opção de âmbito e responsabilidade operacional; explicitamente **em tensão** com apoio de T02/T04/E01 a escrow. Precisa de fundamentação documental/regulatória concreta e não de atribuição fictícia ao campo.
- **RF26–RF28 moderação/administração e RN16 auditoria:** governação e segurança; entrevistas não sustentam, por si, permissões administrativas detalhadas.
- **Integração obrigatória de chat, geolocalização para todos, testes técnicos obrigatórios e matching exclusivo:** **não derivar** de um desejo isolado; existem contraexemplos no corpus.

## 3. Textos candidatos para a ConecTA, seguindo o precedente blockchain

### §3.1 — Quanto à abordagem/procedimentos

> A investigação adoptou uma abordagem predominantemente qualitativa, de natureza aplicada e carácter exploratório. A **revisão bibliográfica e a análise documental constituíram o fundamento principal da identificação e especificação dos requisitos**, mediante exame de literatura científica, relatórios institucionais, princípios de engenharia de software e práticas associadas às plataformas digitais de trabalho. Complementarmente, foram consideradas **entrevistas semiestruturadas** com trabalhadores autónomos de TI e empregadores, cujos registos constam dos anexos. As entrevistas foram utilizadas para contextualizar práticas locais, ilustrar necessidades pontuais, identificar situações divergentes e discutir decisões de concepção, **não como origem exclusiva ou validação universal dos requisitos**. Os resultados técnicos do protótipo foram avaliados separadamente por testes automatizados em ambiente controlado, sem equivalerem a avaliação de impacto sobre o mercado.

### §3.2.1 — Procedimento de recolha de informação

> O levantamento bibliográfico e documental foi utilizado para caracterizar o contexto da contratação de serviços de TI, os desafios das plataformas digitais de trabalho e os mecanismos de confiança, formalização, gestão de pagamentos e governação. A elaboração dos requisitos funcionais e não funcionais partiu da análise dessas fontes e da delimitação do modelo proposto. Alguns requisitos foram **complementarmente relacionados** com experiências descritas nas entrevistas semiestruturadas, sem que essa correspondência constitua prova de que tenham surgido originalmente das entrevistas. O estudo qualitativo reuniu onze transcrições identificadas como T01–T08 e E01–E03; a ficha de recolha situa as entrevistas entre Julho e Setembro de 2024, em modalidade presencial. A transcrição entregue foi identificada pelo responsável como literal e não editada. O processo de registo e os procedimentos de consentimento serão descritos conforme a documentação efectivamente disponível, não presumidos.

### §3.2.2 — Tratamento e análise dos dados

> A análise foi realizada em duas vertentes. Na primeira, as fontes documentais foram interpretadas e relacionadas com problemas, normas e decisões técnicas relevantes para o sistema; a fundamentação dos requisitos foi registada de forma rastreável. Na segunda, as transcrições das entrevistas foram examinadas qualitativamente para identificar exemplos convergentes e divergentes sobre captação de oportunidades, demonstração de competências, alterações contratuais, modalidades de pagamento e confiança. Os registos das entrevistas foram **utilizados como apoio interpretativo** para necessidades seleccionadas, não como base de estimativas estatísticas. A correspondência entre documento, necessidade, requisito e eventual relato de entrevista foi tratada como uma decisão de rastreabilidade que exige justificação, e não como certificação automática de eficácia da solução.

### Capítulo IV — apresentação equilibrada

> A análise do contexto da contratação de profissionais autónomos de TI baseia-se primordialmente na revisão bibliográfica e documental. As entrevistas semiestruturadas, apresentadas nos anexos, fornecem ilustrações qualitativas de situações específicas relevantes para o modelo: variação da evidência de competência entre especialidades; orçamento após diagnóstico em serviços de manutenção; registo de alterações ao âmbito; formalização proporcional e risco bilateral em pagamentos. As divergências são igualmente consideradas, incluindo profissionais que não dependem de plataformas para captar clientes, reservas quanto à obrigatoriedade de testes técnicos e preferência por custódia de fundos, não adoptada no âmbito do protótipo. Esses relatos **não demonstram a prevalência** dos problemas no mercado de Maputo nem a eficácia futura das funcionalidades propostas.

### §5.2.8 — regra de rastreabilidade

> A especificação foi estruturada a partir das fontes documentais e das decisões de engenharia, relacionando necessidades N01–N18, regras RN01–RN16, requisitos RF01–RF28 e critérios de verificação. Algumas relações receberam **suporte qualitativo complementar** de entrevistas semiestruturadas, com referência aos respectivos códigos e excertos no anexo. A ausência de entrevista directamente associada a um requisito não o invalida quando existe justificação documental, normativa ou técnica suficiente. Da mesma forma, a sugestão de uma funcionalidade por um participante não obriga à sua inclusão nem demonstra que a solução esteja validada.

### §5.5 e Capítulo VI — limite da inferência

> A investigação apresenta uma proposta de especificação e um protótipo de contratação parcialmente executado em ambiente de teste. A análise documental fundamentou as decisões principais; as entrevistas permitiram contextualizar algumas delas e evidenciar alternativas ou constrangimentos locais. As verificações técnicas demonstraram o comportamento de determinados fluxos da aplicação, mas não comprovam, isoladamente, eficácia no mercado, diminuição de fraudes, satisfação de utilizadores ou aprovação integral dos requisitos. O contributo académico deve ser apreciado pela coerência da fundamentação, pela rastreabilidade das decisões e pelos resultados efectivamente demonstrados.

**Importante:** textos candidatos, não relatos de procedimentos ainda não auditados. A autoria deve rever a adequação de tempos verbais e a correspondência com a prática realizada antes de os inserir no Word.

## 4. Como referenciar os anexos sem sobrecarregar o Capítulo IV

- Corpo do texto: uma ou duas referências de entrevista **por decisão de requisito cuja contextualização seja relevante**; não repetir cada pergunta/resposta nem criar secção extensa de análise qualitativa que substitua a revisão documental.
- Exemplos de remissão: `(T03 e T06; ver Anexo de Entrevistas, secções T03 e T06)` ou `(E02; ver Anexo de Entrevistas, secção E02)`.
- No anexo: preservar **literalmente** a pergunta e a resposta, sob T01–T08 e E01–E03; não introduzir paráfrases no bloco rotulado «transcrição literal».
- Não anexar como instrumento aplicado o inquérito estruturado do draft. O documento recebido inclui perguntas de questionário em páginas introdutórias que **não pertencem ao método vigente**; o anexo da monografia deve conter apenas o guião de entrevista efectivamente usado e as transcrições.
- Separar o anexo de dados da **matriz de auditoria técnica**: a última pode permanecer num relatório de trabalho, evitando mais uma grande tabela dentro da monografia.
- Não reproduzir transcrições completas num repositório público sem conferir confidencialidade, consentimentos e regras institucionais. O ficheiro original mantém-se como fonte controlada, identificado por checksum.
- Não transportar **dados, participantes, requisitos ou pressupostos de Xitique** para a ConecTA. Reutilizar somente a **estrutura de argumentação documental + apoio qualitativo + anexo**.

## 5. O que falta validar antes do Word definitivo

- [x] Confirmar a metodologia relativa: **documental principal, entrevistas subsidiárias**, conforme instrução da autoria e precedente blockchain.
- [x] Identificar nas 11 transcrições casos específicos e contraexemplos, com páginas e códigos, sem publicar respostas integrais.
- [x] Separar decisões derivadas de normas/engenharia de preferências dos participantes.
- [ ] Conferir e indicar **trecho/página de cada fonte documental** efectivamente consultada que sustenta as decisões de requisito. A lista bibliográfica da D44 identifica fontes, mas **não prova** de forma automática qual recomendação técnica vem de cada uma.
- [ ] Confrontar as ligações N/RN/RF da matriz D45 com a baseline aprovada e os casos de uso reais; estas ligações continuam candidatas.
- [ ] Conferir consentimento/anonimização e critérios de inclusão dos registos antes de anexar integralmente as transcrições à versão divulgada.
- [ ] Integrar apenas o guião de entrevista e os onze depoimentos literais no **anexo da D44 canónica**, com paginação, remissões e normas institucionais, quando houver acesso aos bytes originais.
- [ ] Rever Capítulos III–VI para eliminar inferências de que as entrevistas são a fonte principal dos requisitos, alegações de questionários e menções de validação generalizada.

**D61 não altera o DOCX canónico** e não substitui as verificações técnicas D50–D56. O critério de sucesso é **coerência metodológica e atribuição de fonte**, não o número de entrevistas citadas.
