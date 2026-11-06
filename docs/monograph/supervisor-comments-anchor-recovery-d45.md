# D45 — Recuperação de âncoras dos comentários e revisão editorial

**Data:** 2026-11-02  
**Documento:** `Monografia_D45_Comentarios_Rastreados_Auditoria_Editorial.docx`  
**Baseline:** D44 — `Monografia_D44_Metodologia_Proveniencia_Verificada.docx`.

## Problema técnico confirmado

Todos os documentos reconstruídos desde `Monografia_ConecTA_D5_Engenharia_Solucao_LIMPA.docx` até à D44 continham `word/comments.xml` (14 comentários), mas o `word/document.xml` já **não continha** `w:commentRangeStart`, `w:commentRangeEnd` nem `w:commentReference`. Assim, contar 14 entradas no ficheiro de comentários não demonstrava a existência de anotações associadas ao texto. Foram recuperadas as âncoras identificáveis nas versões D1–D4: D1 tinha 11 comentários referenciados, D2 tinha 10, D3 tinha 6 e D4 tinha 3. Três comentários já não apresentavam âncora na D1.

## Reparação efectuada

Na D45, os **14 comentários originais foram integralmente conservados** em `word/comments.xml` (ficheiro idêntico byte a byte ao da D44). Foram adicionados no documento **14 conjuntos** de `commentRangeStart/commentRangeEnd/commentReference`, permitindo a leitura das âncoras por ferramentas OOXML.

**Advertência de proveniência:** não se afirma que as selecções de texto originais foram restauradas exactamente. Para comentários cujo texto-base foi substituído ao longo da revisão, a âncora é uma **nova associação temática**, escolhida para facilitar decisão pelo supervisor. A associação deve ser revista antes de declarar um comentário formalmente resolvido.

## Matriz de seguimento — sem declaração automática de resolução

| ID | Texto/resumo do comentário | Reassociação na D45 | Situação editorial |
|---|---|---|---|
| 41 | «Super» | 1.2 Justificativa | Informativo; localização original não recuperada |
| 81 | Delimitação espacial e temporal | 1.8 Delimitação do tema | **Parcial:** Cidade de Maputo indicada; período X–Y não documentado; não inventar |
| 86 | Incluir elementos pós-textuais | 1.9 Estrutura do trabalho | Tratado textualmente; acrescentada referência às referências e Apêndice A; revisão do supervisor pendente |
| 107 | Numeração de figuras por capítulo | Figura 2.1 | Figura 2.1 está numerada no padrão; confirmar todas as figuras em M11 |
| 110 | Criar glossário pré-textual | §2.1 — conceito de trabalho autónomo | **Aberto:** glossário ainda não acrescentado; verificar posição e termos no manual USTM |
| 329 | Título de tabela em cima e fonte por baixo | Quadro 5.1 | Convenção presente nesta tabela; auditoria global de legendas e fontes pendente |
| 340 | Rever legenda | Quadro 5.2 | Legenda revista nas versões anteriores; supervisão final pendente |
| 373 | População de Moçambique e repetição | 3.4 População e amostra | A população-alvo é segmento TI/Maputo; inserir total nacional indiscriminado não serviria para inferência; resposta metodológica a validar |
| 384 | «Good :)» | 4.1 Contexto do estudo | Informativo; âncora histórica aproximada |
| 386 | «?? Também com dúvida?» | 4.1 Contexto do estudo — enquadramento | **Aberto:** pergunta original já não corresponde literalmente ao texto actual; solicitar confirmação contextual antes de encerrar |
| 394 | «Good.. Figura 5.1» | Figura 5.1 | Informativo; figura actualmente presente e numerada |
| 398 | Identificar actores do sistema | 5.1.1 Identificação dos actores | Actores listados no Quadro 5.1; revisão de associações pendente |
| 399 | Que actor executa a acção? | 5.2.2 Diagrama de casos de uso | Parcial: modelo tem actores contextuais; rever cada ficha UC/associação em M17 |
| 400 | «WELL DONE» | 5.2.1.2 Requisitos não funcionais | Informativo; âncora histórica aproximada |

## Revisão editorial cirúrgica efectuada

**16 parágrafos** revistos (incluindo resumo e abstract), sem alterar diagramas ou dados:
- referência ao piloto sintético passou a ser descrita como verificação da proveniência documental, sem insinuar recolha real;
- §1.8 passou a indicar fontes documentais e material exploratório, substituindo «dados empíricos disponíveis»;
- §1.8, §2.2 e §5.5 passaram a distinguir desenvolvimento parcial, plano de testes e validação **não executada**;
- §1.9 passou a mencionar expressamente as referências e o Apêndice A;
- §5.1 deixou de referir «resultados empíricos do Capítulo IV», pois a origem dos registos ainda não está comprovada;
- §5.5 e §6.1 deixaram de afirmar que a leitura de código comprova a **viabilidade funcional** de fluxos sem execução;
- substituídas referências operacionais desnecessárias a «repositório» e «auditoria» em trechos narrativos.

As sete indicações `[PLACEHOLDER]` das Figuras 5.13–5.19 não foram eliminadas porque faltam capturas reais do frontend. Eliminá-las agora ocultaria uma pendência documental.

## Verificação técnica

- `word/comments.xml` idêntico à D44, com os **14 textos originais** e respectivos IDs/autores/datas.
- `word/document.xml`: **14** âncoras de início, **14** de fim e **14** referências de comentário; confirmado pelo extractor `comments_extract.py`, que reporta associação actual para todos os IDs.
- `word/styles.xml` e `word/numbering.xml` inalterados; os quadros e imagens anteriores mantidos.
- DOCX renderizado em **82 páginas físicas**; Introdução na página **11**, Referências na **67**, **57/60 páginas inclusivas de corpo**, início do Apêndice A na **68**.
- Páginas afectadas e adjacentes renderizadas e verificadas, com folha de contacto. A auditoria integral a 100% de todas as páginas ainda pertence à M11.
- Nenhum comentário foi marcado como formalmente resolvido ou apagado; a recuperação de âncoras não equivale à aceitação das respostas pelo supervisor.

**Pendências:** glossário pré-textual (110), período de delimitação (81), dúvida sem contexto original recuperável (386), validação das associações actor/UC (399), cronologia da capa Setembro/2025 versus fontes de 2026, evidência empírica, testes e sete figuras de interface.

**Estado:** D45 é uma versão intermédia, não pronta para submissão. M15 parcialmente tratada; M16 revisto localmente, gate editorial global permanece aberto.
