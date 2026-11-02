# Proposta D46 — Secção 5.5: Discussão dos resultados e limitações

**Documento-base:** `Monografia_D44_Metodologia_Proveniencia_Verificada.docx`, §5.5, pp. 62–63.  
**Material de suporte:** §§1.3–1.5, 3.2–3.7, 4.1–4.16, 5.2–5.4, 6.1–6.2 da D44; inspeção estática dos repositórios `enoqueJonas/freelance-frontend` e `enoqueJonas/freelance-backend`.  
**Estado:** texto académico proposto, **não integrado no DOCX canónico**, nem aprovado pela autora/supervisão. As subdivisões 5.5.1–5.5.5 são **propostas estruturais** e deverão ser avaliadas perante o manual USTM aplicável.

O texto entre as linhas de delimitação abaixo destina-se a integrar a monografia; notas de controlo editorial estão fora do corpo.

---

# 5.5 Discussão dos resultados e limitações

A discussão dos resultados deve ser interpretada à luz do objectivo de desenvolver um protótipo de aplicação web para apoiar a conexão e contratação entre trabalhadores autónomos de Tecnologias de Informação e empregadores na Cidade de Maputo. O trabalho produziu uma organização conceptual dos processos de intermediação e contratação, uma especificação de requisitos, modelos do domínio e uma implementação demonstrativa parcial. Estes contributos possuem níveis distintos de evidência: a coerência de uma especificação não equivale à implementação das funcionalidades nela previstas, assim como a existência de uma interface não comprova a sua adequação ao público-alvo.

Os resultados permitem apreciar de que modo os mecanismos propostos se relacionam com o problema de investigação. Não permitem, contudo, concluir que a aplicação melhorou efectivamente as práticas de descoberta, negociação ou contratação em Maputo. A ausência de comprovação da origem empírica dos onze registos temáticos, a integração incompleta do frontend com o backend e a falta de execução documentada dos ensaios de aceitação delimitam o alcance da presente discussão.

## 5.5.1 Correspondência entre os objectivos e os resultados obtidos

O primeiro objectivo específico consistiu na análise do processo de conexão e contratação e na identificação dos seus constrangimentos e necessidades. A revisão bibliográfica, a análise documental e a exploração dos registos textuais permitiram sistematizar dimensões relevantes: descoberta de oportunidades, demonstração de competência, identificação das partes, negociação, formalização, pagamentos, reputação e conflitos. Esta sistematização constitui um enquadramento exploratório e uma base para formular hipóteses de necessidades. Não permite caracterizar empiricamente a frequência, importância relativa ou distribuição desses constrangimentos entre trabalhadores e empregadores reais da Cidade de Maputo, uma vez que a proveniência da recolha dos onze registos permanece por comprovar.

Quanto ao segundo objectivo, foi estabelecida uma especificação conceptual que inclui as hipóteses de necessidades N01–N18, as regras de negócio RN01–RN16, os requisitos funcionais RF01–RF28 e os requisitos não funcionais RNF01–RNF07. A especificação distingue as capacidades pretendidas das restrições de acesso, integridade, privacidade e governação. A correspondência entre estas categorias fornece uma base para o desenvolvimento, mas a existência dos documentos não demonstra que a origem de cada requisito foi empiricamente validada. Em particular, a necessidade N18 representa uma condição de adopção dependente da participação efectiva no ecossistema, e não uma capacidade que possa ser garantida por uma função de software.

O terceiro objectivo previa conceber e desenvolver um protótipo funcional segundo os requisitos definidos. A componente de concepção encontra-se representada em casos de uso, diagramas de classes, actividades, sequências, estados e arquitectura lógica. No código consultado, o frontend React/TypeScript oferece componentes e operações demonstrativas para vários percursos, enquanto o backend Django/DRF dispõe de implementação parcial de contas, perfis e autenticação. Todavia, a interface utiliza dados e operações simulados localmente e não se encontra integrada com o domínio de contratação previsto. Assim, a concretização do terceiro objectivo é parcial, não sendo apropriado tratar a arquitectura-alvo como funcionalidade integralmente desenvolvida.

