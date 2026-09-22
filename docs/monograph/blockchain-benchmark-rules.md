# Regras extraídas da monografia Blockchain/DID — benchmark editorial e técnico

> Documento analisado: `Monografia_Enoque_Macanda_070926.docx`.
> Este ficheiro regista práticas do benchmark que podem ser reutilizadas **somente quando compatíveis com o Manual USTM e com a investigação actual**.

## 1. Formatação física confirmada no DOCX

Todas as 6 secções do benchmark usam:
- A4: 21,0 × 29,7 cm;
- margem superior: 4,0 cm;
- inferior: 3,5 cm;
- esquerda: 3,5 cm;
- direita: 2,0 cm;
- header distance: 1,27 cm;
- footer distance: 1,27 cm.

O estilo Normal usa:
- Times New Roman;
- espaçamento 1,5;
- sem espaço adicional automático antes/depois.

O estilo Caption usa 9 pt, centrado, com espaço posterior de 10 pt.

Heading 2 e Heading 3 no benchmark possuem:
- negrito;
- 8 pt antes;
- 4 pt depois.

A apresentação visual final deve ser confirmada por renderização, pois propriedades directas de parágrafo podem sobrepor os estilos.

## 2. Moldura inicial

O DOCX possui `w:pgBorders` na secção inicial:
- top/bottom: linha simples, sz=4, space=1;
- left/right: linha simples, sz=4, space=4;
- cor automática.

Isto explica a moldura visível na capa/folha inicial. Durante alterações da monografia actual, não remover esta configuração inadvertidamente.

## 3. Capa/folha de rosto

O benchmark:
- centraliza instituição, faculdade, autor, título e data;
- mantém o título visualmente destacado sem alterar a família tipográfica;
- separa capa e folha de rosto;
- acrescenta supervisor e descrição académica na folha de rosto;
- preserva a moldura inicial.

## 4. Hierarquia de capítulos

O benchmark usa visualmente:
- `1 INTRODUÇÃO`;
- `1.1 ...`;
- `1.2 ...`;
- `1.2.1 ...`.

Não utiliza “CAPÍTULO I – INTRODUÇÃO” como título visível do capítulo na versão final.

Regra: manter numeração decimal simples e coerente em toda a monografia.

## 5. Objectivos e hipóteses

O benchmark apresenta explicitamente:
- secção Objectivos;
- subsecção Objectivo geral;
- subsecção Objectivos específicos;
- objectivos específicos em lista com marcadores;
- Hipóteses;
- Hipótese Geral;
- Hipóteses Específicas identificadas individualmente.

**Uso nesta monografia:** replicar a clareza estrutural, mas formular apenas hipóteses que possam ser confrontadas com a metodologia e evidência reais. Não copiar a quantidade ou o conteúdo das hipóteses Blockchain.

## 6. Revisão da literatura

O benchmark possui uma revisão extensa e progressiva, combinando:
- domínio/problema;
- conceitos fundamentais;
- tecnologias/conceitos técnicos;
- soluções existentes;
- engenharia de software;
- modelos/processos de desenvolvimento;
- prototipagem;
- UML/modelação.

Princípios a reutilizar:
- construir do geral para o específico;
- não saltar directamente do contexto para a solução;
- usar figuras e quadros quando esclarecem conceitos;
- relacionar literatura com o problema investigado;
- criar uma base suficiente para que decisões de engenharia posteriores não pareçam arbitrárias.

**Não reutilizar:** volume por volume. O Manual FCTI estabelece máximo de 60 páginas da Introdução às Referências.

## 7. Metodologia

O benchmark separa classificação da pesquisa, recolha/análise e desenvolvimento técnico, em vez de resumir tudo num parágrafo introdutório.

Princípio a reutilizar: a metodologia deve explicar o que foi realmente feito e permitir compreender como se passou da investigação para a solução.

## 8. Capítulo de engenharia/resultados

A principal força estrutural do benchmark é a sequência:
1. actores do sistema;
2. regras de negócio;
3. requisitos;
4. casos de uso;
5. diagrama de classes;
6. diagramas de actividades;
7. diagramas de sequência;
8. diagrama de estados;
9. arquitectura;
10. tecnologias/interfaces/validação conforme o trabalho.

Para a monografia actual, a análise empírica deve anteceder a engenharia o suficiente para demonstrar de onde vêm os requisitos, mas não deve substituir a apresentação formal da solução.

## 9. Casos de uso

O benchmark não se limita a um diagrama geral. Para operações principais, usa descrição estruturada com:
- caso de uso;
- requisito associado;
- actor;
- objectivo;
- pré-condições;
- fluxo principal;
- fluxos alternativos;
- pós-condições;
- regra de negócio associada.

Princípio: diagramas devem ser acompanhados por especificação textual apenas para casos de uso relevantes, evitando documentação redundante de operações triviais.

## 10. Diagramas

O benchmark usa múltiplos diagramas para representar perspectivas diferentes:
- casos de uso: interacções actor–sistema;
- classes: estrutura do domínio;
- actividades: fluxo de processos relevantes;
- sequência: interacções temporais nos cenários centrais;
- estados: ciclo de vida de entidade relevante;
- arquitectura: componentes/camadas da solução.

**Regra:** não criar diagramas apenas para igualar o benchmark. Cada diagrama deve responder a uma necessidade de modelação e manter consistência com RN/RF/modelo de domínio.

## 11. Quadros e figuras

O benchmark usa quadros para:
- regras de negócio;
- requisitos;
- descrições de casos de uso;
- comparações e sínteses.

Usar quadros quando a estrutura tabular melhora leitura/rastreabilidade. Evitar converter texto corrido em tabela sem ganho informacional.

## 12. Cabeçalhos, rodapés e paginação

O benchmark usa cabeçalho/rodapé e numeração consistentes no corpo. Na fase final:
- manter distância de cabeçalho/rodapé do benchmark (1,27 cm) se compatível com a versão institucional;
- garantir que elementos pré-textuais e corpo não herdem indevidamente cabeçalhos;
- verificar visualmente início de capítulos e quebras de secção.

## 13. Regra de comparação contínua

Para cada subcapítulo corrigido, comparar:
1. densidade e legibilidade visual;
2. hierarquia do título;
3. espaço antes/depois;
4. profundidade académica equivalente à função da secção;
5. uso de citações;
6. necessidade de quadro/figura;
7. ligação ao capítulo seguinte.

A pergunta não é “tem o mesmo número de páginas da Blockchain?”, mas “cumpre a mesma função académica com profundidade e clareza compatíveis?”.
