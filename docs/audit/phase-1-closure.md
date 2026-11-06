# Fecho da Fase 1 — Auditoria Estrutural

**Projecto:** Monografia — plataforma web de conexão entre trabalhadores autónomos de TI e empregadores/clientes  
**Data de fecho:** 2026-09-20  
**Estado:** **FASE 1 CONCLUÍDA**

## 1. Objectivo da fase

A Fase 1 teve como objectivo estabelecer uma baseline verificável antes de reescrever a monografia ou alterar funcionalmente o protótipo. A auditoria procurou responder a quatro perguntas:

1. O que a monografia actual afirma?
2. O que o frontend demonstra?
3. O que o backend efectivamente implementa?
4. Que inconsistências científicas, funcionais e técnicas precisam de ser resolvidas nas fases seguintes?

A fase não teve como objectivo aprovar os requisitos existentes nem adaptar a investigação ao código já construído.

## 2. Âmbito auditado

Foram auditados:

- estrutura e coerência interna do draft da monografia;
- problema, pergunta, objectivos, hipótese e delimitação existentes;
- metodologia declarada e evidência disponível da sua execução;
- amostra e apresentação dos resultados;
- requisitos funcionais e não funcionais existentes;
- modelação/arquitectura actualmente documentadas ou ausentes;
- frontend React/TypeScript;
- backend Django;
- alinhamento frontend ↔ backend;
- instrumentos de entrevista;
- processo de derivação de necessidades e requisitos.

## 3. Principais conclusões científicas

### 3.1 Âmbito ainda não está estável

O draft alterna entre aplicação web e aplicação móvel e nem sempre mantém explicitamente o recorte de trabalhadores autónomos da área de TI e Cidade de Maputo. A Fase 2 deve estabilizar o âmbito antes de reescrever capítulos dependentes dele.

### 3.2 A espinha dorsal científica precisa de realinhamento

Problema, pergunta de pesquisa, objectivos, hipótese, metodologia e resultados não formam ainda uma cadeia totalmente consistente. A pergunta existente e alguns objectivos não reflectem exactamente o título/âmbito. A hipótese contém formulação causal forte para o tipo de estudo/protótipo.

### 3.3 A metodologia declarada excede a evidência actualmente documentada

O draft menciona técnicas e análises que precisam de ser confirmadas contra aquilo que foi efectivamente executado. A versão final deverá declarar apenas métodos que possam ser demonstrados.

### 3.4 A amostra está inconsistente no draft

Foram encontrados números diferentes entre metodologia, capítulo de resultados e gráficos. Estes valores não devem ser reconciliados por inferência. A Fase 3 deverá consolidar a amostra efectivamente utilizada e corrigir todo o documento a partir dessa baseline.

### 3.5 Requisitos existentes não possuem rastreabilidade suficiente

Os RF/RNF actuais constituem uma base de trabalho, mas várias funcionalidades aparecem sem origem empírica/documental demonstrada. O código existente não será usado retroactivamente como fonte de requisito.

A cadeia adoptada para as fases seguintes é:

`problema → evidência → necessidade → regra de negócio → requisito → modelação → implementação → teste → conclusão`.

### 3.6 A apresentação dos resultados contém inconsistências

Foram identificadas divergências entre alguns gráficos e a interpretação textual. A reconstrução do capítulo de resultados deverá partir dos dados/evidências consolidados, e não apenas corrigir frases isoladas.

### 3.7 Bibliografia e referências exigem verificação

Existem referências malformadas, potencialmente não verificáveis, terminologia inconsistente e URLs/artefactos inadequados. Afirmações legais deverão ser verificadas em fontes moçambicanas aplicáveis.

## 4. Principais conclusões técnicas

### 4.1 Existem três níveis que não devem ser confundidos

1. **Solução concebida** — aquilo que a monografia pretende propor.
2. **Protótipo interactivo** — experiência demonstrável no frontend.
3. **Implementação técnica** — funcionalidades realmente implementadas/integradas.

A versão final da monografia deverá indicar claramente em qual nível cada funcionalidade se encontra.

### 4.2 Frontend

O frontend é um protótipo interactivo rico, mas utiliza `mockApi` e armazenamento local do browser. Funcionalidades apresentadas na interface não demonstram, por si só, integração real com Django, pagamentos, assinatura digital, mensageria em tempo real ou serviços externos.

### 4.3 Backend

O backend possui estrutura inicial para contas/perfis e partes do domínio, mas várias apps/modelos/views/testes encontram-se incompletos ou como stubs. Foram registados gaps de modelação, serialização, relações de papéis, verificação, segurança/configuração, higiene do repositório e ausência de testes significativos.

