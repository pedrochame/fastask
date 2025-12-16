# 📋 FasTask - Gerenciador de Tarefas (FastAPI + Pytest + Front-End)

## 🚀 Sobre o projeto
Este é um projeto de portfólio desenvolvido com **FastAPI** para gerenciar tarefas (CRUD completo).  
O objetivo é demonstrar conhecimentos em:
- Criação de APIs REST.
- Validação de dados com **Pydantic**.
- Escrita de **testes automatizados** com **Pytest** e `TestClient`.
- Desenvolvimento de **Front-End** com **HTML**, **CSS/Bootstrap** e **Javascript**. 

> ⚠️ As tarefas são armazenadas em **memória** (lista Python). Isso simplifica a persistência, já que o foco é demonstrar CRUD, validação e testes.

## 🛠️ Tecnologias utilizadas
- **Python 3.11+**
- **FastAPI**
- **Pydantic**
- **Pytest**
- **TestClient (FastAPI)**
- **HTML**
- **CSS**
- **Bootstrap**
- **Javascript**


## 📌 Funcionalidades
- **Listar todas as tarefas** (`GET /tasks`)
- **Buscar tarefa por ID** (`GET /tasks/{id}`)
- **Criar nova tarefa** (`POST /tasks`)
- **Editar tarefa existente** (`PATCH /tasks/{id}`)
- **Excluir tarefa** (`DELETE /tasks/{id}`)

## ✅ Testes automatizados
Os testes cobrem:
- Cenários de **sucesso** (CRUD completo).
- Cenários de **falha**:
  - Nome vazio (`400`)
  - Tarefa duplicada (`409`)
  - Tarefa não encontrada (`404`)
  - Erros de validação automática (`422`)

## ▶️ Como testar online
1. Acesse https://pedrochame.github.io/fastask/frontend/

## ▶️ Como executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/pedrochame/fastask.git
   cd fastask

2. Crie o ambiente virtual:
   ``` bash
    python -m venv .venv

3. Ative o ambiente virtual:
   ``` bash
   .venv/Scripts/activate

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt

5. Em frontend/config.js e app/config.py, comente a linha 2 e descomente a linha 3

6. Para rodar os testes:
   ````bash
   pytest

7. Para executar o Back-end:
   ```bash
   uvicorn app.main:app --reload

8. Acesse a documentação da API em http://localhost:8000/docs

9. Acesse o Front-End por meio de frontend/index.html