import uuid
from pydantic import BaseModel

class MensajeBasico(BaseModel):
    mensaje: str

class Producto(BaseModel):
    id: uuid.UUID
    nombre: str
    precio: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "nombre": "Te verde",
                    "precio": 6
                }
            ]
        }
    }