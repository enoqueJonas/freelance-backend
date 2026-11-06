# Auditoria editorial D45 — Índice, referências, terminologia e linguagem de proveniência

**Base:** `Monografia_D44_Metodologia_Proveniencia_Verificada.docx` (82 páginas; texto extraído, sem renderização do ficheiro original).  
**Data de auditoria:** 02-11-2026.  
**Estado:** registo editorial e propostas de substituição; **não** é prova de alteração ao DOCX nem de resolução dos comentários do supervisor.

## 1. Erros e incoerências de edição verificados

| ID | Localização (página do ficheiro D44) | Texto/facto constatado | Acção controlada | Classificação |
|---|---|---|---|---|
| ED-01 | p. 5, cabeçalho do índice | `ĺNDICE` (carácter «ĺ», letra l com acento agudo, em vez de «Í», I maiúsculo com acento agudo) | Corrigir **`ÍNDICE`** e rever o estilo do título | Correcção certa |
| ED-02 | p. 2 e p. 4 | Supervisor identificado como `Ataíde Gildo Pais Chilaúle` vs. `Ataíde Gildo Pais Chilaule` | Uniformizar após confirmação de grafia institucional, sem inventar acento ou grau académico | Exige confirmação |
| ED-03 | p. 4, declaração | «que submeto **a** Universidade São Tomás de Moçambique» | Substituir por «que submeto **à** Universidade São Tomás de Moçambique»; rever pontuação e sintaxe sem alterar o sentido da declaração | Correcção certa |
| ED-04 | pp. 1, 2, 4 e 67 | «Setembro de 2025» no frontispício e declaração, mas referência bibliográfica ao relatório do Banco de Moçambique publicado em 2026 | Confirmar cronologia real de elaboração/revisão/submissão; alterar a data da versão entregue apenas após validação académica | Bloqueio cronológico |
| ED-05 | pp. 46, 49, 50 e 80 | «baseline aprovada», «modelo ... aprovado», «requisitos aprovados», «especificação conceptual aprovada» | Se não houver acta/sign-off, substituir por «baseline consolidada», «modelo conceptual especificado», «requisitos definidos», «especificação conceptual adoptada para o estudo» | Qualificar alegação |
| ED-06 | p. 50, legenda Figura 5.2 | Fonte incorporada na própria legenda entre parênteses, sem linha distinta «Fonte:» | Após verificar formatação do DOCX, separar **legenda** e **fonte** conforme padrão de quadros e outras figuras | Correcção recomendada |
| ED-07 | pp. 5–8 e pp. 20, 44–82 | Índice de capítulos existe; não há entradas de «Lista de Figuras» nem «Lista de Quadros» no texto extraído | Verificar exigência no **manual aplicável** antes de introduzir novas listas; se exigidas, gerar com campos do Word e conferir páginas | Dependente da norma |
| ED-08 | pp. 48–62 | Salto de legendas `Figura 5.4` → `Figura 5.11` e sete `[PLACEHOLDER]` 5.13–5.19 | Já identificado em `UML_ESTADOS_REFERENCIAS_D45.md`; verificar figuras/legendas no Word antes de renumerar | Incidente já rastreado |
| ED-09 | p. 61, §5.3.3 | «ServiPlus» e «ConecTA» explicitamente no corpo da dissertação | Manter evidência da divergência do protótipo sem instituir duas marcas como nomes académicos da solução; a marca pode ser omitida do texto principal, se isso não ocultar a deficiência | Harmonização com integridade |
| ED-10 | pp. 60–62, 80–82 | Quadros longos com colunas estreitas e passagem entre páginas; texto extraído revela palavras/células distribuídas em linhas irregulares | **Não inferir defeito de layout só pela extracção**. Renderizar Word, verificar cortes, títulos, altura das linhas, cabeçalhos repetidos, alinhamento e legibilidade | Verificação visual pendente |

### Redacção da declaração de honra (correcção mínima)

**Original:** «Declaro por minha honra que a presente monografia, que submeto a Universidade São Tomás de Moçambique é fruto do meu trabalho original, declaro que todas as fontes utilizadas foram devidamente referenciadas...»

**Proposta estritamente linguística, sem alterar responsabilidade nem autoria:**

> Declaro, por minha honra, que a presente monografia, submetida à Universidade São Tomás de Moçambique, é fruto do meu trabalho original e que todas as fontes utilizadas foram devidamente referenciadas, em conformidade com as normas estabelecidas para a obtenção do grau de Licenciatura em Desenvolvimento de Software, sob a supervisão do docente Ataíde Gildo Pais [grafia oficial do apelido por confirmar].

