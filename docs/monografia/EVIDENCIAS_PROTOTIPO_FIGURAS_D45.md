# D45 — Auditoria de evidências demonstrativas e figuras 5.13–5.19

**Versão documental:** `Monografia_D44_Metodologia_Proveniencia_Verificada.docx` (pp. 59–62 e 80).  
**Fonte técnica auditada:** `enoqueJonas/freelance-frontend`, commit `f41d72e8ace6c716e799131cb46ce425a1a4c215` (27-05-2026).  
**Método:** leitura estática de `src/services/mockApi.ts`, `src/context/AuthContext.tsx`, `src/pages/Login.tsx`, `src/pages/OffersList.tsx`, `src/pages/Dashboard.tsx`, `src/pages/ProfileDetail.tsx` e `src/types.ts`. **Não houve execução da aplicação nem testes de integração.**

## 1. Achados verificáveis e consequência para a monografia

### EV-01 — Login demonstrativo não valida palavra-passe (P0)

`Login.tsx:110` permite explicitamente entrada sem password, apresentada como simulação de «tokens JWT salvos». `AuthContext.tsx` chama `mockApi.auth.login(emailOrUsername)`. `mockApi.ts` consulta utilizadores em `localStorage` por identificador e devolve o utilizador sem comparar senha ou token.

**Conseqüência:** a Figura 5.13 deve ser descrita como interface de **autenticação simulada** e **não** como prova de segurança, login JWT efectivo ou autenticação integrada. Qualquer referência a «JWT salvos» na interface não constitui evidência de armazenamento de JWT reais no browser.

### EV-02 — Declarações de custódia e garantia são materialmente incompatíveis com a arquitectura proposta (P0)

- `OffersList.tsx:313`: etiqueta «Ativo • Custódia Garantida».
- `Dashboard.tsx:819–822`: descreve «Meus Contratos Ativos & Escrow» e afirma custódia segura local de **todos** os contratos.
- `Dashboard.tsx:1035`: título «Garantia Escrow - Pagamento Seguro».
- `mockApi.ts:763–797`: `payments.createPay` cria um identificador aleatório de referência, grava o pagamento no `localStorage`, marca imediatamente `status:'completed'` e cria notificação afirmando custódia segura. Não faz chamada a serviço financeiro externo na função inspeccionada.
- A monografia D44, RN10 e §5.3.3, **excluem custódia pela aplicação**.

**Conseqüência:** não apresentar essas telas sem uma legenda explícita a identificar a **inconsistência do protótipo antigo e o uso de simulação**. A captura por si só transmite uma afirmação financeira falsa. A versão demonstrativa deveria remover promessas de custódia/garantia e substituir por «estado simulado de pagamento» até haver implementação e avaliação jurídica adequadas. A análise no documento pode mostrar a divergência, mas não a aprovar silenciosamente.

### EV-03 — Reputação e projectos concluídos apresentados sem base transaccional inicial coerente (P1)

- `mockApi.ts:56–57,72–73,88–89`: os perfis de trabalhadores começam com números sintéticos de trabalhos concluídos e classificações médias (`completedJobs`, `averageRating`).
- `mockApi.ts:193–194`: `INITIAL_CONTRACTS=[]` e `INITIAL_PAYMENTS=[]`.
- `mockApi.ts:206–209`: `INITIAL_REVIEWS` contém avaliações ligadas a IDs de contratos históricos, mas o conjunto inicial de contratos está vazio.
- `ProfileDetail.tsx:148,153` exibe essas métricas; `Dashboard.tsx:290,296` também.

**Conseqüência:** esses números são **dados de apresentação sintetizados**, não histórico verificável de serviços executados. A Figura 5.15 e Figura 5.18 não devem apresentá-los como demonstração de reputação rastreada à contratação (RN11–RN12). Qualquer legenda deve identificar «dados fictícios previamente carregados» e a ausência de associação verificável no conjunto inicial.

### EV-04 — Fluxo administrativo de disputa contradiz RN13 (P1)

- `mockApi.ts:738` anuncia que contrato disputado será analisado por «arbitragem».
- `Dashboard.tsx:213–219` usa texto de «mediação técnica», mas o quadro de administração permite resolver disputa alterando o contrato para `completed` ou `active` em `Dashboard.tsx:260–263, 1006, 1012`.
- D44 RN13 delimita reporte, evidência e acompanhamento sem autoridade arbitral universal.

