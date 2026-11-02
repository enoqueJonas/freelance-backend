# D52 — Versionamento de acordos: implementação real, evidências e limites

**Data:** 02-11-2026  
**Código:** PR técnico [#5](https://github.com/enoqueJonas/freelance-backend/pull/5), branch `feat/d52-agreement-amendments`, dependente do PR #4 (D51) → PR #3 (D50).  
**Estado:** *draft*, sem merge e sem integração na D44 canónica.

## 1. Resultado de execução confirmado

A execução [GitHub Actions D52 #41483135110](https://github.com/enoqueJonas/freelance-backend/actions/runs/41483135110) concluiu com sucesso: **65 testes reais de API Django/DRF, 65 aprovados**. Distribuição: D50 (18), D51 (23), D52 (24).

- Execução do Python 3.13 com dependências do projecto.
- `python manage.py check`: sem problemas.
- `python manage.py makemigrations --check --dry-run`: `No changes detected`.
- `contracts.0002_agreement_lifecycle` aplicada com sucesso na base SQLite de teste.
- `Ran 65 tests ... OK`.

O workflow D51 também foi executado no mesmo ramo, com [41/41 aprovados](https://github.com/enoqueJonas/freelance-backend/actions/runs/41483135071), verificando retrocompatibilidade do fluxo base **após** actualização de dois testes D51 cujas expectativas tinham mudado.

**Histórico de falha controlada:** uma execução anterior [D52 #41482944802](https://github.com/enoqueJonas/freelance-backend/actions/runs/41482944802) terminou com **63/65 testes aprovados**, dois falhados por expectativas D51 obsoletas: (a) tentativa de utilizar versão de outra contratação sem enviar a impressão digital (400 antes de alcançar o 404 esperado), (b) expectativa antiga de que contratar em ACTIVE proibiria propor v2 (a nova especificação permite). Os testes foram corrigidos para verificar o contrato de API vigente e reexecutados com 65/65. O histórico de CI foi preservado.

## 2. Comportamentos efectivamente implementados

A aplicação persiste e disponibiliza uma sequência de alterações de acordo:

| Acção | Transição | Efeito sobre a contratação |
|---|---|---|
| Criar v1 | sem versão → v1 PROPOSED | Engagement permanece PENDING_AGREEMENT |
| Uma parte aceitar v1 | v1 PROPOSED com 1 aceite | Engagement permanece PENDING_AGREEMENT |
| Ambas aceitarem v1 | v1 PROPOSED → ACCEPTED | Engagement passa a ACTIVE |
| Propor v2 numa contratação activa | v2 PROPOSED | v1 permanece ACCEPTED e vigente; Engagement continua ACTIVE |
| Só uma parte aceitar v2 | v2 PROPOSED com 1 aceite | v1 mantém-se vigente |
| Ambas aceitarem v2 | v1 ACCEPTED → SUPERSEDED; v2 PROPOSED → ACCEPTED | Engagement continua ACTIVE; actualização atómica |
| Contraparte rejeitar v2 | v2 PROPOSED → REJECTED | v1 permanece ACCEPTED; registo de actor, motivo e data |
| Propor v3 após rejeição de v2 | v3 PROPOSED | Numeração monotónica; não reutiliza o número da versão rejeitada |
| Rejeitar v1 antes da activação | v1 PROPOSED → REJECTED | Engagement continua PENDING_AGREEMENT; pode propor v2 e aceitar |

**Protecções verificadas em testes:** pertença à relação, proibição de autocontratação herdada de D51, impressão digital explícita do conteúdo apresentada pela chamada de aceitação, rejeição de impressões digitais divergentes ou conteúdo alterado, proibição de auto-rejeição pela parte proponente, prevenção de aceite duplicado, rejeição após aceite, restrições de unicidade na base de dados para uma versão PROPOSED e uma versão ACCEPTED por contratação.

**Exemplo de pedido de aceitação** (esquema, não dados reais):

```http
POST /api/contracts/engagements/{engagement_id}/agreements/{version_id}/accept/
Authorization: Bearer <token>
Content-Type: application/json

{"content_fingerprint":"<hex_sha256_da_versao_consultada>"}
```

**Exemplo de rejeição**:

```http
POST /api/contracts/engagements/{engagement_id}/agreements/{version_id}/reject/
Authorization: Bearer <token>
Content-Type: application/json

{
  "content_fingerprint": "<hex_sha256_da_versao_consultada>",
  "reason": "Condições não aceites"
}
```

**Nota:** o SHA-256 é um identificador de integridade de conteúdo no fluxo e **não** assinatura electrónica qualificada, prova de autenticidade da pessoa por si só ou mecanismo criptográfico de não-repúdio.

## 3. Rastreabilidade com a D44

| Regra/requisito | O que D52 acrescenta | Estado científico permitido |
|---|---|---|
| RN05/RN07 — acordo e aceitação bilateral | Duas acções explícitas vinculadas à mesma versão e impressão digital | **Verificado na API**, não na interface |
| RN06 — alteração material acordada | Propor, aceitar ou rejeitar nova versão com preservação do acordo vigente | **Verificado na API para vN+1**, sem ensaio de UI |
| RN14 — preservar decisões | `AgreementAcceptance` e metadados de rejeição persistidos; `SUPERSEDED` preserva versão anterior | **Cobertura parcial**; não existe histórico de eventos completo |
| RF13 — formalização | Aceite inicial após proposta escolhida | **Parte do backend implementada e testada** |
| RF14 — versionamento | v1, v2/v3, rejeição e preservação da anterior | **Comportamento central implementado e testado no backend**; não RF14 completo com UI e todos os casos |
| V03/V04 | Operações de acordo com múltiplos cenários positivos/negativos | **Somente subconjunto de testes de API**; V03/V04 integrais permanecem por executar |

## 4. Decisões de âmbito ainda não aprovadas

- D48/B1: um Engagement em PENDING_AGREEMENT pode existir sem AgreementVersion.
- Proponente e contraparte registam aceitações independentes; propor não conta automaticamente como aceitar.
- A contraparte pode rejeitar, mas o proponente não pode rejeitar a própria versão no endpoint de rejeição. Eventual **retirada pelo proponente** exigirá decisão e fluxo separado.
- Um acordo activo mantém uma única versão vigente. A versão proposta é pendente sem efeitos sobre condições actuais até à segunda aceitação.
- A versão rejeitada preserva aceites preliminares, autor e motivo no histórico; não permite novo aceite.
- Não estão especificados prazos de aceitação, notificações, datas de validade de acordo, requisitos de testemunha, formalidades legais ou direitos de reclamação.

Estas escolhas são justificáveis como hipóteses técnicas, mas devem ser formalmente reconciliadas com a autora/supervisão e com os diagramas de actividades e sequências antes da integração académica.

## 5. Limites e próximos bloqueadores

1. Os testes usam SQLite temporário; transacções simultâneas e bloqueios sob PostgreSQL não foram ensaiados.
2. Não há frontend React ligado à API D51/D52, nem execução de tarefa com utilizadores.
3. Entregas, pagamentos, disputas e reputação são módulos não implementados neste corte.
4. A imutabilidade é aplicada ao nível do protocolo e da ausência de endpoint de actualização; acessos privilegiados à base de dados ainda poderiam editar linhas. O sistema não possui log de auditoria independente.
5. Segurança de produção não avaliada; o backend mantém configurações de desenvolvimento.
6. Nenhum comentário do supervisor foi resolvido por mera execução de testes; a D44 canónica permanece **inalterada**.

## 6. Critérios de fecho D52

- [x] Implementar estados PROPOSED/ACCEPTED/REJECTED/SUPERSEDED e endpoints.
- [x] Manter acordo anterior vigente até aceite bilateral da versão nova.
- [x] Persistir o motivo e a autoria da rejeição.
- [x] Incluir restrições de unicidade para vigente e pendente.
- [x] Executar suite real D50+D51+D52 com 65/65.
- [ ] Integrar frontend e JWT real.
- [ ] Testar concorrência e integridade em PostgreSQL.
- [ ] Confirmar regras B/B1/aceite/rejeição com supervisão.
- [ ] Executar V03/V04 completos com UI, dados e evidências.
- [ ] Actualizar diagramas/§§5.3–5.5 **no DOCX original**, sem perder 14 comentários nem campos automáticos.
