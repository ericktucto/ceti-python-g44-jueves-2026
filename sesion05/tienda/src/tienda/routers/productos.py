import uuid
from tienda.schema.output.productos import Producto as ProductoResponse, MensajeBasico
from tienda.schema.input.productos import NuevoProducto, ActualizarProducto
from tienda.entities.producto import Producto

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/v1", tags=["Productos"])

productos: list[Producto] = []

@router.get("/productos")
def obtener_todos_los_productos():
    return productos

@router.post("/productos")
def crear_un_producto(datos: NuevoProducto) -> MensajeBasico:
    nuevo_producto = Producto(
        id=uuid.uuid4(),
        nombre=datos.nombre,
        precio=datos.precio
    )

    productos.append(nuevo_producto)

    return MensajeBasico(mensaje="Producto creado")


@router.get("/productos/buscar")
def buscar_productos_por_el_nombre(nombre: str):
    print("buscar")
    return [
        p
        for p in productos
        if nombre.lower() in p.nombre.lower()
    ]


# /api/v1/productos/1
# /api/v1/productos/2
# /api/v1/productos/3
# ...
@router.get("/productos/{id}")
def informacion_del_producto(id: str) -> ProductoResponse:
    print("informacion")
    for producto in productos:
        if str(producto.id) == id:
            return ProductoResponse(id=producto.id, nombre=producto.nombre, precio=producto.precio)

    raise HTTPException(status_code=404)



@router.put("/productos/{id}")
def actualizar_producto(id: str, datos: ActualizarProducto) -> MensajeBasico:
    for producto in productos:
        if str(producto.id) == id:
            producto.nombre = datos.nombre
            producto.precio = datos.precio
            return MensajeBasico(mensaje="Producto actualizado")

    raise HTTPException(status_code=404)

@router.delete("/productos/{id}")
def eliminar_producto(id: str) -> MensajeBasico:
    index = None
    for i, p in enumerate(productos):
        if str(p.id) == id:
            index = i
            break
    if index is None:
        raise HTTPException(status_code=404)

    productos.pop(index)

    return MensajeBasico(mensaje="Producto eliminado")

