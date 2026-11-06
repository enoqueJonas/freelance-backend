# Gap Analysis — Protótipo ServiPlus

## Regra de leitura

Três níveis devem permanecer separados:

1. **Solução concebida** — domínio e fluxos pretendidos.
2. **Protótipo interactivo** — funcionalidades demonstradas/simuladas no frontend.
3. **Implementação técnica** — funcionalidades efectivamente suportadas pelo backend.

## Matriz AS-IS

| Capacidade | Frontend | Backend | Gap principal |
|---|---|---|---|
| Registo | Simulado | Parcial | Integração |
| Login | Simulado | JWT disponível | Integração e alinhamento de fluxo |
| Perfil Worker | Rico | skills/experience básicos | Modelo divergente |
| Perfil Employer | Rico | company/address básicos | Modelo divergente |
| Verificação | Simulada | Modelos iniciais | Fluxo/API/regra |
| Pesquisa | Mock | Filtro básico | Matching/pesquisa |
| Ofertas | Simuladas | Placeholder | Implementação backend |
| Propostas | Simuladas | Placeholder | Implementação backend |
| Contratos | Simulados | Placeholder | Implementação backend |
| Assinatura | Simulada | Placeholder | Regra + implementação |
| Pagamentos | Simulados | App vazia | Integração/regra |
| Reviews | Simuladas | Placeholder | Implementação backend |
| Mensagens | Simuladas | Placeholder | Implementação backend |
| Notificações | Simuladas | App vazia | Implementação backend |
| Disputas | Previstas | Placeholder | Necessidade/regra/implementação |
| Administração | Simulada | Django admin básico | Fluxo funcional |
| Testes | Sem baseline significativa | Stubs | Estratégia e cobertura |

## Gaps de investigação

As seguintes decisões já aparecem no protótipo/código, mas ainda precisam de fundamento por entrevistas, análise documental e/ou benchmark:

- separação ou acumulação dos papéis Worker/Employer;
- verificação documental;
- validação de competências/assessment;
- estrutura de perfil e portfólio;
- publicação e moderação de ofertas;
- propostas;
- contratos e assinatura;
- pagamentos integrados e momento de libertação;
- reputação/reviews;
- mensagens internas;
- notificações;
- disputas e intervenção administrativa.

## Critério para evolução

Nenhuma funcionalidade será mantida, removida ou acrescentada apenas porque já existe no protótipo. A reconstrução seguirá:

`Evidência → Necessidade/Regra de negócio → Requisito → Modelação → Implementação → Teste`.

A futura matriz de rastreabilidade deverá incluir a fonte do requisito e o seu estado de implementação.
