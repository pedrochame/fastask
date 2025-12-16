from app.models import TaskResponse
from app.utils import getTaskById, getTaskByName, getNextTaskId, getNameCleaned

# Lista para utilizar nos testes
test_tasks = [
                TaskResponse(id=1, name="IR AO MERCADO"         , done=False),
                TaskResponse(id=2, name="LIMPAR COZINHA"        , done=False),
                TaskResponse(id=3, name="PEGAR CORRESPONDÊNCIA" , done=False),
            ]


### getTaskById() - Função que retorna uma tarefa pelo ID ### 

def test_getTaskById_success():
    # Buscar tarefa por um ID existente
    assert getTaskById(test_tasks, 2) == TaskResponse(id=2, name="LIMPAR COZINHA", done=False)

def test_getTaskById_fail():
    # Buscar tarefa por um ID inexistente
    assert getTaskById(test_tasks, 4) == None
    
def test_getTaskById_empty():    
    # Buscar tarefa sem nenhuma tarefa cadastrada
    assert getTaskById([], 1) == None


### getTaskByName() - Função que retorna uma tarefa pelo Nome ###

def test_getTaskByName_success():

    # Buscar tarefa por um nome existente
    assert getTaskByName(test_tasks, "Limpar cozinha") == TaskResponse(id=2, name="LIMPAR COZINHA", done=False)

    # Buscar tarefa por um nome existente porém maiúsculo/minúsculo
    assert getTaskByName(test_tasks, "LimPaR CoZiNhA") == TaskResponse(id=2, name="LIMPAR COZINHA", done=False)

    # Buscar tarefa por um nome existente porém com espaços extras
    assert getTaskByName(test_tasks, " LIMPAR  COZINHA ") == TaskResponse(id=2, name="LIMPAR COZINHA", done=False)

def test_getTaskByName_fail():

    # Buscar tarefa por um nome inexistente
    assert getTaskByName(test_tasks, "Arrumar quarto") == None
   
    # Buscar tarefa sem nenhuma tarefa cadastrada
    assert getTaskByName([], "Limpar cozinha") == None

    # Buscar tarefa por um nome vazio
    assert getTaskByName(test_tasks, None) == None

    # Buscar tarefa por um nome vazio sem conteúdo (vários espaços)
    assert getTaskByName(test_tasks, "      ") == None


### getNextTaskId() - Função que retorna o ID da próxima tarefa a ser cadastrada ###

def test_getNextTaskId():
    
    test_tasks_1 = [
                TaskResponse(id=1, name="Ir ao mercado"         , done=False),
                TaskResponse(id=5, name="Limpar cozinha"        , done=False)
                ]

    # Retornar próximo ID quando há "IDs faltantes" entre a primeira e última cadastradas
    assert getNextTaskId(test_tasks_1) == 6

    # Retornar próximo ID quando não há "IDs faltantes" entre a primeira e última cadastradas
    assert getNextTaskId(test_tasks) == 4

    # Retornar próximo ID quando não há tarefas cadastradas
    assert getNextTaskId([]) == 1


### getNameCleaned() - Função que recebe um nome de tarefa e o retorna sem espaços extras ###

def test_getNameCleaned():

    # Limpar nome vazio
    assert getNameCleaned(None) == ""

    # Limpar nome sem conteúdo
    assert getNameCleaned("   ") == ""

    # Limpar nome com espaços extras
    assert getNameCleaned(" Limpar                     Cozinha            ") == "LIMPAR COZINHA"