# D45 — Matriz candidata de rastreabilidade N01–N18 → RN → RF/RNF → V

**Base:** D44, §4.15 (pp. 41–42), Quadro 5.2 (p. 45), Quadro 5.3 (pp. 46–47), Quadro 5.4 (p. 47), Quadro A.2 e A.3 (pp. 81–82).

**Natureza:** matriz **proposta pelo auditor** com base em coerência semântica. A D44 afirma haver rastreabilidade, mas **não** contém uma cadeia de ligações individuais integralmente comprovada. Não atribuir estas relações à autora como se fossem vínculos assinados. Antes de as integrar, conferir decisões de concepção, diagramas originais e rastreabilidade do corpus.

**Legenda do estado:**
- **Candidato directo:** há relação semântica clara entre a necessidade, a regra e a funcionalidade; falta confirmação documental da decisão e validação.
- **Candidato indirecto:** relação plausível, não suficiente para provar cobertura integral nem causalidade.
- **Sem RF:** necessidade ou condição não convertível de modo honesto em função da aplicação.
- **V não executado:** é uma associação com plano de teste, não um resultado de teste.

## 1. Vínculos por necessidade

| N | Necessidade formulada em §4.15 | RN candidata(s) | RF/RNF candidatos | Testes propostos | Grau / observações |
|---|---|---|---|---|---|
| N01 | Descoberta de oportunidades e profissionais além da rede imediata | RN01, RN02 (restrições contextuais) | **RF08, RF09**, RF07, RF10 | V02 | Directo em pesquisa; adopção e eficácia da descoberta não verificadas |
| N02 | Evidências profissionais diversas | **RN03**, RN15 (privacidade se houver documentos) | **RF03, RF05**, RNF03 | V01 | Directo; não pressupor avaliação técnica universal |
| N03 | Confiança e identificação bilateral | RN01, **RN15**, RN02 (selecção da contraparte) | **RF03, RF04, RF06**, RF28, RNF02, RNF03 | V01, V08 | Parcial; perfis e verificação são meios possíveis, **confiança** exige avaliação empírica |
| N04 | Pesquisa/filtragem/comparação sem matching obrigatório | RN02 (elegibilidade; indirecto), nenhuma RN própria para filtros | **RF08, RF09, RF10** | V02 | Directo; notar lacuna de cenário: V02 não exercita RF09 e RF10 explicitamente |
| N05 | Condições claras: escopo, preço, prazo e entregáveis | **RN05, RN08, RN09** | **RF13, RF18**, RF11 | V03, V05 | Directo; dados válidos e price-after-diagnosis não estão testados em execução |
| N06 | Registo e aceitação de alterações materiais | **RN06, RN14** | **RF14, RF17**, RNF04 | V03, V04, RNF04 | Directo no modelo; ausência de `AgreementVersion` no código |
| N07 | Formalização proporcional com evidência do acordo | **RN05, RN07, RN14** | **RF13, RF17**, RNF04 | V03, V04 | Directo; não impor assinatura electrónica avançada |
| N08 | Preservar decisões e comunicações relevantes | **RN14**, RN06 | **RF15, RF17**, RNF04 | V04 | Parcial: RF não assegura explicitamente *mensagens ligadas a decisões*; `mockApi.messages` não prova rastreabilidade |
| N09 | Valor, método, etapa e condições de pagamento | **RN09, RN10** | **RF18, RF19**, RF20 (facultativo) | V05, RNF07 se PSP | Directo para condições/estados; RF20 opcional não é pagamento já integrado |
| N10 | Reduzir risco bilateral de pagamento/entrega | **RN09, RN10, RN14**, RN05 | **RF16, RF17, RF18, RF19** | V04, V05 | **Lacuna de resultado:** registo e estados não provam redução de risco. Medida de eficácia futura necessária |
| N11 | Reputação bilateral após contratação elegível | **RN11, RN14** | **RF21, RF22** | V06 | Directo no modelo; registos de reviews iniciais no mock não sustentam elegibilidade comprovada |
| N12 | Contexto e contestação das avaliações | **RN12**, RN11 | **RF22, RF23** | V06 | Directo como requisito; contestação não implementada integralmente |
| N13 | Reporte e seguimento de conflitos | **RN13, RN14** | **RF24, RF25** | V07 | Directo; sem arbitragem por administrador |
| N14 | Preservar evidências ligadas ao conflito | **RN13, RN14**, RN16 (actos de moderação) | **RF24, RF25, RF17**, RNF04 | V07, RNF04 | Parcial: especificar evidência, autoria, integridade e permissão; quadro não é prova |
| N15 | Diferentes formas de serviço e de contratação | **RN03, RN04, RN07, RN08** | **RF07, RF11, RF13, RF18** | V02, V03 | Parcial; provar com cenários distintos: remoto, presencial, diagnóstico, preço variável |
| N16 | Localização contextual, não universal | **RN04** | **RF07, RF08, RF09**, RNF01 | V02 | Parcial; ensaio precisa de tentar serviço remoto sem localização obrigatória e presencial com localização relevante |
| N17 | Simplicidade e proporcionalidade na utilização | **RN07**, RN03 (restrições evitadas) | **RNF01**, RF13 (indirecto) | **RNF01**, V03 | Sem simples RF correspondente; **usabilidade só pode ser validada com tarefas/observações**, não inferida do design |
| N18 | Massa crítica/utilizadores e oportunidades suficientes | — | **Sem RF** | **Sem V funcional** | Condição de adopção/ecossistema; depende de mercado e métricas de adopção, não execução do software isoladamente |

