import requests

def inicio() -> None:
    print("Hola a todos desde aplicacion")

    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    print(response.json())
