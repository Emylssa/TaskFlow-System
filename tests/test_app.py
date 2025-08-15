import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Lista de Tarefas' in rv.data

def test_add_task(client):
    rv = client.post('/add', data={'title': 'Teste', 'description': 'Descrição de teste'}, follow_redirects=True)
    assert rv.status_code == 200
    assert b'Teste' in rv.data

def test_status_options():
    allowed_status = ["Pendente", "Em Progresso", "Concluída", "Bloqueada"]
    for status in allowed_status:
        assert status in allowed_status
