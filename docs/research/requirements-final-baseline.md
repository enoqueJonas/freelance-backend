# Baseline Final de Requisitos — ConecTA

## 1. Critério de fecho

A baseline final resulta da cadeia:

`evidência → necessidade consolidada → regra de negócio → requisito → critério de validação`

Os requisitos foram revistos após a reconciliação dos 32 RF do draft e a modelação dos estados do domínio. A existência de uma funcionalidade no protótipo não é usada como justificação científica.

## 2. Regras de negócio finais

| ID | Regra |
|---|---|
| RN01 | Um utilizador pode possuir perfil de trabalhador, perfil de empregador ou ambos; o papel efectivo depende da acção/contratação. |
| RN02 | Um utilizador não pode ocupar simultaneamente os dois lados da mesma oportunidade/contratação. |
| RN03 | A demonstração de competência deve admitir diferentes tipos de evidência adequados às especialidades de TI, sem assessment universal obrigatório. |
| RN04 | Localização só deve ser exigida/utilizada quando relevante à natureza presencial do serviço. |
| RN05 | Uma contratação deve possuir condições acordadas identificáveis, incluindo escopo/serviço, prazo, entregáveis quando aplicável e condições de pagamento. |
| RN06 | Alterações materiais às condições devem ser registadas, versionadas e aceites antes de se tornarem vigentes. |
| RN07 | A formalização deve ser proporcional ao serviço e não depende de assinatura digital avançada universal. |
| RN08 | O preço pode ser definido na oportunidade/proposta ou após diagnóstico quando a natureza do serviço assim exigir. |
| RN09 | As condições de pagamento devem identificar valor, método, momento/etapa e estado quando aplicável. |
| RN10 | ConecTA não assume custódia de fundos; eventual transacção real deve usar prestador externo apropriado. |
| RN11 | Avaliações devem estar associadas a uma contratação elegível e podem ser realizadas por ambas as partes. |
| RN12 | Reputação deve preservar contexto e admitir contestação segundo regras de moderação. |
| RN13 | Conflitos podem ser reportados, documentados e acompanhados; ConecTA não presume poder arbitral técnico/jurídico. |
| RN14 | Registos relevantes de acordo, alterações, execução, entrega e pagamento devem permanecer associados à contratação. |
| RN15 | Verificação de identidade/perfil, quando utilizada, é distinta de KYC financeiro e limitada à finalidade definida. |
| RN16 | Medidas administrativas de moderação devem possuir motivo/estado registado e seguir regras da plataforma. |

## 3. Requisitos funcionais finais

### MR01 — Conta, perfis e confiança
- **RF01 Registar utilizador:** permitir criar uma conta.
- **RF02 Autenticar utilizador:** permitir autenticação e gestão de sessão.
- **RF03 Gerir perfil profissional:** permitir manter especialidades, experiência e informação profissional.
- **RF04 Gerir perfil de empregador:** permitir manter informação relevante enquanto contratante.
- **RF05 Gerir evidências de competência:** permitir associar diferentes evidências profissionais ao perfil.
- **RF06 Gerir verificação de perfil/identidade:** permitir submissão, consulta de estado e processamento de verificação proporcional quando adoptada.

### MR02 — Descoberta e oportunidades
- **RF07 Gerir oportunidade:** permitir ao empregador criar, editar dentro das regras de estado, publicar, pausar, retomar, encerrar ou cancelar oportunidade.
- **RF08 Pesquisar oportunidades:** permitir pesquisa e filtragem por critérios relevantes.
- **RF09 Pesquisar trabalhadores:** permitir pesquisa e filtragem por critérios profissionais e contextuais.
- **RF10 Consultar perfil:** permitir consultar informação profissional/reputacional visível antes da contratação.

### MR03 — Proposta, negociação e acordo
- **RF11 Gerir proposta própria:** permitir ao trabalhador criar, submeter e retirar proposta conforme o estado.
- **RF12 Avaliar proposta:** permitir ao empregador consultar, aceitar ou rejeitar propostas.
- **RF13 Formalizar condições acordadas:** permitir às partes registar e aceitar as condições da contratação.
- **RF14 Gerir alteração ao acordo:** permitir propor, aceitar/rejeitar e preservar versões de alterações materiais.

### MR04 — Execução e rastreabilidade
- **RF15 Registar actualização relevante:** permitir associar à contratação informação relevante da execução.
- **RF16 Registar entrega/conclusão:** permitir registar entrega e evolução para conclusão conforme o fluxo.
- **RF17 Consultar histórico da contratação:** permitir consultar condições, versões, estados, alterações e registos relevantes.

### MR05 — Pagamento
- **RF18 Gerir condições de pagamento:** permitir definir valor, método, momento/etapa e condições aplicáveis.
- **RF19 Gerir estado de pagamento:** permitir registar e consultar estados de pagamento associados à contratação.
- **RF20 Integrar prestador de pagamento:** permitir, opcionalmente, integração com prestador externo para facilitar/iniciar transacções sem custódia pela ConecTA. **Prioridade Could.**

### MR06 — Reputação e conflitos
- **RF21 Avaliar contraparte:** permitir avaliação bilateral associada a contratação elegível.
- **RF22 Consultar reputação contextualizada:** apresentar avaliações com contexto relevante.
- **RF23 Contestar avaliação:** permitir reportar/contestar avaliação segundo regras.
- **RF24 Reportar conflito:** permitir reportar conflito associado a contratação.
- **RF25 Acompanhar conflito:** permitir acompanhar estado e evidências/registos do conflito.

### MR07 — Governação
- **RF26 Gerir utilizadores:** permitir a administrador autorizado consultar e aplicar medidas administrativas segundo regras, registando motivo.
- **RF27 Moderar oportunidade reportada:** permitir analisar oportunidade reportada e aplicar acção prevista pela política.
- **RF28 Analisar verificação:** quando houver revisão de verificação, permitir a utilizador autorizado analisar evidências e registar decisão/estado.

