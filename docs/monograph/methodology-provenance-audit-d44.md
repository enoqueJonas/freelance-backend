# D44 — Auditoria de proveniência e coerência metodológica (02/11/2026)

**Documento entregue no chat:** `Monografia_D44_Metodologia_Proveniencia_Verificada.docx`  
**Versão de partida:** `Monografia_D43_Quadros_2_1_2_2_Auditoria_Cientifica.docx`  
**Âmbito:** Capítulos III e IV, resumos, considerações éticas, discussão, conclusão e remissões relevantes nos Capítulos I/II/V.  
**Estado:** remediação documental executada; a validação empírica **permanece aberta**.

## 1. Achado de proveniência — o que está e o que não está demonstrado

Foram confrontados os seguintes artefactos do repositório:

- [Piloto de entrevistas — dados sintéticos](../research/interview-pilot-synthetic.md): contém **11 entrevistas fictícias** (T01–T08 e E01–E03) e uma advertência explícita: «DADOS SINTÉTICOS — NÃO UTILIZAR COMO RESULTADOS EMPÍRICOS DA MONOGRAFIA».
- [Descobertas do piloto sintético](../research/interview-pilot-findings.md): qualifica as conclusões como ensaio do instrumento, não resultados empíricos.
- [Codificação temática final](../research/interview-final-thematic-coding.md): descreve onze perfis e analisa temas, convergências e divergências, denominando-os «corpus empírico fornecido».
- [Matriz de triangulação](../research/triangulation-matrix.md): identifica o material como «corpus de trabalho», com documentação adicional.
- [Guiões de trabalhadores e empregadores](../research/interview-guide-workers.md) e [entrevistadores](../research/interview-guide-employers.md).

**Limite probatório:** a codificação temática posterior não é, por si, um registo primário de realização de entrevistas. Nos materiais auditados não foram localizados comprovativos independentes de recrutamento, recolha, transcrição, datas ou condições éticas que permitam estabelecer a origem do conjunto posterior como campo real e autónomo. A existência do piloto sintético **não prova que não tenham ocorrido outras entrevistas**, mas impede tratar os seus conteúdos como depoimentos de pessoas reais. Não se devem inventar documentos de consentimento, gravações, datas nem identificação dos participantes.

## 2. Correcções efectivas na D44

1. **Resumo PT e abstract EN:** carácter aplicado/exploratório, codificação de registos de trabalho e limite de proveniência clarificados. Não são declarados resultados de campo comprovados.
2. **Capítulo I:** metodologia, ética e estrutura do trabalho ajustadas para distinguir análise documental, cenários sintéticos e recolha empírica pendente.
3. **Capítulo II:** linhas de fonte dos Quadros 2.1/2.2 corrigidas para «corpus textual codificado», sem apresentar entrevistas como prova de campo.
4. **Capítulo III:** secção 3.2.2 renomeada «Guiões de entrevista e corpus exploratório», codificação temática descrita como análise do material disponível; 3.4 distingue **população de interesse** de **amostra humana não comprovada**. A concepção incremental não é confundida com execução, e os testes V01–V08/RNF continuam por realizar.
5. **Capítulo IV:** a secção 4.4 passou a «Possíveis pontos de fricção identificados»; a secção 4.6 passou a «Caracterização dos perfis do corpus»; 4.15 a «Síntese de hipóteses de necessidades»; 4.16 a «Confronto do corpus com fontes documentais». Os perfis T01–E03 passam a ser **cenários/registos codificados**, sem afirmações de relato, incidência ou representatividade de amostra real.
6. **Capítulo V:** fontes de quadros e fichas de casos de uso actualizadas para retirar a expressão «análise empírica» onde não há evidência independente.
7. **Capítulo VI:** a pergunta de pesquisa e a discussão das hipóteses são respondidas ao nível de **concepção/modelação**; não se afirma eficácia demonstrada junto de trabalhadores reais.

**Âmbito quantitativo:** 76 parágrafos preexistentes alterados e três células de quadros revistas; sem reconstrução global, sem eliminação de figuras e sem eliminação dos comentários do supervisor.

## 3. O que permanece cientificamente defensável

- A revisão bibliográfica, os documentos institucionais e os modelos de engenharia constituem fontes válidas **dentro do âmbito que efectivamente suportam**.
- Os cenários textuais permitem testar a coerência dos guiões, explorar casos de uso e propor hipóteses de requisitos; não permitem medir necessidades ou preferências dos trabalhadores de TI de Maputo.
- A especificação N01–N18 e a baseline de RN/RF/RNF são **hipóteses de concepção e decisões técnicas**, não resultados de campo confirmados.
- Os doze diagramas UML representam a **arquitectura/modelo-alvo**, não a comprovação de implementação integral.
- A análise estática do frontend/backend e o protocolo de teste não são equivalentes a validação funcional ou usabilidade executadas.

## 4. Gate de recuperação da fundamentação empírica

Antes de restaurar linguagem de «entrevistas realizadas», «participantes» ou «necessidades confirmadas», obter e auditar os **registos originais reais**, se existirem, pelo menos:
1. evidência de que houve recrutamento e participação real, respeitando privacidade e os critérios éticos da universidade;
2. datas/condições de recolha e instrumentos utilizados, sem presumir gravações ou consentimentos não documentados;
3. respostas ou notas de campo originais anonimizadas e sua cadeia de transformação em T01–T08/E01–E03;
4. matriz de excertos originais → códigos → temas → necessidades, com divergências e casos negativos;
5. reavaliação metodológica das hipóteses, conclusões e declaração de limitações.

Se **não houver entrevistas reais**, a monografia deve ser defendida apenas como **estudo exploratório documental com cenários sintéticos e protótipo conceptual**, sujeito à concordância do supervisor e das exigências do curso, ou deverá realizar-se recolha empírica legítima. Os textos simulados nunca devem ser apresentados como pessoas entrevistadas.

## 5. QA editorial e OOXML

- Renderização final: **82 páginas físicas**, Introdução física **11**, Referências física **67** = **57/60 páginas** do corpo com contagem inclusiva conforme manual USTM.
- Comentários originais: **14**, com `word/comments.xml` **byte a byte idêntico à D43**. Também preservados `word/styles.xml` e `word/numbering.xml`.
- Artefactos: **14 quadros**, **22 imagens inline**, **sete marcadores de interfaces reais ainda pendentes**.
- Índice Word automático preservado: **96 entradas** reconciliadas contra as páginas do PDF final; **zero divergências**. Foram actualizados 21 valores de página após a renderização preliminar.
- Inspecção visual: páginas alteradas e páginas adjacentes dos Capítulos III/IV, páginas de índice e conclusões, com folha de contacto; **não** se declara a revisão a 100% de cada uma das 82 páginas nesta etapa.
- **D44 é intermédia**, não pronta para submissão: M04, M05, M08, M09, M10, M11, M12 e a verificação da cronologia de capa M18 permanecem abertas.
