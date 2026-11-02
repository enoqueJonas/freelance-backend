# D49 — Verificação executável do modelo de referência (não do protótipo)

**Data:** 02-11-2026.  
**Base:** [D48 — Diagramas e guardas](D48_MODELO_ESTADOS_DIAGRAMAS_EDITAVEIS.md), [D47 — Inspecção visual dos diagramas](VERIFICACAO_VISUAL_UML_D47.md), [D44 — Monografia](../../README.md).  
**Estatuto:** protótipo matemático/computacional **independente**, produzido durante a auditoria, **não aprovado como modelo final** e **não integrado** no frontend, backend ou DOCX.

## 1. Entrega executável

- [reference_domain.py](d49_reference_model/reference_domain.py) — estados, regras e entidades do **modelo de referência em memória**, sem Django, API ou base de dados.
- [test_reference_domain.py](d49_reference_model/test_reference_domain.py) — **32 testes unitários** para as guardas G01–G16 e condições negativas adicionais.
- [resultados_testes_d49.txt](d49_reference_model/resultados_testes_d49.txt) — saída de execução local, 32 testes terminados com sucesso.

### Como reproduzir

Com Python 3.10+ (somente biblioteca padrão):

```bash
cd docs/monografia/d49_reference_model
python -m unittest -v test_reference_domain
```

**Resultado observado na execução local:** `Ran 32 tests ... OK`. Este resultado é referente ao **modelo D49**, não a V01–V08, RNF01–RNF07, testes de integração da aplicação ou ensaios de usabilidade.

## 2. Que modelo foi efectivamente testado?

- **Decisão B proposta:** as máquinas de estados de `Engagement`, `DisputeCase` e `PaymentRecord` são independentes; abrir/fechar conflito não altera automaticamente a entrega, conclusão ou pagamento.
- **Decisão B1 proposta:** `Engagement` nasce em `PENDING_AGREEMENT` sem obrigação de já possuir `AgreementVersion`; uma versão aceite é necessária para passar a `ACTIVE`.
- **Aceitação explícita proposta:** as duas partes, com identificadores diferentes, aceitam **a mesma versão e conteúdo**; o registo de aceite está associado a um digest SHA-256 dos termos.
- **Conclusão proposta:** entrega registada pelo trabalhador; conclusão validada pelo empregador. Uma reclamação administrativa não substitui este fluxo.
- **Pagamento manual proposto:** o empregador declara o pagamento e a contraparte recebedora pode confirmar/contestar; este processo **não equivale a confirmação de instituição financeira**.
- **Rastreabilidade local:** registos de eventos incluem sequência, identificador da parte, operação e marca temporal UTC.
- **Autorizações de demonstração:** apenas partes podem negociar, entregar e reportar pagamentos; o papel administrativo é injectado na inicialização do modelo e não constitui autenticação de produção.

Estes são **pressupostos candidatos de concepção**. A D44 ainda não contém aprovação formal para a adopção integral deste desenho.

## 3. Matriz de evidência técnica dos guardas

| Guarda | Verificação executada **no modelo D49** | Limites |
|---|---|---|
| G01 | Proíbe autocontratação, imutabilidade dos IDs das partes | Não autentica identidade nem verifica perfis no backend |
| G02 | Nova contratação permanece `PENDING_AGREEMENT` e começa sem versões | Pressupõe B1 |
| G03 | Duas aceitações, rejeita desconhecidos e duplicados | Política de aceitação explícita ainda por aprovar |
| G04 | Versões rejeitadas não alteram versão vigente; histórico permanece; aceita v2 | Não há armazenamento persistente |
| G05 | Proíbe concluir sem entrega | Não verifica realidade do serviço físico/digital entregue |
| G06 | Impede entrega por empregador e conclusão por trabalhador; fluxo válido permitido | Não há serviço de autorização Django |
| G07 | Reportar conflito em `DELIVERED` não altera estado operacional | Decisão B proposta |
| G08 | Fechar conflito não conclui serviço | O papel administrativo existe apenas no modelo |
| G09 | Pagamento externo começa `REPORTED_PAID`, proibido sem acordo aceite | Sem bancos/PSP nem liquidação real |
| G10 | Pagador não auto-confirma; recebedor pode confirmar manualmente | Confirmação manual é política de negócio proposta |
| G11 | Contestar pagamento não altera `Engagement.status` | Não resolve reconciliação financeira futura |
| G12 | Eventos têm sequência, actor, acção e timestamp UTC | Sem assinatura de evento, não-repúdio ou persistência |
| G13 | Terceiro não pode propor nem administrar conflito; privilégios controlados por conjunto de admins | Administração injectada em memória, não RBAC real |
| G14 | Encerramento administrativo não altera o estado do contrato | Não implica autoridade jurídica |
| G15 | Ausência de mecanismo de transferência de fundos/PSP no modelo | O teste de ausência de métodos é **verificação limitada**, não prova de inexistência de PSP noutros sistemas |
| G16 | Digest divergente rejeitado e dados de AgreementVersion imutáveis ao nível de objecto | SHA-256 não é assinatura digital nem garante imutabilidade da base de dados |

