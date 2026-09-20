# Derivação de Requisitos — ConecTA

## 1. Regra de derivação

A derivação parte da matriz de triangulação e não do código existente.

`Necessidade consolidada → Regra de negócio → Requisito funcional/RNF → Modelação → Implementação → Teste`

A prioridade inicial usa **Must / Should / Could / Out**, e deverá ser revista antes da escrita final.

## 2. Regras de negócio candidatas

| ID | Regra de negócio | Fonte | Estado |
|---|---|---|---|
| RN01 | Um utilizador pode acumular os perfis de trabalhador autónomo e empregador. O papel relevante deve ser determinado pelo contexto de cada acção/contratação, sem obrigar o utilizador a possuir contas separadas. | Decisão de domínio + N03, N11 | **Aprovada** |
| RN02 | A apresentação de competências deve admitir evidências adequadas a diferentes especialidades de TI, não dependendo de um único mecanismo de validação. | N02, N15 | Candidata |
| RN03 | A localização só deve ser exigida/utilizada como critério quando a natureza do serviço exigir presença física ou tornar a localização relevante. | N15, N16 | Candidata |
| RN04 | Uma contratação deve possuir condições acordadas identificáveis, incluindo escopo/serviço, prazo, entregáveis quando aplicável e condições de pagamento. | N05, N07, N09 | Candidata |
| RN05 | Alterações materiais às condições acordadas devem ser registadas e aceites pelas partes antes de substituírem as condições anteriores. | N06, N08, N14 | Candidata |
| RN06 | O nível de formalização deve ser proporcional ao serviço; a plataforma não deve exigir assinatura digital avançada para toda contratação. | N07 + análise normativa | Candidata |
| RN07 | O preço pode ser definido na publicação/proposta ou posteriormente, quando a natureza do serviço exigir diagnóstico/avaliação prévia. | N05, N15 | Candidata |
| RN08 | As condições de pagamento devem identificar, quando aplicável, valor, método, momento/etapa e estado do pagamento. | N09, N10 | Candidata |
| RN09 | O protótipo não deve representar a ConecTA como custodiante ou prestadora de serviços financeiros; eventual processamento real deve ser externo e sujeito ao enquadramento aplicável. | N09, N10 + BdM | Candidata/limite de âmbito |
| RN10 | Avaliações devem decorrer de relações/contratações concluídas ou suficientemente estabelecidas, para reduzir avaliações sem contexto. | N11, N12 | Candidata |
| RN11 | A reputação deve poder existir para ambas as partes da relação, preservando contexto da contratação. | N03, N11, N12 | Candidata |
| RN12 | Conflitos podem ser reportados e acompanhados, mas o protótipo não presume poder arbitral da ConecTA sobre disputas técnicas/financeiras. | N13, N14 | Candidata/limite |
| RN13 | Registos relevantes de acordo, alterações, execução, entrega e pagamento devem permanecer associados à contratação para rastreabilidade. | N08, N14 | Candidata |
| RN14 | Verificação de identidade/perfil, se adoptada, deve ser distinta de KYC financeiro e limitada à finalidade definida pela plataforma. | N03 + análise normativa | Candidata |

## 3. Macro requisitos funcionais candidatos

### MR01 — Contas, perfis e confiança

