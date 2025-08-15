# TaskFlow System

Projeto acadêmico de gerenciamento de tarefas com **Flask** e **SQLite**, desenvolvido como atividade da disciplina de Engenharia de Software.

---

## Objetivo

O TaskFlow System tem como objetivo permitir que equipes gerenciem tarefas de forma ágil, acompanhando o fluxo de trabalho em tempo real, priorizando tarefas críticas e monitorando o desempenho da equipe.

---

## Escopo

O sistema implementa:

- CRUD completo de tarefas (Criar, Listar, Atualizar, Excluir);
- Campos adicionais:
  - **Status**: Pendente, Em Progresso, Concluída e Bloqueada;
  - **Prioridade**: Baixa, Normal, Alta;
- Banco de dados SQLite;
- Testes automatizados com **PyTest**;
- Integração contínua com **GitHub Actions**.

---

## Metodologia

- **Kanban**: organizado nas colunas **A Fazer**, **Em Progresso** e **Concluído** no GitHub Projects;
- **Fluxo Ágil**: commits estruturados, mudanças de escopo documentadas e controle de qualidade automatizado.

---

## Instalação e Execução

1. Criar ambiente virtual e ativar:

```bash
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
Mudança de Escopo
Durante o desenvolvimento, adicionamos o status "Bloqueada" para as tarefas, permitindo marcar atividades que não podem ser iniciadas até que dependências sejam resolvidas. Esta alteração está documentada no Kanban e no histórico de commits.

Estrutura de Pastas
bash
Copiar
Editar
taskflow/
├── app.py
├── requirements.txt
├── instance/
│   └── taskflow.db
├── templates/
│   └── index.html
├── tests/
│   └── test_app.py
└── .github/
    └── workflows/test.yml
Controle de Qualidade
GitHub Actions configurado para rodar testes automatizados via PyTest a cada commit;

Logs disponíveis na aba Actions do GitHub.

Histórico de Commits
Exemplos de mensagens utilizadas:

feat: adiciona campo prioridade e atualiza index.html para CRUD completo

fix: corrige workflow do GitHub Actions

docs: atualização README com descrição completa e mudança de escopo

Beneficiados
Equipe de Desenvolvimento: acompanhamento fácil do fluxo de tarefas;

Gestores: monitoramento em tempo real de prioridades e status;

Cliente/Usuário Final: visibilidade das entregas e progresso do projeto.

Observações Finais
O projeto é funcional, com todas as funcionalidades implementadas.