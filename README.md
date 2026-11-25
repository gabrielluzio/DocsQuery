# DocQuery

**API REST para processamento de documentos PDF e consultas inteligentes utilizando Inteligência Artificial.**

O DocQuery é uma aplicação backend desenvolvida com Python e FastAPI que permite a autenticação de usuários, o recebimento e processamento de documentos PDF e a realização de perguntas sobre o conteúdo desses documentos utilizando o Google Gemini.

O projeto foi desenvolvido com foco em organização, separação de responsabilidades, validação de dados, segurança e integração com serviços externos de inteligência artificial.

## Funcionalidades

- **Cadastro de usuários:** criação de contas com persistência em banco de dados MySQL.
- **Autenticação JWT:** geração e validação de tokens para autenticação de requisições.
- **Segurança de senhas:** utilização de Argon2 para geração e verificação de hashes.
- **Upload de documentos PDF:** recebimento e processamento de arquivos enviados pelos usuários.
- **Validação de arquivos:** verificação de tamanho, conteúdo, formato e integridade dos documentos.
- **Extração de texto:** leitura e extração do conteúdo de documentos PDF, página por página.
- **Consultas com IA:** integração com Google Gemini para responder perguntas com base no conteúdo extraído dos documentos.
- **Validação de dados:** utilização de Pydantic para validar os dados recebidos pela API.
- **Documentação interativa:** disponibilização dos endpoints através do Swagger UI.

## Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| Python 3.13 | Linguagem principal |
| FastAPI | Desenvolvimento da API REST |
| Pydantic | Validação e estruturação de dados |
| SQLAlchemy | Mapeamento objeto-relacional (ORM) |
| MySQL | Banco de dados relacional |
| Argon2 | Hash e verificação de senhas |
| JWT | Autenticação e autorização |
| Google Gemini | Processamento de linguagem natural e geração de respostas |
| Google Gen AI SDK | Comunicação com a API do Gemini |
| PyMuPDF | Leitura e extração de conteúdo de PDFs |
| Poetry | Gerenciamento de dependências |
| Git e GitHub | Versionamento de código |

## Arquitetura do projeto

O projeto possui uma organização modular, separando as responsabilidades de autenticação, processamento de documentos, validação de dados, acesso ao banco de dados e integração com inteligência artificial.

### Estrutura de pastas

```text
DocQuery/
│
├── main.py
├── config.py
├── database.py
├── models.py
├── schemas.py
├── routes.py
├── routes_documentos.py
├── security.py
├── jwt_handler.py
├── dependencies.py
├── service_ia.py
│
├── .env
├── .gitignore
├── pyproject.toml
└── poetry.lock
```

### Responsabilidade dos módulos

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Inicialização da aplicação FastAPI e registro das rotas. |
| `config.py` | Configurações da aplicação e variáveis de ambiente. |
| `database.py` | Configuração da conexão com MySQL e sessões do banco. |
| `models.py` | Definição dos modelos e tabelas do banco de dados. |
| `schemas.py` | Definição dos schemas e validações com Pydantic. |
| `routes.py` | Endpoints de cadastro, login e consultas. |
| `routes_documentos.py` | Recebimento, validação e extração de conteúdo dos PDFs. |
| `security.py` | Geração e verificação de hashes de senhas. |
| `jwt_handler.py` | Geração e validação de tokens JWT. |
| `dependencies.py` | Dependências utilizadas para autenticação das requisições. |
| `service_ia.py` | Integração com Google Gemini e processamento das perguntas. |

## Como funciona

### 1. Autenticação

O usuário realiza seu cadastro informando os dados necessários.

A senha é processada utilizando Argon2 antes de ser armazenada no banco de dados.

Durante o login, as credenciais são verificadas e, caso sejam válidas, a aplicação gera um token JWT.

Esse token é utilizado na autenticação das requisições protegidas.

### 2. Upload e processamento de documentos