O quarto objectivo previa validar o protótipo perante os requisitos, identificando o respectivo grau de implementação. A análise estática do código permitiu classificar capacidades representadas, ausentes ou divergentes e estabelecer um protocolo prospectivo de verificação. Os cenários V01–V08 e as verificações RNF01–RNF07, porém, continuam sem resultados de execução documentados. A inspecção estática não constitui validação funcional, avaliação de usabilidade ou ensaio de integração. Consequentemente, foi realizado um diagnóstico preliminar de cobertura, mas não foi demonstrada a validação do protótipo requerida pelo objectivo.

## 5.5.2 Apreciação da hipótese geral e das hipóteses específicas

A hipótese geral sustenta que uma aplicação web concebida com base nas necessidades dos trabalhadores autónomos de TI e dos empregadores pode integrar mecanismos adequados para apoiar a conexão e as etapas principais da contratação. A modelação produzida mostra uma forma tecnicamente estruturada de combinar pesquisa, perfis, propostas, condições acordadas, registo de execução, pagamentos e acompanhamento de conflitos. Esta correspondência oferece **sustentação conceptual** à possibilidade de construir a solução. Não confirma, porém, que as necessidades tenham sido verificadas no público-alvo nem que os mecanismos sejam eficazes ou adequados nas condições reais de utilização em Maputo.

A primeira hipótese específica (HE1) relaciona descoberta e avaliação de prestadores com perfis profissionais, evidências de competência, oportunidades e pesquisa. Os requisitos e os modelos de interface representam esses mecanismos, e o frontend contém componentes demonstrativos de perfis, listagem e filtragem. A sua presença no código permite identificar uma **representação parcial da solução**, mas não demonstra a validade dos dados profissionais, a qualidade das pesquisas ou a melhoria efectiva na capacidade de trabalhadores e empregadores se encontrarem.

A segunda hipótese (HE2) refere-se ao registo das condições acordadas e à aceitação de alterações. O modelo proposto distingue o aceite de uma proposta da activação da contratação e prevê versões sucessivas do acordo, preservando as versões anteriormente aceites. Esta separação constitui um contributo relevante da especificação, pois permite definir autoria, momento e estado de cada alteração. Contudo, o frontend conserva um contrato simplificado e o backend não implementa integralmente a entidade de versionamento nem as transições previstas. A HE2 encontra, portanto, **sustentação de modelação**, não verificação funcional do mecanismo.

A terceira hipótese (HE3) associa confiança e gestão de conflitos à reputação bilateral, à contestação de avaliações, ao reporte e à preservação de registos. A especificação prevê avaliações vinculadas a relações elegíveis, contextualização da reputação e acompanhamento administrativo de ocorrências, sem atribuir à plataforma autoridade arbitral universal. O protótipo apresenta avaliações e operações simplificadas de disputa, mas não implementa o modelo completo de contestação e gestão autónoma do processo de conflito. Acresce que os dados iniciais de reputação da demonstração não constituem histórico transaccional comprovado. A HE3 está **conceptualmente representada e parcialmente simulada**, sem demonstração de impacto na confiança das partes.

A quarta hipótese (HE4) relaciona os pagamentos e o risco bilateral com condições acordadas e registos de estado, sem custódia de fundos pela aplicação. O modelo define a separação entre o estado operacional da contratação e o estado financeiro, admite pagamentos por etapa ou após entrega e prevê eventual integração externa desacoplada. No frontend, porém, o serviço de demonstração pode assinalar um pagamento como concluído sem confirmação de um prestador financeiro real e utiliza mensagens que sugerem custódia de fundos. Essas mensagens não representam a política da solução especificada. A HE4 tem **sustentação conceptual**, acompanhada de simulação financeira insuficiente para comprovar pagamentos, garantias ou redução de riscos.

A avaliação das cinco hipóteses é, assim, uma apreciação do seu suporte documental, conceptual e técnico. Não corresponde a confirmação ou rejeição por teste empírico. A formulação em termos de possibilidades de concepção pode ser discutida pela coerência dos modelos; a efectividade dos mecanismos depende de ensaios executados e de avaliação junto do público-alvo.

