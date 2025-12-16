from app.models import TaskResponse
from typing import List

# Função que busca uma tarefa pelo nome
def getTaskByName(tasks: List[TaskResponse],taskName: str):

    if taskName is None:
        return None

    for task in tasks:
        if getNameCleaned(task.name).lower() == getNameCleaned(taskName).lower():
            return task
    return None

# Função que busca uma tarefa pelo ID
def getTaskById(tasks: List[TaskResponse],taskId: int):
    for task in tasks:
        if task.id == taskId:
            return task
    return None

# Função que retorna o ID adequado para a próxima tarefa a ser cadastrada
def getNextTaskId(tasks: List[TaskResponse]):
    n = len(tasks)
    if n > 0:
        return tasks[n-1].id+1
    return 1

# Função que retorna o nome da tarefa somente com letras maiúsculas e espaços únicos, caso exista
def getNameCleaned(name: str):

    if name is None:
        return ""

    finalName = ""
    for i in name.strip().split(" "):
        if i != "":
            finalName += i + " "
    
    return finalName.strip().upper()