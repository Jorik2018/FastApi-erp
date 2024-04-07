from typing import Optional, TypeVar
from pydantic import BaseModel

# creamos un tipo de variable "cualquiera"
T = TypeVar("T")

# Creamos el esquema del libro
class BookSchema(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    
    class Config:
        # le especificamos que será para uso de un ORM
        orm_mode = True
        # Colocamos un ejemplo que se mostrará en el SWAGGER
        schema_extra  = {
            "example":
                {
                    "id": 0,
                    "title": "titulo del libro",
                    "description": "decripción del libro"
                }
        }

# Creamos un schema de respuesta
class Response(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T]