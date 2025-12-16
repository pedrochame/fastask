from pydantic import BaseModel, ConfigDict
from typing import Optional

class TaskBase(BaseModel):
    name : str
    model_config = ConfigDict(
                    extra = "forbid", # Gerar erro caso não haja somente a(s) chave(s) definida(s)
                    json_schema_extra = {"example":{
                                            "name" : "Fazer Compras"
                                            }
                                        }
                    )

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    name : Optional[str] = None
    done : Optional[bool] = None

    model_config = ConfigDict(
        extra = "forbid",# Gerar erro caso não haja somente a(s) chave(s) definida(s)
        json_schema_extra = {"example":{
                                            "name" : "Ir ao treino",
                                            "done" : False
                                       }
                        }
    )


class TaskResponse(TaskBase):
    id : int
    done : bool

    model_config = ConfigDict(
        extra = "forbid",# Gerar erro caso não haja somente a(s) chave(s) definida(s)
        json_schema_extra = {"example":{
                                            "id"   : 1,
                                            "name" : "Fazer Compras",
                                            "done" : True
                                       },
                            
                            }
    )