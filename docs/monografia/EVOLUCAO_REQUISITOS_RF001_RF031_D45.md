# D45 — Reconciliação histórica da especificação: RF001–RF031 vs. RF01–RF28

**Origem antiga:** `DocumentoDeRequisitos.docx`, Google Drive, criado em 20-09-2025 e modificado em 19-04-2026, 31 requisitos identificados `RF001`–`RF031`. URL:
https://docs.google.com/document/d/1ZEPLpljTsaXghR7rtJD049cgrKTsVsvk/edit

**Versão em auditoria:** `Monografia_D44_Metodologia_Proveniencia_Verificada.docx`, Quadro 5.3, pp. 46–47, 28 requisitos identificados `RF01`–`RF28` e RN01–RN16.

**Estatuto:** **comparação pelo conteúdo e semântica**, não por semelhança de números. Este documento NÃO demonstra que a versão antiga era formalmente aprovada, que a nova foi aprovada, ou que uma substituiu oficialmente a outra. O documento anterior diz no início «Isso é adição ao rascunho que fizemos no papel ...», pelo que deve ser tratado como **rascunho histórico**, não como baseline contratual.

## 1. Mapeamento por função: 31 requisitos antigos

| Requisito antigo | Intenção documentada na fonte antiga | Situação face à D44 | Referência na D44 / decisão a verificar |
|---|---|---|---|
| RF001 | Criar conta | Mantido, alterado | RF01 registar utilizador; campos e evidências do registo diferem |
| RF002 | Iniciar sessão | Mantido | RF02 autenticar utilizador; frontend actual só simula acesso |
| RF003 | Actualizar conta e carregar documentos | Redefinido | RF03/RF04 perfis, RF05 evidências, RF06 verificação; detalhes de alteração de senha precisam de decisão |
| RF004 | Submeter testes para verificar habilidades | **Deixou de ser requisito central** | RN03 dispensa avaliação universal obrigatória. Facultatividade não é teste implementado |
| RF005 | Consultar estado da avaliação de habilidades | **Mudou a finalidade** | RF06 acompanhar verificação; não presumir que subsiste teste de competências |
| RF006 | Submeter documentos de empregador para verificação | Generalizado | RF06 verificação do perfil, RN15 finalidade e minimização |
| RF007 | Consultar estado da verificação de empregador | Generalizado | RF06 solicitar e acompanhar verificação |
| RF008 | Publicar oportunidade se verificado | Mantido com regra alterada | RF07 ciclo de oportunidade; RN15 não exige aprovação documental universal. Regra antiga bloqueia publicação |
| RF009 | Pesquisar oferta | Mantido | RF08 pesquisar oportunidades |
| RF010 | Notificações de ofertas compatíveis | **Sem RF explícito central** | Pode existir no frontend demonstrativo, mas não deve ser reivindicado como requisito final validado |
| RF011 | Pesquisar trabalhador | Mantido | RF09 pesquisar trabalhadores |
| RF012 | Submeter proposta se verificado | Mantido com regra alterada | RF11, RN02; bloquear todos os não verificados não consta como regra universal da D44 |
| RF013 | Editar/cancelar proposta antes de avaliação | Generalizado | RF11 gerir proposta própria; etapas/limites de alteração exigem critérios |
| RF014 | Consultar propostas recebidas | Generalizado | RF12 avaliar proposta recebida; a consulta é pré-condição a explicitar |
| RF015 | Efectuar pagamento por API externa | Transformado em integração facultativa | RF18 termos, RF19 estado, RF20 prestador externo **quando aplicável** |
| RF016 | Registar e mostrar confirmação de pagamento via API | Reformulado | RF19 estado, RF20 condicional; distinguir declarado/confirmado e sem simular prova bancária |
| RF017 | Receber pagamento através das APIs | **Sem prestação financeira central garantida** | RF20 condicional. Não presumir que o sistema paga/recebe fundos |
| RF018 | Avaliar trabalhador | Generalizado | RF21 avaliação bilateral, RN11 elegibilidade |
| RF019 | Avaliar empregador | Generalizado | RF21 avaliação bilateral, RN11 |
| RF020 | Gerir utilizadores e aprovar verificações | Desdobrado | RF26 gerir utilizadores; RF28 analisar verificação |
| RF021 | Administrador validar testes de habilidades | **Deixou de ser obrigação central** | RN03; não substituir por RF28 sem especificar que RF28 é verificação de perfil, não prova técnica |
| RF022 | Validar documentos do empregador | Generalizado | RF28 analisar verificação, RN15 |
| RF023 | Remover oportunidades fraudulentas | Mantido em governação | RF27 moderar oportunidade reportada; RN16 exige motivo/estado |
| RF024 | Remover propostas suspeitas | **Sem RF autónomo claro** | RF26 gerir utilizadores não prova capacidade de moderação de propostas; decidir se é exclusão deliberada ou lacuna |
| RF025 | Bloquear publicação/submissão de contas não verificadas | **Deixou de ser regra universal** | RN15 minimização/verificação contextual; frontend ainda mantém bloqueio antigo |
| RF026 | Notificar ofertas, propostas, mensagens e verificação | **Sem RF explícito central** | Notificações existem no mock, mas não correspondem por si a requisito final aprovado |
| RF027 | Mensagens privadas trabalhador–empregador | **Sem RF explícito central** | N08 e RN14 exigem conservar decisões relevantes, não chat obrigatório |
| RF028 | Gerar contrato digital a partir de proposta aceite | Reformulado | RF13 formalizar condições, com Engagement e versão de acordo |
| RF029 | Assinatura electrónica bilateral de contrato | Reformulado | RF13 + RN07; aceitação bilateral não equivale a assinatura electrónica avançada universal |
| RF030 | Consultar contratos activos/concluídos | Alargado | RF17 consultar histórico; estados e versões conceptualizados |
| RF031 | Administrador intervir em contratos disputados | Restringido | RF24/25 denúncia e acompanhamento, RN13 proíbe arbitragem presumida |

