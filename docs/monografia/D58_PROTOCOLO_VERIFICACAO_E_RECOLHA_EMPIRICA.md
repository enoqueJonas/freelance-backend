# D58 — Protocolo operacional para recuperar fontes primárias ou realizar recolha empírica verificável

**Natureza:** procedimento proposto à autora/supervisão, **não** relato de entrevistas realizadas nem aprovação ética.  
**Monografia:** protótipo de ligação entre profissionais autónomos de TI e empregadores na Cidade de Maputo (ConecTA/ServiPlus).  
**Dependência de decisão:** [Auditoria D58 às alegações históricas de 83 participantes](D58_AUDITORIA_83_PARTICIPANTES_VS_11_PERFIS.md).  
**Data:** 03-11-2026.

## Gate 0 — Não iniciar recolha duplicada antes de recuperar o estudo alegado

O draft histórico refere **83 participantes** em Julho de 2025 e vários gráficos percentuais. A D44 contém apenas **11 perfis textuais cuja proveniência não foi certificada**. A primeira actividade é **verificar o acervo original**; não substituir automaticamente um levantamento potencialmente existente por outro.

**Se existir exportação de questionário:**
- preservar o ficheiro original **inalterado**, registar origem/autoria/data, gerar checksum e criar cópia de análise separada;
- manter identificadores pessoais fora do repositório GitHub e de partilhas abertas;
- recolher o instrumento aplicado, lógica de salto, tipos de pergunta, datas e exclusões;
- atribuir um ID pseudónimo distinto a cada resposta, remover ou proteger identificadores e deduplicar por critério documentado;
- reconstruir uma tabela de fluxo amostral: convidados → elegíveis → consentidos → iniciaram → concluíram → válidos por pergunta;
- reconstruir Figura 2 (30 respondentes) e reconciliá-la com 83 participantes/68 trabalhadores/15 empregadores;
- para cada figura, registar `pergunta_id`, filtro aplicado, `n_eligible`, `n_answered`, `n_missing`, numerador por opção, tipo de resposta (única/múltipla) e arredondamento;
- verificar se as percentagens e as conclusões do draft são reproduzíveis; **não inventar respostas ausentes nem ajustar números para forçar 83**.

**Se existirem entrevistas de 2025:**
- verificar que as transcrições/notas são originais e datáveis;
- identificar os procedimentos éticos aplicados, sem publicar contactos, áudios ou consentimentos no GitHub;
- demonstrar a relação (ou inexistência) entre entrevistas antigas, inquiridos de 2025 e T01–T08/E01–E03;
- confrontar o resumo temático e os excertos do draft com os registos originais, incluindo **casos divergentes**.

**Se nada for recuperável:** registar essa limitação de proveniência, pedir decisão académica sobre novo trabalho de campo ou reformulação documental. A simples impossibilidade de localizar ficheiros nesta conta **não prova** que a autora nunca os produziu.

## Gate 1 — Definir a pesquisa real **antes** de convidar participantes

**Questão orientadora de diagnóstico:** como trabalhadores autónomos de TI e empregadores de Maputo **efectivamente** encontram contrapartes, avaliam competência/legitimidade, negociam e formalizam serviços e acompanham alterações, pagamentos e conflitos?

**População de interesse:** adultos que prestam serviços autónomos de TI ou que contrataram/seleccionaram tais serviços na Cidade de Maputo. Uma conta em rede social, um contacto ou uma indicação não basta para comprovar elegibilidade.

**Amostragem candidata:** intencional, buscando diversidade de serviços (web, design, redes, suporte, mobile, QA), experiência, modalidades remota/presencial, tipos de clientes e padrões de contratação. Não fixar `n=11` apenas para reproduzir o piloto sintético: a dimensão deve ser fundamentada pela natureza do estudo, recursos e parecer da supervisão. A composição antiga 8 trabalhadores/3 empregadores não constitui automaticamente amostra ideal e pode sub-representar a perspectiva do empregador.

**Critérios de inclusão/exclusão a aprovar:** relação real com TI freelance/contratação, enquadramento geográfico, possibilidade de consentimento livre, participação voluntária, idade e condições éticas aplicáveis; excluir contactos sem experiência relevante quando o estudo requer relatos de prática, mantendo-os apenas se outra categoria tiver sido aprovada.

**Separação de corpora:** entrevistas novas recebem identificadores como `P-TI-2026-001` e `P-EMP-2026-001`, nunca os códigos `T01–T08/E01–E03` do material exploratório da D44. Não reutilizar respostas sintéticas, mesmo que sejam verosímeis, como citações de pessoas reais.

**Gate de ética:** confirmar com a USTM/supervisão a necessidade de aprovação, o modelo de consentimento, a informação prévia, os procedimentos de gravação, segurança, conservação e eliminação dos dados. Não alegar aprovação nem escolher unilateralmente prazos de retenção.

## Gate 2 — Modelo de convite e consentimento (minuta, não formulário institucional aprovado)

**Explicação inicial sugerida, a ser adaptada à aprovação institucional:**

