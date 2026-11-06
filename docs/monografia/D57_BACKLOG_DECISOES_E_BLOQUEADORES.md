# D57 — Registo de decisões pendentes e tarefas P0/P1 da monografia

**Data:** 03-11-2026. **Estado:** backlog operacional; não implica autorização, aprovação ou tarefa concluída.  
**Ramo:** `audit/monografia-d45-coerencia-cientifica`, PR académico #2.  
**Nota de gestão:** foi tentada a criação de Issues GitHub para estes bloqueadores, mas a API devolveu **HTTP 410 — "Issues has been disabled in this repository"**. Por conseguinte, as tarefas ficam aqui, no repositório versionado. Não inventar IDs ou links de issues que não existem.

## P0-01 — Acesso à D44 canónica editável e preservação do Word

**Situação actual:** o `Monografia_D44_Metodologia_Proveniencia_Verificada.docx` (82 páginas) está indexado e pode ser lido no Project, mas a materialização dos bytes originais falhou: `This Project file does not have an authorized raw-byte materialization path`. Pesquisas exactas do nome canónico na conta Google Drive ligada não identificaram uma cópia que pudesse ser descarregada com segurança.

**Não se deve:** reconstruir um .docx a partir do texto extraído, eliminar imagens/UML, resolver comentários do supervisor automaticamente ou simular um ficheiro actualizado.

- [ ] Disponibilizar bytes originais da D44 por upload directo ou URL Drive exacto verificável.
- [ ] Guardar cópia de segurança e checksum antes de qualquer edição.
- [ ] Inspeccionar estrutura OOXML, campos automáticos, secções, bordas, imagens, listas, notas e comentários da supervisão.
- [ ] Aplicar **apenas alterações revistas** dos documentos D57, preservando formato e figuras.
- [ ] Exportar DOCX + PDF e inspeccionar todas as páginas para sobreposição, margens e numeração.
- [ ] Verificar que não há textos do auditor, prompts, mensagens de commit ou placeholders involuntários no corpo final.

**Actualização D59 — decisão de metodologia:** a recolha foi realizada por **entrevistas semiestruturadas**, sem questionários. Alegações quantitativas do draft anterior foram arquivadas, **fora do escopo**. Não voltar a pedir ficheiros de respostas, validar percentagens nem programar inquéritos. A tarefa activa consiste em conferir o **arquivo primário das entrevistas efectivamente realizadas**, a quantidade e o vínculo com a codificação T01–T08/E01–E03, separando o piloto sintético. Consultar [D59](D59_DECISAO_METODOLOGICA_ENTREVISTAS_SEMIESTRUTURADAS.md) e [protocolo actualizado](D58_PROTOCOLO_VERIFICACAO_E_RECOLHA_EMPIRICA.md).

> **Actualização D60:** o responsável confirmou que o DOCX de 21 páginas agora entregue contém as **onze transcrições literais originais não editadas**, identificadas como T01–T08/E01–E03. A descrição anterior de ausência de registos primários textuais está ultrapassada. Prossegue a análise temática, a conferência das condições de produção/consentimento e a correspondência com a D44; gravações áudio não são obrigatórias. Ver [D60](D60_CONFIRMACAO_TRANSCRICOES_LITERAIS.md).

## P0-02 — Documentar e relacionar entrevistas semiestruturadas efectivamente realizadas

**Método confirmado pela D59:** entrevistas semiestruturadas; a opção por questionários ou a reformulação para investigação exclusivamente documental **não está em discussão**. O problema pendente é a rastreabilidade da recolha: a D44 apresenta perfis T01–T08/E01–E03, mas os respectivos originais não foram localizados no acervo acessível. Um piloto sintético também aparece no histórico e deve ficar separado.

- [x] Confirmar técnica de recolha: **entrevistas semiestruturadas**.
- [ ] Localizar o guião realmente aplicado e a documentação de realização das entrevistas, respeitando privacidade e ética.
- [ ] Registar o número efectivo de entrevistas a partir do arquivo original; **não assumir n=11** apenas porque há onze perfis na D44.
- [ ] Relacionar cada entrevista, registo de notas/transcrição e excerto à codificação temática T/E, com datas e procedimentos na medida em que estão documentados.
- [ ] Excluir o piloto sintético de qualquer conjunto de evidências de participantes reais.
- [ ] Rever Capítulos III, IV, §5.5 e VI e a matriz N01–N18 segundo os resultados autênticos, não segundo percentagens históricas.
- [ ] Não inventar participantes, depoimentos, consentimentos ou generalizações sobre a Cidade de Maputo.
- [ ] Aplicar o [protocolo de verificação D59](D59_DECISAO_METODOLOGICA_ENTREVISTAS_SEMIESTRUTURADAS.md) antes da integração na D44.