## 5.5.3 Confronto com a literatura e decisões de concepção

A Organização Internacional do Trabalho identifica nas plataformas digitais mecanismos de apresentação de perfis, intermediação, gestão de oportunidades e reputação, mas assinala também problemas associados a condições de trabalho, informação assimétrica e governação (OIT, 2021). O modelo proposto partilha com essas plataformas a organização de processos de descoberta e contratação. Difere, no entanto, da adopção automática de funcionalidades de uma plataforma comercial, ao considerar como opções de âmbito a avaliação técnica facultativa, a localização contextual e a ausência de custódia financeira própria.

Estas opções exigem uma distinção importante. A heterogeneidade dos serviços de TI torna plausível permitir evidências profissionais variadas e preços definidos após diagnóstico; não prova que todas essas escolhas sejam preferidas ou utilizadas pelos profissionais de Maputo. Do mesmo modo, a decisão de não exigir correspondência algorítmica obrigatória ou chat permanente é uma delimitação funcional, e não uma conclusão de que tais funcionalidades não tenham valor para qualquer utilizador.

No domínio dos pagamentos, a separação entre condições acordadas, declaração de pagamento e eventual confirmação externa contribui para uma modelação mais precisa do processo. Não elimina o risco de incumprimento, não substitui verificação de transacções e não implica que a plataforma seja um prestador financeiro. A documentação sobre inclusão financeira e economia digital pode enquadrar meios de acesso e limitações do ecossistema, mas não permite extrapolar estatísticas nacionais para o comportamento específico de profissionais autónomos de TI da Cidade de Maputo (Banco Mundial, 2019; Banco de Moçambique, 2025).

A principal contribuição da comparação com a literatura reside, portanto, em **fundamentar escolhas que podem ser verificadas posteriormente**, não em declarar que o protótipo produz os mesmos resultados de plataformas internacionais ou que os cenários do corpus correspondem a hábitos efectivamente observados.

## 5.5.4 Distância entre o modelo concebido e a implementação existente

A inspecção estática identificou uma separação entre arquitectura proposta e código disponível. A arquitectura prevê componentes de contas e perfis, oportunidades, propostas, contratações, acordos versionados, execução, pagamentos, reputação e conflitos. No backend consultado, os módulos centrais do ciclo de contratação ainda não materializam as respectivas entidades e operações. A persistência encontra-se configurada em SQLite, enquanto PostgreSQL integra a arquitectura-alvo.

No frontend, a autenticação demonstrativa recorre a registos locais e não constitui integração com os mecanismos de autenticação expostos pelo backend. O modelo de utilizador utiliza um papel principal exclusivo, embora a especificação permita perfis de trabalhador e empregador na mesma conta. As operações locais de contrato não asseguram, no estado examinado, todo o ciclo proposto de `PENDING_AGREEMENT`, `ACTIVE`, `DELIVERED` e `COMPLETED`, nem a preservação de versões aceites de um acordo.

O tratamento financeiro do protótipo deve ser distinguido de transacções reais. Um pagamento assinalado como concluído por uma função simulada não comprova liquidação, confirmação de uma carteira móvel ou custódia. Também o estado `disputed` aplicado ao contrato e as operações de decisão administrativa não representam integralmente a separação prevista entre a contratação e um processo próprio de acompanhamento de conflitos.

Estas diferenças impedem interpretar a existência de ecrãs ou de estruturas de código como cumprimento dos 28 requisitos funcionais e dos sete requisitos não funcionais. O estado do protótipo sustenta uma **demonstração de interface e de parte das regras simuladas**, não uma afirmação de conformidade integral da solução. A verificação de segurança e autorização, privacidade, integridade de registos, responsividade, manutenibilidade e interoperabilidade depende de critérios e evidências próprios, ainda não apresentados como resultados de execução.

## 5.5.5 Limitações, validade e implicações

