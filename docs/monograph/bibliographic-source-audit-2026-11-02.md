# M10 — Auditoria da bibliografia e das citações da monografia (D41)

**Data:** 2026-11-02  
**Versão canónica proposta:** `Monografia_D41_Auditoria_Bibliografica.docx` (binário entregue no chat, não no GitHub).  
**Baseline:** D40 (`Monografia_D40_Protocolo_Validacao_V01_V08.docx`).  
**Âmbito:** parágrafos do texto principal, quadros e Capítulo 7, com verificação institucional/editorial dos títulos e datas. Não inclui a verificação página a página de **todas** as afirmações e inferências da revisão bibliográfica; essa etapa de M03/M10 continua aberta.

## 1. Correspondência bidireccional

A D40 continha **13 referências**, sendo **9 efectivamente citadas** no texto/quadros e quatro sem citações identificáveis. A D41 contém **9 referências**, todas citadas.

| Referência mantida | Ocorrências autor/ano no texto principal (aproximadas) | Evidência de verificação |
|---|---:|---|
| Banco de Moçambique (2025), ENIF 2025–2031 | 3 | [Fonte oficial do BM](https://www.bancomoc.mz/pt/areas-de-actuacao/inclusao-financeira/quadro-conceptual-da-inclusao-financeira/); publicada em 06/08/2025; PDF original disponível nos ficheiros de trabalho |
| Banco de Moçambique (2026), Relatório de Inclusão Financeira 2025 | 1 | [Listagem oficial do BM](https://www.bancomoc.mz/pt/publicacoes-e-estudos/?category=Relat%C3%B3rio+de+Inclus%C3%A3o+Financeira); publicado em **15/07/2026**, apesar de cobrir 2025 |
| Banco Mundial (2019), Mozambique Digital Economy Diagnostic: Executive Summary Report | 5 | [PDF original World Bank](https://pubdocs.worldbank.org/en/833211594395622030/Mozambique-DECA.pdf), copyright 2019; ficheiro `MozambiqueDECA.pdf` consultado |
| Instituto Nacional de Estatística (2023), INFOR 2021/22: documentação de metadados | 4 | [Catálogo INE, estudo 89](https://mozdata.ine.gov.mz/index.php/catalog/89/study-description); `ddi-documentation-portuguese-89.pdf`, **gerado em 25/04/2023**. Importante: trata-se dos metadados, **não** do relatório final INFOR publicado em 2022 |
| International Labour Organization (2018), Digital labour platforms and the future of work | 3 | [Publicação oficial OIT](https://www.ilo.org/publications/digital-labour-platforms-and-future-work-towards-decent-work-online-world), data 20/09/2018; PDF local `wcms_645337.pdf` |
| International Labour Organization (2021), World Employment and Social Outlook 2021 | 19 | [Publicação oficial OIT](https://www.ilo.org/resource/role-digital-labour-platforms-transforming-world-work-0), publicado 23/02/2021; PDF local `wcms_771749.pdf` |
| International Labour Organization (2024a), Digital labour platforms in Kenya | 1 | [Publicação OIT](https://www.ilo.org/publications/digital-labour-platforms-kenya-exploring-womens-opportunities-and-0), 04/04/2024; PDF local do relatório |
| International Labour Organization (2024b), Platform work in Uganda | 1 | [Publicação OIT](https://www.ilo.org/publications/platform-work-uganda-promoting-decent-work-all-0), 15/11/2024; [catálogo institucional ILO](https://researchrepository.ilo.org/esploro/outputs/report/Platform-work-in-Uganda-promoting-decent/995619540702676) confirma **Kampala** como local editorial |
| Upwork (s.d.), A Freelancer’s Guide to Upwork | 2 | `FreelancerGuide.pdf` fornecido como fonte de trabalho, 33 páginas; a capa identifica o guia, mas **não comprova ano editorial**: manter «s.d.» até localizar data fiável |

A contagem de ocorrências é do texto principal e visa correspondência de autor/ano, não comprovação de cada conteúdo citado.

## 2. Alterações efectivamente executadas no DOCX D41

1. **Retiradas quatro obras sem referência no corpo nem nos quadros:** Booch, Rumbaugh & Jacobson (2005); Marconi & Lakatos (2017); Pressman & Maxim (2020); Sommerville (2016). São obras reais, mas não devem figurar numa lista de **referências citadas** sem remissão. Se o Capítulo III ou a secção de modelação passar a citá-las com fundamento e análise pertinente, podem ser reintegradas; não fabricar citações para justificar a bibliografia.
2. **Fonte INE (2023):** designação alterada para «documentação de metadados do estudo», explicitando por que surge 2023 num inquérito 2021/22 cujo **relatório final é de 2022**. O corpo continua a usar o estudo como contexto, não como medida específica do universo de freelancers TI de Maputo.
3. **OIT Uganda (2024b):** `Geneva: ILO` foi corrigido para `Kampala: ILO`, conforme catálogo editorial da OIT.
4. **Normalização bibliográfica:** os nove parágrafos possuem alinhamento à esquerda e recuo suspenso/hanging de 0,7 cm. Foram mantidos textos, títulos e nomenclatura das fontes citadas, sem inventar páginas de excertos.
5. **Nenhuma alteração** foi introduzida nas afirmações científicas do texto, nas entrevistas, nos dados ou nos resultados dos ensaios. Todas essas questões devem ter auditoria substantiva própria.

## 3. Achados ainda abertos (não ocultar)

### Crítico: cronologia do manuscrito
Capa/folha inicial da monografia continuam a indicar **«Maputo, Setembro de 2025»**, mas o texto e a bibliografia citam o Relatório de Inclusão Financeira 2025 do Banco de Moçambique **divulgado em 15 de Julho de 2026**. Sem uma identificação editorial válida, a apresentação é cronologicamente impossível como trabalho concluído em Setembro de 2025. **Não corrigir a data por suposição:** confirmar mês/ano reais de entrega e actualizar capa, folha de rosto e referências cronológicas de modo consistente antes da submissão. Rastrear em M18.

### Bibliografia e base teórica técnica
A retirada dos quatro livros torna explícita uma fragilidade pré-existente: as secções de metodologia, engenharia de requisitos e UML podem precisar de **fundamentação técnica directamente utilizada e citada**. Não adicionar livros apenas para preencher uma lista; verificar as obras realmente consultadas, atribuir conceitos específicos e citar a edição efectiva. Resolver nos trabalhos M03/M04/M17.

### Rastreabilidade das afirmações
A correspondência autor/ano demonstra que os nove itens são citados, **mas não prova** que cada proposição do Capítulo II esteja fundamentada na página certa, nem que resumos do Quénia/Uganda sejam aplicáveis a Maputo. É necessário prosseguir com a verificação de conteúdo por secção e páginas-fonte.

### Fontes normativas
Existem afirmações prudentes sobre pagamentos e custódia, mas **não há demonstração jurídica** da aplicabilidade de uma norma específica ao protótipo. O estudo não pode afirmar isenção regulatória por inferência. Se forem feitas afirmações jurídicas futuras, citar diploma e artigo aplicável após análise.

## 4. QA de integridade e apresentação

- D41 renderizada em **82 páginas**. Introdução na física **11**, Referências na **67**: corpo **57/60** páginas, contagem inclusiva; Apêndice A inicia na **68**.
- Página 67, índice 8, e páginas adjacentes 66/68 foram inspeccionados, sem quebra de página ou sobreposição bibliográfica.
- `word/comments.xml` **byte a byte idêntico à D40**: 14 comentários preservados; `word/styles.xml` também preservado.
- 14 tabelas e 22 imagens inline mantidas, assim como **sete marcadores de capturas de interface** ainda não validados.
- Índice automático Word preservado e numeração das rubricas principais inalterada; não se reescreveu a estrutura global.

**Estado da M10:** correspondência formal autor/ano e verificação de identidade das nove fontes concluídas nesta passagem; M10 **permanece aberta** por necessidade de verificar conteúdo citado e resolver cronologia. D41 é **intermédia**, não pronta para submissão.
