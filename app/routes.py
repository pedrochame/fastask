from fastapi import APIRouter, HTTPException # Importação da classe APIRouter
from app.models import TaskCreate, TaskUpdate, TaskResponse # Importação da classe Task (arquivo models.py)
from typing import List
from app.utils import getTaskById, getTaskByName, getNextTaskId, getNameCleaned

# Criação do objeto Router
router = APIRouter()

# Lista para armazenar as tarefas, quando em modo teste, utilizar lista com algumas tarefas
def create_initial_tasks(test_mode=False):
    if test_mode == False:
        return []
    else:
        return [TaskResponse(id=1, name="IR AO MERCADO"         , done=False),
                TaskResponse(id=2, name="LIMPAR COZINHA"        , done=False),
                TaskResponse(id=3, name="PEGAR CORRESPONDÊNCIA" , done=False)]
    
tasks = create_initial_tasks()


# Constante que armazena a mensagem a ser retornada caso uma tarefa não seja encontrada
TAREFA_NAO_ENCONTRADA = "Tarefa não encontrada."

# Constante que armazena a mensagem a ser retornada caso uma tarefa não seja encontrada
TAREFA_EXISTENTE = "Já existe uma tarefa cadastrada com esse nome."

# Constante que armazena a mensagem a ser retornada caso o nome de uma tarefa esteja vazio
NOME_TAREFA_VAZIO = "O nome da tarefa não deve estar vazio."


# Rota para criar tarefa
@router.post("/tasks",
             response_model=TaskResponse,
             status_code=201, 
             name="Cadastrar Tarefa", 
             tags=["Tarefa"],
             summary="Cria uma nova tarefa",
             description="Recebe o nome da tarefa e retorna o objeto criado com ID e estado inicial")
def create_task(task: TaskCreate):

    # Limpando nome
    task.name = getNameCleaned(task.name)

    # Somente avança caso o nome tenha conteúdo
    if len(task.name) == 0:
        raise HTTPException(status_code=400, detail=NOME_TAREFA_VAZIO)

    # Somente avança caso não exista uma tarefa com o nome fornecido
    if getTaskByName(tasks,task.name) is not None:
        raise HTTPException(status_code=409, detail=TAREFA_EXISTENTE)

    # Crição do objeto newTask (nova tarefa)
    newTask = TaskResponse  (
                                #id = len(tasks) + 1,      # ID único 
                                id = getNextTaskId(tasks), # ID único
                                name = task.name,          # Nome recebido na requisição
                                done = False,              # Novas tarefas sempre iniciam não finalizadas
                            )
    
    tasks.append(newTask)

    return newTask

# Rota para editar tarefa
@router.patch("/tasks/{id}", 
              response_model=TaskResponse, 
              status_code=200, 
              name="Editar Tarefa", 
              tags=["Tarefa"],
              summary="Edita uma tarefa existente",
              description="Recebe o ID como parâmetro e um JSON no corpo incluindo nome e/ou estado, e retorna o objeto atualizado")
def update_task(id: int, taskUpdated: TaskUpdate):

    task_to_update = getTaskById(tasks,id)
    if task_to_update == None:
        raise HTTPException(status_code=404,detail=TAREFA_NAO_ENCONTRADA)
    else:

        if taskUpdated.name is not None:
            # Limpando nome
            taskUpdated.name = getNameCleaned(taskUpdated.name)

            # Somente avança caso o nome tenha conteúdo
            if len(taskUpdated.name) == 0:
                raise HTTPException(status_code=400, detail=NOME_TAREFA_VAZIO)

            # Somente avança caso não haja outra tarefa com o mesmo nome
            task_searched = getTaskByName(tasks,taskUpdated.name)
            if task_searched is not None and task_searched != task_to_update:
                raise HTTPException(status_code=409, detail=TAREFA_EXISTENTE)
            
            task_to_update.name = taskUpdated.name
        
        if taskUpdated.done is not None:
            task_to_update.done = taskUpdated.done
    
    return task_to_update

# Rota para deletar tarefa
@router.delete("/tasks/{id}", 
               status_code=204, 
               name="Deletar Tarefa", 
               tags=["Tarefa"],
               summary="Deleta uma tarefa já existente",
               description="Recebe o ID como parâmetro e retorna uma exceção caso não seja possível deletar")
def delete_task(id: int):

    task_to_delete = getTaskById(tasks,id)
    if task_to_delete == None:
        raise HTTPException(status_code=404,detail=TAREFA_NAO_ENCONTRADA)
    else:
        tasks.remove(task_to_delete)
        return

# Rota para listar tarefas
@router.get("/tasks", 
            response_model=List[TaskResponse], 
            status_code=200, 
            name="Visualizar Tarefas", 
            tags=["Tarefa"],
            summary="Lista as tarefas cadastradas",
            description="Retorna os objetos das tarefas cadastradas até o momento")
def get_tasks():
    return tasks # Retornamos a lista que armazena as tarefas

# Rota para listar uma tarefa específica
@router.get("/tasks/{id}", 
            response_model=TaskResponse, 
            status_code=200, 
            name="Buscar Tarefa", 
            tags=["Tarefa"],
            summary="Lista informações de uma determinada tarefa cadastrada",
            description="Recebe o ID como parâmetro e retorna o objeto da respectiva tarefa")
def get_task(id: int):
    
    task_to_return = getTaskById(tasks,id)
    if task_to_return == None:
        raise HTTPException(status_code=404, detail=TAREFA_NAO_ENCONTRADA)
    else:
        return task_to_return