**Não** substituir o nome do supervisor por uma forma incerta. Confrontar também a designação oficial da faculdade/curso.

## 2. Regresso inadvertido à linguagem de «entrevistas locais» sem proveniência confirmada

As redacções da D44 que qualificam o corpus como não comprovado são importantes e devem ser preservadas. Contudo, sobrevivem ocorrências que criam a impressão contrária:

| ID | Localização | Trecho original | Proposta para substituição |
|---|---|---|---|
| ED-11 | p. 20, §2.1 | «... ampliar o quadro analítico aplicado às entrevistas locais.» | «... ampliar o quadro analítico utilizado na análise documental e na exploração dos cenários textuais do estudo.» |
| ED-12 | p. 21, §2.2 | «... práticas dos trabalhadores autónomos de TI entrevistados nesta investigação.» | «... práticas de trabalhadores autónomos de TI da Cidade de Maputo, população de interesse cuja caracterização empírica não foi confirmada por entrevistas documentadas.» |
| ED-13 | p. 23, §2.4 | «A selecção dos sinais concretos a apresentar pela aplicação decorre das necessidades recolhidas ...» | «A selecção dos sinais concretos a apresentar na proposta resulta de hipóteses de necessidade derivadas de fontes documentais e cenários exploratórios, a validar junto da população de interesse ...» |
| ED-14 | p. 25, §2.6 | «... cenário a gerir na concepção e a confrontar com as entrevistas ...» | «... cenário a considerar na concepção e a confrontar futuramente com recolha empírica verificável ...» |
| ED-15 | p. 58, §5.2.8 | «... porque a evidência recolhida não sustenta a sua imposição universal.» | «... por não existir justificação documental suficiente para os impor universalmente e por carecerem de validação com utilizadores reais.» |

**Importante:** não eliminar a explicação da origem sintética dos registos. Apenas remover reivindicações indirectas de entrevistas de campo, conservando a limitação metodológica explicita no resumo, capítulos I, III, IV e conclusão.

## 3. Uso de «auditoria» e «repositório» na monografia

A D44 usa o termo «auditoria» em p. 9, 32, 36, 38, 62 e 64. Há ocorrências de «repositório» nas pp. 16, 17, 31 e 32 referentes aos ficheiros de origem (além de «repositórios de código» em contextos tecnológicos legítimos).

**Não é errado mencionar uma análise de proveniência.** Mas a narrativa deve tornar o método **reprodutível** e não parecer uma nota interna de manutenção editorial. Recomendação:

- Manter o facto «existem onze registos cuja recolha independente não está documentalmente demonstrada».
- Referir, no Capítulo III, **quais materiais** foram examinados, seus nomes e papel, critérios para classificação de material sintético e lacunas documentais identificadas, quando isso for eticamente adequado.
- Substituir `A auditoria demonstra que...` (p. 62) por `A inspecção estática do código-fonte identificou...` se o objecto do parágrafo é implementação; reservar «análise de proveniência» para a origem dos registos qualitativos.
- Não converter a falta de comprovação em «entrevistas não realizadas» (não é conclusão logicamente permitida), nem atribuir à investigação consentimentos/actas inexistentes.
- Não remover deliberadamente o histórico de limitações para aumentar artificialmente a impressão de rigor.

## 4. Auditoria do alinhamento entre citações e bibliografia

### ED-16 — Identificador de autor institucional: «OIT» vs. «International Labour Organization»

- Corpo: `OIT (2018)`, `OIT (2021)`, `OIT (2024a)`, `OIT (2024b)`.
- Lista: `International Labour Organization. (2018)/(2021)/(2024a)/(2024b)`.

São referências à mesma instituição, mas a abreviação PT e a forma EN devem estar conectadas mediante uma primeira ocorrência explícita e apresentação consistente segundo o estilo bibliográfico aplicável. Não substituir nomes oficiais de títulos publicados; escolher **uma convenção** para autor institucional e citações.

**Fontes editoriais oficiais de confirmação:**
- Relatório sobre o Quénia: https://www.ilo.org/publications/digital-labour-platforms-kenya-exploring-womens-opportunities-and-0 (04-04-2024).
- Registo institucional do Uganda: https://researchrepository.ilo.org/esploro/outputs/report/Platform-work-in-Uganda-promoting-decent/995619540702676 (2024).
- Repositório ILO do Quénia fornece sete autores individuais e distingue organização editora; o PDF da OIT fornece recomendação de atribuição institucional. Escolher de acordo com as normas aplicáveis, não misturar estilos.

