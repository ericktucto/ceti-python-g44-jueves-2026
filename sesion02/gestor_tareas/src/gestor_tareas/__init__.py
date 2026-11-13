from gestor_tareas.tareas import guardar_tareas, listar_tareas, cargar_tareas, agregar_tarea, normalizar_texto, marcar_tarea

MENU = """=== GESTOR DE TAREAS ===
1. Agregar una tarea
2. Listar las tareas
3. Marcar una tarea como completada
4. Salir y guardar
"""

AGREGAR_TAREA = 1
LISTAR_TAREAS = 2
MARCA_TAREA = 3
SALIR_GUARDANDO = 4

def mostrar_menu():
    print(MENU)

def inicio() -> None:
    texto = "   hola   mundo  , que tal todos ?  ?   "
    print(
        normalizar_texto(texto)
    )

def obtener_opcion(mensaje: str) -> int:
    while True:
        try:
            opcion = int(input(mensaje))
            return opcion
        except ValueError:
            print("La opcion no es valida")


def main() -> None:
    lista_tareas = cargar_tareas()
    while True:
        mostrar_menu()
        """
        try:
            opcion = int(input("Elige una opcion: "))
        except ValueError:
            print("La opcion no es valida")
            continue
        """
        opcion = obtener_opcion("Elige una opcion: ")

        if opcion == AGREGAR_TAREA:
            texto = input("Escribe la nueva tarea: ")
            texto = normalizar_texto(texto)

            if texto == "":
                print("No escribiste ninguna tarea")
                continue

            agregar_tarea(lista_tareas, texto)
            print("Tarea agrega exitosamente")
            continue
        elif opcion == LISTAR_TAREAS:
            listar_tareas(lista_tareas)
            continue
        elif opcion == MARCA_TAREA:
            listar_tareas(lista_tareas)

            tarea_opcion = obtener_opcion("Elegi la tarea que deseas marcar como completada: ")

            marcar_tarea(lista_tareas, tarea_opcion - 1)

            continue
        elif opcion == SALIR_GUARDANDO:
            guardar_tareas(lista_tareas)
            print("Guardado exitoso")
            break
        else:
            print("La opcion no es valida")