O usuário autenticado envia um documento PDF através da API.

Antes da extração, o sistema realiza validações:

- Verificação do tamanho máximo permitido de 10 MB.
- Verificação de arquivos vazios.
- Verificação da assinatura do arquivo PDF.
- Verificação da integridade do documento.
- Verificação da existência de texto extraível.

Após as validações, o PyMuPDF realiza a extração do conteúdo, organizando o texto por página.

### 3. Integração com inteligência artificial

Após a extração do conteúdo do documento, o usuário pode enviar uma pergunta sobre as informações presentes no PDF.

A aplicação encaminha o conteúdo extraído e a pergunta para a camada responsável pela integração com o Google Gemini.

O serviço constrói a solicitação para o modelo de linguagem e retorna a resposta gerada pela inteligência artificial.

## Endpoints da API

A aplicação disponibiliza os seguintes endpoints:

| Método | Endpoint | Descrição |
|---|---|---|
| POST | `/auth/cadastrar` | Cadastro de usuários. |
| POST | `/auth/login` | Autenticação e geração de JWT. |
| POST | `/documentos/criar_documentos` | Upload e processamento de documentos PDF. |
| POST | `/auth/pergunta` | Envio de perguntas sobre o documento. |

**Autenticação:** os endpoints protegidos exigem um token JWT no cabeçalho da requisição, utilizando o esquema Bearer.

Exemplo:

```http
Authorization: Bearer SEU_TOKEN_JWT
```

## Instalação e execução

### Pré-requisitos

- Python 3.13 ou compatível com o projeto.
- MySQL.
- Poetry.
- Chave de API do Google Gemini.

### 1. Clone o repositório

```bash
git clone https://github.com/gabrielluzio/DocsQuery.git

cd DocsQuery
```

### 2. Instale as dependências

```bash
poetry install
```

### 3. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto.

Adicione as credenciais necessárias para a conexão com o MySQL e a chave de API do Google Gemini.

Exemplo da variável de IA:

```env
API_GEMINI=sua_chave_de_api
```

Configure também as variáveis de conexão com o banco conforme os nomes definidos em `config.py`.

**Importante:** nunca compartilhe ou envie seu arquivo `.env` para o GitHub.

### 4. Execute a aplicação

```bash
poetry run uvicorn main:app --reload
```

A API estará disponível em:

```text
http://127.0.0.1:8000
```

### 5. Acesse a documentação

O FastAPI disponibiliza uma documentação interativa através do Swagger UI.

```text
http://127.0.0.1:8000/docs
```

Por meio dela, é possível visualizar os endpoints, consultar os schemas e realizar requisições diretamente à API.

## Segurança

O DocQuery utiliza mecanismos de segurança para proteger o acesso à aplicação e os dados dos usuários:

- Armazenamento de senhas utilizando hashes Argon2.
- Autenticação baseada em tokens JWT.
- Validação de tokens nas dependências de autenticação.
- Validação dos dados recebidos com Pydantic.
- Validação de arquivos enviados à API.
- Armazenamento de credenciais em variáveis de ambiente.

## Objetivos de desenvolvimento

O DocQuery foi desenvolvido para consolidar conhecimentos em desenvolvimento backend com Python, incluindo:

- Desenvolvimento de APIs REST com FastAPI.
- Organização de aplicações em módulos e camadas.
- Modelagem e persistência de dados relacionais.
- Utilização de SQLAlchemy como ORM.
- Autenticação e segurança com JWT e Argon2.
- Validação e tratamento de erros.
- Processamento de arquivos PDF.
- Integração com APIs externas de inteligência artificial.
- Utilização de SDKs para comunicação com modelos de linguagem.
- Gerenciamento de dependências com Poetry.
- Versionamento de código com Git e GitHub.
---

Desenvolvido como projeto de portfólio para aplicação prática de conceitos de desenvolvimento backend e integração com inteligência artificial.
