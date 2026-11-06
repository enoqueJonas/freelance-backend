# D70 — Comentários do supervisor, glossário, legendas dos quadros e índice

**Estado:** versão Word de revisão efectivamente construída e entregue na conversa; **não publicada no GitHub** por incluir as transcrições integrais. A versão original D44 e a intermédia D69 não foram sobrescritas. Esta D70 **não equivale à aprovação da monografia**.

## 1. Entregável real

- **Ficheiro:** `Monografia_ConecTA_D70_Supervisor_Indice_Validado.docx`.
- **SHA-256:** `3dab31affea17173803d4968d7a3834c534080a6a8fec814574edd1be5eb1b3a`.
- **Base:** `Monografia_ConecTA_D69_Integrada_Indice_Validado.docx`.
- **Renderização de verificação:** **110 páginas**, com alterações verificadas visualmente no índice, glossário, delimitação, descrição pós-textual e quadros. A paginação no Word de outro sistema pode variar.

### Correcções aplicadas

1. Inserido **GLOSSÁRIO** nos elementos pré-textuais, numa página autónoma antes do Resumo, com **12 definições operacionais** relevantes para o domínio (incluindo distinção entre emprego e trabalho autónomo, significado de «empregador» no modelo, versões de acordo, rastreabilidade e escrow). **Não são definições jurídicas universais.**
2. Secção **1.8**: acrescentada a delimitação temporal da componente de entrevistas, **Julho–Setembro de 2024** em Maputo, de acordo com a ficha; os ensaios de evolução do protótipo são tratados como período posterior, sem atribuir-lhes data de recolha de campo.
3. Secção **1.9**: acrescentada a referência explícita aos elementos pré-textuais e pós-textuais — glossário, referências bibliográficas, Apêndice A e Anexos A/B.
4. Acrescentadas **legenda em cima e fonte em baixo** a três tabelas do Capítulo V, agora **Quadros 5.7, 5.8 e 5.9** (estado de implementação, cenários V01–V08, verificações RNF).
5. **Índice do Word:** actualizadas as páginas, inserido o glossário e corrigidos **cinco destinos de hyperlinks internos** que estavam sem marcador na D69. Auditoria da renderização encontrou **100 entradas, 0 divergências de título/página e 0 marcadores em falta**. Campo TOC e links preservados.

### Integridade preservada

- **14 tabelas**, agora **todas com legenda acima e fonte imediatamente abaixo**.
- **183 perguntas, 183 respostas e 11 perfis** transcritos literalmente, idênticos à D69.
- Ficheiros de imagem **originários da D44** preservados **byte a byte**; não foram substituídos diagramas ou evidências.
- `word/comments.xml` **idêntico** ao original D44, com **14 comentários**. **Não existem marcadores de ancoragem** `commentRangeStart/commentReference` no documento herdado da D44; a retenção do XML não prova que os comentários continuem seleccionáveis na interface do Word.
- **Não** alteradas as datas da capa, da contracapa e da declaração de honra, nem as palavras das entrevistas.

## 2. Matriz de apreciação dos 14 comentários do supervisor

Os comentários foram encontrados em `word/comments.xml`; as respectivas âncoras já não constavam da D44. Por isso a correspondência comentário→parágrafo abaixo é **inferida do conteúdo da observação**, não uma reconstrução exacta da posição do comentário na versão original.