### Cuidado ao interpretar «31 → 28»

A redução numérica é **enganadora como medida de escopo**. A D44 combina antigos requisitos, altera condições e acrescenta capacidades inexistentes no rascunho. Há reestruturação de conceitos, não uma simples operação «retirar três linhas». Nenhum identificador deve ser equiparado por semelhança de número (RF015 antigo ≠ RF15 actual).

## 2. Capacidades explicitadas ou introduzidas na D44

| Capacidade actual | Identificador | Evidência na especificação antiga | Razão e origem que ainda exigem rastreabilidade |
|---|---|---|---|
| Um utilizador com perfis acumuláveis | RN01, RF03, RF04 | A versão antiga distingue papéis, mas não especifica acumulação | Decisão de domínio e potencial maior cobertura de casos |
| Anti-autocontratação | RN02 | Não aparece como regra explícita independente | Integridade/autorização; caso negativo V02 |
| Evidências profissionais diversas | RN03, RF05 | GitHub/portfólio na conta e testes de habilidades | Optou-se por flexibilidade, sem impor exames |
| Localização facultativa conforme serviço | RN04 | Não explicitada como regra | Serviços TI remotos vs presenciais; corpus não comprovado como campo real |
| Preço condicionado ao diagnóstico | RN08, RF18 | RFs anteriores não prevêem explicitamente | Serviços de suporte/manutenção e cenários exploratórios |
| Versionamento das condições do acordo | RN06, RF14, RNF04 | Não explicitado como requisito autónomo | Rastreabilidade e histórico de decisões; verificar modelos |
| Registos estruturados de execução/entrega | RF15, RF16, RF17 | Contratos antigos focados em assinatura/consulta | Necessidade de acompanhar execução e não só contratação |
| Reputação contextual e contestável | RN12, RF22, RF23 | Avaliação bilateral básica já prevista | Contestar reviews e moderar reputação |
| Reporte de conflito separado de arbitragem | RN13, RF24, RF25 | Intervenção administrativa em disputa | Limitação de poderes e preservação de evidências |
| Regra expressa de não custódia | RN10, RF19/20 | Integração de pagamento anteriormente obrigatória | Decisão de âmbito jurídico-técnica; não atribuída a autorização regulatória verificada |
| RNF de privacidade, integridade e interoperabilidade | RNF02–RNF07 | Texto da fonte antiga contém cabeçalhos mas não lista detalhada | Decisões de qualidade e governação a fundamentar |

## 3. Registo de decisão pendente (não inventar aprovações)

A versão final necessita de um **log de decisões** que permita responder à banca e ao supervisor:

| ID | Decisão que deve ser documentada | Alternativa anterior | Justificação aceitável | Evidência ainda necessária |
|---|---|---|---|---|
| DEC-01 | Tornar testes técnicos facultativos | RF004/RF021 antigos obrigatórios | Heterogeneidade das profissões; custo/risco de prova universal | Comparação de literatura, requisitos de qualidade e aprovação de âmbito |
| DEC-02 | Não exigir documentos aprovados para todas as operações | RF008/RF012/RF025 antigos | Minimização de dados, adequação ao risco da operação e acesso inclusivo | Política verificável de verificação e dados; validação jurídica se alegada |
| DEC-03 | Tornar integração financeira opcional e eliminar custódia própria | RF015–RF017 antigos + mensagens de escrow no frontend | Delimitação funcional e redução da superfície regulatória | Justificação técnica/documental, avaliação de riscos, clarificação de não custódia |
| DEC-04 | Não tornar chat e notificações funcionalidades centrais | RF010/RF026/RF027 antigos | Rastreabilidade pode existir sem chat em tempo real, evitar escopo desnecessário | Análise custo/valor, necessidades testadas futuramente, aprovação do âmbito |
| DEC-05 | Versionar acordos e aceitar alterações bilateralmente | Contrato digital + assinatura simples RF028–RF030 | Preservação de decisões e prova do acordo | Regras de negócio e testes V03 |
| DEC-06 | Distinguir conflito reportado de arbitragem | RF031 antigo | Limitação de competência do operador e preservação de evidência | Política de moderação e critérios para encaminhamento externo |
| DEC-07 | Admitir ambos os perfis na mesma conta | Modelo antigo de papéis separados | RN01 e casos de uso de trabalhador/empregador | Autorização contextual, prevenção de autocontratação e ensaios V01/V02 |
| DEC-08 | Retirar ou manter moderação específica de propostas | RF024 antigo | Se retirada, razão de âmbito; se mantida, RF e actor explícitos | Decisão de escopo, regras e casos de abuso |

