# D72 — Remediação canónica da monografia ConecTA segundo a monografia blockchain

**Estado:** backlog operativo, com critérios de aceitação e evidências; trabalho por executar, salvo itens marcados.  
**Registo:** 07-11-2026.  
**Fonte de referência REAL:** `Monografia_Canonica_Entrevistas_Documento_Original_Verificado_30102026.docx`, 26 tabelas, Capítulo IV «Contexto de aplicação», Capítulo V «Apresentação de resultados e discussão», Apêndice A de diagramas complementares e Anexos de entrevistas. **É o padrão editorial/estrutural/visual, não fonte de requisitos da ConecTA.**  
**Documento de trabalho:** `Monografia_ConecTA_D71_Quadros_Uniformizados_PRETOC.docx`, com 16 RN, 28 RF, 7 RNF, 14 tabelas e figuras. **Não editar directamente a D44 nem sobrescrever a D71.**  
**Restrição de gestão:** tentativa de criar GitHub Issue devolveu HTTP 410: «Issues has been disabled in this repository». Este Markdown versionado no ramo do PR #2 assume a função de tarefas acompanháveis até a funcionalidade de Issues estar disponível.

## Princípios não negociáveis

1. A blockchain é referência de **estrutura, estilo, fichas de requisito, disposição gráfica, tamanho/legibilidade, legendas, tabelas e anexos**; não transportar conceitos ou funcionalidades de DID/Xitique para a ConecTA.
2. A monografia pública contém apenas **conteúdo académico necessário**, não códigos de auditoria de projecto, compromissos Dxx, matrizes N01–N18 ou explicações de tracker.
3. Requisitos **RN, RF e RNF** e diagramas **casos de uso, classes, actividades, sequência, estados e arquitectura** permanecem. Não eliminar uma funcionalidade da especificação sem confronto técnico/documental.
4. Entrevistas são **complementares à fundamentação documental** e respostas literais ficam em **anexo**. T01–T08 = trabalhadores autónomos; E01–E03 = empregadores/contratantes. Explicar códigos uma vez, não espalhar identificadores pelo corpo da monografia. **Preservar 183 perguntas e respostas sem modificação.**
5. Todos os **diagramas e legendas devem estar em português**, com termos do domínio coerentes. Nos desenhos, trocar «Aplicação Web Proposta» por **«Sistema»** (não confundir com o título da própria monografia).
6. Nada de anotações internas ou textos «Prossegue DA02», «DA01 encerrado», «série Dxx», «gerado», notas de produção, testes inventados, pseudo-evidências, rótulos que não tenham função UML.
7. Separar **proposta/modelo** de funcionalidades **efectivamente implementadas** e testadas; não reproduzir afirmações de aprovação do protótipo sem evidência.

## Actividades e critérios de aceitação

### P0 — T01 Inventário comparativo e padrão canónico
- [x] Aceder ao Word blockchain canónico original e identificar capítulos, subtítulos, quadro de RN, fichas de RF por macro-requisito, RNF, casos de uso, classes, actividades, sequências e apêndice.
- [x] Inspeccionar a ConecTA D71: 16 RN, 28 RF, 7 RNF, quadros, 20 imagens de diagramas no corpo/apêndice; **sequências DS01–DS04 existem no apêndice**, logo não estão «em falta», mas **mal localizadas/fragmentadas** face à referência.
- [ ] Produzir mapa de correspondência **índice blockchain → índice ConecTA**: títulos canónicos do Capítulo V, distribuição entre corpo/apêndice/anexo, exclusões justificadas.

### P0 — T02 Remover estruturas de rastreabilidade internas e reduzir o Capítulo IV
- [x] Eliminar **4.15 «Síntese de hipóteses de necessidades»** e enumeração N01–N18 do manuscrito na cópia D72 Etapa 1.
- [x] Eliminar **4.16 «Confronto da fundamentação documental, entrevistas e especificação»** como secção de tracker na cópia D72 Etapa 1.
- [x] Eliminar **5.2.8 «Rastreabilidade entre investigação e solução»** como título académico na cópia D72 Etapa 1.
- [x] Condensar **4.1–4.14** em **4.1 Caracterização do contexto de contratação** e **4.2 Caracterização do grupo-alvo**, segundo a estrutura do Capítulo IV blockchain. Verificar no final remissões/consistência de toda a monografia.
- [x] Remover os códigos N01–N18 do texto principal da cópia D72, mantendo RN/RF/RNF e a análise de origem dos requisitos no documento de auditoria.
- [x] Actualizar **índice de 85 entradas** após a mudança da estrutura; **0 divergências de página, 0 bookmarks quebrados**. [ ] Rever lista de figuras/quadros após as próximas substituições de diagramas.

### P0 — T03 Normalizar o quadro de REGRAS DE NEGÓCIO
- [ ] Seguir a tabela blockchain **ID | Regra de negócio | Descrição | Módulo** ou simplificar apenas com justificação, em vez de uma lista solta de duas colunas.
- [ ] Conservar RN01–RN16, cada uma com nome, enunciado completo e módulo pertinente; não introduzir módulos não existentes.
- [ ] Usar PT-MZ e evitar nomes de classes técnicas em regras de negócio onde não acrescentem clareza.