### Testes negativos adicionais

A revisão após a primeira execução detectou e corrigiu no **modelo D49**:
1. Aceitar uma versão depois de cancelar a contratação;
2. Reportar pagamento sem acordo aceite;
3. Alterar os IDs das partes depois da criação;
4. Utilizar identificadores inválidos de versão, pagamento ou conflito;
5. Confirmar duas vezes o mesmo pagamento;
6. Propor uma segunda versão enquanto outra está pendente;
7. Pedir revisão de entrega com actor não autorizado;
8. Saltar etapas do processo administrativo de conflito.

Estes cenários já estão abrangidos pela execução final **32/32**. A descoberta destes defeitos no próprio modelo ilustra por que a simples existência de diagramas não é evidência suficiente de invariantes implementados.

## 4. Dependências bloqueadoras e decisões não resolvidas

| ID | Ponto | Política adoptada **só para ensaio** | Decisão formal ainda necessária |
|---|---|---|---|
| DEC-B | Independência entre estados de serviço, conflito e pagamento | Sim | Aprovação de alteração à Figura 5.11, A.2, A.6 e domínio |
| DEC-B1 | `AgreementVersion 0..*` em Engagement | Sim | Aprovação da cardinalidade da Figura 5.2 e DS01/DS02 |
| DEC-ACT | Aceite da parte proponente | Explícito, acção própria | Pode proposta equivaler a aceite? Regras de prova da identidade/conteúdo |
| DEC-PAY | Confirmação manual por recebedor | Sim | Evidência suficiente, política de contestação, tratamento de PSP |
| DEC-REV | `DELIVERED → ACTIVE` por pedido do empregador | Sim | Prazos, evidência, número de tentativas, relação com acordo vigente |
| DEC-CAN | Cancelamento | Requer parâmetro `permitted_by_policy` passado por camada superior | Política real, guarda derivada de regras e estados, sem aceitar boolean fornecido por cliente |
| DEC-DIS | Abrir conflito | Permitido em `ACTIVE`/`DELIVERED` | Elegibilidade após `COMPLETED` ou `CANCELLED`; vários conflitos concorrentes; recurso |
| DEC-HIS | Integridade do histórico | Objectos de versão congelados; eventos UTC em memória | Persistência, atomicidade, autoria autenticada, imutabilidade de dados e retenção |
| DEC-AUTH | Operações administrativas | Conjunto `admin_ids` atribuído à instância | Gestão de permissões no backend; nunca permitir escolha de perfil privilegiado pelo cliente |

**Não declarar qualquer uma destas políticas como regra final aprovada.** A configuração de ensaio é um instrumento de exploração conceptual, não uma delegação da supervisão nem um contrato de software.

## 5. Correspondência correcta com a monografia

O resultado D49 pode ser descrito **num documento de acompanhamento técnico** como «foram executados 32 ensaios unitários contra um modelo computacional de referência em memória que formaliza opções de desenho propostas». Se a banca aceitar esta experiência como material auxiliar, será obrigatório indicar claramente o objecto testado, o código, os pressupostos e as limitações.

**Não** escrever na secção 5.4 da D44 que `V01–V08` ou `RNF01–RNF07` passaram: esses cenários exigem observar o **software real**, não o modelo D49. Também não alterar a avaliação HG/HE1–HE4 como «comprovadas». Nenhum resultado aqui constitui demonstração de necessidades reais dos trabalhadores e empregadores em Maputo.

### Próxima etapa tecnicamente útil

A próxima acção de engenharia deve ser definir a **decisão de domínio** e implementar um primeiro conjunto vertical completo no backend e frontend (proposta aceite → `PENDING_AGREEMENT` → `AgreementVersion ACCEPTED` → `ACTIVE`), com verificações de API, persistência e autorização. Só então executar V02/V03 num ambiente identificado e transportar os resultados à monografia.

## 6. Critério de fecho D49

- [x] Modelar os três ciclos separados sem afirmar que estão implementados na aplicação.
- [x] Executar 32 testes locais unitários do modelo, incluindo negativos.
- [x] Disponibilizar código e registo de execução em ficheiros versionados.
- [ ] Rever e aprovar B/B1, aceitação bilateral, revisão e cancelamento.
- [ ] Alinhar figuras e requisitos com as decisões aprovadas, sem omitir divergências.
- [ ] Executar V01–V08 e RNF01–RNF07 contra o protótipo implementado, produzindo evidência real.
- [ ] Integrar a versão aprovada no Word canónico, conservando comentários, estilo, imagens e campos.

**Última revisão:** 02-11-2026. **DOCX canónico não modificado**.