### 4.4 Frontend e backend não constituem actualmente uma solução integrada

O frontend simula uma quantidade de funcionalidades superior à implementação disponível no backend. A Fase 4 deverá reconciliar ambos somente depois de os requisitos terem sido reconstruídos e validados.

## 5. Instrumentos e exploração qualitativa

Foram preparados dois guiões semiestruturados:

- trabalhadores autónomos de TI;
- empregadores/clientes.

Foi ainda realizado um exercício estruturado de simulação de 11 entrevistas para testar o instrumento e o processo de análise temática. A simulação produziu N01–N18 como necessidades candidatas e evidenciou questões importantes para investigação, incluindo:

- confiança/reputação bilateral;
- diferentes formas de demonstrar competência;
- limitações de assessment obrigatório;
- formalização proporcional ao serviço;
- alterações de escopo como parte do domínio;
- diferentes modelos de preço/pagamento;
- comunicação versus necessidade real de chat interno;
- evidência necessária para conflitos;
- cold-start de reputação;
- localização relevante sobretudo para serviços presenciais.

**Regra de integridade:** o exercício simulado permanece separado dos registos de entrevistas efectivamente realizadas. Apenas dados efectivamente recolhidos podem ser apresentados como respostas empíricas de participantes.

## 6. Artefactos produzidos

A Fase 1 deixa como baseline:

- `docs/audit/backend-as-is.md`
- `docs/audit/frontend-as-is.md`
- `docs/audit/prototype-gap-analysis.md`
- `docs/research/interview-guide-workers.md`
- `docs/research/interview-guide-employers.md`
- `docs/research/interview-pilot-synthetic.md`
- `docs/research/interview-pilot-findings.md`
- `docs/research/document-analysis-matrix.md` — estrutura preparatória; análise documental ainda não concluída
- `docs/TRACKING.md`

## 7. Decisões carimbadas

1. O código não é fonte científica de requisitos.
2. Funcionalidades existentes não serão justificadas retroactivamente.
3. O frontend não será descrito como integrado com o backend enquanto essa integração não existir e for testada.
4. Simulações não serão descritas como integrações reais.
5. Necessidades candidatas não serão convertidas automaticamente em RF/RNF.
6. A triangulação só será executada depois de existir corpus empírico documentado e análise documental concluída.
7. Business rules devem anteceder RF/RNF na reconstrução.
8. A modelação será revista depois da especificação, não usada para justificar requisitos.
9. Testes deverão ser rastreáveis aos requisitos implementados.
10. A conclusão deverá responder à pergunta/objectivos com base no que foi efectivamente demonstrado.

## 8. Riscos transferidos para fases seguintes

- scope inconsistente;
- amostra contraditória;
- métodos declarados sem evidência suficiente;
- RF/RNF sem origem rastreável;
- funcionalidades do protótipo potencialmente não justificadas;
- discrepância frontend/backend;
- ausência de validação técnica suficiente;
- referências e afirmações legais por verificar;
- modelação incompleta;
- risco de sobreafirmar funcionalidades simuladas como implementadas.

Nenhum destes riscos é considerado resolvido apenas pelo fecho da Fase 1. O fecho significa que foram identificados, documentados e encaminhados.

## 9. Critério de saída

A Fase 1 é considerada concluída porque existe uma baseline suficiente para impedir que a reconstrução prossiga a partir de pressupostos não auditados:

- estado científico do draft diagnosticado;
- frontend e backend auditados;
- gaps técnicos documentados;
- problemas de rastreabilidade identificados;
- instrumentos qualitativos preparados;
- tracker e gates definidos.

## 10. Handoff para Fase 2

A Fase 2 — **Espinha dorsal científica** — deverá começar sem alterar ainda os requisitos definitivos.

Ordem prevista:

1. estabilizar âmbito e terminologia;
2. reconstruir problema de pesquisa;
3. alinhar pergunta de pesquisa;
4. rever objectivo geral;
5. rever objectivos específicos;
6. decidir tratamento da hipótese;
7. completar delimitação;
8. verificar a cadeia `Problema → Pergunta → Objectivos → Metodologia`.

A Fase 3 continuará depois com a reconciliação do estudo empírico e análise documental. A triangulação é um gate para a derivação definitiva de RN/RF/RNF.

---

**Marco:** `PHASE-1-CLOSED`  
**Próxima fase:** `PHASE-2-SCIENTIFIC-BACKBONE`
