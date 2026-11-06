# D69 — Integração efectiva no DOCX canónico e verificação de índice

**Estado:** nova versão de trabalho editável **entregue no chat** como `Monografia_ConecTA_D69_Integrada_Indice_Validado.docx`. **Não publicar o ficheiro no repositório público:** contém transcrições integrais de entrevistas. A D44 original foi preservada sem sobrescrita. Revisão científica ainda condicionada a validações académicas e éticas.

## 1. Entradas, versões e integridade

- **DOCX canónico de base:** `Monografia_D44_Metodologia_Proveniencia_Verificada.docx`, disponibilizado novamente como anexo de conversa; hash SHA-256 `ba1239c31c31f1fa35aea24700224572e4f83e8b9fde65210d9cfef38aeb436d`.
- **Anexos:** `D66_Anexos_Entrevistas_Semiestruturadas_ConecTA.docx`, com o guião dos cinco blocos e onze transcrições literais T01–T08/E01–E03, previamente conferidas com o ficheiro original `Estudo_de_Mercado_Entrevistas_e_Inquerito_TI_Maputo(1).docx`.
- **Saída D69:** `Monografia_ConecTA_D69_Integrada_Indice_Validado.docx`, hash SHA-256 `ddd4ff986ff89d341f5326cc0cb9d9570f59660010b38db94af7cea8a7637973`.
- **Derivação:** D67 integrou o texto e anexos numa cópia da D44; D68 corrigiu os elementos do índice; D69 compactou somente espaçamento no final do índice para eliminar a página em branco provocada por overflow. O DOCX D69 é a versão preferida para revisão, não D67/D68.

## 2. O que foi efectivamente editado no Word

- Resumo e Abstract actualizados para distinguir fontes documentais principais, onze entrevistas subsidiárias e implementação/testes parciais.
- Capítulo I §§1.6–1.9, Capítulo II emendas de proveniência, Capítulo III §§3.1–3.7, Capítulo IV §§4.1–4.16, Capítulo V (entradas, estado técnico, figuras parciais, quadros de aceitação e discussão de HG/HE1–HE4) e Capítulo VI (conclusão e recomendações) foram reconciliados **cirurgicamente**, adaptando as propostas académicas D62–D65 ao DOCX original para não destruir tabelas/figuras.
- O quadro de implementação e os quadros de V01–V08/RNF foram actualizados para reflectir cobertura **V01–V03 parcial** e **V04–V08 sem execução canónica integral**. Ensaios de Django/React em branches draft não equivalem a aceitação académica completa nem a publicação em produção.
- Inseridas três capturas reais de ensaios de branches para Figuras **5.13, 5.16 e 5.17**. Figuras **5.14, 5.15, 5.18 e 5.19** permanecem explicitamente assinaladas como sem demonstração visual completa, sem imagens fabricadas.
- Acrescentada secção **9 ANEXOS**, com **Anexo A — guião semiestruturado** e **Anexo B — onze transcrições literais**. Não se incluiu o questionário estruturado nem o piloto sintético como investigação de campo.
- O índice Word foi actualizado mantendo o seu campo e introduzindo entradas para os três novos títulos dos anexos.

## 3. Verificações estruturais automáticas

- **108 páginas** no PDF de verificação produzido a partir de D69; **99 entradas do índice** confrontadas com títulos e páginas correspondentes: **0 discrepâncias**. Não existe a página em branco extra presente na renderização intermédia D68.
- **46 ficheiros de imagem originais** preservados **byte a byte** na saída. **14 tabelas** conservadas.
- **14 comentários do supervisor** presentes na parte `word/comments.xml` e essa parte é **byte a byte idêntica** à D44 original. **Ressalva:** a D44 original já não apresentava marcadores `commentRangeStart/commentReference` em `word/document.xml`; a preservação do XML não prova que os comentários estejam ancorados de modo interactivo a trechos do corpo. Verificação de ancoragem é tarefa separada.
- As onze entrevistas incluem **183 perguntas e 183 respostas** cuja sequência textual foi comparada exactamente com os blocos do D66 original.
- Rendimentos de controlo: páginas 1, 5, 8, 9, 44, 61, 63, 64, 68, 72, 87, 88, 89, 107 e 108 inspeccionadas em imagens; os demais elementos de conteúdo já tinham sido inspeccionados na renderização intermédia D67, sendo a única alteração visual da D69 o índice (e a eliminação da página em branco).

## 4. Critérios científicos / editoriais ainda não fechados

- [ ] **Confidencialidade e consentimento:** verificar autorização para reproduzir e circular todas as transcrições integrais; confirmar riscos de identificação indirecta. Não publicar DOCX em repositório aberto antes desta revisão.
- [ ] **Cronologia:** capa e declaração continuam «Setembro de 2025», mas bibliografia e ensaios técnicos incluem fontes/resultados de **2026**. A data de revisão deve ser acordada com a autora/supervisão, não inventada pelo auditor.
- [ ] **Bibliografia:** conferir páginas exactas e autoria das publicações usadas na D62, especialmente a literatura da OIT, e reconciliar citação e lista final. Conferir quadro jurídico de pagamentos antes de afirmar obrigações específicas.
- [ ] **Comentários:** os 14 comentários estão no pacote, mas a ancoragem não foi demonstrada porque faltam marcadores na D44 de origem.
- [ ] **Aceitação:** V01–V03 incompletos, V04–V08 não executados integralmente. É incorrecto declarar as hipóteses ou os RF como empiricamente validados por mera execução de testes automatizados.
- [ ] **Figuras:** completar evidências reais 5.14/5.15/5.18/5.19 ou manter a ausência declarada; não substituir por imagens sintéticas.
- [ ] **Aprovação institucional:** revisão da autora/supervisão, das normas do manual e das tabelas/capítulos antes de submissão formal.

**Conclusão:** o bloqueio de acesso aos bytes da D44 foi resolvido, e existe **Word editável integrado e indexado**, mas ainda **não é uma monografia academicamente finalizada/aprovada**. As entrevistas continuam fonte subsidiária, como decidido no precedente blockchain/Xitique.
