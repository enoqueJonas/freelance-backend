# D64 — Correcções transversais do Capítulo I e controlo de integridade da metodologia

**Texto candidato**, não aplicado no DOCX D44.  
**Dependência:** [Capítulo III consolidado D64](D64_CAPITULO_III_METODOLOGIA_CONSOLIDADA.md), [Capítulo IV consolidado D63](D63_CAPITULO_IV_CONSOLIDADO_DOCUMENTAL.md), [D61 fundamentação documental principal](D61_MATRIZ_DOCUMENTAL_APOIO_ENTREVISTAS.md), [D60 transcrições literais](D60_CONFIRMACAO_TRANSCRICOES_LITERAIS.md) e [D57 verificação V01–V08/RNF](D57_MATRIZ_VALIDACAO_V01_V08_RNF.md).  
**Fonte principal dos trechos a corrigir:** `Monografia_D44_Metodologia_Proveniencia_Verificada.docx`, pp. físicas 15–18 e 31–35.

## 1. Capítulo I — §1.6 Metodologia: redacção substitutiva

A D44 original (p.16) afirma que não foram localizados registos primários capazes de confirmar a realização das entrevistas e que todas as interpretações se limitam a cenários exploratórios. O novo corpus de onze transcrições literais, entregue e confirmado pelo responsável como não editado, **ultrapassou essa descrição histórica**. A mesma secção fazia as necessidades parecerem derivadas principalmente dos textos T/E, ao passo que a decisão metodológica D61 estabelece **documental principal e entrevistas subsidiárias**.

**Proposta de substituição integral:**

> A investigação adopta uma abordagem predominantemente qualitativa, de natureza aplicada e carácter exploratório e descritivo. A **revisão bibliográfica e a análise documental** constituíram a principal base para caracterizar a intermediação e contratação de serviços autónomos de TI, identificar limitações e alternativas de concepção e fundamentar a especificação de necessidades, regras de negócio e requisitos da aplicação. Foram utilizadas fontes científicas, institucionais, normativas e técnicas relevantes ao contexto da investigação, sem extrapolar automaticamente resultados internacionais ou estatísticas nacionais para a população de trabalhadores autónomos de TI da Cidade de Maputo.
>
> **Complementarmente**, foram realizadas entrevistas semiestruturadas a trabalhadores autónomos de TI e empregadores ou clientes, cujas onze transcrições literais são identificadas por **T01–T08 e E01–E03**. Os depoimentos foram considerados para contextualizar situações e discutir **alguns** requisitos e decisões de desenho, incluindo divergências em relação às opções adoptadas, sem constituírem a origem exclusiva da especificação nem uma amostra estatística representativa. O guião e as transcrições são apresentados nos anexos, sujeitos aos cuidados necessários de confidencialidade.
>
> As decisões de engenharia foram traduzidas em modelos, arquitectura e funcionalidades do protótipo, cujo grau de implementação e os ensaios técnicos são apresentados separadamente. Os testes automatizados verificaram **subconjuntos** dos cenários de aceitação previstos, em ambiente controlado, sem demonstrarem a eficácia da plataforma na contratação real em Maputo. A metodologia distingue, por isso, **fundamentação documental, apoio qualitativo das entrevistas, decisão de especificação e verificação técnica**, evitando tratá-los como formas equivalentes de validação.

**Cuidado:** o texto candidato menciona anexos prospectivamente; **não entregar a D44 com essa afirmação até inserir os anexos**.

## 2. Capítulo I — §1.7 Considerações éticas: redacção substitutiva

A D44 p.16–17 associa directamente a ausência de provas primárias à inexistência de entrevistas confirmadas. Agora existem transcrições textuais, embora não se tenham demonstrado **procedimentos individuais de consentimento, gravação, recrutamento ou aprovação ética**. Não inventar tais procedimentos nem concluir que não houve consentimento só porque não foi encontrado o documento.

**Texto candidato:**

> O tratamento da informação qualitativa procurou limitar a exposição dos participantes, utilizando os identificadores T01–T08 para trabalhadores autónomos e E01–E03 para empregadores ou contratantes. Os registos de entrevistas disponibilizados são apresentados como transcrições literais, conforme identificação do responsável pela recolha. A utilização de códigos reduz a identificação directa, mas não elimina o risco de reconhecimento indirecto pela combinação de informações sobre profissão, empresa, datas ou projectos.
>
> A utilização e divulgação integral das transcrições devem respeitar os procedimentos éticos efectivamente aplicados no estudo e as exigências da instituição, incluindo informação aos participantes, consentimento e condições de acesso, quando documentados. A presente revisão **não presume** consentimento escrito, aprovação ética formal ou gravação áudio sem fonte que o demonstre. Antes da versão de divulgação, a inclusão dos anexos requer revisão de dados identificadores e confidencialidade, preservando a fidelidade do conteúdo das respostas.
>
> O material denominado «Piloto de Entrevistas — Dados Sintéticos», encontrado no histórico do projecto, foi separado das onze transcrições utilizadas na investigação e não constitui evidência de depoimentos de pessoas reais. Na descrição dos resultados, distinguem-se ainda relatos dos participantes, interpretações da investigadora e decisões de engenharia.

## 3. Capítulo I — §1.9 Estrutura do trabalho

A versão actual descreve o Capítulo III como análise de «registos de trabalho» e «piloto sintético» com «recolha empírica não comprovada», o que já não corresponde à fonte entregue.

