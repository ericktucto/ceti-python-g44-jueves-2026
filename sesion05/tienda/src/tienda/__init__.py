from tienda.routers.productos import router as productoRouter
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def saludo():
    return {"mensaje": "Hola"}

# MODULO DE PRODUCTOS
app.include_router(productoRouter)


def main() -> None:
    print("Hello from tienda!")

