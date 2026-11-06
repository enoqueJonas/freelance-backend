# D66 — Preflight de integração: anexo autónomo produzido, D44 original indisponível para edição segura

**Estado (06-11-2026):** **ANEXOS construídos e verificados em DOCX autónomo**; não integrados no manuscrito canónico. Documento de trabalho disponível nesta conversa, **não publicado no GitHub** para proteger o corpus. O PR académico continua draft.

## 1. Ficheiro produzido

- **Nome de saída local:** `D66_Anexos_Entrevistas_Semiestruturadas_ConecTA.docx`.
- **Conteúdo:** `Anexo A — Guião semiestruturado` reproduz **os cinco blocos orientadores**; `Anexo B — Transcrições literais`, com **11 entrevistas** T01–T08 e E01–E03 em sequência, sem as perguntas do inquérito estruturado.
- **Fonte:** `Estudo_de_Mercado_Entrevistas_e_Inquerito_TI_Maputo(1).docx` (versão declarada pelo responsável como **literal, não editada**, com 21 páginas).
- **Hash SHA-256 da fonte:** `e85420e8d306c3914028fd75f24e56624d90d0df649e916ce9a49c6025a3e64f`.
- **Hash SHA-256 do anexo produzido:** `92be99d3c316922a784ca68ae4b3b8afbb9ccb749a73d5bf1560bf7ea23619a5`.
- **Inventário verificado:** **8 trabalhadores T01–T08, 3 empregadores E01–E03, 183 perguntas e 183 respostas**. Comparação programática carácter por carácter entre parágrafos `Pergunta:`, `Resposta:` e `Perfil:` da fonte e do DOCX de saída: **todas as sequências idênticas**. O cabeçalho da T01 foi separado do título «Entrevistas realizadas» apenas para organizar a secção; nenhum depoimento foi alterado.
- **Guia de entrevista:** reproduz literalmente apenas os cinco **blocos temáticos gerais** do instrumento. Não supor que exista um formulário rígido de perguntas idênticas administrado a todos.
- **Exclusões:** nenhuma pergunta de inquérito estruturado, nenhum gráfico/percentagem do inquérito, nenhum cenário do piloto sintético.
- **QA técnico/editorial:** arquivo DOCX passou no teste ZIP, renderização de **23 páginas**, verificação por amostra de páginas e contact sheet sem sobreposições observadas. Antes da incorporação na D44 verificar novamente paginação e remissões.
- **Privacidade:** não colocar texto integral dos depoimentos num repositório público. Antes da publicação académica, verificar consentimento de divulgação, nomes/identificadores indirectos e normas da instituição.

## 2. Por que a D44 não foi alterada

A D44 `Monografia_D44_Metodologia_Proveniencia_Verificada.docx` está localizável como arquivo indexado da Biblioteca (82 páginas; aproximadamente 6,4 MB), mas **duas tentativas de materialização de bytes originais** falharam: «This Project file does not have an authorized raw-byte materialization path». A D44 **não está montada em `/mnt/data`** neste ambiente.

A pesquisa na conta Drive por `D44` não devolveu cópia exacta. O ficheiro `DraftMonografia.docx` encontrado no Drive, de Fevereiro de 2026, contém uma versão anterior com conteúdo/estrutura diferentes; **não deve ser usado como substituto canónico** e não se realizou qualquer alteração sobre ele. Criar uma nova monografia a partir de texto indexado poderia eliminar **14 comentários do supervisor, quadros, diagramas, campos, imagens e formatação**. Essa substituição foi deliberadamente evitada.

## 3. Matriz de integração (dependências já disponíveis)

| Bloco da D44 | Fonte candidata | Acção ao recuperar o DOCX canónico |
|---|---|---|
| **Capítulo I §§1.6,1.7,1.9** | [D64](D64_CORRECOES_CAPITULO_I_E_CONTROLO.md) | Aplicar patches limitados e preservar comentários |
| **Capítulo II** | [D62](D62_EMENDAS_CAPITULOS_II_IV.md) | Conferir referências e substituir passagens incoerentes |
| **Capítulo III §§3.1–3.7** | [D64](D64_CAPITULO_III_METODOLOGIA_CONSOLIDADA.md) | Inserir integral mantendo numeração e secções |
| **Capítulo IV §§4.1–4.16** | [D63](D63_CAPITULO_IV_CONSOLIDADO_DOCUMENTAL.md) | Substituir texto, manter N01–N18 e remissões |
| **Capítulo V** | [D57 §§5.3–5.4](D57_CAPITULO_V_REVISAO_INTEGRAL.md) + [D65 §5.5](D65_DISCUSSÃO_HIPOTESES_CAPITULOS_V_VI.md) | Conferir quadros, figuras e remissões; não substituir provas por mocks |
| **Capítulo VI §§6.1–6.2** | [D65](D65_DISCUSSÃO_HIPOTESES_CAPITULOS_V_VI.md) | Aplicar conclusão/recomendações, respeitando níveis de evidência |
| **Anexo A + B** | `D66_Anexos_Entrevistas_Semiestruturadas_ConecTA.docx` (entregue **somente no chat**) | Inserir blocos e transcrições na versão canónica, com ética/confidencialidade |

## 4. Estado de controlo e próximo marco

- [x] Preparar **DOCX autónomo** com guião e onze transcrições literais.
- [x] Conferir **183 perguntas / 183 respostas / 11 perfis** com o original, carácter por carácter.
- [x] Excluir inquérito estruturado e piloto sintético.
- [x] Renderizar e inspeccionar amostras de páginas; resultado 23 páginas.
- [x] Não alterar o draft antigo nem reconstituir a D44 a partir de texto indexado.
- [ ] Obter **ficheiro D44 DOCX original em bytes editáveis**, por upload directo ou acesso autorizado que forneça os bytes.
- [ ] Inserir §§1.6–1.9/II–VI e os Anexos A/B no próprio Word, preservando **14 comentários**, figuras, índices, tabelas e estilos; coordenar referências cruzadas.
- [ ] Verificar ética e condições de divulgação dos depoimentos integrais.
- [ ] Resolver cronologia da capa Setembro/2025 versus fontes e ensaios de 2026.
- [ ] Renderizar **todas** as páginas da nova D44 e comparar com a cópia base antes da entrega.

**Resultado D66:** há um novo documento Word de anexos **utilizável**. A monografia D44 **continua não modificada**, e o bloqueio remanescente é acesso seguro ao original — não a ausência das transcrições ou falta de redacções académicas candidatas.