### ED-17 — Referência de Upwork sem URL recuperável na bibliografia

**Original, p. 67:** «Upwork. (s.d.). A Freelancer’s Guide to Upwork. Upwork.»

Foi localizado o PDF no próprio domínio da plataforma:

https://www.upwork.com/mc/documents/FreelancerGuide.pdf

**Proposta provisória:** `Upwork. (s.d.). *A Freelancer’s Guide to Upwork*. https://www.upwork.com/mc/documents/FreelancerGuide.pdf`

Confirmar data/edição no documento antes de optar por `s.d.`. É guia de mercado de uma plataforma privada, **não** fonte científica que comprova necessidades em Maputo, aplicabilidade de escrow ou neutralidade das suas regras.

### ED-18 — Verificação das restantes referências e prudência de estilo

- Banco Mundial (2019), *Mozambique Digital Economy Diagnostic*: fonte institucional apoiada por documento oficial (https://pubdocs.worldbank.org/en/833211594395622030/Mozambique-DECA.pdf). Confirmar subtítulo e ano exacto na página editorial consultada; não inferir ano a partir da data do PDF pesquisado.
- Banco de Moçambique (2026), *Relatório de Inclusão Financeira 2025*: manter ano editorial correcto; corrigir data da monografia, se necessário, e não eliminar a fonte para parecer que a obra foi concluída em 2025.
- INE (2023), *INFOR 2021/22*: o texto da D44 esclarece que consultou **metadados**, não relatório analítico; não atribuir estatísticas específicas que esses metadados não fornecem.
- ISO/IEC/IEEE 29148:2018, OMG UML 2.5.1 e OWASP ASVS 5.0.0: URLs constam da bibliografia. Uniformizar pontuação, itálico, nomes de entidade e endereços.
- Não foi demonstrado por este relatório que todas as citações, autores e referências estão formatados segundo o manual da instituição. Para essa aprovação, é necessária comparação com a versão oficial das normas.

## 5. Ponto normativo: não assumir APA 7 por defeito

Fonte USTM 1: workshop de 03-04-2025 analisou **proposta de normas unificadas** baseada na APA 7, a regulamentar trabalhos **após aprovação**:
https://ustm.ac.mz/index.php/component/content/article/27-workshop?Itemid=101&catid=36

Fonte USTM 2: página das instruções de submissão para a III Conferência Nacional e Jornadas Científicas 2026 diz expressamente: **«estilo APA, 6ª edição, actualmente em uso na USTM (Manual de Investigação Científica, de Agosto 2018)»**:
https://conferencias.ustm.ac.mz/index.php/IIICNDAMS2026/about/submissions

A segunda página descreve **artigos de conferência**, não necessariamente monografias. Por isso:
- não transpor automaticamente margens, extensão, estrutura, APA 6 ou APA 7 de regras de artigos para este trabalho;
- identificar e consultar a **cópia institucional do manual aplicável à licenciatura** e eventuais instruções do supervisor;
- até confirmação, usar auditoria de **consistência bibliográfica interna** e não declarar «conforme APA 7» nem «conforme APA 6».

## 6. Itens obrigatórios para fecho da D45 editorial

- [ ] Corrigir graficamente o título `ÍNDICE` e a crase na declaração.
- [ ] Conferir com documento oficial a grafia/título académico do supervisor.
- [ ] Corrigir ED-11–ED-15 sem alegar entrevistas reais.
- [ ] Exigir registo de aprovação antes de usar «aprovado» ou optar por «consolidado».
- [ ] Confirmar manual USTM aplicável e formatar referências de acordo.
- [ ] Associar referência Upwork ao PDF verificável e distinguir manual privado de evidência científica.
- [ ] Inspeccionar figura 5.2 e todas as legendas; não inserir listas de figuras/quadros sem exigência verificada.
- [ ] Renderizar todas as 82 páginas do DOCX e conferir quadros continuados, TOC, campos, índices e posição dos títulos.
- [ ] Preservar todos os comentários do supervisor até resolução fundamentada.
- [ ] Executar varrimento final para marcas `[PLACEHOLDER]`, texto de manutenção, mensagens técnicas e referências sem fonte.
- [ ] Não atribuir a este registo qualquer alteração ao DOCX, porque os seus bytes originais continuam indisponíveis nesta sessão.

## 7. Classificação de prioridade

**Corrigir com elevada certeza sem alterar a ciência:** ED-01, ED-03.  
**Corrigir com validação do texto em contexto:** ED-11–ED-17 e ED-05.  
**Exige confirmação externa/acesso ao Word:** ED-02, ED-04, ED-06–ED-10, ED-18 e conformidade com o manual institucional.

**Ficheiro técnico:** este registo pertence à branch `audit/monografia-d45-coerencia-cientifica` e deve ser aplicado à D44 antes de nova declaração de prontidão editorial.


## 8. Verificação automatizada da coerência textual do índice (nova execução)

A leitura integral paginada da D44 identifica **96 entradas no índice**, das quais **94 têm numeração hierárquica** (1–8, 1.1, 1.1.1, etc.) e duas são pré-textuais (RESUMO e ABSTRACT).

**Procedimento reprodutível:** extrair as páginas 5–8; para cada linha com identificador hierárquico e número de página final, comparar o respectivo ID, início do título e página com o primeiro cabeçalho correspondente no texto extraído de todas as 82 páginas. O texto integral foi lido em cinco janelas consecutivas de linhas `1–500`, `501–1000`, `1001–1500`, `1501–2000` e `2001–2210`, sem lacunas. A primeira tentativa de validação usou intervalos que deixavam linhas por ler e gerou falsos negativos; esses números **não** foram usados na conclusão.

**Resultado:** `94/94` entradas hierárquicas coincidem com o título e a página identificados no texto extraído, sem discrepância. As duas entradas pré-textuais correspondem a RESUMO (p. 9) e ABSTRACT (p. 10).

**Limite:** o resultado comprova correspondência textual e paginação já extraída, mas não comprova estado dos campos `TOC`/`PAGEREF` do Word, legibilidade visual nem estabilidade da paginação após revisão. Por isso, a validação final dos campos e do índice continua pendente de acesso ao DOCX original.

## 9. Siglas e terminologia PT-MZ — verificações adicionais

| ID | Ocorrência | Achado | Acção proposta |
|---|---|---|---|
| ED-19 | `JWT`, p. 34 | Primeira ocorrência em «autenticação baseada em JWT» sem expansão observável | Na primeira ocorrência escrever `JSON Web Token (JWT)`; não afirmar que o mock frontend utiliza JWT real |
| ED-20 | `KYC`, p. 45 (RN15) | `KYC financeiro` surge sem definição prévia | Acrescentar `Know Your Customer (KYC; conhecimento do cliente)` na primeira ocorrência, ligado ao contexto de identificação financeira, sem atribuir obrigações regulatórias específicas à aplicação |
| ED-21 | `API` e `ORM`, p. 57 | Termos técnicos sem expansão na primeira ocorrência textual | Definir brevemente `interface de programação de aplicações (API)` e `mapeamento objecto-relacional (ORM)` uma vez, sem transformar o capítulo em glossário |
| ED-22 | `PSP`, p. 61 | Usado antes de ser definido no texto extraído | Introduzir `prestador de serviços de pagamento (PSP)` antes de usar a sigla, no contexto de integração opcional e sem custódia própria |
| ED-23 | `Engagement`, p. 45 | Nome de entidade de domínio em inglês no quadro de regras, sem definição explícita na primeira ocorrência | Acrescentar legenda breve `relação de contratação (Engagement, no modelo de domínio)`; conservar nome exacto de classe em diagramas e pseudocódigo |
| ED-24 | `Telas`, p. 58 e índice p. 8 | Registo de português brasileiro numa dissertação PT-MZ; o restante texto fala em `interfaces` | Preferir `Interfaces do protótipo e estado de implementação` ou `Ecrãs e estado de implementação`, actualizando o índice automaticamente |
| ED-25 | `matching`, várias passagens de pp. 21, 25, 42 e 58 | Anglicismo coexistente com `correspondência` | Na primeira menção, usar `correspondência (matching)`, depois privilegiar `correspondência automática` se não houver motivo técnico para manter o inglês |

As siglas `UML` encontram-se correctamente introduzidas em §2.12 como «Linguagem de Modelação Unificada (UML)». Não alterar abreviaturas já explicadas.

### Critério para este grupo

Não substituir automaticamente identificadores de domínio (`Engagement`, `AgreementVersion`, `mockApi`, `localStorage`) por traduções, pois isso impediria a rastreabilidade com o código. Traduzir **prosa académica**, manter **símbolos de implementação** exactos, com explicação suficiente na primeira ocorrência.

### Nota adicional sobre citações em linhas quebradas

A citação do OWASP na p. 27 está presente como `(OWASP,` numa linha e `2025)` na seguinte. Um detector lexical que procure apenas `OWASP (2025)` sem normalização de espaço assinalá-la-ia erradamente como ausente. **Não é uma referência omissa**. A auditoria deve normalizar a quebra de linha antes de contar citações.
