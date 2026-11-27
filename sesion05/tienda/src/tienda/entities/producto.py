from pydantic import BaseModel
import uuid


class Producto(BaseModel):
    id: uuid.UUID
    nombre: str
    precio: int