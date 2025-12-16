from fastapi.testclient import TestClient # Simulação de requisições HTTP
from app.main import app   # Importação da aplicação FastAPI

# Objeto cliente para testes
client = TestClient(app)

# Através de uma fixture, antes de cada função de teste ser executada, a lista será recriada
import pytest
from app import routes
@pytest.fixture(autouse=True)
def reset_tasks():
    routes.tasks = routes.create_initial_tasks(test_mode=True)

# Buscar todas as tarefas
def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == [task.model_dump() for task in routes.tasks]

# Buscar tarefa específica: Sucesso
def test_get_task_success():
    response = client.get("/tasks/2")
    assert response.status_code == 200
    assert response.json() == {"id":2,"name":"LIMPAR COZINHA","done":False}

# Buscar tarefa específica: Falha
def test_get_task_fail():
    response = client.get("/tasks/200")
    assert response.status_code == 404
    assert response.json() == {"detail": routes.TAREFA_NAO_ENCONTRADA}

# Criar tarefa: Sucesso
def test_create_task_success():
    response = client.post("/tasks",json={"name":"  Consertar   chuveiro"})
    assert response.status_code == 201
    assert response.json() == {"id":4, "name":"CONSERTAR CHUVEIRO", "done": False}

# Criar tarefa: Falha (tarefa sem conteúdo)
def test_create_task_fail_noContent():
    response = client.post("/tasks",json={"name":"  "})
    assert response.status_code == 400
    assert response.json() == {"detail":routes.NOME_TAREFA_VAZIO}

# Criar tarefa: Falha (tarefa já registrada)
def test_create_task_fail_nameTaskExist():
    response = client.post("/tasks",json={"name":"   Ir   ao            MerCado  "})
    assert response.status_code == 409
    assert response.json() == {"detail":routes.TAREFA_EXISTENTE}

# Criar tarefa: Falha (erro de validação no JSON da requisição)
def test_create_task_fail_wrongJson():
    response = client.post("/tasks",json={"id":10,"name":"  Consertar   chuveiro"})
    assert response.status_code == 422

# Editar tarefa: Sucesso
def test_update_task_success():
    response = client.patch("/tasks/1",json={"name":"Ir de carro até o supermercado"})
    assert response.status_code == 200
    assert response.json() == {"id":1, "name":"IR DE CARRO ATÉ O SUPERMERCADO", "done": False}

# Editar tarefa: Falha (tarefa sem conteúdo)
def test_update_task_fail_noContent():
    response = client.patch("/tasks/1",json={"name":"  "})
    assert response.status_code == 400
    assert response.json() == {"detail":routes.NOME_TAREFA_VAZIO}

# Editar tarefa: Falha (tarefa já registrada)
def test_update_task_fail_nameTaskExist():
    response = client.patch("/tasks/1",json={"name":"   LimpaR CoZInha  "})
    assert response.status_code == 409
    assert response.json() == {"detail":routes.TAREFA_EXISTENTE}

# Edita tarefa: Falha (erro de validação no JSON da requisição)
def test_update_task_fail_wrongJson():
    response = client.patch("/tasks/1",json={"id":1,"name":"Consertar chuveiro"})
    assert response.status_code == 422

# Deletar tarefa: Sucesso
def test_delete_task_success():
    response = client.delete("/tasks/1")
    assert response.status_code == 204

# Deletar tarefa: Falha
def test_delete_task_fail():
    response = client.delete("/tasks/10")
    assert response.status_code == 404