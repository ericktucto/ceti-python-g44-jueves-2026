from pydantic import BaseModel, Field


class NuevoProducto(BaseModel):
    nombre: str = Field(description="Nombre de tu nuevo producto", min_length=5, max_length=255)
    precio: int = Field(description="Precio de tu nuevo producto", gt=0)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "nombre": "Te verde",
                    "precio": 6
                },
                {
                    "nombre": "7 semillas",
                    "precio": 12
                }
            ]
        }
    }

class ActualizarProducto(BaseModel):
    nombre: str = Field(description="Nombre de tu producto", min_length=5, max_length=255)
    precio: int = Field(description="Precio de tu producto", gt=0)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "nombre": "Te verde",
                    "precio": 6
                },
                {
                    "nombre": "7 semillas",
                    "precio": 12
                }
            ]
        }
    }