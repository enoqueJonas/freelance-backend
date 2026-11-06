# D67 — Integração efectuada no DOCX canónico recebido, com QA estrutural e renderização

**Estado:** 06-11-2026. Foi recebido em upload directo o DOCX canónico `Monografia_D44_Metodologia_Proveniencia_Verificada.docx`, com 82 páginas. A versão integrada D67 foi **criada e entregue no chat como DOCX editável de trabalho**, sem substituir o original. **Não publicar o ficheiro integral nos repositórios**, pois contém as onze entrevistas completas.

**Ficheiro de saída:** `Monografia_ConecTA_D67_Integracao_Documental_Entrevistas.docx`.

- SHA-256 base: `ba1239c31c31f1fa35aea24700224572e4f83e8b9fde65210d9cfef38aeb436d`.
- SHA-256 D67: `db6edc9bbbea64620c0b0f5de3ab09861e7fac67bb2e0e810e0f86b0f096930c`.
- **108 páginas** na renderização PDF de QA; Word actualizado a partir da D44, não reconstruído de texto indexado.
- **106 intervenções textuais/editoriais** registadas no script de integração, abrangendo Resumo/Abstract, §§1.6–1.9, partes do Capítulo II, Capítulos III–IV, §§5.1 e 5.3–5.5, Capítulo VI e notas do protocolo do Apêndice A.
- **Anexo A** com os cinco blocos do guião semiestruturado; **Anexo B** com 11 transcrições identificadas T01–T08/E01–E03; preservação exacta de **183 perguntas + 183 respostas + 11 perfis**, comparados carácter por carácter com o caderno D66, sem questionários e sem piloto sintético.
- **14 tabelas originais mantidas**. O pacote preserva os **46 ficheiros de imagem originais byte-a-byte** e adiciona três capturas reais das branches D55/D56 relativas a perfil de empregador, proposta e versão do acordo.
- `word/comments.xml` original preservado **byte-a-byte** com 14 textos de comentários. **A D44 de origem já não contém âncoras `commentReference` ou `commentRangeStart` no document.xml**, pelo que a retenção do ficheiro interno **não equivale à garantia de ancoragem visual activa**. Não eliminar estes comentários nem reconstruir âncoras arbitrárias.
- A estrutura do índice da D44 foi mantida e o Word marcado com `w:updateFields=true`; como houve repaginação e os anexos são novos, **abrir no Microsoft Word e actualizar o índice inteiro**. A imagem/PDF gerada pelo LibreOffice pode continuar a apresentar números em cache.
- Revisão visual realizada em mosaicos das 108 páginas e páginas críticas, incluindo figuras 5.13, 5.16 e 5.17. O sombreado cinzento de placeholders foi retirado. Os módulos de pesquisa integral, evidências, reputação e conflitos sem captura real continuam identificados como **não demonstrados**, em vez de imagens inventadas.

## Alcance científico incorporado

- A fundamentação dos requisitos é **primariamente bibliográfica/documental**; as entrevistas apoiam pontualmente e preservam divergências (T05, escrow em T02/T04/E01).
- As transcrições são tratadas como literais conforme confirmação expressa do responsável, sem supor áudio ou procedimentos éticos não comprovados.
- V01–V03 **parcialmente exercitados** em branches; V04–V08 não executados como casos canónicos; RNF02–RNF05 cobertura parcial e RNF01, RNF06 e RNF07 sem execução integral.
- HG e HE1–HE4 discutidas distinguindo suporte conceptual, implementação técnica parcial e impacto em Maputo não medido.
- O backend D50–D56 não é apresentado como branch principal ou versão de produção.

## Pendências antes da submissão

1. **Actualizar e conferir índice e paginação no Word**; verificar remissões de todas as figuras/tabelas.
2. **Rever a cobertura documental por páginas**, autoria da bibliografia e texto legal aplicável; D62 permanece auditoria de escopo, não confirmação integral de cada recorte.
3. **Resolver a cronologia** da capa e declaração de honra («Setembro de 2025») face ao relatório do Banco de Moçambique 2026 e evoluções técnicas de Novembro de 2026 — não alterar datas sem instrução da autoria.
4. **Conferir consentimento, riscos de reidentificação e autorização institucional** antes da circulação pública dos anexos integrais.
5. **Aprovação do supervisor e revisão académica de coerência fina**, incluindo avaliação das hipóteses, enquadramento, imagens e quadros.
6. **Revisar a correspondência das figuras 5.13–5.19**: as figuras sem capturas foram marcadas como não apresentadas; para um manuscrito definitivo, devem ser substituídas por evidência real quando possível, ou a numeração e as remissões devem ser reestruturadas.

**Importante:** D67 é uma **versão integrada de trabalho**, não uma monografia final aprovada e não está comprometida como DOCX integral no GitHub. O PR académico #2 continua draft.
