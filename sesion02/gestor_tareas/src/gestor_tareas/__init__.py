from gestor_tareas.tareas import guardar_tareas
from gestor_tareas.tareas import cargar_tareas

MENU = """=== GESTOR DE TAREAS ===
1. Agregar una tarea
2. Listar las tareas
3. Marcar una tarea como completada
4. Salir y guardar
"""

def mostrar_menu():
    print(MENU)

def main() -> None:
    lista_tareas = cargar_tareas()
    while True:
        mostrar_menu()
        print(lista_tareas)
        opcion = int(input("Elige una opcion: "))

        if opcion == 1:
            # agregar tarea
            continue
        elif opcion == 2:
            # listar las tareas
            continue
        elif opcion == 3:
            # marcas como completada
            continue
        elif opcion == 4:
            guardar_tareas(lista_tareas)
            break
        else:
            print("La opcion no es valida")
