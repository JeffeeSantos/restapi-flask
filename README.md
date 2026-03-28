# restapi-flask

🚀 REST API Flask - User Management

API REST desenvolvida em Flask para gerenciamento de usuários, com forte foco em práticas de CI/CD (Integração e Entrega Contínua), automação de deploy e padronização de ambiente.

🔗 Repositório: https://github.com/JeffeeSantos/restapi-flask.git

🎯 Objetivo do Projeto

Este projeto foi desenvolvido com o objetivo principal de aplicar conceitos reais de CI/CD, simulando um fluxo completo de desenvolvimento moderno:

🔁 Integração contínua com testes automatizados
🚀 Deploy automatizado
🐳 Padronização de ambiente com Docker
⚙️ Automação de tarefas com Makefile
📦 Estrutura pronta para pipelines (GitHub Actions, etc.)
📌 Funcionalidades
✅ Cadastro de usuários
✅ Listagem de usuários
✅ Validação de CPF
✅ API REST estruturada
✅ Testes automatizados
✅ Containerização com Docker
✅ Preparado para CI/CD

🛠️ Tecnologias Utilizadas
Python 3.x
Flask
Flask-RESTful
MongoEngine
MongoDB | MongoDB Atlas
Docker / Docker Compose
Pytest
GitHub Actions (CI/CD)
Heroku

🔄 Pipeline CI/CD

O projeto inclui configuração de pipeline utilizando GitHub Actions, permitindo:

✔️ Execução automática de testes a cada push
✔️ Validação de build
✔️ Preparação para deploy automatizado (ex: Heroku, containers, etc.)

Exemplo de fluxo:
Dev faz push → GitHub Actions dispara → roda testes → valida build → deploy

📂 Estrutura do Projeto
.
├── application/
├── tests/
├── .github/workflows/   # Pipeline CI/CD
├── Dockerfile
├── docker-compose.yaml
├── Makefile
├── requirements.txt
└── wsgi.py

⚙️ Como Executar o Projeto
🔹 Ambiente local
git clone https://github.com/JeffeeSantos/restapi-flask.git

cd restapi-flask
python3 -m venv .venv
source .venv/bin/activate  # Linux
# ou
.venv\Scripts\activate     # Windows

pip install -r requirements.txt
python3 wsgi.py

🐳 Executando com Docker
docker compose build
docker compose up

📡 Endpoints
🔹 GET /users
Lista todos os usuários

🔹 POST /user
Cria um novo usuário

🔹 GET /user/<cpf>
Obtem as informações do usuário com determinado cpf

🧪 Testes
pytest

📦 Automação com Makefile
make run
make test
make heroku

💡 Diferencial do Projeto

O grande diferencial deste projeto não é apenas a API em si, mas sim a aplicação prática de conceitos de:

DevOps
CI/CD
Automação de deploy
Infraestrutura como código (Docker)