Para cada DEC, preencher: autor/responsável da decisão, data **real**, origem do pedido, argumento, impacto no modelo/UML/código/testes, e evidência de revisão. Não inferir autorização do supervisor a partir da palavra «aprovada» presente na D44.

## 4. Implicações científicas e redacção proposta

### §3.5 / §5.2.1 — explicitar evolução histórica dos requisitos

> A especificação foi consolidada a partir de documentos de trabalho anteriores e da revisão conceptual das necessidades, tendo algumas funcionalidades inicialmente consideradas sido reformuladas, classificadas como opcionais ou excluídas do âmbito obrigatório. Entre as alterações encontram-se a opção por verificação de competências não universal, a definição contextual da verificação de perfis, a separação de pagamentos realizados por prestadores externos e o registo versionado de condições acordadas. Estas decisões de engenharia devem ser distinguidas das necessidades empiricamente validadas, uma vez que a proveniência de parte do corpus exploratório permanece por comprovar. A correspondência entre a especificação anterior e a actual encontra-se no registo de evolução de requisitos.

**ATENÇÃO:** incluir «encontra-se no registo de evolução» apenas se o registo final efectivamente for incorporado/anexado à monografia com referência controlada. Não afirmar existência de log aprovado enquanto só há proposta de auditoria.

### §5.5 — interpretação correcta da alteração do âmbito

> A comparação com a especificação de trabalho anterior demonstra uma reorganização do âmbito, e não apenas uma redução do número de requisitos. Algumas funcionalidades, como notificações e conversação privadas, deixaram de constituir obrigações centrais; outras, como aceitação e versionamento de acordos, contestação de reputação e separação entre acompanhamento de conflitos e arbitragem, tornaram-se mais explícitas. Esta evolução orientou o modelo-alvo, mas a justificação de cada decisão deve ser conservada como elemento de rastreabilidade da engenharia, sem ser apresentada como resultado empírico comprovado de entrevistas não documentadas.

**Condição de uso:** confirmar a proveniência e a intenção do documento antigo; como rascunho, não fornece por si só prova de decisão formal/assinatura.

## 5. Riscos observados que a evolução do escopo não resolve

1. Os mecanismos antigos mantidos no **frontend mock** podem contradizer a nova regra: verificação universal para propostas, role exclusivo e promessa de custódia. A monografia descreve correctamente várias dessas discrepâncias.
2. **A simples contagem dos RF pode esconder requisitos perdidos**: é necessário demonstrar por que moderação de proposta (RF024 antigo), chat e notificações não constam da baseline.
3. **Falta ligação formal a cada origem**: documento antigo, fonte publicada, cenário exploratório, risco normativo, decisão de engenharia e sign-off, quando existente.
4. **Aprovado vs consolidado**: D44 usa «baseline aprovada», mas a pesquisa actual não encontrou no material examinado um registo identificável de aprovação da passagem RF001–RF031 para RF01–RF28.

## 6. Próximas acções e critérios

- [ ] Revisar este mapa 31→28 com a autora e a supervisão; não inventar sign-offs ou mudar requisitos sem aprovação.
- [ ] Corrigir narrativa da monografia para esclarecer que o documento antigo é um rascunho de evolução, não necessariamente uma baseline formal.
- [ ] Preencher DEC-01–DEC-08 com evidências reais e confirmar escopo final.
- [ ] Actualizar os casos de uso, UML e V01–V08 conforme **somente** decisões confirmadas.
- [ ] Confrontar a versão final com o frontend/backend, mantendo distinção conceptual vs executado.
- [ ] Não modificar o DOCX canónico sem acesso aos seus bytes originais e preservação de comentários/estilos/figuras.

**Resultado:** comparação documental fundada entre uma versão anterior de RF001–RF031 e a D44 RF01–RF28; a formalização e aprovação das decisões permanecem pendentes.