**Limitação importante:** a menção a RN03, RN04, RN15 etc. não significa que cada regra tenha uma origem empírica específica confirmada. Estas ligações são uma proposta de rastreabilidade com base no **conteúdo** da D44.

## 2. Requisitos sem origem exclusiva em N01–N18

A rastreabilidade inversa exige aceitar que parte das regras e requisitos decorre de **restrições de segurança, governação, engenharia ou decisão de âmbito**, e não de uma necessidade demonstrada pelo corpus. Forçar uma ligação empírica artificial seria um erro.

| Elemento | Origem possível | O que precisa de documentação |
|---|---|---|
| RF01/RF02 registo e autenticação | Pré-condição técnica para perfis e autoria; RNF02 | Justificar como habilitador técnico, não «necessidade mencionada por entrevistados» |
| RF26 gestão de utilizadores | Governação e administração do sistema | Definir papéis e acções autorizadas; origem de decisão de engenharia |
| RF27 moderação de oportunidades | Segurança/governação e prevenção de abuso | Explicitar política e categoria de denúncias; não confundir com conflito de contrato |
| RF28 analisar verificação | RN15 e acção administrativa | Justificar minimização, critério de decisão, retenção, contestação e autorização |
| RN02 anti-autocontratação | Integridade do processo e conflito de interesse | Fonte normativa/de engenharia; cenário negativo V02 |
| RN10 sem custódia própria | Delimitação de serviços financeiros e redução de exposição normativa | Explicar que se trata de decisão de âmbito, **não** prova de cumprimento de normas nem de eliminação do risco |
| RN16 rastreio de moderação | Auditabilidade e controlo de acções administrativas | Requisito de governação, derivação não atribuível necessariamente ao corpus |
| RNF02–RNF04 segurança, privacidade e integridade | Normas técnicas e boas práticas de software + risco da operação | Citar fonte apropriada, definir verificações e não afirmar conformidade |
| RNF05–RNF07 responsividade, manutenção e interoperabilidade | Qualidade técnica do artefacto, contextos e integração opcional | Especificar critérios verificáveis compatíveis com o protótipo; sem prova de testes executados |

## 3. Matriz de evidência — o que falta para declarar cada ligação validada

Para cada necessidade N01–N18, a matriz académica final precisa de colunas adicionais:

