# D45 — Auditoria de rastreabilidade e adequação dos testes V01–V08

**Base documental:** `Monografia_D44_Metodologia_Proveniencia_Verificada.docx` — pp. 42, 44–58, 62, 80–82.  
**Natureza:** análise do conteúdo; **não** comprova execução dos testes nem altera o DOCX.  
**Estado dos testes:** todos V01–V08 e RNF01–RNF07 são **não executados**, conforme §3.7 e §5.4.

## Achados prioritários

### RT-01 — Alegação de 27 casos de uso sem catálogo textual verificável (P1)

A secção 5.2.2 (pp. 47–48) afirma: «Foram identificados 27 casos de uso lógicos para os 28 requisitos funcionais; o RF28 integra a análise administrativa prevista no UC06». Também refere correspondência com um «catálogo de UC01–UC27». Porém, o texto extraído da D44 só contém os identificadores **UC01, UC06, UC13, UC14 e UC27**, dos quais UC01/UC27 surgem em referência ao intervalo, UC06 surge como afirmação de agregação e apenas **UC13 e UC14** estão detalhados em quadros.

**Não é possível afirmar que o catálogo completo esteja presente ou que falte nas imagens sem inspecção visual.** Exigir mapa de casos UC01–UC27 (ID, nome, actor, RF, RN, pré/pós-condição, estado/modelo e figura) em anexo ou documento controlado e referenciado inequivocamente. Se o catálogo não existir, não apresentar «27 casos identificados» como uma contagem auditada; clarificar primeiro o que foi realmente elaborado.

### RT-02 — Referências cruzadas indevidas em DS04 (P1)

- **Figura A.6(B), p. 78**: fonte refere `RF24, RF25 e RF26`. Todavia, segundo o Quadro 5.3, `RF26` é **Gerir utilizadores**; a sequência de «análise e recolha de informação adicional» do conflito corresponde primariamente a `RF25 — Acompanhar conflito` e `RN13/RN14/RN16`. Conservar RF26 apenas se houver uma operação real de gestão de contas explicitamente representada.
- **Figura A.6(C), p. 79**: fonte refere `RF25–RF27`. `RF27` é **Moderar oportunidade reportada**, não concluir disputa contratual. Diferenciar moderação de conteúdo/oportunidades de seguimento e encerramento de conflito. Se a figura apenas encerra uma disputa, usar `RF24–RF25`, `RN13–RN14` e `RN16`, com justificação contextual. Não alterar o diagrama sem inspeccionar os elementos gráficos.
- **Figura A.2, p. 69**: fonte associa `RF17 e RF24–RF27`. `RF26–RF27` exigem verificação visual do desenho; não presumir que são pertinentes.
- **Figura 5.1 e catálogo UC**: verificar se actor «Administrador» está ligado só a operações efectivamente cobertas pelo requisito, e não a «arbitragem» não prevista pela RN13.

### RT-03 — Rastreabilidade N→RN→RF→UC→V não é integralmente observável (P1)

A secção 4.15 enumera **N01–N18**; o Capítulo V apresenta **RN01–RN16**, **MR01–MR07**, **RF01–RF28** e **RNF01–RNF07**, mas não contém uma matriz explícita que demonstre **cada** ligação necessidade → regra → requisito → caso de uso → critério de teste. A secção 5.2.8 afirma o vínculo global, insuficiente para auditar individualmente todos os itens. `N18` é correctamente classificada como condição do ecossistema e não deve ser forçada a um RF software.

**Acção:** criar quadro de rastreabilidade com colunas `N / origem (documental ou cenário sintético) / RN / RF ou RNF / UC / cenário V / implementação / evidência`. Cada linha deve ter apenas links sustentados por requisito e figura; «não aplicável» quando justificado. Evitar inferir que a origem de N seja uma entrevista real.

## 4. Matriz analítica de cobertura dos 28 requisitos funcionais

Critério:
- **Explícita** = os passos de V01–V08 mandam exercer ao menos a operação principal; não equivale a teste executado nem a cobertura completa de variantes.
- **Parcial** = cenário menciona a área, mas faltam operações críticas ou passos observáveis.
- **Não explícita** = nenhuma instrução de passos materializa directamente a operação; associação por intervalo RF não prova teste.

