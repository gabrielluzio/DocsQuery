# DocQuery API

**API REST para processamento e consulta inteligente de documentos PDF.**
O DocQuery é uma aplicação backend desenvolvida em **Python e FastAPI**, com o objetivo de permitir que usuários armazenem, processem e consultem informações de documentos PDF utilizando inteligência artificial.

O projeto está em desenvolvimento e tem como foco autenticação, persistência de dados, validação de arquivos, segurança e integração com modelos de linguagem.

## Tecnologias

| Tecnologia | Utilização |
|---|---|
| Python | Linguagem principal |
| FastAPI | Desenvolvimento da API REST |
| Pydantic | Validação de dados |
| SQLAlchemy | Mapeamento objeto-relacional (ORM) |
| MySQL | Persistência dos dados |
| Argon2 | Hash e verificação de senhas |
| Poetry | Gerenciamento de dependências |
| Git e GitHub | Versionamento do projeto |

## Funcionalidades

### Implementadas
- Cadastro de usuários.
- Autenticação por e-mail e senha.
- Armazenamento seguro de senhas utilizando Argon2.
- Validação de credenciais durante o login.
- Persistência dos usuários em banco de dados MySQL.
- Estrutura inicial de rotas para recebimento de documentos PDF.

### Em desenvolvimento
- Autenticação com JWT e expiração de tokens.
- Validação de arquivos PDF por tamanho, assinatura e conteúdo.
- Extração de texto por página.
- Identificação de documentos duplicados por hash.
- Armazenamento de trechos associados à página original.
- Controle de acesso aos documentos por usuário.
- Integração com IA para perguntas e respostas baseadas no conteúdo dos PDFs.
- Testes automatizados.

## Executando localmente

### Pré-requisitos
- Python compatível com a versão definida no `pyproject.toml`.
- MySQL.
- Poetry.

**1. Clone o repositório**
bash
git clone https://github.com/gabrielluzio/docquery-api.git
cd docquery-api

**2. Instale as dependências**
bash
poetry install

**3. Configure o ambiente**
Crie um arquivo `.env` na raiz do projeto e configure as variáveis exigidas pela aplicação, incluindo a conexão com o MySQL.
As credenciais devem permanecer fora do controle de versão.

**4. Inicialize a API**
bash
poetry run uvicorn main:app --reload


**5. Acesse a documentação interativa**
Após iniciar a aplicação, acesse a documentação Swagger que permite visualizar e testar os endpoints disponíveis.