| ID | Nome | Declaração | Fonte | Prioridade | Observação |
|---|---|---|---|---|---|
| RF01 | Registar utilizador | O sistema deve permitir o registo de utilizadores para utilização da plataforma. | Base operacional; N03 | Must | Autenticação não equivale a verificação. |
| RF02 | Autenticar utilizador | O sistema deve permitir autenticação e gestão de sessão de utilizadores registados. | Base operacional | Must | Segurança detalhada em RNF. |
| RF03 | Gerir perfil profissional | O sistema deve permitir a um utilizador com perfil de trabalhador manter dados profissionais, especialidades, experiência e evidências de capacidade adequadas ao seu tipo de serviço. | N02, N15; RN01/RN02 | Must | O mesmo utilizador pode também possuir perfil de empregador; não limitar evidências a GitHub/portfólio. |
| RF04 | Gerir perfil de empregador | O sistema deve permitir a um utilizador com perfil de empregador manter informação relevante para identificação/apresentação enquanto contratante. | N03; RN01 | Must | O mesmo utilizador pode também possuir perfil de trabalhador; dados mínimos serão definidos no modelo. |
| RF05 | Registar evidências de competência | O sistema deve permitir associar ao perfil diferentes tipos de evidência, como portfólio, projectos, referências, certificações ou ligações externas. | N02, N15 | Should | Assessment obrigatório fica fora. |
| RF06 | Verificar identidade/perfil | O sistema deve permitir um mecanismo proporcional de verificação de identidade/perfil quando definido pelas regras da plataforma. | N03; RN14 | Should | Mecanismo exacto ainda a modelar; não chamar KYC. |

### MR02 — Descoberta e oportunidades

| ID | Nome | Declaração | Fonte | Prioridade | Observação |
|---|---|---|---|---|---|
| RF07 | Publicar oportunidade | O sistema deve permitir ao empregador publicar uma necessidade/oportunidade de serviço de TI com informação suficiente para potenciais trabalhadores avaliarem o trabalho. | N01, N05 | Must | Preço pode ser opcional conforme RN07. |
| RF08 | Pesquisar oportunidades | O sistema deve permitir ao trabalhador pesquisar e filtrar oportunidades segundo critérios relevantes. | N01, N04 | Must | Sem matching algorítmico obrigatório. |
| RF09 | Pesquisar trabalhadores | O sistema deve permitir ao empregador pesquisar e filtrar trabalhadores segundo critérios profissionais relevantes. | N01, N04, N16 | Must | Localização apenas quando aplicável. |
| RF10 | Consultar perfil | O sistema deve permitir consultar informação profissional relevante de um trabalhador antes da contratação. | N02, N04 | Must | Respeitar visibilidade/privacidade. |

### MR03 — Proposta, negociação e acordo

| ID | Nome | Declaração | Fonte | Prioridade | Observação |
|---|---|---|---|---|---|
| RF11 | Submeter proposta | O sistema deve permitir ao trabalhador responder a uma oportunidade através de proposta contendo as condições aplicáveis ao serviço. | N05 | Must | Estrutura varia com serviço. |
| RF12 | Avaliar proposta | O sistema deve permitir ao empregador consultar e aceitar/rejeitar propostas recebidas. | N04, N05 | Must | Preservar estado/histórico. |
| RF13 | Registar condições acordadas | O sistema deve permitir às partes formalizar electronicamente as condições aceites para a contratação. | N05, N07, N09; RN04/RN06 | Must | Não implica assinatura digital avançada. |
| RF14 | Registar alteração ao acordo | O sistema deve permitir propor, registar e aceitar alterações materiais às condições da contratação. | N06; RN05 | Must | Preservar versão/histórico. |

### MR04 — Execução e rastreabilidade

| ID | Nome | Declaração | Fonte | Prioridade | Observação |
|---|---|---|---|---|---|
| RF15 | Registar actualizações relevantes | O sistema deve permitir associar à contratação informação/actualizações relevantes à sua execução. | N08, N14 | Should | Não obriga a chat em tempo real. |
| RF16 | Registar entrega/conclusão | O sistema deve permitir registar a entrega ou conclusão do serviço e o respectivo estado. | N10, N14 | Must | Necessário para ciclo/reputação. |
| RF17 | Consultar histórico da contratação | O sistema deve permitir às partes consultar condições, alterações, estados e registos relevantes associados à contratação. | N08, N14; RN13 | Must | Elemento central de rastreabilidade. |

### MR05 — Pagamento

