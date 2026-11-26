from dataclasses import dataclass

class Vendedor:
    def __init__(self, nombre: str, email: str):
        self.nombre = nombre
        self.email = email

@dataclass
class Cliente:
    nombre: str
    email: str

c1 = Cliente("Ana", "ana@testing.com")

print(c1.nombre)

print(c1)

v1 = Vendedor("Juan", "juan@testing.com")

print(v1)
