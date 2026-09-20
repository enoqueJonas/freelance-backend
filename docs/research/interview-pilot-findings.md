# Descobertas do Piloto de Entrevistas

> **Origem:** análise de dados sintéticos do piloto. Estas descobertas validam o método e geram hipóteses/necessidades candidatas; não constituem resultados empíricos da monografia.

## Método de análise

A leitura foi feita sem usar os RF existentes como grelha. A cadeia aplicada foi:

`resposta/excerto → código inicial → subtema → tema → necessidade emergente`.

Divergências e casos negativos foram preservados.

## Temas e necessidades emergentes

| Tema | ID | Necessidade emergente | Estado no piloto |
|---|---|---|---|
| Descoberta e matching | N01 | Facilitar descoberta de trabalhadores e oportunidades para além das redes pessoais existentes | Convergência forte |
| Descoberta e matching | N04 | Permitir pesquisa, filtragem e comparação segundo critérios relevantes, sem restringir indevidamente outras opções | Convergência moderada |
| Perfil, competências e confiança | N02 | Permitir demonstrar experiência/capacidade através de diferentes tipos de evidência adequados à especialidade e experiência | Convergência forte |
| Perfil, competências e confiança | N03 | Reduzir incerteza sobre identidade e legitimidade da contraparte | Convergência forte |
| Perfil, competências e confiança | N15 | Suportar diferenças entre tipos de serviços de TI sem impor um único modelo de apresentação, contratação ou preço | Convergência forte |
| Perfil, competências e confiança | N16 | Considerar localização quando relevante para execução presencial | Necessidade específica |
| Negociação e formalização | N05 | Registar claramente escopo, preço, prazo e entregáveis | Convergência forte |
| Negociação e formalização | N06 | Registar e obter aceitação de alterações relevantes às condições acordadas | Convergência forte |
| Negociação e formalização | N07 | Adequar o nível de formalização à natureza/complexidade do serviço, preservando evidência do acordo | Convergência moderada |
| Comunicação e rastreabilidade | N08 | Preservar informação relevante da comunicação e decisões relacionadas com a execução | Convergência moderada |
| Pagamentos e protecção | N09 | Definir valor, método, momento e condições de pagamento | Convergência forte |
| Pagamentos e protecção | N10 | Reduzir risco de incumprimento associado a pagamento e entrega para ambas as partes | Convergência forte |
| Reputação | N11 | Permitir reputação bilateral baseada nas relações realizadas | Convergência forte |
| Reputação | N12 | Contextualizar/contestar reputação quando necessário | Convergência moderada |
| Conflitos | N13 | Reportar, documentar e acompanhar conflitos | Convergência moderada |
| Conflitos | N14 | Preservar evidências úteis à resolução de conflitos | Convergência moderada |
| Adopção | N17 | Manter a utilização simples e proporcional à complexidade do serviço | Convergência moderada |
| Adopção | N18 | Existir massa crítica de oportunidades e profissionais | Condição de adopção |

“Forte/moderada/específica” é apenas uma indicação qualitativa da recorrência no piloto, não uma escala estatística.

## Descobertas que desafiam o desenho actual

### Confiança é bilateral
O trabalhador também assume risco ao aceitar um cliente desconhecido. Verificação e reputação não devem ser assumidas como mecanismos exclusivamente dirigidos ao trabalhador.

### Assessment não está validado como gate
O piloto contém posições divergentes. Testes podem ser úteis em alguns contextos, mas especialidades como suporte, redes e hardware tornam inadequado assumir um teste técnico uniforme ou obrigatório.

### Portfólio não é universal
GitHub/Behance funcionam para alguns perfis, mas referências, certificações, projectos pessoais, experiência e outras evidências podem ser mais adequadas noutros.

### Chat não emerge como necessidade autónoma
WhatsApp já satisfaz comunicação básica para vários participantes. O valor potencial da plataforma está sobretudo em preservar decisões/evidências ligadas ao trabalho.

### Formalização deve ser proporcional
O piloto não sustenta assinatura electrónica/contrato pesado como condição obrigatória para todo serviço. O elemento recorrente é conseguir provar o que foi acordado.

### Preço nem sempre pode ser conhecido na publicação
Serviços de diagnóstico/manutenção podem exigir avaliação prévia. O modelo não deve assumir preço fechado em todos os casos.

### Alterações fazem parte do domínio
Scope creep, mudança de preço/prazo e aprovação de alterações aparecem repetidamente. A alteração do acordo deve ser analisada como parte própria do ciclo.

### Disputas dependem de evidências
O piloto sustenta reporte/acompanhamento de conflitos, mas não demonstra que um administrador possa arbitrar tecnicamente qualquer disputa.

### Reputação tem cold-start e risco de abuso
Profissionais novos podem não possuir histórico. Avaliações isoladas também podem ser injustas ou pouco contextualizadas.

### Localização é contextual
É importante para serviços presenciais, mas não deve ser assumida como critério universal para todo trabalho de TI.

## Modelo de domínio sugerido pelo piloto

O fluxo candidato deixa de ser apenas:

`Worker → Verification/Assessment → Offer → Proposal → Contract → Signature → Payment → Review`.

O piloto sugere investigar um ciclo mais flexível:

`confiança bilateral → descoberta/matching → proposta/negociação → condições acordadas → execução/alterações → entrega/pagamento → reputação bilateral`

com comunicação/rastreabilidade e conflitos/evidências como aspectos transversais.

## Limite desta análise

Nenhuma N01–N18 deve ser promovida automaticamente a requisito. A validação científica deverá considerar entrevistas reais e, posteriormente, análise documental/benchmark. O código actual também não constitui evidência científica.
