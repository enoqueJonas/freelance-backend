# Plano de Reconstrução da Monografia — Conteúdo e Formatação

## 1. Baseline documental
Documento actual: `DraftMonografia (1).docx`, 67 páginas.
Benchmark de organização/modelação: monografia de Blockchain/DID.
Base científica já fechada: G-EMPIRICAL-FINAL, G-REQ e G-MODEL.

A reconstrução não será uma revisão cosmética. O draft mistura escopos web/mobile, questionários e amostras incompatíveis, requisitos sem origem demonstrada e capítulos incompletos. A estratégia é preservar apenas conteúdo que permaneça verificável e reescrever as secções cuja fundamentação mudou.

## 2. Problemas estruturais imediatos do draft
- capa e folha de rosto divergem no nome da autora e no título;
- título da capa restringe a TI, folha de rosto não;
- índice apresenta numeração irregular (1.5 → 1.8; 4.1 → 4.3);
- Cap. I alterna aplicação móvel e web;
- Problema introduz funcionalidades antes da derivação empírica;
- metodologia declara questionários, observação participante, 83 participantes e testes de usabilidade/piloto não sustentados pelo corpus final;
- Cap. IV mistura “caso de estudo” e apresentação de resultados de inquérito;
- Cap. V contém gráficos/percentagens incompatíveis com as 11 entrevistas finais;
- requisitos actuais não correspondem à baseline final;
- modelação, arquitectura, implementação, validação e conclusão estão ausentes/incompletas;
- referências incluem fontes a verificar/remover.

## 3. Estrutura TO-BE

### Elementos pré-textuais
1. Capa
2. Folha de rosto
3. Declaração de honra
4. Dedicatória (se aplicável)
5. Agradecimentos (se aplicável)
6. Índice
7. Lista de figuras
8. Lista de quadros
9. Lista de abreviaturas e siglas
10. Glossário, apenas se necessário
11. Resumo
12. Summary

Uniformizar:
- autora: **Chirley da Techa Narciso Mtefula**;
- título: **Desenvolvimento de um protótipo de uma aplicação web de conexão entre trabalhadores autónomos na área de Tecnologias de Informação e empregadores na Cidade de Maputo**;
- supervisor conforme registo institucional existente;
- data final a confirmar na versão de submissão.

### CAPÍTULO I — INTRODUÇÃO
1.1 Contextualização  
1.2 Justificativa  
1.3 Problema  
1.4 Objectivos  
1.4.1 Objectivo geral  
1.4.2 Objectivos específicos  
1.5 Hipótese  
1.6 Metodologia  
1.7 Considerações éticas  
1.8 Delimitação do tema  
1.9 Estrutura do trabalho

**Acções:** reescrever quase integralmente. Usar a backbone aprovada; remover mobile, claims não verificados, funcionalidades predefinidas e estatísticas sem fonte confirmada.

### CAPÍTULO II — REVISÃO DA LITERATURA
2.1 Trabalho autónomo, freelancing e plataformas digitais  
2.2 Intermediação digital, descoberta e matching  
2.3 Assimetria de informação, perfil, competência e confiança  
2.4 Negociação, formalização e rastreabilidade  
2.5 Pagamentos e risco bilateral  
2.6 Reputação, governação, conflitos e contestabilidade  
2.7 Segurança, privacidade e enquadramento digital moçambicano  
2.8 Análise de soluções existentes / benchmark  
2.9 Engenharia de software, prototipagem e UML

**Acções:** reduzir secções genéricas de “Sistema de Informação”; reaproveitar conceitos válidos após verificação; reconstruir comparação de plataformas; inserir corpus documental aprovado; verificar toda referência antes de permanecer.

### CAPÍTULO III — METODOLOGIA, MATERIAIS E MÉTODOS
3.1 Tipo de pesquisa  
3.1.1 Quanto à natureza  
3.1.2 Quanto à abordagem  
3.1.3 Quanto aos objectivos  
3.1.4 Quanto aos procedimentos  
3.2 Recolha, tratamento e análise de dados  
3.2.1 Pesquisa documental e bibliográfica  
3.2.2 Entrevistas semi-estruturadas  
3.2.3 Participantes e selecção  
3.2.4 Tratamento/codificação temática  
3.2.5 Triangulação e derivação de requisitos  
3.3 Procedimento de desenvolvimento do protótipo  
3.4 Procedimento de validação

**Substituir:** questionários, observação participante, população/amostra 100/83/30 e técnicas estatísticas não realizadas.  
**Corpus:** 11 entrevistas: T01–T08 e E01–E03.  
**Não inventar:** datas, duração, local exacto, forma de gravação/transcrição ou consentimento se não estiverem documentados.

### CAPÍTULO IV — CASO DE ESTUDO
4.1 Contexto do trabalho autónomo e digital em Moçambique/Maputo  
4.2 Contexto da contratação de serviços autónomos de TI  
4.3 Caracterização do grupo estudado  
4.4 Processo actual de descoberta, contratação e prestação de serviços

