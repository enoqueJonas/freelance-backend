# M09 — Protocolo de validação de requisitos e estado da evidência

**Data:** 2026-11-02  
**Monografia:** D40, `Monografia_D40_Protocolo_Validacao_V01_V08.docx`, secção 5.4 e Apêndice A, secção 8.8.  
**Fontes internas:** [baseline final de requisitos](../research/requirements-final-baseline.md), [matriz M08 de interfaces](interface-evidence-audit-2026-11-02.md), [modelação cruzada](../modeling/model-cross-audit.md).  
**Situação:** protocolo concluído como planeamento; **0/8 ensaios funcionais executados e 0/7 verificações RNF executadas**. Inspecção estática do código não constitui prova de execução da interface ou integração backend.

## Erro científico corrigido na D40

Na D39, o campo de resultado V01–V08 continha «Parcial» para **todos** os casos. Tal classificação podia ser interpretada como resultado de ensaio sem que existissem ambiente, execução, evidência observada e critério de decisão documentados. A D40 substitui o resultado por **«Não executado»** e mantém os aspectos identificados no código numa coluna distinta de **«Observação do código»**. O mesmo princípio aplica-se aos RNF: a coluna «Verificação» é agora «Teste não executado» e a análise estática permanece descritiva. Nenhuma funcionalidade é declarada aprovada ou reprovada apenas por leitura do código.

## V01–V08: cenários e oráculos previstos

| Caso | RF/RN | Pré-condição/acção de validação | Oráculo esperado | Estado |
|---|---|---|---|---|
| V01 | RF01–RF05; RN01, RN03 | Criar utilizador sintético; associar WorkerProfile e EmployerProfile à mesma conta e duas modalidades de evidência profissional | Perfis acumuláveis; evidências múltiplas; dados persistentes após nova sessão | NÃO EXECUTADO |
| V02 | RF07–RF12; RN02, RN04 | Publicar oportunidade, pesquisar, submeter proposta como outro utilizador e tentar propor ao próprio anúncio | Só OPEN aceita; auto-contratação rejeitada; aceitação inicia Engagement PENDING_AGREEMENT | NÃO EXECUTADO |
| V03 | RF13–RF14, RF18; RN05–RN09 | Propor v1; registar aceitações; propor v2; rejeitar e depois aceitar v2 em ensaios separados | ACTIVE apenas com acordo aceite; versão recusada não altera vigência; versões aceites anteriores imutáveis | NÃO EXECUTADO |
| V04 | RF15–RF17; RN14 | Registar execução e entrega, pedir conclusão e tentar conclusão sem condições válidas | ExecutionRecord com autoria/data; DELIVERED e COMPLETED separados; histórico consultável | NÃO EXECUTADO |
| V05 | RF18–RF20; RN09–RN10 | Definir etapas de pagamento, reportar/confirmar/contestar pagamento externo; PSP apenas se existir implementação | Condições por versão; REPORTED_PAID ≠ CONFIRMED; nenhuma custódia; RF20 opcional | NÃO EXECUTADO |
| V06 | RF21–RF23; RN11–RN12 | Testar avaliação bilateral elegível e inelegível, bem como contestação | Avaliação contextualizada e condicionada; contestação não apaga automaticamente registo | NÃO EXECUTADO |
| V07 | RF24–RF25; RN13–RN14 | Reportar conflito com evidência, iniciar análise, pedir informação adicional e encerrar | OPEN → UNDER_REVIEW ↔ WAITING_INFORMATION → RESOLVED/CLOSED, histórico preservado, sem arbitragem jurídica | NÃO EXECUTADO |
| V08 | RF06, RF26–RF28; RN15–RN16 | Executar revisão de verificação e moderação com actor autorizado e não autorizado | Autorização por capacidade/relação, actor, motivo e data; sem afirmar KYC financeiro | NÃO EXECUTADO |

## RNF01–RNF07: técnicas de verificação e evidências

| RNF | Procedimento previsto | Evidência mínima | Estado |
|---|---|---|---|
| RNF01 | Tarefas de registo, descoberta, proposta e contratação com participantes reais de teste | Ficha por tarefa, resultado, erros, dificuldades e assistência | NÃO EXECUTADO |
| RNF02 | Testar operações sem sessão, com papel errado e recurso de outro utilizador | Respostas 401/403 ou resultado equivalente fundamentado; registos anonimizados | NÃO EXECUTADO |
| RNF03 | Verificar dados públicos/privados, exposição de documentos e sessão local | Inventário de campos por perfil e saídas observadas | NÃO EXECUTADO |
| RNF04 | Propor nova versão sem modificar acordo aceite e conferir trilho | Registos anteriores/posteriores, timestamps e actor | NÃO EXECUTADO |
| RNF05 | Percorrer tarefas centrais em 390×844 e 1365×900 | Capturas autênticas e relatório de recorte/sobreposição | NÃO EXECUTADO |
| RNF06 | Inspeccionar separação lógica UI/API/domínio/adaptadores | Mapa de responsabilidades e análise de mudanças | NÃO EXECUTADO |
| RNF07 | Se PSP existir, exercitar contrato adaptador com êxito e falha | Contrato de integração e registos/estados observados | NÃO EXECUTADO |

## Campos obrigatórios por evidência executada

- Código e revisão Git exactos, ambiente, ferramentas, configuração e data;
- cenário, requisito, identificação sintética da conta e pré-condições;
- passos, entradas, resultado esperado e **resultado efectivamente observado**;
- decisão `PASSOU`, `FALHOU`, `PARCIAL` ou `NÃO EXECUTADO`, com justificação;
- imagens/logs anonimizados, sem segredos, tokens, PII nem documentos reais;
- limitações, dependências e referência ao commit/issue de defeito aplicável.

**Gate:** marcar um cenário «parcial» só após uma execução que tenha demonstrado uma parte verificável; «não implementado» por análise estática não equivale a «falhou teste» sem tentativa. Sem evidências completas, M09 permanece aberta.

## QA editorial efectuada na D40

- D40 possui **82 páginas físicas**; Introdução na 11 e Referências na 67 = **57 páginas de corpo inclusivas**, dentro do limite USTM de 60.
- Acrescentados Quadros A.2 (oito cenários) e A.3 (sete RNF) no Apêndice A, sem acréscimo de páginas do corpo.
- Reparada apresentação das matrizes na secção 5.4 (largura de colunas, alinhamento à esquerda, sem espaços artificiais) e no apêndice.
- Índice Word conserva campo automático e duas novas entradas para 8.8 e 8.8.1. Reconciliadas **96 entradas com a paginação renderizada, sem divergências**.
- Conservados **14 comentários** anteriores, `word/comments.xml` idêntico à D39, 22 imagens e sete marcadores de captura pendentes.
- **Não ocorreu qualquer teste de aceitação da aplicação nesta tarefa.**

## Próximo trabalho
A M08 continua bloqueada até captura da aplicação efectivamente executada. Para M09, executar os cenários prioritários após integração backend–frontend, e só então actualizar resultados e a discussão científica do Capítulo V. A M10 (auditoria bibliográfica) pode prosseguir em paralelo, sem pressupor sucesso de M08/M09.
