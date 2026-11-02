# D51 — Primeira implementação real de contratação e limites da evidência

**Data:** 02-11-2026. **Fonte técnica:** PR #4, https://github.com/enoqueJonas/freelance-backend/pull/4, branch feat/d51-contract-core, dependente do PR #3 (D50).

## 1. Evidência verificável

- GitHub Actions run #41481395290: https://github.com/enoqueJonas/freelance-backend/actions/runs/41481395290
- Resultado confirmado nos logs: **Ran 41 tests ... OK**, sendo 18 testes herdados de D50 e 23 novos testes D51 contra Django/DRF real em base de dados SQLite temporária.
- O system check reportou zero problemas; makemigrations --check --dry-run reportou No changes detected; marketplace.0001_initial e contracts.0001_initial foram aplicadas no ambiente de teste.
- A revisão testada continha o código de implementação e os testes. Um commit posterior adicionou apenas documentação de âmbito.
- Os resultados não são do modelo independente D49, nem da UI React, nem de utilizadores reais.

## 2. Fluxo efectivamente implementado na API

1. Criar oportunidade DRAFT e publicar OPEN por empregador titular.
2. Submeter uma proposta SUBMITTED por trabalhador de outra conta (uma proposta por trabalhador/oportunidade).
3. Empregador aceitar uma proposta, rejeitar outras pendentes e criar Engagement PENDING_AGREEMENT; oportunidade fecha.
4. Criar AgreementVersion v1 PROPOSED com âmbito e preço definido ou preço posterior a diagnóstico.
5. Registar a aceitação explícita por cada interveniente sobre a mesma versão e fingerprint do conteúdo.
6. Depois das duas aceitações, AgreementVersion ACCEPTED e Engagement ACTIVE.

## 3. Cobertura parcial (não confundir com V02/V03 integrais)

| Elemento D44 | Verificado na API D51 | Lacuna |
|---|---|---|
| RN01 / RN02 | Perfis acumuláveis e proibição de auto-contratação por User ID | Autorização completa em todos os recursos e interface React |
| RF07 | Criar/publicar oportunidade; encerramento após seleção | Editar, cancelar e outras transições |
| RF11 | Submeter proposta, detectar duplicados e validar oportunidade aberta | Alterar, retirar e consultar estado na UI |
| RF12 | Selecionar proposta e recusar automaticamente alternativas | Rejeição manual, histórico e regras adicionais |
| RF13 | Primeira versão do acordo e aceite explícito de ambas as partes | Prazos, entregáveis, condições e fluxo visual completo |
| RF14 | Identificador e fingerprint da v1; aceites registados | Versionamento subsequente v2, rejeição, preservação histórica de adendas |
| RF18 | Preço definido ou após diagnóstico na primeira versão | Condições por etapa, periodicidade e integração financeira |
| RNF02 / RNF04 | Controlo básico de permissão, atomicidade e duas aceitações persistidas | Concorrência em PostgreSQL, integridade a longo prazo, auditoria persistente integral, segurança da aplicação |
| V02 / V03 | **Subconjunto de comportamentos** comprovado por testes de API | V02/V03 completos continuam NÃO EXECUTADOS: falta frontend e vários caminhos |

## 4. Decisões provisórias não aprovadas

- Assumiu-se B1: Engagement nasce sem AgreementVersion, que só é proposta depois da escolha da proposta.
- Assumiu-se que o proponente regista um aceite explícito separado da submissão dos termos.
- Assume-se activação com duas aceitações distintas da mesma versão e fingerprint. A impressão digital SHA-256 não constitui assinatura digital nem prova jurídica independente.
- O modelo B proposto separa status operacional do contrato de processos de conflito e pagamento, mas D51 **não implementa** ainda conflito, pagamento, entrega ou conclusão.
- Não tratar estes pressupostos como aprovação académica. Figuras 5.2/5.4/5.11/DS01/DS02 e RN05/RN07 requerem reconciliação antes de integrar a D48 no Word.

## 5. Implicações precisas para o texto da monografia

- §5.3 pode reportar a execução técnica de um **corte vertical de API**, com commit e ambiente, depois de a D44 ser integrada na versão canónica e a autora aceitar a formulação.
- §5.4 continua sem comprovação de V01–V08 em versão completa; **não substituir Não executado por Passou** com base nestes 41 testes.
- §5.5 e Capítulo VI podem mencionar progresso técnico posterior, mas devem continuar a distinguir: especificado, API implementada, interface integrada, ensaio executado e validação com público-alvo.
- Não inferir que a aplicação já facilita a contratação de trabalhadores e empregadores reais em Maputo; nenhum estudo de utilização foi executado.

## 6. Próximas acções

- [x] Implementar e testar ciclo mínimo da API, com dois perfis de contas distintas e aceitação bilateral.
- [x] Confirmar migrações e resultados com GitHub Actions: 41/41 testes.
- [ ] Rever código de autorização, concorrência e imutabilidade com PostgreSQL.
- [ ] Completar v2/adendas e fluxo de rejeição antes de atribuir a RF14 estado integral de implementado.
- [ ] Integrar frontend React com backend JWT e endpoints D51; remover simulação do caminho testado.
- [ ] Executar V02/V03 completos e RNF pertinentes, com resultados reais e capturas autênticas.
- [ ] Confirmar decisões B/B1/aceite com supervisão antes de alterar figuras e metodologia.
- [ ] Inserir resultados na D44 original **apenas com acesso seguro ao DOCX**, mantendo os 14 comentários e os campos.

**Limite documental:** este é um relatório de auditoria de API, não alteração ao Word, nem certificado de segurança, usabilidade ou adequação empírica.