**Conseqüência:** Figura 5.19 deve ser rotulada «representação demonstrativa de disputa; incompatibilidades com o modelo final», não como validação da governação proposta. Se a mudança de estado configurar decisão substantiva sobre obrigação contratual, a arquitectura precisa de limitar permissões e distinguir encerramento administrativo da resolução entre partes.

### EV-05 — Verificação documental simulada e exigência generalizada (P1)

- `mockApi.ts:438,508` impõe `documentStatus === 'approved'` para operações de oportunidade/proposta; `OffersList.tsx:415` apresenta essa condição como «conformidade legal».
- O modelo-alvo RN15 distingue verificação de perfil de KYC financeiro e condiciona recolha à finalidade necessária.

**Conseqüência:** a Figura 5.16 e a secção 5.3.3 devem conservar a discrepância de requisitos. Não afirmar uma exigência legal universal sem referência normativa verificada; tratar a validação documental como regra do protótipo e alternativa de desenho ainda sujeita a análise.

## 2. Protocolo para figuras autênticas

Sete marcadores `[PLACEHOLDER]` na D44 pp. 61–62 devem ser substituídos **apenas por capturas reais** ou removidos com indexação corrigida. Para qualquer captura, registar:

- hash do commit da versão executada; data da captura; browser/viewport; utilizador e cenário sintético; dados necessários para reprodução; estado da integração (mock ou API);
- a imagem deve mostrar um estado efectivamente observado, não ser reconstruída/manipulada para simular execução ou esconder uma falha;
- anonimizar informação pessoal e segredos; nunca apresentar contas, ratings e pagamentos fictícios como acontecimentos reais;
- confirmar se a numeração e legenda referenciadas existem também no índice de figuras.

### Legendas candidatas — não afirmar sucesso de testes

| Figura | Legenda sugerida | Nota de evidência |
|---|---|---|
| 5.13 | Interface demonstrativa de acesso e gestão inicial de perfis | Login baseado em dados locais; sem validação de password no mock |
| 5.14 | Pesquisa e filtragem de oportunidades no protótipo frontend | Dados simulados; sem confirmação de pesquisa backend |
| 5.15 | Apresentação de perfil profissional com dados de demonstração | Avaliações e trabalhos concluídos iniciais não derivam de contratos persistidos no conjunto inicial |
| 5.16 | Submissão simulada de proposta numa oportunidade | Exigências de verificação do protótipo divergem da especificação final |
| 5.17 | Representação demonstrativa de acordo e acompanhamento | Não representa `AgreementVersion` aceite bilateralmente |
| 5.18 | Apresentação de avaliações e indicadores de reputação simulados | Relação com contratações elegíveis e contestação não comprovada |
| 5.19 | Interface demonstrativa de reporte e gestão administrativa de disputa | Uso anterior de «arbitragem» não cumpre RN13 |

**Modelo de nota de fonte, apenas quando a captura existir:** «Fonte: Captura da execução do protótipo web, versão [SHA], [data], cenário sintético [ID]; dados de demonstração, sem integração com backend». Não inventar SHA da execução, data nem resultado.

## 3. Redacção pronta a inserir em §5.3.1 (bloco técnico complementar)

> A inspecção do código permite identificar algumas limitações que devem acompanhar a apresentação visual do protótipo. O fluxo de login é demonstrativo e permite seleccionar contas sem validação de palavra-passe, não se confundindo com a autenticação JWT configurada no backend. Os perfis iniciais incluem avaliações e indicadores de projectos concluídos fornecidos como dados de exemplo, sem correspondência integral com contratos persistidos no conjunto inicial de dados. A interface também conserva referências a custódia financeira garantida, embora os pagamentos sejam simulados e a arquitectura final exclua custódia própria. Por estas razões, as telas descrevem o estado demonstrativo de uma versão do frontend, não constituindo prova da segurança, integridade transaccional ou conformidade dos mecanismos concebidos.

## 4. Condições de aceitação

- [ ] Figuras genuínas obtidas a partir de versão executada ou marcadores removidos, sem substituição por imagens inventadas.
- [ ] Legendas e fontes preservam o carácter simulado dos dados.
- [ ] Nenhuma tela é citada para provar pagamentos, custódia financeira, elegibilidade de reputação ou autenticação real.
- [ ] Divergências entre requisitos e implementação são visíveis na secção de resultados e na discussão.
- [ ] Testes V01–V08 permanecem «não executado» até evidência reproduzível.
- [ ] Revisão visual e dos elementos gráficos do DOCX original, quando estiver disponível para edição.

**Nota:** esta entrega é auditoria de texto/código, não validação com browser nem alteração do Word.