| ID | Conteúdo resumido | Estado D70 |
|---|---|---|
| **41** | «Super» | Elogio; sem acção editorial |
| **81** | Delimitar Maputo e períodos x/y | **Tratado**: §1.8 indica Maputo e Julho–Setembro de 2024 para recolha; cronologia integral do projecto ainda requer decisão |
| **86** | Mencionar elementos pós-textuais | **Tratado** em §1.9 |
| **107** | Numeração de figuras por capítulo (ex.: Figura 2.1) | **Verificado no material existente**: figuras referenciadas como 2.x, 5.x e A.x; correspondência concreta do comentário original não recuperável |
| **110** | Criar página de glossário, incluindo «emprego» | **Tratado**: glossário pré-textual de 12 termos, integrado no índice |
| **329** | Legenda de tabela em cima, fonte em baixo | **Tratado transversalmente:** 14/14 tabelas têm legenda antes e fonte depois, incluindo três corrigidas na D70 |
| **340** | Rever legenda | **Pendente de identificação precisa:** sem marcador ancorado, não é possível provar qual legenda era a objectada; rever com supervisor |
| **373** | Questão sobre população de Moçambique, com «pode deixar» | **Sem alteração:** não inserir estatística populacional que a metodologia não utiliza; confirmar se o comentário foi dispensado |
| **384** | «Good :)» | Elogio; sem acção |
| **386** | «?? Tambem com duvida?» | **Pendente**: excerto original não identificável sem âncora |
| **394** | «Good.. Figura 5.1» | Elogio; figura original preservada |
| **398** | «Quais são os actores do sistema?» | **Coberto em §5.1 e Quadro 5.1**, mas não é possível determinar se isto elimina integralmente a observação original |
| **399** | «Que actor executa a acção? Já tens isso no diagrama» | **Parcialmente coberto** por Quadro 5.1, diagrama de casos de uso e quadros UC13/UC14; revisão de localização exacta pendente |
| **400** | «WELL DONE» | Elogio; sem acção |

**Não declarar os 14 comentários formalmente resolvidos**: o DOCX contém texto dos comentários mas não ancora as referências; alguns são elogios, outros dependem de verificação localizada pelo supervisor.

## 3. Bloqueadores de submissão que a D70 não resolve

1. **Cronologia:** capa/declaração permanecem «Setembro de 2025», mas a bibliografia inclui publicação de **2026** e os testes técnicos D50–D56 ocorreram posteriormente. **Não alterar a data de assinatura ou de submissão por suposição**; corrigir com decisão da autora e supervisor.
2. **Referências:** conferir autoria, edições e páginas exactas de algumas fontes da D62, particularmente OIT 2018 e estudos africanos 2024. Nesta etapa **não foram introduzidas referências novas**.
3. **Ética/confidencialidade:** registos integrais constam do anexo; requer confirmar consentimento/condições de circulação e risco de identificação indirecta antes de partilhar a terceiros.
4. **Validação técnica:** V01–V03 parcialmente exercitados, V04–V08 sem execução canónica integral; RNF e impacto real não comprovados integralmente. A D70 não altera os resultados.
5. **Figuras sem evidência real:** os espaços para as Figuras 5.14, 5.15, 5.18 e 5.19 continuam identificados como não demonstrados; não inserir capturas fictícias.
6. **Revisão institucional/manual:** glossário foi pedido pelo supervisor e adoptado numa posição pré-textual convencional, mas a norma final da instituição (ordem dos elementos, formatos, margens) precisa de conferência com o manual.
7. **Comentários:** o XML foi conservado sem alteração; a ausência de âncoras precisa de revisão no Word e, quando necessário, pedido ao supervisor para identificar os dois comentários ambíguos (IDs 340, 386).

## 4. Validação e limites

**Verificações automatizadas:** 110 páginas do PDF de controlo, 100 entradas do índice conferidas com a paginação renderizada (0 discrepâncias), bookmarks (0 quebrados), 14 quadros com fontes, contagem e fidelidade literal de 183+183 respostas/perguntas/11 perfis; comentários e media originais preservados.

**Verificação visual:** foram inspeccionadas páginas de índice, glossário, delimitação, quadros relegendados e limites dos anexos em renderização, incluindo montagens de páginas. **Não se afirma uma revisão manual a 100% de cada uma das 110 páginas nesta etapa**; a revisão final de submissão continua necessária.

**Conclusão D70:** problemas editoriais verificáveis foram corrigidos com modificação real da cópia Word e preservação do corpus. A decisão da data de capa e as condições de divulgação das entrevistas são factos externos que não devem ser inventados para aparentar conclusão.
