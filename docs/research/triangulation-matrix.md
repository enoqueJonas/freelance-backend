# Matriz de Triangulação — Corpus de Trabalho

## Regra de proveniência

Esta matriz é um artefacto interno de engenharia de requisitos. Usa:
- o corpus de trabalho de 11 entrevistas (8 trabalhadores e 3 empregadores) para testar a derivação;
- as notas empíricas adicionais fornecidas sobre o Desenvolvedor Web e o Especialista em Redes;
- o corpus documental consolidado em `document-analysis-matrix.md`.

A matriz não transforma automaticamente uma necessidade em RF. A cadeia é:

`entrevista → código/tema → evidência documental → convergência/divergência → necessidade consolidada → RN/RF/RNF candidato`.

## Triangulação N01–N18

| ID | Evidência do corpus de trabalho | Evidência documental | Leitura da triangulação | Estado |
|---|---|---|---|---|
| N01 | Trabalhadores referem referências, LinkedIn, WhatsApp e outros canais; Desenvolvedor Web também usa anúncios pagos na Meta. Empregadores recorrem sobretudo a referências/redes. | ILO/WESO: descoberta e matching são funções centrais; dificuldade de encontrar clientes aparece como limitação. | Convergência forte: existe necessidade de ampliar descoberta para além das redes existentes. Meta reforça esforço activo de aquisição, mas não prova redução de custo pela ConecTA. | **Consolidar** |
| N02 | GitHub, Behance, projectos, referências, certificações, experiência e entrevistas são usados de modo diferente por especialidade. | WESO/benchmarks: perfil, histórico, portfólio e reputação são sinais de capacidade. | Convergência forte; solução deve aceitar evidências heterogéneas. | **Consolidar** |
| N03 | Trabalhadores e empregadores demonstram preocupação com legitimidade da contraparte e publicações suspeitas. | WB/BdM: identidade/confiança são relevantes em ecossistemas digitais; KYC financeiro é conceito distinto. | Necessidade bilateral confirmada; mecanismo de verificação ainda aberto. | **Consolidar** |
| N04 | Empregadores querem comparar área, experiência, trabalho anterior, preço e, quando relevante, localização; trabalhadores rejeitam matching excessivamente restritivo. | WESO/Upwork: pesquisa, filtros e sinais de perfil são mecanismos comuns. | Pesquisa/filtragem é suportada; algoritmo obrigatório não. | **Consolidar** |
| N05 | Escopo, preço, prazo e entregáveis aparecem repetidamente em problemas/negociação. | ILO/Upwork: condições e propostas estruturadas fazem parte da contratação. | Convergência forte. | **Consolidar** |
| N06 | Scope creep e mudanças não documentadas aparecem em vários perfis; participantes valorizam aprovação de alterações. | Literatura de plataforma suporta acompanhamento/condições; necessidade específica é reforçada sobretudo pelo corpus de trabalho. | Forte no corpus; documentalmente compatível. | **Consolidar** |
| N07 | Participantes divergem quanto ao nível de formalidade: serviços pequenos pedem confirmação simples; serviços maiores podem exigir contrato. | Lei 3/2017 enquadra transacções electrónicas; assinatura avançada é mecanismo, não necessidade universal. | Formalização proporcional é melhor formulação que assinatura obrigatória. | **Consolidar** |
| N08 | WhatsApp/email já satisfazem comunicação básica; valor adicional está em preservar decisões, aprovações e evidências. | ILO documenta canais oficiais e comunicação, sem impor chat como única solução. | Necessidade é rastreabilidade, não chat. | **Consolidar** |
| N09 | M-Pesa, transferência bancária, dinheiro e pagamentos parciais aparecem; participantes discutem adiantamento, momento e condições. | ILO Kenya/BdM: múltiplos meios digitais; pagamentos são parte relevante do ecossistema. | Convergência forte sobre condições de pagamento. | **Consolidar** |
| N10 | Trabalhadores receiam não pagamento; clientes receiam pagar sem entrega; alguns consideram mecanismos de reserva/protecção. | ILO documenta não pagamento, rejeição e escrow como benchmark; BdM delimita actividade regulada. | Risco bilateral confirmado; escrow não é requisito derivado. | **Consolidar** |
| N11 | Ambos os lados valorizam histórico/reputação; vários participantes defendem reputação bilateral. | WESO: ratings/reviews são sinais comuns, com efeitos de governação. | Reputação suportada; bilateralidade tem suporte forte no corpus. | **Consolidar** |
| N12 | Participantes alertam para avaliações injustas e necessidade de contexto/contestação. | ILO mostra efeitos relevantes dos ratings sobre participação/acesso ao trabalho. | Convergência suficiente para exigir desenho contestável/contextual. | **Consolidar** |
| N13 | Participantes querem canal para reportar e acompanhar conflitos, sem consenso de que a plataforma deva arbitrar tecnicamente. | ILO: dispute resolution e governação são temas recorrentes. | Reporte/acompanhamento suportados; arbitragem não. | **Consolidar** |
| N14 | Evidências de escopo, alterações, comunicação, entrega e pagamento são consideradas úteis em conflitos. | ILO: rejeição/não pagamento/disputas reforçam necessidade de registos. | Necessidade transversal de preservação de evidência. | **Consolidar** |
| N15 | Web, UX, mobile, redes, hardware, dados/automação têm formas diferentes de demonstrar capacidade, executar e precificar. Especialista em Redes: ~3 anos de mercado. | WESO distingue diferentes modalidades e tipos de trabalho digital/location-based. | Modelo não deve impor fluxo rígido único. | **Consolidar** |
| N16 | Localização é importante sobretudo para hardware/redes/serviços presenciais e pouco relevante para trabalhos totalmente remotos. | Literatura distingue web-based e location-based work. | Necessidade condicional. | **Consolidar como regra contextual** |
| N17 | Participantes rejeitam burocracia desproporcional, especialmente em serviços pequenos; complexidade pode ser barreira. | Literatura de plataformas suporta preocupação com experiência/governação, mas evidência é principalmente do corpus. | Simplicidade é atributo de adopção/usabilidade, não RF isolado. | **Promover para RNF/critério UX** |
| N18 | Plataforma só cria valor se houver oportunidades e profissionais suficientes. | Efeitos de rede são compatíveis com plataformas multilaterais, mas o corpus documental actual não mede massa crítica local. | Condição de adopção/ecossistema, não requisito funcional. | **Manter como condição/limitação** |

