from tienda.exceptions import SaldoInsuficiente
from tienda.exceptions import IndexInvalido
from dataclasses import dataclass

class Cliente:
    def __init__(self, nombre: str, saldo: int):
        self.nombre = nombre
        self.saldo = saldo
        self.carrito = Carrito()

    def pagar(self):
        if self.saldo < self.carrito.total:
            raise SaldoInsuficiente('No tiene suficiente saldo')
        self.saldo -= self.carrito.total
        # self.saldo = self.saldo ? self.carrito.total
        self.carrito.clear()

@dataclass
class Producto:
    codigo: str
    nombre: str
    precio: float

class Carrito:
    def __init__(self):
        self.__items: list[CarritoItem] = []

    @property
    def items(self) -> list[CarritoItem]:
        return self.__items

    @property
    def total(self):
        return sum([i.total for i in self.__items])

    def clear(self):
        self.__items = []

    def agregar(self, producto: Producto, cantidad: int):
        if cantidad <= 0:
            return None
        self.__items.append(CarritoItem(producto, cantidad))

    def quitar(self, index: int) -> CarritoItem:
        if index < 0 or index >= len(self.__items):
            raise IndexInvalido('Index invalido')

        return self.__items.pop(index)


@dataclass
class CarritoItem:
    producto: Producto
    cantidad: int

    @property
    def total(self):
        return self.producto.precio * self.cantidad

    def display(self):
        return f"{self.producto.nombre} - ({self.producto.codigo}) Unit P.: {self.producto.precio} | Cant.: {self.cantidad} | Total: {self.total}"
