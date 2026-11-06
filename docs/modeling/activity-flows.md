# Fluxos de Actividade Representativos — ConecTA

## 1. Critério de selecção

Não serão produzidos diagramas de actividade para operações CRUD simples nem um diagrama por requisito. Os fluxos seleccionados concentram decisões de negócio, estados e interacção entre os dois lados da plataforma.

Foram consolidados quatro diagramas:

1. **DA01 — Publicar oportunidade e seleccionar proposta**
2. **DA02 — Formalizar e alterar condições da contratação**
3. **DA03 — Executar serviço, registar entrega e acompanhar pagamento**
4. **DA04 — Reportar e acompanhar conflito**

Em conjunto cobrem RF07–RF19 e RF24–RF25, além das RN centrais de contratação. Registo/perfis, reputação e administração permanecem modelados por casos de uso/requisitos e podem ser detalhados se a implementação revelar necessidade.

---

## 2. DA01 — Publicar oportunidade e seleccionar proposta

### Actores/raias
Empregador | Sistema ConecTA | Trabalhador

### Fluxo principal
1. Empregador inicia criação de oportunidade.
2. Sistema solicita dados da necessidade: título, descrição/escopo, categoria, prazo e, quando aplicável, preço/orçamento e localização.
3. Empregador preenche os dados.
4. Sistema valida campos e regras.
5. **[Dados válidos?]**
   - Não → apresenta erros e regressa à edição.
   - Sim → guarda oportunidade em DRAFT.
6. Empregador publica.
7. Sistema altera estado para OPEN.
8. Trabalhador pesquisa/consulta oportunidades.
9. Trabalhador selecciona oportunidade OPEN.
10. Sistema apresenta condições disponíveis e perfil/contexto do empregador.
11. Trabalhador prepara proposta.
12. **[Preço pode ser definido sem diagnóstico?]**
    - Sim → inclui preço/condições na proposta.
    - Não → pode submeter proposta indicando necessidade de diagnóstico/definição posterior.
13. Sistema verifica que trabalhador não é o autor da oportunidade e que a oportunidade continua OPEN.
14. **[Elegível?]**
    - Não → rejeita submissão e informa motivo.
    - Sim → regista Proposal SUBMITTED.
15. Empregador consulta propostas recebidas.
16. Empregador rejeita ou selecciona proposta.
17. **[Rejeitada?]** → sistema marca REJECTED; fluxo dessa proposta termina.
18. **[Aceite?]** → sistema marca ACCEPTED e inicia Engagement PENDING_AGREEMENT.
19. O fluxo continua em DA02.

### Alternativas relevantes
- Trabalhador pode retirar Proposal SUBMITTED antes da aceitação → WITHDRAWN.
- Empregador pode PAUSE/retomar Opportunity.
- Oportunidade reportada pode entrar em MODERATION_HOLD.
- Opportunity CLOSED/CANCELLED/REMOVED não recebe novas propostas.

### Regras cobertas
RN01, RN02, RN04, RN08; RF07–RF12.

---

## 3. DA02 — Formalizar e alterar condições da contratação

### Actores/raias
Empregador | Sistema ConecTA | Trabalhador

### Parte A — formalização inicial
1. Sistema cria Engagement em PENDING_AGREEMENT a partir da Proposal ACCEPTED.
2. Sistema apresenta condições provenientes da oportunidade/proposta.
3. Partes completam/confirmam: escopo, entregáveis quando aplicável, prazo, preço e condições de pagamento.
4. Uma parte propõe a AgreementVersion v1.
5. Sistema regista v1 como PROPOSED, com autor e data/hora.
6. Contraparte consulta a versão.
7. **[Aceita?]**
   - Não → REJECTED; condições podem ser revistas através de nova versão.
   - Sim → regista aceitação.
8. **[Todas as aceitações necessárias registadas?]**
   - Não → mantém PENDING_AGREEMENT.
   - Sim → AgreementVersion torna-se ACCEPTED e Engagement torna-se ACTIVE.
9. Sistema preserva v1 como versão vigente.

### Parte B — alteração durante execução
10. Durante ACTIVE surge necessidade de alteração material.
11. Uma parte propõe nova condição.
12. Sistema copia a base vigente e cria AgreementVersion vN+1 PROPOSED.
13. Sistema preserva a versão anterior sem sobrescrita.
14. Contraparte analisa alteração.
15. **[Aceita?]**
    - Não → nova versão REJECTED; versão anterior continua vigente.
    - Sim → nova versão ACCEPTED; versão anterior torna-se histórica/superseded para vigência.
16. Sistema passa a considerar a nova versão como vigente.
17. Execução continua segundo condições actualizadas.

### Regras
- Não existe assinatura digital avançada obrigatória.
- Alteração material nunca modifica silenciosamente versão aceite.
- Condições de pagamento pertencem à versão do acordo.
- Preço pode ter sido definido após diagnóstico.

### Regras cobertas
RN05–RN09, RN14; RF13, RF14, RF17, RF18; RNF04.

---

