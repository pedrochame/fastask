from fastapi import FastAPI # Importação do FastAPI
from app.routes import router   # Importação do objeto router (arquivo routes.py)
from fastapi.middleware.cors import CORSMiddleware


# Criação do objeto aplicativo
app = FastAPI(
    title="FasTask API",
    description="""
API para gerenciamento de tarefas 🚀

Com ela você pode:
- Criar tarefas
- Listar todas as tarefas
- Buscar uma tarefa específica
- Editar tarefas
- Deletar tarefas

Documentação automática disponível em /docs (Swagger UI) e /redoc (ReDoc).
""",
    version="1.0.0",
    contact={
        "name": "Pedro Chame",
        "url": "https://github.com/pedrochame",
        "email": "pedrohik@gmail.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

# Importando arquivo de configuração, onde é possível alterar a URL do Front-End
from app import config

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[config.urlFrontEnd],    # lista de origens permitidas
    allow_credentials=True,
    allow_methods=["*"],            # métodos HTTP permitidos
    allow_headers=["*"],            # cabeçalhos permitidos
)

app.include_router(router) # Incluindo objeto router no aplicativo