## Divergências que devem permanecer visíveis

1. **Assessment:** alguns participantes admitem utilidade opcional; outros consideram inadequado por especialidade. Não consolidar como gate.
2. **Chat:** comunicação é necessária, mas chat interno não emerge como necessidade autónoma.
3. **Assinatura:** formalização é necessária; assinatura digital avançada não é universal.
4. **Pagamento integrado:** protecção é necessária; integração/custódia não é consequência automática.
5. **Preço:** alguns serviços permitem preço antecipado; diagnóstico/manutenção podem exigir avaliação prévia.
6. **Localização:** importante em serviços presenciais, irrelevante em parte dos serviços remotos.
7. **Disputas:** reporte/evidência são suportados; poder arbitral da plataforma não.
8. **Reputação:** útil, mas há cold-start e risco de avaliações injustas.

## Necessidades consolidadas para a engenharia

As necessidades N01–N16 ficam aceites como necessidades de domínio, com N16 condicional. N17 passa a atributo de qualidade/adopção. N18 permanece condição de ecossistema.

Isto **não significa** que existirão 16 requisitos funcionais. A etapa seguinte deve agrupar necessidades por capacidades do domínio e decidir o que é:
- regra de negócio;
- requisito funcional;
- requisito não funcional;
- condição/limitação;
- decisão de arquitectura;
- fora do âmbito.

## Gate de triangulação

**G-TRI: PASS para derivação de requisitos candidatos.**

A aprovação significa que há base suficiente para iniciar RN/RF/RNF candidatos. A proveniência deve continuar visível em cada requisito.