A primeira limitação diz respeito à proveniência do corpus qualitativo. Estão disponíveis onze registos textuais codificados e um piloto expressamente identificado como sintético, mas a documentação examinada não permite confirmar a realização independente das entrevistas atribuídas à codificação posterior. Deste modo, a diversidade interna do corpus apoia a formulação de cenários e a comparação de alternativas, sem permitir atribuir padrões de comportamento, preferências ou frequências à população da Cidade de Maputo.

A segunda limitação relaciona-se com a implementação técnica. A distância entre o modelo-alvo e o código existente é particularmente significativa na formalização versionada, na execução, no registo de pagamentos, na contestação e nos conflitos. O emprego de dados locais simulados limita a interpretação do protótipo a funcionalidades demonstrativas e impede inferências sobre persistência multiutilizador, integrações externas ou integridade de registos em ambiente real.

A terceira limitação é a ausência de testes de aceitação executados com resultados documentados. O protocolo previsto organiza os cenários, mas os seus critérios ainda não foram confrontados com comportamento observado. De igual modo, não foram realizados ensaios documentados com participantes que permitam avaliar compreensão, esforço, utilidade percebida ou adequação da interface ao processo real de contratação.

Estas limitações não anulam a utilidade da especificação como artefacto de engenharia. Delimitam, antes, o que o estudo efectivamente produziu: um enquadramento exploratório, um conjunto de requisitos candidatos e uma arquitectura conceptual, acompanhados por uma implementação demonstrativa parcial. A sua continuidade exige comprovar a origem dos dados qualitativos, confirmar ou rever necessidades com o público-alvo, integrar o domínio funcional e executar verificações adequadas. Até que essas etapas sejam concluídas, não se pode afirmar que a aplicação facilita efectivamente a conexão e a contratação entre trabalhadores autónomos de TI e empregadores na Cidade de Maputo.

---

## Matriz de controlo da revisão (não incluir no corpo da monografia)

| Elemento | Documento D44 | Integração proposta | Verificação exigida |
|---|---|---|---|
| 5.5 | Três parágrafos, sem avaliação individual HG/HE1–HE4 | 5.5.1–5.5.5 com objectivos, hipóteses, comparação, técnica e validade | Confirmar se subdivisão é permitida pelo manual USTM |
| OE1 | Identificação de necessidades e constrangimentos | Delimitar como análise documental e exploratória | Evidência de campo em falta |
| OE2 | Baseline conceptual de 28 RF | Reconhecer especificação, sem pressupor aprovação ou validação empírica | Confirmar decisões de âmbito |
| OE3 | Protótipo funcional conforme requisitos | Classificar como implementação parcial/demonstrativa | Integração, domínio e testes |
| OE4 | Validar face aos requisitos | Distinguir diagnóstico de cobertura de ensaios | Resultados V01–V08 e RNF01–RNF07 pendentes |
| HG/HE1–HE4 | Hipóteses definidas em §1.4 | Apreciação individual sem linguagem de prova empírica | Revisão académica |
| RN10/HE4 | Sem custódia no modelo; mensagens do mock contraditórias | Mostrar divergência e evitar prometer garantias financeiras | Corrigir a simulação ou separá-la claramente da solução |
| RN13/HE3 | Moderação, não arbitragem | Distinguir estado do conflito e decisão sobre direitos | Rever regras e implementações |
| Literatura | OIT/BM/BdM já citados na D44 | Confrontar princípios sem atribuir dados específicos a Maputo TI | Verificar a referência completa e a cronologia da fonte |

### Gatilhos de não integração

- Não inserir resultados de testes ou entrevistas que não foram efectivamente produzidos.
- Não manter o texto anterior da secção 5.5 em duplicado.
- Não apresentar este quadro de controlo como «Quadro» da investigação.
- Não inserir caminhos GitHub, commits, notas de processo, títulos «D46» ou observações do auditor no corpo académico.
- Rever o resumo e a conclusão para manter a mesma avaliação da hipótese geral e dos objectivos.
- Preservar todos os comentários, figuras, estilos e campos da D44 durante integração autorizada.
