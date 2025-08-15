# TaskFlow System

## Descrição do Projeto
O **TaskFlow System** é um projeto acadêmico desenvolvido para gerenciar tarefas utilizando **Flask** e **SQLite**, aplicado em um contexto de metodologias ágeis.  
O sistema permite acompanhar o fluxo de trabalho em tempo real, priorizar tarefas críticas e monitorar o desempenho da equipe.

---

## Objetivo
Desenvolver um sistema de gerenciamento de tarefas para uma startup de logística, aplicando conceitos de Engenharia de Software e metodologias ágeis, simulando um ambiente real de desenvolvimento.

---

## Escopo do Projeto
- Cadastro de tarefas (CRUD: Create, Read, Update, Delete)  
- Acompanhamento do status das tarefas  
- Prioridade das tarefas para identificar atividades críticas  
- Fluxo de trabalho baseado em Kanban

---

## Metodologia
O projeto utiliza **Kanban** para gestão de tarefas e **GitHub Actions** para controle de qualidade, incluindo testes automatizados:

- **Kanban:** A Fazer → Em Progresso → Concluído  
- **Controle de qualidade:** Testes automatizados com `pytest` rodando em workflow GitHub Actions  

---

## Instalação e Execução

1. Clonar o repositório:
```bash
git clone https://github.com/Emylssa/TaskFlow-System.git
cd TaskFlow-System

## Criar e ativar ambiente virtual:

python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows


Instalar dependências:

pip install -r requirements.txt


Rodar o sistema:

python3 app.py


Acesse o sistema em http://127.0.0.1:5000.

Rodar testes automatizados:

pytest

Mudança de Escopo

Durante o desenvolvimento, foi necessário adicionar um campo de Prioridade no CRUD de tarefas.

Justificativa:
Permitir que o cliente identifique tarefas críticas rapidamente e melhore o acompanhamento do fluxo de trabalho.

Impacto no projeto:

Alteração do modelo de tarefas no banco de dados (SQLite).

Atualização do formulário de criação/edição de tarefas para incluir prioridade.

Atualização da listagem de tarefas para exibir a prioridade.

## Mudança de Escopo

Durante o desenvolvimento, foi adicionada a opção de status **"Bloqueada"** para as tarefas.  
Essa alteração permite que a equipe marque tarefas que estão temporariamente impossíveis de avançar, mantendo o controle do fluxo de trabalho.


Estrutura do Projeto
taskflow/
├── app.py               # Aplicação principal Flask
├── requirements.txt     # Dependências do projeto
├── README.md            # Documentação
├── .github/
│   └── workflows/
│       └── test.yml    # Workflow GitHub Actions
├── templates/           # Templates HTML
├── static/              # Arquivos estáticos (CSS, JS)
└── tests/
    └── test_app.py      # Testes automatizados