## 4. Requisitos não funcionais verificáveis

| ID | Nome | Declaração / critério verificável |
|---|---|---|
| RNF01 | Usabilidade | Os fluxos essenciais de registo, publicação/pesquisa, proposta, formalização e conclusão devem ser executáveis pela interface sem exigir conhecimento técnico do sistema; a validação usará cenários de tarefa definidos. |
| RNF02 | Segurança e autorização | Rotas/acções protegidas devem exigir autenticação e rejeitar operações quando o utilizador não possuir a capacidade/perfil ou relação necessária para a acção. |
| RNF03 | Privacidade/minimização | Dados não definidos como públicos não devem ser expostos a utilizadores sem autorização; os formulários devem solicitar apenas dados previstos para a finalidade funcional correspondente. |
| RNF04 | Integridade/rastreabilidade | Condições aceites e alterações não devem ser sobrescritas sem histórico; registos relevantes devem identificar autoria e data/hora. |
| RNF05 | Responsividade | Os fluxos essenciais devem permanecer utilizáveis nos tamanhos de ecrã suportados pelo protótipo, verificados por testes de interface em viewport móvel e desktop. |
| RNF06 | Manutenibilidade | Regras do domínio e integrações externas devem permanecer separadas em componentes/módulos com responsabilidades identificáveis, verificável por revisão da arquitectura/código. |
| RNF07 | Interoperabilidade | Integrações externas implementadas devem ocorrer por interfaces/APIs desacopladas do núcleo do domínio e permitir substituição do prestador sem alterar as regras centrais da contratação. |

Não são inventados limites de desempenho, disponibilidade ou carga que não tenham sido definidos/testados no projecto.

## 5. Matriz final de rastreabilidade

| Necessidade | RN principal | RF/RNF derivados | Critério de validação futuro |
|---|---|---|---|
| N01 Descoberta/visibilidade | — | RF07–RF10 | Empregador encontra trabalhadores e trabalhador encontra oportunidades fora da sua rede prévia através do protótipo. |
| N02 Evidências de competência | RN03 | RF03, RF05, RF10 | Perfil aceita e apresenta diferentes evidências sem assessment universal. |
| N03 Confiança bilateral | RN01, RN15 | RF04, RF06, RF10, RF21 | Perfis/estados de verificação e reputação são consultáveis conforme autorização. |
| N04 Pesquisa/comparação | RN04 | RF08–RF10 | Pesquisa/filtros retornam opções sem impedir consulta de alternativas. |
| N05 Condições claras | RN05, RN08 | RF07, RF11–RF13, RF18 | Cenário permite chegar a acordo identificando condições essenciais. |
| N06 Alterações | RN06 | RF14, RF17; RNF04 | Alteração cria nova versão e histórico anterior permanece consultável. |
| N07 Formalização proporcional | RN05, RN07 | RF13, RF17 | Contratação pode ser formalizada sem assinatura avançada obrigatória. |
| N08 Rastreabilidade | RN14 | RF15, RF17; RNF04 | Decisões/registos relevantes permanecem associados à contratação. |
| N09 Condições de pagamento | RN09, RN10 | RF18–RF20 | Valor/método/momento/estado são representáveis; integração externa não implica custódia. |
| N10 Risco bilateral | RN09, RN10, RN13 | RF16, RF18–RF20, RF24–RF25 | Entrega, pagamento e eventual conflito podem ser registados e acompanhados. |
| N11 Reputação bilateral | RN11 | RF21–RF22 | Ambas as partes elegíveis conseguem avaliar a contraparte. |
| N12 Reputação contextual/contestável | RN12 | RF22–RF23 | Avaliação apresenta contexto e pode ser contestada. |
| N13 Reporte/acompanhamento de conflito | RN13 | RF24–RF25 | Parte abre caso e acompanha estado sem arbitragem automática. |
| N14 Evidência de conflito | RN14 | RF17, RF25; RNF04 | Histórico/evidências relevantes permanecem ligados ao caso/contratação. |
| N15 Diversidade dos serviços | RN03, RN08 | RF03, RF05, RF07, RF11, RF18 | Fluxos suportam serviços com evidências/preço/condições diferentes. |
| N16 Localização contextual | RN04 | RF07–RF09 | Localização pode ser usada quando relevante sem se tornar universal. |
| N17 Simplicidade/proporcionalidade | RN07 | RNF01, RNF05 | Cenários essenciais são concluíveis sem formalização/complexidade desnecessária. |
| N18 Massa crítica | — | **Não é requisito** | Tratada como condição de adopção/limitação do estudo. |

## 6. Requisitos excluídos explicitamente
Não pertencem à baseline: assessment obrigatório, validação universal de competências pelo administrador, assinatura digital avançada obrigatória, escrow/custódia pela ConecTA, matching algorítmico obrigatório, geolocalização universal, arbitragem administrativa, chat em tempo real como capacidade central e notificações como macro requisito.

Mensagens/notificações podem ser mecanismos auxiliares de implementação se ajudarem a satisfazer RF/RNF existentes, sem ganhar rastreabilidade científica autónoma.

## 7. Gate final

**G-REQ: PASS.**

A baseline de engenharia fica fechada em:
- **16 RN**
- **28 RF**
- **7 RNF**
- **7 Macro Requisitos**

Alterações posteriores exigem nova evidência, correcção de inconsistência ou decisão de âmbito explicitamente registada.

O próximo gate é **G-MODEL**, iniciando modelação UML a partir desta baseline: actores/casos de uso → classes/domínio → actividades → sequências → estados → arquitectura.