Usar fontes documentais para contexto e entrevistas apenas onde correspondem à evidência recolhida.

### CAPÍTULO V — APRESENTAÇÃO DE RESULTADOS E DISCUSSÃO
5.1 Resultados empíricos
- caracterização dos participantes;
- descoberta e confiança;
- demonstração de competência;
- escopo/preço/prazo/alterações;
- formalização/rastreabilidade;
- pagamentos/risco;
- reputação;
- conflitos/evidências;
- diversidade/localização/adopção.

5.2 Triangulação e necessidades N01–N18  
5.3 Actores do sistema  
5.4 Regras de negócio (RN01–RN16)  
5.5 Requisitos funcionais (RF01–RF28)  
5.6 Requisitos não funcionais (RNF01–RNF07)  
5.7 Casos de uso  
5.8 Diagrama de classes  
5.9 Diagramas de actividades  
5.10 Diagramas de sequência  
5.11 Diagrama de estados  
5.12 Arquitectura da solução  
5.13 Tecnologias utilizadas  
5.14 Protótipo e interfaces  
5.15 Validação dos requisitos/protótipo

Remover gráficos do questionário antigo. Entrevistas serão analisadas qualitativamente; citações directas apenas quando reproduzem fielmente a transcrição.

### CAPÍTULO VI — CONCLUSÃO E RECOMENDAÇÕES
6.1 Conclusão
- responder pergunta de pesquisa;
- confrontar objectivo geral e OE1–OE4;
- discutir hipótese à luz da validação;
- sintetizar resultados sem introduzir evidência nova;
- declarar limitações.

6.2 Recomendações
- evolução técnica;
- validação/amostra futura;
- RF20/PSP se não implementado;
- estudos futuros.

### REFERÊNCIAS
Auditoria completa: referência citada ↔ entrada bibliográfica; remover URLs contaminados e fontes não verificadas.

### ANEXOS/APÊNDICES
- guiões de entrevista;
- transcrições anonimizadas ou excertos conforme decisão académica;
- material complementar de modelação/testes quando necessário.

## 4. Ordem de edição
**Passo D1 — Pré-textuais + Capítulo I**  
Corrigir identidade, título, numeração e backbone científica.

**D2 — Capítulo III**  
Fixar metodologia real antes de resultados.

**D3 — Capítulo IV + 5.1/5.2**  
Inserir contexto, análise temática, necessidades e triangulação.

**D4 — Capítulo II**  
Reconstruir literatura em função do problema e dos achados; validar referências.

**D5 — Capítulo V engenharia**  
Inserir RN/RF/RNF e UML/arquitectura já aprovados.

**D6 — Implementação e validação**  
Só descrever como implementado aquilo que existir e tiver evidência.

**D7 — Capítulo VI + resumo/summary**  
Fechar apenas depois dos resultados e validação.

**D8 — Formatação final**  
Aplicar estilos, índices automáticos, legendas, listas, paginação, tabelas/quadros, referências internas e revisão visual integral.

## 5. Regras editoriais
- português moçambicano/europeu consistente;
- “Tecnologias de Informação” e “Cidade de Maputo” consistentes com o escopo;
- “ConecTA” como nome da solução;
- “trabalhador autónomo” preferencial; “freelancer” apenas quando conceitualmente necessário/citado;
- não usar “aplicação móvel”;
- não apresentar protótipo como sistema comercial/produção;
- não chamar verificação de perfil de KYC;
- não afirmar escrow/custódia;
- distinguir dado empírico, fonte documental, decisão de engenharia e implementação;
- preservar anonimato T01–T08/E01–E03.

## 6. Formatação — estratégia
A formatação será aplicada com estilos Word, não manualmente parágrafo a parágrafo:
- estilos hierárquicos para capítulos/subcapítulos;
- legendas automáticas de Figura/Quadro;
- índice/listas automáticos;
- referências cruzadas;
- numeração coerente;
- quebras de página/secção controladas;
- cabeçalho/rodapé e paginação consistentes;
- tabelas uniformes;
- normalização de fonte, alinhamento, recuos e espaçamento conforme norma institucional confirmada.

Não copiar cegamente a aparência actual: o draft apresenta inconsistências visíveis de capa, índice, títulos e paginação.

## 7. Gates documentais
- G-DOC-I: Capítulo I coerente.
- G-DOC-METHOD: metodologia corresponde ao estudo realizado.
- G-DOC-EMPIRICAL: resultados correspondem às 11 entrevistas.
- G-DOC-LIT: literatura e referências verificadas.
- G-DOC-ENG: requisitos/modelação rastreáveis.
- G-DOC-VALIDATION: afirmações de implementação/validação evidenciadas.
- G-DOC-FORMAT: estrutura e formatação institucional consistentes.
- G-MONOGRAPH: auditoria final aprovada.

## 8. Próximo passo
Executar **D1 — pré-textuais + Capítulo I**, preservando o ficheiro original e produzindo uma nova versão controlada do DOCX.