### P0 — T04 Reconstruir a apresentação dos REQUISITOS FUNCIONAIS
- [ ] Reproduzir **o template real do Word blockchain**: título de **macro-requisito**, ficha individual com **código RF**, **nome**, **declaração («O sistema deve…»)**, **Fonte / Prioridade / Data** e **Observação** quando materialmente útil.
- [ ] Organizar RF01–RF28 pelas **sete áreas MR01–MR07**, substituindo «MR01» sem descrição por um **macro-requisito nomeado**.
- [ ] Dados «Fonte», «Prioridade» e «Data» devem ser **verificáveis**; não copiar a data 30/08/2026 da blockchain nem marcar prioridade arbitrária. Se desconhecidos, omitir ou marcar «por ratificar» na cópia de auditoria, não inventar no texto final.
- [ ] Verificar **28/28 RF** presentes e declaração sem ambiguidade, sem alterar significado ou escopo.
- [ ] QA visual de largura, colunas fundidas, fontes, alinhamentos, alturas e paginação de todas as fichas.

### P0 — T05 Normalizar REQUISITOS NÃO FUNCIONAIS
- [ ] Usar tabela blockchain **ID | Nome | Declaração | Rastreabilidade**, em vez de ID/Categoria/Declaração. A rastreabilidade para RN/RF é conteúdo de especificação, **não matriz de auditoria**.
- [ ] Preservar RNF01–RNF07; evitar declarações sem critérios observáveis ou conformidade fictícia.
- [ ] QA visual de células e tabela.

### P0 — T06 Diagrama de CASOS DE USO
- [ ] Trocar fronteira «Aplicação Web Proposta» por **«Sistema»**.
- [ ] Refazer diagrama com **maior espaçamento vertical e horizontal**, sem cruzamentos desnecessários, rótulos legíveis, actores correctamente relacionados com casos.
- [ ] Verificar nomes de casos de uso e nomes de actores **em português**; distingui-los dos termos técnicos inevitáveis e explicar esses quando apropriado.
- [ ] Conferir a correspondência com RF/UC em vez de inventar casos de uso.
- [ ] Renderizar a **página efectiva** do Word e comprovar legibilidade ao tamanho impresso.

### P0 — T07 Diagrama de CLASSES
- [ ] Passar **todos os nomes de classes, atributos e relações apresentados no diagrama académico para português**, mantendo mapeamento interno dos nomes de código inglês.
- [ ] Reorganizar hierarquia por **identidade / oportunidades / contratação / acordos / execução / pagamentos / reputação / conflitos**.
- [ ] Fazer com que **cardinalidades 0..1, 1..*, 0..*** não se sobreponham a linhas, setas ou caixas; remover cruzamentos.
- [ ] Definir legenda concisa de que classes do modelo conceptual não significam classes implementadas na branch principal.
- [ ] Conferir nomes/associações com modelo D49 e baseline RF/RN.

### P0 — T08 Diagramas de ACTIVIDADES
- [ ] Refazer **DA01, DA02** (Capítulo V) e **DA03, DA04** (apêndice) com mais espaço entre passos, actores e setas.
- [ ] Usar **português integral** nas acções/decisões e no título de cada pista, conservando estados técnicos apenas com tradução/legenda quando necessários.
- [ ] Excluir **«Prossegue DA02…», «DA01 encerrado…»**, notas de auditoria, instruções de produção e parágrafos demasiado extensos no desenho. A transição entre processos pode constar no texto académico exterior, não no desenho.
- [ ] Garantir que as guardas de decisão «Sim/Não» não chocam com linhas e que o fluxo não tem saídas/entradas ambíguas.
- [ ] Renderizar cada figura a tamanho de página e conferir tamanho mínimo legível.

### P0 — T09 Diagramas de SEQUÊNCIA
- [x] **Localizados:** DS01–DS04 no apêndice, divididos em painéis A/B/C; não registar como «diagramas inexistentes».
- [ ] Seguir a referência blockchain: colocar **sequências essenciais no Capítulo V em §5.2.5** com enquadramento e legendas; reservar **apêndice para diagramas complementares** sem duplicação injustificada.
- [ ] Reorganizar interacções, objectos, lifelines e mensagens com **textos em português e espaçamento suficiente**, reduzir microfontes e painéis demasiado comprimidos.
- [ ] Representar como **modelo conceptual**, distinguindo as operações não implementadas/testadas. Não acrescentar chamadas reais inexistentes.
- [ ] Actualizar lista de figuras, números e remissões cruzadas.

