from abc import ABC, abstractmethod

# clase abstracta
class MetodoPago(ABC):
    @abstractmethod
    def pagar(self):
        pass

class Yape(MetodoPago):
    def pagar(self):
        print("Pagando con yape")

class TarjetaDebito(MetodoPago):
    def pagar(self):
        print("Pagando con tarjeta de debito")

def checkout(metodo_pago: type[MetodoPago]):
    metodo_pago.pagar()


def main():
    mp = MetodoPago()
    checkout(mp)

main()

"""
# clase abstracta
class MetodoPago():
    def pagar(self):
        raise RuntimeError("No implementaste el metodo pagar")

class Yape(MetodoPago):
    def pagar(self):
        print("Pagando con yape")

class TarjetaDebito(MetodoPago):
    def pagar(self):
        print("Pagando con tarjeta de debito")

def checkout(metodo_pago: type[MetodoPago]):
    metodo_pago.pagar()


def main():
    mp = TarjetaDebito()
    checkout(mp)

main()
"""