| Campo | Exemplo de valor legítimo | Proibição |
|---|---|---|
| Proveniência | `Documento OIT 2021, página específica`; `Cenário T03 (corpus exploratório sem proveniência de campo confirmada)`; `Decisão de engenharia` | Inventar participante, data de entrevista, página ou consentimento |
| Tipo de inferência | Documento contextual / possível necessidade / restrição técnica / decisão de âmbito | Converter **uma hipótese** em resultado empírico |
| Regra e requisito | RN03 → RF05 | Afirmar ligação formal aprovada sem acta ou registo |
| Modelo | UC e figura efectiva verificada visualmente | Inventar UC de catálogo UC01–UC27 ausente do texto |
| Implementação | Ficheiro e commit inspeccionados, ou não implementado | Confundir o mock com backend Django |
| Critério de aceitação | V01 ou RNF02 com passos e oráculo | Confundir critérios planeados com testes passados |
| Resultado | `Não executado` ou resultado real e evidências de execução | Preencher «passou» antes de testar |
| Aprovação | Identificador/data da revisão (se existir) | Inventar aprovação do supervisor |

## 4. Lacunas no processo decisório da D44 que dependem de verificação

- **N10:** «reduzir risco bilateral» é uma alegação de resultado. Pode-se especificar mecanismos que *visam apoiar* a rastreabilidade; só dados, testes pertinentes ou estudo empírico autorizam afirmar redução efectiva.
- **N17:** «utilização simples» depende de tarefas, pessoas e critérios observáveis. O RNF01 não contém limiar e nenhum ensaio foi executado; não afirmar boa usabilidade.
- **N18:** a D44 age correctamente ao classificar como condição de adopção. A experiência com um protótipo não permite comprovar massa crítica de mercado.
- **N08:** não está claro que as *comunicações relevantes* sejam seleccionadas, associadas à contratação e preservadas conforme regras; o simples chat em localStorage não satisfaz RN14.
- **N03:** «confiança» é um constructo comportamental mais amplo que identificação/verificação. Não tratá-lo como automaticamente cumprido por RF06.
- **N15:** o modelo é flexível em teoria, mas não foram demonstrados ensaios para serviços de diferentes tipos.

## 5. Texto integrável para §5.2.8, sem extrapolações

> A rastreabilidade entre as dezoito hipóteses de necessidades e a especificação foi analisada por associação semântica entre as categorias do Capítulo IV, as regras RN01–RN16, os requisitos RF01–RF28 e os critérios de verificação previstos. N01–N17 orientam capacidades e restrições do modelo, enquanto N18 representa uma condição de adopção que não depende exclusivamente de funcionalidades do sistema. Parte dos requisitos, em particular os relativos à autenticação, privacidade e administração, resulta também de decisões de engenharia e governação, não podendo ser atribuída como necessidade empírica comprovada aos registos exploratórios. Esta correspondência constitui rastreabilidade conceptual; a sua validação técnica dependerá de implementação e ensaios, e a confirmação das necessidades dependerá de investigação junto do público-alvo.

**Inserir na versão final apenas após aprovar os vínculos e elaborar a tabela/quadros necessários para as normas da USTM.**

## 6. Critérios de fecho

- [ ] Rever e aprovar/rectificar os 18 vínculos propostos, sem atribuir origem empírica falsa.
- [ ] Distinguir RF que correspondem directamente às necessidades dos RF habilitadores, normas, governação e decisões de âmbito.
- [ ] Construir matriz final `N→origem→RN→RF/RNF→UC→V→implementação→resultado`.
- [ ] Preservar N18 como condição de mercado sem teste funcional fictício.
- [ ] Resolver planos para N08, N10, N17, N18 com avaliações adequadas e métricas definidas **antes** da recolha.
- [ ] Nenhum teste de execução declarado concluído e nenhuma nova conclusão atribuída a entrevistados sem proveniência.
