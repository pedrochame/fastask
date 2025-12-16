# 📋 FasTask - Projeto de Tarefas (FastAPI + Pytest)

## 🚀 Sobre o projeto
Este é um projeto de portfólio desenvolvido com **FastAPI** para gerenciar tarefas (CRUD completo).  
O objetivo é demonstrar conhecimentos em:
- Criação de APIs REST.
- Validação de dados com **Pydantic**.
- Escrita de **testes automatizados** com **Pytest** e `TestClient`.

> ⚠️ As tarefas são armazenadas em **memória** (lista Python). Isso simplifica a persistência, já que o foco é demonstrar CRUD, validação e testes.

## 🛠️ Tecnologias utilizadas
- **Python 3.11+**
- **FastAPI**
- **Pydantic**
- **Pytest**
- **TestClient (FastAPI)**

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

## ▶️ Como executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/fastask.git
   cd fastask

2. Instale as dependências:
  ```bash
  pip install -r requirements.txt

3. Execute a aplicação:
  ```bash
  uvicorn app.main:app --reload

4. Acesse em: http://localhost:8000/docs

5. Rode os testes:
  ````bash
  pytest