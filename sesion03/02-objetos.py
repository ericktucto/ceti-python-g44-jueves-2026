class Usuario:
    def __init__(self, nombre: str, email: str):
        self.nombre = nombre
        self.email = email

    def saludar(self) -> str:
        return f"Hola soy {self.nombre}"


u1 = Usuario("Ana", "ana@testing.com")
u2 = Usuario("Juan", "juan@testing.com")

print(u1.nombre)
print(u2.nombre)
print(u1.email)

print(
    u2.saludar()
)

class Notificar:
    def notificar(self):
        print("Notificando por correo")

class Cliente(Usuario, Notificar):
    def __init__(self, nombre: str, email: str, saldo: int):
        super().__init__(nombre, email)
        self.saldo = saldo

cliente1 = Cliente("Pedro", "pedro@testing.com", 300)

print(cliente1.saludar())
print(cliente1.saldo)
cliente1.notificar()

class Administrador(Usuario):
    def saludar(self):
        return f"Soy administrador, mi nombre es {self.nombre}"

class Vendedor(Usuario):
    def saludar(self):
        return f"Soy vendedor, mi nombre es {self.nombre}"


cliente2 = Cliente("Ana", "ana@testing.com", 500)
vendedor1 = Vendedor("Pedro", "pedro@testing.com")
admin = Administrador("Jorge", "jorge@testing.com")
usuario1 = Usuario("Juan", "juan@testing.com")

for u in [cliente2, vendedor1, admin, usuario1]:
    print(u.saludar())