## 4. DA03 — Executar serviço, registar entrega e acompanhar pagamento

### Actores/raias
Trabalhador | Sistema ConecTA | Empregador | Prestador de Pagamento (opcional)

### Fluxo
1. Engagement está ACTIVE com AgreementVersion ACCEPTED.
2. Trabalhador executa o serviço fora da plataforma.
3. Partes podem registar actualizações relevantes da execução.
4. Sistema associa cada registo ao Engagement com autor e data/hora.
5. Trabalhador regista entrega/conclusão.
6. Sistema cria ExecutionRecord de entrega e muda Engagement para DELIVERED.
7. Empregador consulta entrega.
8. **[Há problema material?]**
   - Sim → pode solicitar alteração válida ou reportar conflito (DA04).
   - Não → confirma/fecha conclusão.
9. Sistema muda Engagement para COMPLETED conforme regra aplicável.
10. Para cada PaymentTerms aplicável, sistema mantém PaymentRecord.
11. **[Pagamento é registado externamente/manual?]**
    - Sim → parte autorizada regista REPORTED_PAID; contraparte confirma → CONFIRMED.
12. **[Existe integração PSP implementada?]**
    - Sim → sistema solicita operação ao PSP externo; guarda apenas referência/estado devolvido.
    - Falha → PaymentRecord FAILED.
    - Sucesso confirmado → CONFIRMED.
13. **[Pagamento contestado?]**
    - Sim → PaymentRecord DISPUTED e pode originar DA04.
14. Sistema mantém histórico de entrega, condições e pagamento.

### Limites
- ConecTA não executa o trabalho.
- ConecTA não guarda fundos.
- COMPLETED e CONFIRMED são estados distintos: conclusão do serviço não deve ser confundida com confirmação financeira.
- A ordem entrega/pagamento pode variar conforme PaymentTerms (adiantamento, etapa, final).

### Regras cobertas
RN09, RN10, RN14; RF15–RF20; RNF04, RNF07.

---

## 5. DA04 — Reportar e acompanhar conflito

### Actores/raias
Trabalhador/Empregador | Sistema ConecTA | Administrador

### Fluxo
1. Parte consulta contratação/histórico.
2. Parte selecciona “Reportar conflito”.
3. Sistema solicita categoria, descrição e evidências relevantes.
4. Parte submete.
5. Sistema cria Dispute OPEN associado ao Engagement e preserva autor/data/hora.
6. Quando aplicável, estado operacional relacionado é sinalizado como IN_DISPUTE e PaymentRecord pode estar DISPUTED.
7. Administrador autorizado consulta o caso.
8. Sistema muda para UNDER_REVIEW.
9. **[Informação suficiente?]**
   - Não → WAITING_INFORMATION; sistema solicita informação/evidência à(s) parte(s).
   - Parte fornece informação → volta a UNDER_REVIEW.
   - Sim → prossegue.
10. Administrador regista acompanhamento/resultado permitido pela política.
11. **[Caso encerrado com resolução registada?]**
    - Sim → RESOLVED.
    - Encerramento administrativo sem decisão substantiva → CLOSED.
12. Sistema preserva histórico, evidências, estados e acções.
13. Engagement regressa ao estado operacional apropriado ou termina conforme resultado e regras aplicáveis.

### Limite de autoridade
O administrador documenta, acompanha e aplica políticas da plataforma. O diagrama não atribui à ConecTA poder de determinar juridicamente culpa, obrigação de pagamento ou mérito técnico da prestação.

### Regras cobertas
RN13, RN14, RN16; RF17, RF24–RF27 quando aplicável; RNF04.

---

## 6. Cobertura

| Fluxo | Necessidades dominantes | RF principais |
|---|---|---|
| DA01 | N01, N04, N05, N15, N16 | RF07–RF12 |
| DA02 | N05, N06, N07, N08, N09 | RF13, RF14, RF17, RF18 |
| DA03 | N08, N09, N10 | RF15–RF20 |
| DA04 | N10, N13, N14 | RF17, RF24–RF27 |

N02/N03 e N11/N12 são cobertos por perfis/verificação/reputação e serão representados no modelo de classes/casos de uso e nos testes correspondentes, sem forçar diagramas de actividade adicionais.

## 7. Orientação para desenho UML

Ao produzir as figuras:
- usar swimlanes por actor/sistema;
- usar losangos apenas para decisões reais;
- mostrar estados importantes junto às acções que os alteram;
- não representar páginas/botões como actividades de negócio;
- não transformar chamadas técnicas de API em passos do actor;
- DA02 deve evidenciar claramente versionamento;
- DA03 deve separar execução, entrega e pagamento;
- DA04 deve evidenciar que acompanhamento administrativo não equivale a arbitragem.

## 8. Gate

**G-MODEL-ACTIVITY: PASS.**

Os quatro fluxos são suficientes para derivar os diagramas de sequência sem duplicar CRUD. Próximo: definir sequências correspondentes, identificando boundary/service/domain/repository e integrações externas apenas onde realmente existam.
