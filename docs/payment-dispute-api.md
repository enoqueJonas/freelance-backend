# ConecTA — API de pagamentos externos e acompanhamento de conflitos

Estado: protótipo Django/DRF, branch `feat/conecta-backend-payments-disputes` (base PR #9). Esta API **não** processa pagamentos, não controla fundos e não oferece arbitragem.

## Pagamentos externos — RN09/RN10

A declaração do empregador só é aceite com contrato em estado `active` ou `completed` e uma versão de acordo `active`. O servidor associa a declaração à versão e etapa aprovadas; a parte que reporta é sempre o utilizador autenticado (não um ID escolhido pelo browser).

| Método | Caminho | Autorização |
|---|---|---|
| GET | `/api/payments/contracts/{contract_id}/` | Ambas as partes |
| POST | `/api/payments/contracts/{contract_id}/` | Empregador |
| POST | `/api/payments/{payment_id}/respond/` | Trabalhador |

Exemplo de declaração:
```json
{
  "amount": "3000.00",
  "method": "M-Pesa",
  "stage": "ADVANCE",
  "moment": "Após aprovação bilateral do acordo",
  "paid_on": "2026-11-10",
  "agreement_condition_id": "advance",
  "external_reference": "DEMONSTRACAO-001",
  "notes": "Apenas informação sintética."
}
```

Resposta do trabalhador:
```json
{"action": "CONFIRMED"}
```
ou
```json
{"action": "CONTESTED", "reason": "Não recebi o valor declarado."}
```

Estado: `REPORTED_PAID → CONFIRMED | CONTESTED`. `CONFIRMED` significa **afirmação do trabalhador de ter recebido**, não confirmação pelo operador de pagamento. O sistema não guarda saldos nem emite comprovativos bancários. Registos são preservados com autoria e data. As somas consideram declarações ainda pendentes ou confirmadas; uma contestação exclui o registo do teto declarativo mas **não prova que o pagamento não ocorreu**.

## Conflitos — RN13/RN14/RN16, RF24/RF25, V07

| Método | Caminho | Autorização |
|---|---|---|
| GET / POST | `/api/disputes/` | Listagem das partes/administrador; reporte das partes |
| GET | `/api/disputes/{id}/` | Partes ou administrador |
| POST | `/api/disputes/{id}/evidence/` | Uma das partes |
| POST | `/api/disputes/{id}/begin-review/` | Administrador `is_staff` |
| POST | `/api/disputes/{id}/request-information/` | Administrador `is_staff` |
| POST | `/api/disputes/{id}/result/` | Administrador `is_staff` |
| POST | `/api/disputes/{id}/close/` | Administrador `is_staff` |

Exemplo de reporte:
```json
{
  "contract_id": 1,
  "category": "DELIVERABLE",
  "description": "O relatório de testes acordado não foi entregue na data prevista.",
  "evidence_description": "Descrição da comunicação relativa ao relatório em falta.",
  "evidence_url": "https://example.test/referencia-sintetica"
}
```

Evidência adicional: `{"description": "...", "url": "https://example.test/..."}`.

Ações administrativas:
- Iniciar análise: `{"note": "Justificação da abertura de análise"}`
- Solicitar informação: `{"requested_from_user_id": 123, "note": "Indique a data de aprovação"}`
- Registar resultado: `{"note": "Resultado documental não vinculativo ..."}`
- Encerrar: `{"note": "Motivo do encerramento administrativo"}`

O estado progride `OPEN → UNDER_REVIEW → WAITING_INFORMATION → UNDER_REVIEW → RESOLVED → CLOSED`. Apenas a resposta da parte **solicitada** liberta `WAITING_INFORMATION`. Nem a abertura nem o encerramento do conflito alteram automaticamente o contrato ou qualquer pagamento. O resultado da análise **não é sentença nem decisão arbitral**.

## Limitações

- O backend autentica, autoriza e guarda eventos em base de dados, mas o histórico **não é criptograficamente inviolável**; administradores da base de dados podem alterar os dados.
- URLs de evidências são apenas referências HTTP(S); não há upload seguro, verificação da autenticidade ou garantia de conservação do recurso remoto. Não utilizar dados pessoais reais nesta demonstração.
- Ações administrativas só são disponibilizadas a contas Django com `is_staff=True`. Isto não equivale a formação profissional ou licença para arbitragem.
- A integração UI está pendente. O frontend tem campos camelCase; os DTOs da API são em snake_case. Adaptar autenticação e valores monetários antes de desativar o `mockApi`.
- Não há integração com M-Pesa, e-Mola, bancos ou prestadores de identidade.
- A aceitação jurídica dos contratos e os requisitos específicos da monografia precisam de revisão documental independente.

## Verificação

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test apps.accounts.tests apps.marketplace.tests apps.contracts.tests apps.payments.tests apps.contracts.test_disputes --verbosity 2
```

Executar testes com diferentes contas: empregador, trabalhador, administrador e terceiro. A contagem mínima esperada na CI desta etapa é **60 casos**; a execução real e o resultado constam do GitHub Actions.
