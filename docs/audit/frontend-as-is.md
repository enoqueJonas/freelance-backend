# Auditoria AS-IS — Frontend

## Escopo

Repositório: `enoqueJonas/freelance-frontend`.

## Stack observada

- React 19
- TypeScript
- Vite 6
- React Router 7
- Tailwind CSS 4
- Lucide React
- Motion

A aplicação apresenta-se como **ServiPlus Maputo**.

## Natureza do protótipo

O frontend é um protótipo interactivo de alta fidelidade que simula grande parte do ciclo de um marketplace. A camada de dados usa `mockApi` e `localStorage`, não uma integração efectiva com o backend Django.

Persistências simuladas incluem utilizadores, trabalhadores, empregadores, ofertas, propostas, contratos, pagamentos, mensagens, notificações e avaliações.

## Fluxo concebido

`Registo → Perfil → Verificação → Oferta → Proposta → Contrato → Assinatura → Pagamento → Avaliação`

Mensagens, notificações, administração e disputas aparecem como capacidades transversais ou previstas.

## Papéis

O frontend modela `employer`, `worker` e `admin` como roles explícitos. Esta é uma decisão de desenho a validar na investigação; não deve ser automaticamente promovida a regra de negócio.

## Capacidades

| Capacidade | Estado no protótipo |
|---|---|
| Registo | Simulado |
| Login | Simulado |
| Perfis | Simulados |
| Verificação documental | Simulada |
| Pesquisa de trabalhadores | Simulada |
| Ofertas | Simuladas |
| Propostas | Simuladas |
| Contratos | Simulados |
| Assinatura | Simulada |
| Pagamentos | Simulados |
| Avaliações | Simuladas |
| Mensagens | Simuladas |
| Notificações | Simuladas |
| Administração | Simulada/parcial |

## Autenticação

O login inclui acesso de demonstração e não representa autenticação de produção. A sessão é persistida localmente. Qualquer referência a JWT na interface é uma simulação do comportamento esperado e não prova integração com o backend.

## Perfis

O WorkerProfile concebido é mais rico do que o modelo backend e inclui elementos como título profissional, biografia, skills, GitHub, portfólio, experiência, trabalhos concluídos, rating, verificação e localização.

O EmployerProfile inclui empresa, contacto, descrição, localização, website, indústria e verificação.

## Pagamentos

O protótipo representa M-Pesa, e-Mola e transferência bancária. Estes métodos são simulados; não existem integrações reais demonstradas pelo frontend.

## Delimitação geográfica

O produto é apresentado como ServiPlus Maputo e a investigação está centrada na Cidade de Maputo, mas o formulário inclui Matola. A delimitação do produto deve ser reconciliada posteriormente com a delimitação científica.

## Conclusão da baseline

O frontend demonstra a visão do produto de forma muito mais completa do que o backend, mas não deve ser descrito como sistema integrado. É evidência da solução concebida/prototipada, não evidência da necessidade científica de cada funcionalidade.
