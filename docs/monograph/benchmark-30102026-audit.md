# Auditoria comparativa — benchmark Blockchain de 30/10/2026

**Documento recebido:** `Monografia_Enoque_Macanda_30102026.docx`.
**Documento de trabalho da outra monografia:** D26 → D27.
**Precedência:** Manual USTM > benchmark editorial > preferências de apresentação.

## Comparação verificável

| Dimensão | Benchmark de 30/10 | Aplicação à monografia de contratação de TI |
|---|---|---|
| Formato | A4, 4 cm superior, 3,5 inferior e esquerda, 2 direita; TNR | Manter |
| Pré-textuais | Capa, folha de rosto, índice, listas, siglas, glossário, resumos | Só elementos fundamentados e exigidos pela USTM; não duplicar páginas vazias |
| Revisão da literatura | Expõe conceitos, características, alternativas e limitações, com figuras e quadros | Aprofundar conceitos específicos de plataformas/trabalho/contratação em vez de copiar secções Blockchain |
| Requisitos | Macro-requisitos e fichas com identificação, descrição, fonte, prioridade e observações | Manter 16 RN/28 RF/7 RNF auditáveis; exigir origem empírica/documental demonstrada |
| Casos de uso | Diagramas por processo e fichas com actores, condições, fluxo principal/alternativas | D27 acrescentou uma visualização focal e fichas UC13/UC14; catálogo UC01–UC27 permanece no repositório |
| UML | Casos de uso, classes, actividades, sequências, estados, arquitectura, com anexos complementares | Usar diagramas essenciais no corpo e deslocar apenas os complementares para apêndices |
| Resultados | Explicita testes técnicos e distingue resultados em ambiente controlado de impacto não testado | Manter separação rigorosa entre mock frontend, backend parcial, plano de testes e testes realmente executados |
| Figuras/quadros | Legendas e fontes de tamanho reduzido; explicação no texto | Uniformizar sem descrever códigos internos/processos de edição |

## Reservas — não copiar cegamente

1. A referência tem 157 páginas totais e muito mais de 60 páginas entre introdução e referências: não cumpre como modelo de extensão o limite FCTI de 60 páginas do corpo estabelecido no Manual USTM.
2. O resumo contém seis palavras-chave; a USTM requer três a cinco.
3. Um diagrama no documento de referência pode ilustrar uma ideia sem comprovar implementação; em todas as secções distinguir especificação, protótipo e teste.
4. A numeração profunda (2.3.3.1, etc.) é útil quando justificada; não criar subcapítulos só por simetria.
5. Os dados, actores, UML e bibliografia Blockchain **não** são fontes para esta investigação sobre contratação de TI.

## Orçamento de páginas

A D27 renderizada ocupa 62 páginas totais; o corpo inicia-se na página física 11 e referências surgem na página 62. Há **18 placeholders** restantes (11 diagramas/UML de 5.2 e 7 capturas do frontend). O comprimento do corpo pode ultrapassar 60 páginas se todas forem inseridas sem reorganização. Em cada nova figura calcular novamente a extensão do corpo e usar apêndices para complementos, conservando a discussão e os requisitos essenciais no corpo.

## Etapa executada

- **D27:** Figura 5.1 (visão de UC07, UC08, UC11, UC12, UC13, UC14, UC24, UC25), texto delimitando explicitamente a visão não exaustiva, e dois quadros de especificação detalhada (UC13 e UC14).
- **Fonte editável no GitHub:** [figura-5-1-casos-uso-centrais.puml](figures/figura-5-1-casos-uso-centrais.puml), correspondente semanticamente ao diagrama incorporado, que foi preparado em SVG.
- A figura ilustra **o modelo concebido**, não integração ou execução do frontend/backend.
- A D27 foi renderizada em 62 páginas e houve inspecção das páginas alteradas e limítrofes; o índice Word foi actualizado com transplante apenas de conteúdo de cache, preservando os 14 comentários originais.