> Está a ser convidado(a) a participar numa investigação académica sobre como profissionais autónomos de Tecnologias de Informação e clientes ou empregadores encontram e contratam serviços na Cidade de Maputo. O objectivo é compreender práticas reais, dificuldades e alternativas, não vender uma plataforma. A sua participação é voluntária; pode não responder a qualquer pergunta e terminar a conversa. A decisão de participar não interfere com relações profissionais. A informação será tratada segundo os procedimentos de protecção de dados e consentimento aprovados para o estudo. Não serão publicados o seu nome nem contactos no relatório, salvo autorização específica e justificada. Antes de iniciar, explicaremos quem pode aceder aos registos, onde ficarão guardados e o prazo aplicável.

**Registar separadamente:** autorização para participar; autorização para notas; **autorização opcional** de gravação, nunca presumida; entendimento sobre tratamento de dados e retirada, nos termos aprovados. Pseudonimização **não** equivale a anonimato absoluto enquanto a chave existir. Guardar consentimento e chave de correspondência fora do repositório, com acesso limitado.

## Gate 3 — Guiões semiestruturados **não sugestivos**

A primeira fase de cada entrevista é retrospectiva: pedir **um episódio concreto**, perguntar o que aconteceu de facto, quem decidiu, o que foi registado e que alternativas foram usadas. Não começar com «uma plataforma com escrow resolveria os seus problemas?» ou «precisa de avaliações?»: a pergunta incorpora a solução e contamina a resposta.

### Guião A — Trabalhador autónomo de TI

| ID | Pergunta inicial | Sondagens não sugestivas | Temas N01–N18 |
|---|---|---|---|
| WT-01 | «Descreva o serviço autónomo de TI mais recente que realizou ou tentou contratar.» | Tipo de serviço, contacto, canal, resultado, sem exigir que o relato seja problemático | N01, N15, N18 |
| WT-02 | «Como surgiu o contacto com o cliente e que outras possibilidades considerou?» | Recomendação, rede, anúncio, procura activa; quando não procura oportunidades e porquê | N01, N04, N18 |
| WT-03 | «Que elementos o cliente pediu para avaliar a sua competência?» | Projectos, demonstração, certificados, referências, confidencialidade, ou nenhum | N02, N03 |
| WT-04 | «Como foram definidos preço, prazo, âmbito e entregáveis nessa contratação?» | Antes/depois de diagnóstico, proposta, mensagens, contrato; quem aprovou | N05, N07, N09 |
| WT-05 | «Houve alguma alteração às condições? Como decidiram e guardaram o acordo?» | Exemplo de alteração; se não houve, o que teria feito | N06, N08, N14 |
| WT-06 | «Como foi combinado e efectuado o pagamento, quando aplicável?» | Momento, meio, condições, confirmação, atrasos ou ausência deles | N09, N10 |
| WT-07 | «Como avaliou se podia confiar no cliente antes e durante o trabalho?» | Informação disponível, verificações usadas, deslocações e localização | N03, N16 |
| WT-08 | «Houve alguma divergência, avaliação ou reclamação? O que aconteceu?» | Caso negativo é igualmente relevante; documentos, resoluções e terceiros | N11–N14 |
| WT-09 | «O que torna útil ou inútil para si uma ferramenta de descoberta de trabalho?» | Tempo, custo, informação, notificações, acessibilidade; não apresentar ecrã ainda | N04, N17, N18 |
| WT-10 | «Há um caso que contradiga os problemas que costumamos imaginar sobre trabalho autónomo?» | Situações sem dificuldade de clientes, pagamento ou confiança | Contraexemplos, N18 |

### Guião B — Empregador ou cliente de serviços TI

| ID | Pergunta inicial | Sondagens | Temas N01–N18 |
|---|---|---|---|
| EM-01 | «Descreva a contratação de um serviço de TI que realizou mais recentemente.» | Natureza, urgência, organização, resultado | N01, N15 |
| EM-02 | «Como encontrou os profissionais considerados?» | Recomendação, pesquisa, redes, oportunidades, alternativas excluídas | N01, N04 |
| EM-03 | «Como avaliou competência e legitimidade antes de escolher?» | Portfólio, referências, entrevistas, demonstração, ou sem verificação | N02, N03 |
| EM-04 | «Como acordaram valor, prazo, entregáveis e eventuais alterações?» | Quem propôs, revisões, confirmação por escrito ou verbal | N05–N08 |
| EM-05 | «Que condições de pagamento acordaram e como soube que foram satisfeitas?» | Etapas, comprovativos, métodos, conflitos ou inexistência deles | N09, N10 |
| EM-06 | «Como documentou a conclusão e avaliou o serviço?» | Verificações, reclamações, avaliações, contestação | N11–N14 |
| EM-07 | «Quando a localização do prestador é importante para si? Quando é irrelevante?» | Presencial/remoto, dispositivos, disponibilidade | N15, N16 |
| EM-08 | «Em que condições passaria a usar uma ferramenta nova, ou preferiria os métodos actuais?» | Custo, confiança, usabilidade, diversidade de prestadores | N17, N18 |
| EM-09 | «Que parte do último processo correu bem, sem necessidade de mudança?» | Casos negativos e eficiência dos canais actuais | Contraexemplos |