### P1 — T10 Diagramas de ESTADOS e ARQUITECTURA
- [ ] Rever os elementos da Figura 5.11 e 5.12, com rótulos de estado em português (**Pendente de acordo, Activa, Entregue, Concluída**, etc.) e notas externas concisas, sem termos inglês no corpo desenhado quando dispensáveis.
- [ ] Arquitetura com **«Sistema»** na fronteira e nomes de camadas em português; React/Django/PostgreSQL preservados como nomes de tecnologias.
- [ ] Não afirmar que pagamentos/contestações externos já estão implementados; manter «opcional» conforme arquitectura.

### P1 — T11 Limpeza da monografia versus documentos internos
- [ ] Varredura completa por `N01`–`N18`, `MR01`–`MR07` isolados, `D44`/`D50`–`D71`, «piloto sintético», «Prossegue», «tarefa», «commit», «gerado por», «captura não incluída» e «matriz interna». Corrigir somente ocorrências inadequadas, sem apagar conteúdo científico necessário.
- [ ] Explicar uma única vez Txx/Exx e usá-los de forma discreta em remissões para as entrevistas **preservadas no Anexo B**. Não eliminar a identificação dos depoimentos dentro dos anexos.
- [ ] Distinguir o que vai ao manuscrito (RN/RF/RNF, UC e diagramas) do que fica apenas no **backlog D72** e na **matriz D62**.
- [ ] Verificar termos PT-MZ uniformes, por exemplo **«âmbito»** em vez de «escopo» quando o documento adopta esse termo; não alterar citações literais dos entrevistados.

### P1 — T12 Revisão tipográfica e editorial integral
- [ ] Padronizar design de **quadros/tabelas da blockchain**, legendas acima e fontes abaixo, tipos e tamanhos de letra, entrelinhas, margens, sequência de títulos e quebras.
- [ ] Auditar coerência entre 28 RF / 16 RN / 7 RNF e casos de uso; eliminar matrizes duplicadas da monografia, preservando a versão interna no GitHub.
- [ ] Resolver índice, listas de figuras/quadros e referências cruzadas após mudança das imagens. Não deixar «figura de sequência» apenas no apêndice quando o capítulo anuncia sua apresentação no corpo.
- [ ] **Preservar as 183 perguntas, 183 respostas, 11 perfis, 14 comentários XML, materiais originais** e não divulgar transcrições no GitHub.
- [ ] Renderização final integral DOCX→PDF→PNG e inspeção visual das páginas afectadas **e de todo o documento**, sem texto ilegível/clipping/cardinalidade sobreposta.
- [ ] Registar separadamente os bloqueios que dependem de terceiros: consentimento, comentário do supervisor sem âncora, data de capa 2025 vs fontes/resultados 2026 e aprovação institucional.

## Critério de fecho

Uma versão D72+ só é «corrigida» após **auditoria comparativa com o Word blockchain, validação da tabela RF com 28 requisitos, diagramas em português sem sobreposições, sequências localizáveis no Capítulo V, remissão/índice válido, preservação literal de entrevistas e revisão visual**. Não confundir ficheiros gerados com evidências de qualidade verificada.

## Registo de execução

- 2026-11-07: **T01 concluída quanto ao inventário inicial**; leitura do Word blockchain e da ConecTA D71 feita. A estrutura actual contém `4.15`, `4.16`, `5.2.8` que devem sair; RF em quadro condensado de três colunas; diagramas de sequência foram localizados no Apêndice A.


## D72 — Etapa 1 concluída em cópia autónoma (07-11-2026)

**DOCX entregue na conversa, não no repositório:** `Monografia_ConecTA_D72_Etapa1_Estrutura_Indice_Validado.docx`.

- Base real: D71 com quadros tipográficos uniformizados e bibliografia corrigida.
- Capítulo IV reduzido a **4 CONTEXTO DE APLICAÇÃO**, §§4.1–4.2, em **duas páginas renderizadas** (págs. 36–37), em substituição das antigas 16 secções de contexto e rastreabilidade.
- Secção 5.2.8 de rastreabilidade interna removida e **N01–N18 retirados de todo o corpo académico**, mas as 16 RN, 28 RF e 7 RNF **mantidas**.
- A explicação dos pseudónimos Txx/Exx foi clarificada **uma vez no procedimento metodológico**, sem alterar a identificação dos depoimentos no Anexo B.
- D72 etapa 1: **101 páginas** na renderização, **85 entradas de índice**, **0 inconsistências título/página**, **0 links internos quebrados**.
- Comparação XML: **14 tabelas** e todos os media pré-existentes e `word/comments.xml` preservados byte a byte; **183 perguntas + 183 respostas** e perfis mantidos literalmente.
- **Limite:** ainda não se remodelaram os quadros RN/RF/RNF nem diagramas e esta cópia **não é versão para submissão**. O ponto seguinte é T03/T04/T05, depois T06–T10.
- SHA-256 da cópia: `4a5a7561fbfc13f1babb91ef03c71a29d9c312930d486a640e5d7a783a54ca47`.

**Nota de gestão:** GitHub Issues está desactivado no repo (HTTP 410); todas estas tarefas permanecem sob controlo através do backlog Markdown do PR académico.
