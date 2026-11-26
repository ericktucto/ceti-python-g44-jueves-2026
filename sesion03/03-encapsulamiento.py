class Cliente:
    def __init__(self, nombre, saldo, email):
        self.nombre = nombre
        self._saldo = saldo
        self.__email = email
        # puedes usar el setter para reutilizar la validacion
        # self.saldo = saldo

    # GETTER
    @property
    def saldo(self):
        return self._saldo

    @property
    def email(self):
        return self.__email

    # SETTER
    @saldo.setter
    def saldo(self, nuevo_valor):
        if nuevo_valor < 0:
            nuevo_valor = 0
        self._saldo = nuevo_valor


c1 = Cliente("Ana", 3000, "ana@testing.com")


print("Antes", c1.saldo)


nuevo_saldo = 1000

c1.saldo = nuevo_saldo

print("Despues", c1.saldo)

c1._saldo = -1000
print(c1.saldo)

print(c1._saldo)

c1.__email = "erick@testing.com"
c1.no_existo = 1234

print(c1.no_existo)
print(c1.__email)
print(c1.email)

# c2 = Cliente("Juan", -3000)

# print(c2.saldo)