## P0-03 — Aprovar requisitos, estados e cronologia do manuscrito

- [ ] Confirmar a baseline de **16 RN, 28 RF e sete RNF** e a transição do documento anterior RF001–RF031, sem tratar a palavra «aprovada» como prova de decisão formal.
- [ ] Confirmar com autora/supervisão os estados `PENDING_AGREEMENT`, `ACTIVE`, `PROPOSED`, `ACCEPTED`, `SUPERSEDED` e `REJECTED`, os dois aceites explícitos e a regra de autocontratação.
- [ ] Só depois alinhar UC13/UC14, Figura 5.2, Figura 5.4, Figura 5.11 e Apêndices A.3/A.4 à implementação técnica.
- [ ] Seleccionar qual revisão/commit do backend e frontend **faz parte da versão académica**; as alterações D50–D56 ainda são PRs draft.
- [ ] Resolver **capa Setembro de 2025 vs referências e testes de 2026** com o calendário universitário e uma cronologia defensável.

## P0-04 — Substituir as afirmações científicas ultrapassadas de §§5.3–5.5 e Capítulo VI

- [x] Redigir [matriz D57 V01–V08/RNF01–RNF07](D57_MATRIZ_VALIDACAO_V01_V08_RNF.md).
- [x] Redigir [Capítulo V revisto](D57_CAPITULO_V_REVISAO_INTEGRAL.md).
- [x] Redigir [Capítulo VI e patches transversais](D57_CAPITULO_VI_CORRECOES_TRANSVERSAIS.md).
- [x] Corrigir errata V04 em relatórios D52–D54.
- [ ] Revisar as redacções com a autora, sem presumir aprovação; confirmar que a fase técnica D50–D56 pode entrar nos resultados.
- [ ] Integrar todas as partes no DOCX original, não somente no GitHub.
- [ ] Verificar estados exactos: **V01–V03 parcialmente exercitados; V04–V08 não executados**; RNF02–RNF05 parcialmente verificados tecnicamente, sem RNF01/usabilidade com participantes.

## P1-05 — Figuras 5.13–5.19 e Apêndice A

- [ ] Rever [capturas reais D56](https://github.com/enoqueJonas/freelance-frontend/actions/runs/41612082795/artifacts/13219546872) e etiquetar como dados sintéticos.
- [ ] Preparar composições fiéis para **5.16 oportunidade/proposta** e **5.17 acordo/histórico** e, se apropriado, parte da **5.13 perfis**; falta captura completa de login.
- [ ] Não preencher **5.14 filtros, 5.15 evidências profissionais, 5.18 reputação, 5.19 conflitos** com imagens de `mockApi` apresentadas como funções reais.
- [ ] Se não existirem imagens reais, adequar títulos/legendas a propostas conceptuais **ou** remover figuras com renumeração autorizada.
- [ ] Atualizar Quadro A.1 preservando distinção UI legada vs rota `/#/real`.
- [ ] Confirmar listas automáticas de figuras, quadros e referências cruzadas após edição do Word.

## P1-06 — Completar a validação funcional/não funcional

- [ ] Executar **V01** completo com evidências profissionais e persistência após nova sessão.
- [ ] Executar **V02** completo com filtros, pesquisa, regras de elegibilidade e propostas.
- [ ] Executar **V03** completo com alteração de prazo/preço, rejeição e aceitação de v2 em casos independentes.
- [ ] Implementar e executar **V04** (ExecutionRecord, entrega, DELIVERED/COMPLETED) sem confundir com acordo versionado.
- [ ] Implementar/testar V05 pagamentos (sem custódia), V06 reputação, V07 conflitos e V08 governação.
- [ ] Executar RNF01 com **participantes reais**, não um algoritmo de browser.
- [ ] Completar matriz RNF02–RNF07 e testar PostgreSQL em concorrência/segurança de produção antes de qualquer deployment.

## Fonte e critério de fecho

Cada tarefa P0/P1 deve referir evidência verificável, commit/branch, ambiente e decisão de quem aprova. Uma alteração num documento de auditoria **não altera por si só** o manuscrito original; uma suite de testes verde **não confirma** hipóteses sociais, nem torna a plataforma pronta para produção.

**Tarefas de maior risco para a defesa:** P0-02 (proveniência empírica), P0-01 (Word canónico editável) e P0-03 (aprovação e cronologia). Resolver estes pontos antes de declarar a monografia finalizada.