**Substituir apenas as orações relativas ao Capítulo III e IV por:**

> O Capítulo III descreve a metodologia, materiais e métodos utilizados, destacando a análise bibliográfica e documental como fundamento principal da especificação, as entrevistas semiestruturadas de carácter complementar, a análise qualitativa dos respectivos registos e o desenvolvimento e verificação técnica do protótipo. O guião e as transcrições são apresentados nos anexos. O Capítulo IV examina o contexto de contratação e organiza as necessidades da solução com primazia da fundamentação documental, utilizando exemplos seleccionados das entrevistas para contextualizar ou questionar decisões de concepção.

**Nota:** não reescrever outras secções de §1.9 por estilo, apenas os trechos incoerentes.

## 4. Capítulo I — §1.5.2 Objectivo específico 1

A D44 estabelece «Analisar o processo actual ... identificando os principais constrangimentos e necessidades». Esta frase pode permanecer como **objectivo**, mas a interpretação dos resultados não deve declarar uma hierarquia de «principais problemas do mercado» estatisticamente comprovada a partir de onze entrevistas não probabilísticas.

**Recomendação:** manter o enunciado para preservar a baseline, mas formular o cumprimento no Capítulo VI como **sistematização de problemas, necessidades candidatas e experiências qualitativas contextualizadas**. Alterar o objectivo só com decisão da autora/supervisão.

## 5. Controlos entre os Capítulos III, IV, V, VI e anexos

| Eixo | Capítulo III (D64) | Capítulo IV (D63) | Capítulo V/VI (D57) | Anexo (D61) | Evidência/estado |
|---|---|---|---|---|---|
| Fundamento principal | §3.2.1 documental | §4.1 e §4.16 documental primeiro | Traço DOC→N→RN/RF | Não é apêndice bibliográfico | D62 identifica fontes mas nem todas as páginas foram conferidas |
| Entrevistas | §3.2.2 T01–T08/E01–E03 | Apoio selectivo com casos divergentes | Algumas decisões contextualizadas, hipóteses sem generalização | **Guião e onze transcrições literais** | Fonte entregue (21 pp.), anexo **não inserido na D44** |
| Sintético | Piloto explicitamente separado | Não fundamenta depoimentos reais | Testes usam contas sintéticas, não pessoas reais | **Não incluir piloto** | D60/D61 |
| Questionários | **Excluídos** do método | Sem percentagens de inquérito | Sem resultados quantitativos próprios | **Não incluir páginas iniciais de inquérito** | Decisão expressa D59 |
| Requisitos | DOC principal + engenharia + ENT opcional | N01–N18 preservados | RN01–RN16, RF01–RF28, 7 RNF, aprovação pendente | Entrevistas não substituem especificação | D45/D57/D61/D62 |
| Verificação técnica | §3.7 V01–V03 parcial, V04–V08 não executado | Não implica eficácia | D57 resultados por branch e revisão | Não é teste de software | 80 testes Django, 8 HTTP React, 2 Chromium; apenas subconjuntos canónicos |

## 6. QA editorial e riscos pendentes

### Concluído neste conjunto D64

- [x] Comparação com a D44 §§3.1–3.7 e §§1.6–1.7, incluindo contradições de proveniência do corpus.
- [x] Redacção integral candidata do Capítulo III com documental principal, entrevistas subsidiárias e técnica independente.
- [x] Manutenção da enumeração `3.1–3.7`, `3.1.1–3.1.4`, `3.2.1–3.2.2` e `3.3.1`.
- [x] Redacções candidatas específicas para §1.6, §1.7 e trecho de §1.9 da D44.
- [x] Separação entre testes automatizados e aceitação funcional integral; V04 = execução/entrega, não versionamento.
- [x] Preservação de opiniões divergentes e distinção entre depoimento, documento e decisão.
- [x] Estado original do Word tratado com honestidade: **não editado**.

### Bloqueadores antes de integrar e declarar finalizado

- [ ] Dispor dos **bytes originais editáveis da D44** para substituir trechos sem perder comentários, margens, imagens, campos, tabelas e formatação.
- [ ] Inserir os **anexos do guião e das onze entrevistas literais**, com revisão de dados identificadores, consentimento/documentação ética real e referências cruzadas.
- [ ] Obter informação factual sobre o registo das entrevistas (quem as conduziu, como as transcrições foram produzidas, condições de selecção e consentimento), **sem fabricar procedimentos**.
- [ ] Ratificar baseline RN/RF/RNF e a relação com N01–N18; confirmar a distinção entre planeamento, testes técnicos e validação académica.
- [ ] Confirmar páginas da bibliografia D62 e autoria de publicações, além de compatibilizar capa da D44 («Setembro de 2025») e materiais de 2026.
- [ ] Realizar QA visual completo do DOCX/PDF final, incluindo comentários de supervisão e paginação de anexos.

## 7. Próxima etapa proposta

**D65** deverá reconciliar as passagens do **Capítulo V e VI** ainda baseadas na antiga ideia de «onze perfis não comprovados» com D60–D64 e resolver a hierarquia DOC→ENG→ENT→TECH. A matriz de aceitação e a análise de hipóteses devem continuar proporcionais aos testes efectivamente executados, e nenhum anexo deve ser apresentado como existente no Word até ter sido inserido.
