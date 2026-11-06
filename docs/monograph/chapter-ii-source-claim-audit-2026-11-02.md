# D42 — Auditoria científica das afirmações do Capítulo II (02/11/2026)

**Artefacto:** `Monografia_D42_Revisao_Cientifica_Capitulo_II.docx` (entregue no chat).  
**Baseline:** `Monografia_D41_Auditoria_Bibliografica.docx`.  
**Foco:** Capítulo II, secções 2.1–2.13; verificação substantiva de afirmações seleccionadas, terminologia e limites de extrapolação. Revisão com base nos PDFs originais disponíveis e nas páginas oficiais das normas técnicas. A monografia **não** foi tratada como material de conhecimento comprovado apenas por conter uma citação.

## Fontes primárias consultadas e correspondência

| Afirmação/tema | Fonte primária efectivamente consultada | Conclusão auditada e limite |
|---|---|---|
| Tipologia web vs. baseada na localização, modelos freelance/microtarefas | OIT, *World Employment and Social Outlook 2021* (`wcms_771749.pdf`; quadro de conteúdos pp. físicas 8–9 e capítulos 2–4) | Suportada como tipologia internacional; **não** medir frequência de tais modalidades em Maputo |
| Trabalho online, remuneração e riscos | OIT, *Digital labour platforms and the future of work* (`wcms_645337.pdf`; resumo executivo, pp. PDF 17–22) | Cobertura primordial de **crowdwork/tarefas online**; não generalizar incidência nem conclusões ao conjunto de freelancers TI de Maputo |
| Matching, ratings, gestão algorítmica e efeitos de rede | OIT, 2021; sumário executivo e capítulo 2; [página oficial de síntese](https://www.ilo.org/infostories/en-GB/Campaigns/WESO/World-Employment-Social-Outlook-2021) | Fonte descreve mecanismos e efeitos; proposta de pesquisa manual/filtros é **escolha de concepção** e não teste empírico de superioridade |
| Pilares da economia digital de Moçambique | Banco Mundial, 2019, `MozambiqueDECA.pdf`, sumário/índice PDF pp. 6–12 | Cinco pilares: infra-estrutura, plataformas, serviços financeiros, empreendedorismo e competências digitais. Dados nacionais não caracterizam especificamente os participantes |
| Informalidade nacional | INE, `ddi-documentation-portuguese-89.pdf`, capa e metadados PDF pp. 1–3 | Documento é **metadados do inquérito INFOR**, gerado em 25/04/2023, não relatório analítico completo. Não atribuir-lhe estatísticas ou conclusões não disponíveis no documento |
| Política financeira e confiança | Banco de Moçambique, *ENIF 2025–2031*, PDF pp. 8–10; relatório anual de inclusão | Fonte identifica protecção do consumidor e pagamentos digitais; **não** garante integração PSP nem autoriza o software a custodiar fundos |
| Requisitos de engenharia | [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html); [IEEE Standards](https://standards.ieee.org/ieee/29148/6937/) | O escopo normativo confirma processos e itens de informação de requisitos. Sem acesso ao texto integral da norma, usar apenas o resumo institucional/descrição pública; **não** atribuir recomendações de cláusulas não consultadas |
| UML | [OMG UML 2.5.1](https://www.omg.org/spec/UML/2.5.1) (versão de Dezembro de 2017) | Referencial oficial para as categorias de diagramas; diagramas da monografia representam **modelo lógico**, não testes de implementação |
| Segurança web | [OWASP ASVS v5.0.0](https://asvs.owasp.org/) (publicada em 30/05/2025) | Referencial técnico de requisitos de segurança; **não** se declara conformidade do protótipo sem execução de testes e revisão específica |

## Edições realizadas e motivo científico

**21 parágrafos do Capítulo II modificados, sem substituição global do texto:**
- §2.1: parágrafos 116 e 117 — precisar tipologia, alcance da investigação de 2018 e impossibilidade de extrapolação para Maputo;
- §2.2: 125, 127, 128 — corrigir os cinco pilares, explicitar que INFOR disponível é metadados e separar contextualização financeira da decisão «sem custódia»;
- §2.3: 130, 133 — distinguir descrição do matching algorítmico da decisão de usar pesquisa/filtros;
- §2.4: 138 — tornar a confiança bilateral e os critérios transparentes, em vez de duplicar mecanismos de reputação;
- §2.5: 143 — separar termos da plataforma e acordo bilateral versionado, que é escolha do domínio proposto;
- §2.6: 147–148 — não afirmar autorização regulatória ou incidência estatística de incumprimento local a partir de fontes internacionais;
- §2.7: 153 — clarificar as limitações de ratings e que contestação ainda precisa de validação;
- §2.8: 158 — evitar equiparar acompanhamento administrativo a arbitragem;
- §2.9: 163–164 — distinguir critérios OWASP e recomendações de acesso da conformidade funcional não demonstrada; não confundir desafios nacionais com testes de responsividade;
- §2.10: 166 — fundamentar comparação de mercados no guia efectivamente consultado (Upwork), evitando afirmações laterais sobre LinkedIn sem fonte;
- §2.11: 174–175 — dar base institucional a engenharia de requisitos/iteratividade e ressalvar que rastreabilidade documental não é implementação;
- §2.12: 177 — citar a especificação oficial da UML;
- §2.13: 180–181 — descrever o desenvolvimento incremental como estratégia, não realização demonstrada.

## Bibliografia e integridade do ficheiro

- Inclusas três novas entradas **efectivamente citadas no Capítulo II**: ISO/IEC/IEEE (2018), Object Management Group (2017) e OWASP (2025), junto às nove existentes. **12 referências no total**. Os anos e versões foram verificados nas páginas institucionais. As entradas foram reorganizadas alfabeticamente, mantendo alinhamento à esquerda e recuo suspenso.
- Formato USTM preservado, sem alteração ao Capítulo III–VII, a quadros, aos diagramas de modelação e às secções de apêndices. `word/comments.xml` da D42 é **idêntico byte a byte** ao da D41: **14 comentários** mantidos.
- DOCX renderizado novamente: **82 páginas totais**, Intro na física 11, Bibliografia na 67: **57/60 páginas do corpo**. Capítulo II nas físicas 19–30; anexos iniciam na física 68. Foram produzidas e inspeccionadas folhas de contacto do Capítulo II e da bibliografia, com inspecção a tamanho integral da bibliografia.
- O índice automático não precisou de atualização de páginas porque os títulos e as páginas de início de capítulo se mantiveram.
- Estão por resolver outros defeitos herdados (por ex. marcações coloridas em quadro de comparação, página 3 em branco e sete figuras de interfaces sem evidência real).

## Riscos e trabalhos que continuam abertos

1. **Cadeia citação → proposição → página da fonte:** este trabalho verificou directamente as fontes que sustentam as principais proposições corrigidas, mas não todas as afirmações do manuscrito nem todos os dados numéricos de todos os capítulos. M10 e M03 **ainda abertas**.
2. **Fontes técnicas de referência:** foi usada a documentação institucional **publicamente acessível** de ISO/IEC/IEEE 29148 e OMG UML, sem afirmar leitura integral de documentos de acesso condicionado. OWASP ASVS citado como referencial técnico, sem certificar conformidade.
3. **Hipóteses e resultados empíricos:** a evidência de 11 entrevistas não deve ser substituída por inferências da OIT nem por estatísticas nacionais. A reconciliação parágrafo→entrevista permanece em M04/M05.
4. **Cronologia:** a capa apresenta «Setembro de 2025», mas existe citação ao relatório do Banco de Moçambique divulgado em Julho de 2026. A data deve ser confirmada documentalmente antes de se alterar.
5. **Validação do software:** as figuras de interface 5.13–5.19 e os testes V01–V08/RNF01–RNF07 continuam sem prova de execução; não transformar opções de desenho em resultados.

**Estado:** D42 é versão intermédia e M03/M10 são parcialmente tratadas, **não** encerradas.
