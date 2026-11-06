# Auditoria AS-IS — Backend

## Escopo

Repositório: `enoqueJonas/freelance-backend`  
Baseline: `master@6617ddf1d6dc29ccdebef6adb91602cecafe26ab`

O repositório é um fork de `ChirleyTecha/freelance-backend` e, no momento da auditoria, contém o mesmo baseline funcional.

## Stack observada

- Django
- Django REST Framework
- SimpleJWT
- SQLite para desenvolvimento

## Domínio implementado

### User
Utilizador customizado com dados de identificação/contacto e campos herdados de `AbstractUser`.

### Worker
Relação 1:1 com User. O modelo representa competências e experiência como texto.

### Employer
Relação 1:1 com User. O modelo representa nome da empresa e endereço.

### Verification
Existem modelos iniciais para documento de empregador e assessment de trabalhador. A implementação é incompleta e não deve ser tratada como fluxo de verificação funcional.

## Estrutura prevista mas não implementada

Existem apps/ficheiros para:
- marketplace (ofertas, propostas, categorias);
- contracts (contratos, assinaturas, disputas);
- messaging;
- notifications;
- payments;
- reviews;
- verification.

Grande parte destes módulos é placeholder ou contém modelos/ficheiros vazios. A presença da estrutura não constitui evidência de funcionalidade implementada.

## Fluxo funcional principal

O backend ainda não representa integralmente:

`Employer → Offer → Proposal → Contract → Payment → Review`.

O core do marketplace permanece por implementar.

## Achados técnicos

### Relações e perfis
- O reverse accessor de Worker é `user.worker`, mas há código que tenta aceder a `request.user.worker_profile`.
- O mesmo fluxo usa nomes diferentes para a relação do trabalhador.
- Worker e Employer são relações independentes com User; o modelo não impõe exclusividade entre os papéis.

### Validação de telefone
O serializer contém `validate_phone_number()`, enquanto o campo se chama `phone`. A validação específica do DRF não fica correctamente associada ao campo.

### EmployerSerializer
Existe divergência entre `employer_name` e os campos declarados no serializer, devendo ser corrigida/testada.

### Verification
- Document está modelado como OneToOne com Employer, limitando o empregador a um documento.
- Assessment está modelado como OneToOne com Worker.
- A regra `score >= 50` aprova automaticamente o assessment, mas a origem de negócio dessa regra não está documentada.
- Estas decisões não devem ser convertidas em requisitos apenas porque existem no código.

### Competências
`skills` e `experience` são strings. O modelo não representa competências estruturadas, nível, anos por competência ou categorias. A pesquisa actual por skills é demasiado básica para matching robusto.

### Configuração/segurança
- SECRET_KEY versionada;
- DEBUG activo;
- configuração local sem separação adequada por ambiente;
- SQLite versionado;
- ausência de evidência de hardening para produção.

### Higiene do repositório
Foram encontrados artefactos versionados como `.venv`, `__pycache__`, `.pyc`, `.DS_Store` e `db.sqlite3`.

### Testes
As apps inspeccionadas não apresentam uma suite automatizada significativa; vários `tests.py` são apenas stubs.

## Conclusão da baseline

O backend deve ser descrito como implementação parcial da fundação da solução, sobretudo contas/perfis, com esqueleto arquitectural para funcionalidades futuras. Não deve ser apresentado como marketplace completo.

O código será usado para medir o estado de implementação dos requisitos futuros, nunca como fonte científica desses requisitos.
