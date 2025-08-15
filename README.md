# TaskFlow System

Projeto acadêmico de gerenciamento de tarefas com Flask e SQLite.

## Descrição

O **TaskFlow System** é uma aplicação web para gerenciamento de tarefas com funcionalidades de CRUD (Criar, Ler, Atualizar, Excluir). Cada tarefa possui título, descrição, status e prioridade.

O projeto foi desenvolvido como parte de uma atividade acadêmica, incluindo integração com GitHub Actions para testes automáticos.

---

## Funcionalidades

- Criar tarefas com título, descrição e prioridade (Baixa, Normal, Alta)
- Listar todas as tarefas
- Atualizar status (Pendente, Em Progresso, Concluída, Bloqueada) e prioridade
- Excluir tarefas
- Testes automatizados com Pytest
- Integração contínua com GitHub Actions

---

## Tecnologias

- **Python 3.13**
- **Flask 2.3.3**
- **SQLite** para armazenamento local
- **HTML/Jinja2** para templates
- **Pytest** para testes automatizados
- **GitHub Actions** para CI/CD

---

## Estrutura do Projeto

taskflow/
├── app.py
├── requirements.txt
├── README.md
├── instance/
│ └── taskflow.db
├── templates/
│ └── index.html
├── tests/
│ └── test_app.py
└── .github/
└── workflows/
└── test.yml

yaml
Copiar
Editar

---

## Instalação e Execução

1. Clonar o repositório:

```bash
git clone https://github.com/Emylssa/TaskFlow-System.git
cd TaskFlow-System
Criar e ativar o ambiente virtual:

bash
Copiar
Editar
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
Instalar dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Rodar a aplicação:

bash
Copiar
Editar
python3 app.py
Abrir no navegador:

cpp
Copiar
Editar
http://127.0.0.1:5000
Testes Automatizados
Rode os testes locais com:

bash
Copiar
Editar
pytest
No GitHub, os testes são executados automaticamente via GitHub Actions a cada commit.

Mudança de Escopo
Durante o desenvolvimento, foi adicionada a prioridade das tarefas e o status "Bloqueada" como nova funcionalidade.