| ID | Nome | Declaração | Fonte | Prioridade | Observação |
|---|---|---|---|---|---|
| RF18 | Definir condições de pagamento | O sistema deve permitir registar valor, método, momento/etapa e condições de pagamento aplicáveis. | N09, N10; RN08 | Must | Pode haver adiantamento/parcelas/etapas. |
| RF19 | Registar estado de pagamento | O sistema deve permitir registar e consultar o estado do pagamento associado à contratação. | N09, N10 | Must | Não significa processar/custodiar fundos. |
| RF20 | Integrar prestador de pagamento | O sistema poderá integrar um prestador autorizado para iniciar/facilitar pagamentos, caso esta capacidade seja seleccionada para o âmbito técnico. | N09, N10 + BdM | Could | Não é necessária para validar o protótipo base. |

### MR06 — Reputação e conflitos

| ID | Nome | Declaração | Fonte | Prioridade | Observação |
|---|---|---|---|---|---|
| RF21 | Avaliar contraparte | O sistema deve permitir que trabalhador e empregador avaliem a contraparte no contexto de uma contratação elegível. | N11; RN10/RN11 | Should | Bilateral. |
| RF22 | Consultar reputação contextualizada | O sistema deve apresentar avaliações com contexto suficiente para interpretação, incluindo relação com trabalhos realizados quando apropriado. | N11, N12 | Should | Evitar score sem contexto como único sinal. |
| RF23 | Contestar avaliação | O sistema deve permitir reportar/contestar uma avaliação segundo regras definidas. | N12 | Should | Não implica remoção automática. |
| RF24 | Reportar conflito | O sistema deve permitir a uma parte reportar conflito relacionado com uma contratação. | N13 | Should | Escopo de intervenção limitado. |
| RF25 | Acompanhar conflito | O sistema deve permitir consultar estado e registos/evidências associados ao conflito reportado. | N13, N14 | Should | Sem arbitragem automática. |

## 4. Requisitos não funcionais candidatos

| ID | Nome | Declaração candidata | Fonte | Prioridade |
|---|---|---|---|---|
| RNF01 | Usabilidade | Os fluxos principais devem minimizar passos e informação não necessária, mantendo complexidade proporcional ao tipo de serviço. | N17 | Must |
| RNF02 | Segurança de autenticação | Credenciais e sessões devem ser protegidas segundo práticas adequadas à aplicação web e os acessos devem respeitar autorização por utilizador/papel. | Análise normativa/técnica | Must |
| RNF03 | Privacidade e minimização | O sistema deve recolher e expor apenas dados necessários às finalidades definidas, com controlo de acesso sobre informação não pública. | N03 + análise normativa | Must |
| RNF04 | Integridade/rastreabilidade | Registos de condições acordadas, alterações, estados e evidências relevantes devem preservar autoria, data/hora e histórico suficiente para rastreabilidade. | N06, N08, N14 | Must |
| RNF05 | Responsividade | A interface web deve adaptar-se aos principais tamanhos de ecrã suportados sem perda das funções essenciais. | Decisão de produto web | Should |
| RNF06 | Manutenibilidade | A implementação deve separar responsabilidades do domínio e integrações externas, especialmente pagamentos/verificação. | Análise técnica | Should |
| RNF07 | Interoperabilidade | Integrações externas, quando implementadas, devem utilizar interfaces/APIs desacopladas do domínio central. | WB/BdM + análise técnica | Should |

> Critérios quantitativos de desempenho, disponibilidade, acessibilidade e segurança só serão acrescentados quando houver base técnica/testável; não serão inventados números.

## 5. Fora do âmbito / não derivados

| Capacidade | Decisão |
|---|---|
| Assessment técnico obrigatório | **Out** — evidência divergente e inadequado como gate universal. |
| Assinatura digital avançada obrigatória | **Out** — formalização electrónica é suficiente para o requisito actual. |
| Escrow/custódia de fundos pela ConecTA | **Out** — não derivado e regulatoriamente sensível. |
| Matching algorítmico obrigatório | **Out** — pesquisa/filtros são suportados; algoritmo não. |
| Geolocalização universal | **Out** — localização é contextual. |
| Arbitragem técnica/financeira pela administração | **Out** — reporte/acompanhamento sim; poder arbitral não demonstrado. |
| Chat em tempo real como requisito autónomo | **Out nesta baseline** — rastreabilidade é a necessidade; mensagens podem ser decisão posterior de implementação. |
| Notificações como macro necessidade | **Não derivado nesta baseline** — pode surgir como mecanismo auxiliar de UX após modelação. |