| RF | Comportamento (Quadro 5.3) | Cenário proposto | Cobertura dos passos | Gap e ajuste |
|---|---|---|---|---|
| RF01 | Registar utilizador | V01 | Explícita | Acrescentar registo inválido/duplicado e resposta esperada |
| RF02 | Autenticar utilizador | V01 | Não explícita | Acrescentar login válido/inválido, expiração de sessão e logout; distinguir mock de autenticação JWT |
| RF03 | Gerir perfil profissional | V01 | Parcial | Completa perfil, mas não testa edição, leitura posterior nem autorização |
| RF04 | Gerir perfil de empregador | V01 | Parcial | Cria perfil, mas não testa edição e consulta |
| RF05 | Gerir evidências profissionais | V01 | Parcial | Associa evidência, mas falta verificação de visibilidade, remoção e permissão |
| RF06 | Solicitar e acompanhar verificação | V08 | Não explícita | V08 só revê verificação como administrador; incluir pedido e consulta de estado pelo titular |
| RF07 | Gerir ciclo de vida de oportunidade | V02 | Parcial | Publica, mas não verifica edição, fecho, cancelamento e transições de estado |
| RF08 | Pesquisar oportunidades | V02 | Explícita | Acrescentar resultados vazios, filtros combinados e restrição por estado |
| RF09 | Pesquisar trabalhadores | V02 | Não explícita | Inserir pesquisa de trabalhadores por competências e localização, com resultados e filtros |
| RF10 | Consultar perfil | V02 | Não explícita | Incluir consulta de perfil autorizado/público e prevenção de exposição de dados privados |
| RF11 | Submeter e gerir proposta própria | V02 | Parcial | Submete, mas falta retirar/alterar quando permitido e consultar estado |
| RF12 | Avaliar proposta recebida | V02 | Parcial | Aceita, mas falta rejeitar e impedir avaliação por actor não autorizado |
| RF13 | Formalizar condições acordadas | V03 | Explícita | Testar rejeição inicial, campos obrigatórios e assinatura/aceitação dos dois lados |
| RF14 | Alterar e versionar acordo | V03 | Explícita | Confirmar imutabilidade de v1 e vigência só de v2 aceite |
| RF15 | Registar actualização da execução | V04 | Explícita | Autor e data, restrições de actor/estado |
| RF16 | Registar entrega e conclusão | V04 | Explícita | Testar conclusão sem entrega aceite e não conformidade |
| RF17 | Consultar histórico da contratação | V04 | Parcial | Critério menciona histórico, mas falta passo de consulta e verificação de ordem/autoria |
| RF18 | Definir condições de pagamento | V03, V05 | Explícita | Definir por etapa, preço posterior ao diagnóstico e vínculo à versão vigente |
| RF19 | Registar e acompanhar estado de pagamento | V05 | Explícita | Separar relato de pagamento, confirmação e contestação |
| RF20 | Integrar prestador externo de pagamento (quando aplicável) | V05 | Condicional | Testar apenas se houver integração; reportar como não implementado/não aplicável para versão sem PSP, não como aprovação |
| RF21 | Avaliar contraparte | V06 | Explícita | Testar elegibilidade e regra bilateral |
| RF22 | Consultar reputação contextual | V06 | Não explícita | Incluir consulta por ambas as partes e visualização de estado de avaliação contestada |
| RF23 | Contestar avaliação | V06 | Explícita | Exigir registo da contestação e preservação de evidência |
| RF24 | Reportar conflito | V07 | Explícita | Testar identificação do autor e integridade dos anexos |
| RF25 | Acompanhar conflito | V07 | Parcial | Testa transições administrativas; acrescentar consulta de estado pelas partes e histórico/auditoria |
| RF26 | Gerir utilizadores | V08 | Não explícita | Acrescentar operação administrativa concreta e autorização; «aceder como admin» não é gerir utilizadores |
| RF27 | Moderar oportunidade reportada | V08 | Parcial | «moderar denúncia» não especifica oportunidade, estado, acto ou regra; inserir reporte, decisão e trilho |
| RF28 | Analisar verificação | V08 | Parcial | «rever verificação» existe, mas falta decisão aceitação/rejeição e motivo/consulta de estado |

**Observação:** as classificações acima referem apenas os **passos textuais no Quadro A.2**, não todas as descrições da monografia ou possíveis detalhes nas figuras. O Quadro 5.4 e Quadro A.3 não foram executados, e a formulação de critérios de aceitação não equivale a cobertura observada.

## 5. Complementos V01–V08 — passos concretos para fechar lacunas documentais

- **V01 / perfis e autenticação:** registar e autenticar com credenciais, falhar autenticação inválida, editar perfis, associar evidências, consultar visibilidade privada/pública e terminar sessão. Se frontend mock continuar sem password, documentar comportamento demonstrativo como lacuna de RF02, não como aprovação.
- **V02 / descoberta e propostas:** criar/editar/fechar oportunidade, procurar tanto oportunidades **como trabalhadores**, consultar perfil, submeter/retirar proposta, aceitar/rejeitar, proibir auto-contratação, validar transição `PENDING_AGREEMENT`.
- **V03 / acordo:** testar v1, v2 rejeitada/aceite, vigência e imutabilidade; adiar `ACTIVE` até aceitação bilateral.
- **V04 / execução:** consultar histórico após actualização e entrega, verificar actor, data e manutenção de versões.
- **V05 / pagamento:** simular registo externo e contestação sem tratar relato como confirmação, não declarar integração PSP sem código/testes.
- **V06 / reputação:** visualizar reputação contextual e contestação, além de submeter avaliação.
- **V07 / conflito:** cada parte consulta evolução administrativa e evidências; não atribuir à plataforma poder de arbitragem legal.
- **V08 / governação:** gerir utilizadores, moderar **oportunidade reportada**, tratar pedido de verificação criado pelo utilizador e testar rejeições por falta de permissão.

## 6. Regras para a representação de resultados na monografia

- A secção 5.4 deve **continuar a indicar «Não executado»** para todos os oito casos; nenhum dos gaps acima comprova falha de execução.
- Tabela de cobertura separada da tabela de resultados: `requisito → caso proposto → passos cobertos → evidência de execução → resultado`.
- A ausência de operação no teste representa **lacuna no plano**, mesmo quando a implementação correspondente está parcialmente representada no código. Não misturar `não especificado no teste`, `não implementado`, `não executado` e `falhou`.
- A RF20 é condicional; retirar eventual inferência de integração com prestador financeiro na versão actual.
- Conferir manual USTM e formatar quadros conforme padrão académico quando houver acesso ao DOCX original e à referência normativa.

## 7. Verificações finais antes de aprovar

- [ ] Catálogo completo UC01–UC27 localizado e auditável ou contagem corrigida.
- [ ] Fonte das Figuras A.2, A.6(B), A.6(C) reconciliada com RF26 e RF27.
- [ ] Matriz por requisito criada, incluindo N18 como condicionante não funcional de adopção.
- [ ] V01–V08 abrangem comportamentos principais, negativos e de autorização, com requisitos/estados precisos.
- [ ] Nenhum teste marcado aprovado antes de execução real, e nenhum esquema conceptual apresentado como módulo backend implementado.
