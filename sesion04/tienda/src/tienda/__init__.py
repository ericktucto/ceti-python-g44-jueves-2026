from tienda.exceptions import SaldoInsuficiente
from tienda.exceptions import IndexInvalido
from tienda.utils import listar_carrito
from tienda.exceptions import ProductoNoEncontrado
from tienda.utils import obtener_producto
from tienda.utils import listar_productos
from tienda.utils import cargar_productos
from tienda.entidades import Cliente
from tienda.utils import obtener_respuesta
from random import randint

MENU = """== TIENDA VIRTUAL ==
1. Ver productos
2. Agregar al carrito
3. Quitar del carrito
4. Ver carrito
5. Pagar
6. Salir
"""

VER_PRODUCTOS = 1
AGREGAR_CARRITO = 2
QUITAR_CARRITO = 3
VER_CARRITO = 4
PAGAR = 5
SALIR = 6

def get_opcion(mensaje: str) -> int:
    return int(obtener_respuesta(mensaje))


def main() -> None:
    nombre: str = obtener_respuesta('¿Cuál es tu nombre? ')
    saldo: int = randint(30, 60)

    cliente = Cliente(nombre, saldo)

    print(f"Bienvenido, {cliente.nombre}, tienes S/ {cliente.saldo}")

    lista_productos = cargar_productos()

    while True:
        print(MENU)

        try:
            opcion = get_opcion('Elige una opcion ')
        except ValueError:
            print("La opcion no es correcta")
            continue

        if opcion == VER_PRODUCTOS:
            listar_productos(lista_productos)
            continue
        elif opcion == AGREGAR_CARRITO:
            listar_productos(lista_productos)

            try:
                opcion = get_opcion('Elige un producto ')
                cliente.carrito.agregar(
                    obtener_producto(lista_productos, opcion),
                    get_opcion('¿Cuantos deseas? ')
                )
            except ValueError:
                print("La opcion no es correcta")
                continue
            except ProductoNoEncontrado:
                print("El producto que elegiste no existe")
                continue
            else:
                print("Producto agregado")
                continue

        elif opcion == QUITAR_CARRITO:
            listar_carrito(cliente.carrito)

            try:
                opcion = get_opcion('Elige un producto ')
                cliente.carrito.quitar(
                    opcion - 1
                )
            except ValueError:
                print("La opcion no es correcta")
                continue
            except IndexInvalido:
                print("El producto no esta en el carrito")
                continue
            else:
                print("Producto quitado")
                continue
        elif opcion == VER_CARRITO:
            listar_carrito(cliente.carrito)
            continue
        elif opcion == PAGAR:
            try:
                cliente.pagar()
                print(f"Compra exisitosa ahora tienes {cliente.saldo}")
                continue
            except SaldoInsuficiente:
                print('No tienes suficiente saldo, quita productos de tu carrito')
                continue
        elif opcion == SALIR:
            break
        else:
            print("La opcion no es correcta")
            continue

    print("Hasta luego, gracias por visitarnos")
