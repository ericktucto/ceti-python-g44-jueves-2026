from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def saludo():
    return {"mensaje": "Hola Erick"}






def main() -> None:
    print("Hello from catalogo-productos!")