## 6. Condições que não são requisitos

- **N18 — massa crítica:** condição de adopção/ecossistema; o software não consegue garantir oferta/procura suficiente.
- Redução do desemprego, aumento de rendimento ou redução do custo de aquisição de clientes não são resultados prometidos pela baseline.
- A ConecTA é um protótipo académico, não uma plataforma financeira nem autoridade de resolução de disputas.

## 7. Comparação preliminar com o protótipo existente

| Área existente | Resultado científico |
|---|---|
| Registo/login | Mantém-se, mas precisa integração real frontend/backend. |
| Perfis | Mantêm-se; modelo deve aceitar diversidade de evidências. |
| Verificação | Pode manter-se de forma proporcional; desenho actual precisa revisão. |
| Ofertas/propostas | Mantêm-se e ganham fundamento. |
| Contratos | Reformular como **condições/acordo**, com formalização proporcional. |
| Assinatura | Não manter como obrigação universal. |
| Pagamentos | Reformular: condições/estado são core; processamento é opcional/externo. |
| Reviews | Mantêm-se, preferencialmente bilaterais e contextualizadas. |
| Mensagens | Não justificadas como core; avaliar como mecanismo de rastreabilidade. |
| Notificações | Auxiliar, não necessidade demonstrada. |
| Disputas | Manter reporte/acompanhamento/evidência; retirar pressuposto de arbitragem. |
| Assessment | Retirar como gate obrigatório. |
| Localização | Tornar condicional. |

## 8. Gate de engenharia de requisitos

**G-REQ-CANDIDATE: PASS.**

A baseline candidata contém **14 RN, 25 RF e 7 RNF**, ainda sujeita a:
1. revisão de redundância e atomicidade;
2. modelação técnica do modelo de papéis acumuláveis Worker/Employer já aprovado;
3. modelação de estados de oportunidade, proposta, acordo, execução, pagamento e conflito;
4. confronto detalhado com os 32 RF do draft e com o modelo/código;
5. transformação das declarações em critérios verificáveis antes do gate final de requisitos.


## 9. Decisão de domínio — acumulação de papéis

**Decisão aprovada:** um utilizador pode ser trabalhador autónomo e empregador em simultâneo.

### Consequências para o modelo

- `User` representa a identidade/conta e não deve possuir um único campo de papel mutuamente exclusivo como fonte de verdade.
- `WorkerProfile` e `EmployerProfile` são capacidades/perfis opcionais e acumuláveis associados ao mesmo utilizador.
- Um utilizador pode possuir apenas `WorkerProfile`, apenas `EmployerProfile` ou ambos.
- O papel efectivo é contextual: ao publicar uma oportunidade actua como empregador; ao submeter uma proposta actua como trabalhador.
- Autorização deve ser baseada na capacidade/perfil necessário para a acção, e não num enum global exclusivo `worker | employer`.
- Reputação continua bilateral, mas deve distinguir a perspectiva/contexto em que a avaliação foi obtida.
- A interface deve permitir activar/completar o segundo perfil sem criar outra conta.
- A modelação deve impedir relações inválidas, incluindo um utilizador contratar-se a si próprio na mesma oportunidade.

### Impacto no AS-IS

Esta decisão aproxima o domínio do modelo backend, onde Worker e Employer já são relações independentes, e entra em conflito com o frontend actual, que usa um papel singular `employer | worker | admin`. O frontend deverá ser reformulado durante a implementação para representar perfis/capacidades acumuláveis.
