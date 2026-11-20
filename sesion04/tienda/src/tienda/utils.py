from tienda.exceptions import ProductoNoEncontrado
from tienda.entidades import Producto
ARCHIVO = 'productos.txt'

def cargar_productos() -> list[Producto]:
    productos: list[Producto] = []
    with open(ARCHIVO, "r", encoding='utf-8') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea == '':
                continue

            # 0   , 1     , 2      = ['A01', 'Cafe', '15.90']
            codigo, nombre, precio = linea.split(',')
            """
            dividido = linea.split(',')
            codigo = dividido[0]
            nombre = dividido[1]
            precio = dividido[2]
            """
            productos.append(Producto(codigo, nombre, float(precio)))
    return productos


def obtener_respuesta(mensaje: str) -> str:
    while True:
        respuesta = input(mensaje).strip()
        if respuesta == '':
            print('No escribiste nada')
            continue
        return respuesta


def listar_productos(productos: list[Producto]):
    for index, producto in enumerate(productos):
        print(f"{index + 1}. {producto.nombre} - {producto.precio}")

def obtener_producto(productos: list[Producto], opcion: int) -> Producto:
    for index, producto in enumerate(productos):
        if index + 1 == opcion:
            return producto
    raise ProductoNoEncontrado('Producto no encontrado')

def listar_carrito(carrito):
    for index, item in enumerate(carrito.items):
        print(f"{index + 1}. {item.display()}")

