from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__, instance_relative_config=True)

db_path = os.path.join(app.instance_path, 'taskflow.db')
os.makedirs(app.instance_path, exist_ok=True)

def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT DEFAULT 'Pendente',
            priority TEXT DEFAULT 'Normal'  -- Nova coluna adicionada
        )
    ''')
    conn.commit()
    conn.close()

# ----------- ROTAS CRUD -----------

# Listar tarefas
@app.route('/')
def index():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

# Criar tarefa
@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    priority = request.form.get('priority', 'Normal')  # Novo campo
    if title:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, description, priority) VALUES (?, ?, ?)",
            (title, description, priority)
        )
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

# Atualizar tarefa (status e prioridade)
@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    status = request.form.get('status')
    priority = request.form.get('priority', 'Normal')  # Novo campo
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status=?, priority=? WHERE id=?", (status, priority, task_id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Excluir tarefa
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# -------------------- INÍCIO DO FLASK --------------------
if __name__ == '__main__':
    init_db()       # Cria tabela se não existir
    app.run(debug=True)

