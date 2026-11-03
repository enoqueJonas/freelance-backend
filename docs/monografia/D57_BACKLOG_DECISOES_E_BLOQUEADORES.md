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

**Adenda D58 — descoberta crítica em versão histórica:** o `DraftMonografia.docx` afirma **83 participantes (68 trabalhadores, 15 empregadores) de 1 a 30-07-2025**, com questionários, entrevistas, observação e percentagens. A Figura 2 refere **30 respostas (96,7% trabalhadores; 3,3% empregadores)**, sem reconciliação dos denominadores e subconjuntos. Estes números e procedimentos ainda **não foram autenticados**; o corpus D44 tem onze perfis textuais de origem independente não confirmada. A prioridade **é recuperar os dados originais de 2025 antes de iniciar entrevistas novas ou aceitar a reformulação documental**. Consultar [D58 — auditoria 83 vs 11](D58_AUDITORIA_83_PARTICIPANTES_VS_11_PERFIS.md) e [protocolo de recuperação/recolha](D58_PROTOCOLO_VERIFICACAO_E_RECOLHA_EMPIRICA.md).

## P0-02 — Resolver proveniência de entrevistas e desenho científico

**Situação actual:** o piloto com 11 entrevistas está expressamente identificado como sintético; T01–T08 e E01–E03 não dispõem de documentação primária suficiente para comprovar recolha independente. D44 §§1.6, 3.2.2 e 6.1 reconhecem o problema; §§1.2, 3.2.1 e 3.5 contradizem-no.

- [ ] A autora deve confirmar se existem arquivos **autênticos e independentes do piloto sintético** de recrutamento/recolha/transcrição/consentimento, com tratamento de dados ético.
- [ ] Se existirem, auditar correspondência do corpus, datas, procedimentos, codificação e fontes antes de falar em entrevistas reais.
- [ ] Se não existirem, manter T/E como **registos exploratórios de trabalho** e rever objectivos, métodos, resultados e alcance das hipóteses.
- [ ] Verificar com a supervisão se investigação documental + prototipagem atende aos requisitos científicos da USTM; caso contrário, planear recolha empírica real.
- [ ] Não inventar participantes, entrevistas, depoimentos, consentimentos, triangulações ou frequências de problemas reais.
- [ ] Aplicar os patches metodológicos D57 apenas após decisão de autoria.

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