**Regra:** não forçar o participante a declarar um problema, uma fraude ou uma necessidade. Guardar as respostas «não aconteceu», «não precisei» e «não usaria» com a mesma prioridade das convergências.

## Gate 4 — Registo da evidência e tratamento de dados

### 4.1 Ficha mínima por caso (modelo vazio)

**ID pseudónimo:** `[P-TI-2026-___ / P-EMP-2026-___]`  
**Elegibilidade e motivo de inclusão:** `[por preencher]`  
**Canal de recrutamento / referência ao convite:** `[por preencher]`  
**Data/hora aproximada e contexto (sem endereço privado):** `[por preencher]`  
**Versão do guião:** `[por preencher]`  
**Procedimento ético/consentimento verificado:** `[referência restrita]`  
**Registo de entrevista:** `[identificador de armazenamento restrito]`  
**Registo de transcrição/notas:** `[identificador restrito]`  
**Gravação autorizada?** `[sim/não/não aplicável]`  
**Pedido de retirada/rectificação:** `[estado]`  
**Transcritor/revisor e data:** `[por preencher]`  
**Estado da análise:** `[não analisada / codificada / revista]`

**Importante:** não preencher ficticiamente esta ficha para obter onze participantes. Não guardar PII, gravações, contactos, identificadores de WhatsApp ou dados financeiros em GitHub.

### 4.2 Quadro de codificação por excerto (modelo vazio)

| Fonte-ID | Localizador original | Excerto autorizado | Código inicial | Tema candidato N | Descrição/interpretação | Caso divergente? | Revisor |
|---|---|---|---|---|---|---|---|
| [vazio] | [página/minuto] | [omitido até recolha] | [vazio] | [N__] | [vazio] | [sim/não] | [vazio] |

**Regras:**
- Primeiro codificar o que foi **dito**, depois inferir a necessidade. Não mudar a declaração para coincidir com RF definidos.
- Distinguir relatório, evidência do entrevistado, interpretação da autora e decisão técnica.
- Conservar citações com localização recuperável e contexto suficiente; nunca gerar «transcrições» por IA a partir de resumos.
- Registar casos divergentes, recusas e necessidades não antecipadas; não afirmar saturação sem descrever decisão e material analisado.
- Fazer confrontação com literatura como **triangulação interpretativa** limitada às fontes, sem alegar representatividade estatística.

## Gate 5 — Estudo de usabilidade separado da entrevista

O estudo com pessoas **não substitui** os testes CI; destina-se a observar se participantes compreendem a interface e conseguem realizar tarefas. Usar apenas funções que realmente existem na revisão técnica seleccionada da aplicação.

**Fluxo candidato com dados de ensaio e consentimento:**
1. Abrir `/#/real`, criar conta e activar o perfil adequado;
2. Enquanto empregador, criar/publicar oportunidade;
3. Enquanto trabalhador de outra conta, localizar oportunidade e submeter proposta;
4. Enquanto empregador, consultar/aceitar proposta e distinguir `PENDING_AGREEMENT` de `ACTIVE`;
5. Enquanto uma das partes, ler e aceitar a versão de um acordo; interpretar alteração e rejeição.

**Para cada tarefa:** versão do protótipo, actor, pré-condição, instrução exacta, resultado esperado, resultado observado, conclusão sem ajuda, dúvidas, erros, assistência prestada, comentários e consentimento. Não inferir satisfação apenas por completar a tarefa. Separar defeitos de interface de dificuldades de conectividade, literacia e servidor. Não pedir números de documento de identificação nem pagamentos reais.

**Não testar como funcionais:** escrow, transferência financeira, reputação, disputa, entrega e moderação quando esses módulos não estiverem implementados no backend. Uma imagem ou mock não é equivalente a operação real.

## Gate 6 — Critérios para transportar evidências à monografia

- [ ] Proveniência certificada e procedimentos éticos verificados.
- [ ] Cada citação tem `fonte_id + localizador original`; cada percentagem tem `n`, numerador e pergunta.
- [ ] A versão do protótipo observada está identificada por commit/ambiente, sem confundir PR draft com produção.
- [ ] Separação explícita entre documental, entrevistas reais, corpus sintético, decisão de desenho e testes automatizados.
- [ ] Conclusões distinguem alcance dos participantes entrevistados de afirmações populacionais sobre Maputo.
- [ ] N01–N18, RN/RF/RNF e HG/HE1–HE4 são revistos conforme evidência, aceitando hipóteses não confirmadas.
- [ ] Autora e supervisão ratificaram o desenho científico e o tratamento dos resultados.

## Resultado honesto esperado

Se não houver material bruto de 2025 e nenhuma nova recolha for aprovada/executada, **continuará a faltar prova empírica**. Este documento é um plano preparado, **não** uma forma de transformar os 83 participantes ou os onze perfis alegados em dados autênticos. Se a autora optar pela via documental, o trabalho deve ser coerentemente apresentado como **investigação documental + concepção e avaliação técnica de protótipo**, sob aprovação académica.
