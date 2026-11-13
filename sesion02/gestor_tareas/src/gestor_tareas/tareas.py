ARCHIVO = "tareas.txt"

def cargar_tareas():
    """Lee las tares dentro de un archivo. Devuelve una lista"""
    tareas = []
    try:
        with open(ARCHIVO, "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                estado, texto = linea.split("|", 1)
                tareas.append({
                    "texto": texto,
                    "hecha": estado == "1" # estado = 1 es por que esta completada, si es 0 es por que falta completar
                })
    except FileNotFoundError:
        print("No existe el archivo de tareas")
        return []
    return tareas
    
def guardar_tareas(tareas: list[dict]) -> None:
    try:
        with open(ARCHIVO, "w") as archivo:
            for tarea in tareas:
                hecha = "1" if tarea['hecha'] else "0"
                archivo.write(f"{hecha}|{tarea['texto']}\n")
    except FileNotFoundError:
        print("No existe el archivo de tareas")

def listar_tareas(tareas: list[dict]) -> None:
    """Mostra la lista de tareas
    1. [ ] Estudiar python
    2. [ ] Salir al mall
    3. [x] Terminar proyecto
    """
    for index, tarea in enumerate(tareas):
        brackets = "[x]" if tarea["hecha"] else "[ ]"
        print(f"{index + 1}. {brackets} {tarea['texto']}")

def agregar_tarea(tareas: list[dict], texto: str) -> None:
    tareas.append({
        "texto": texto,
        "hecha": False
    })


def normalizar_texto(texto: str) -> str:
    lista_palabras = texto.strip().split(" ")
    lista_limpia = [palabra for palabra in lista_palabras if palabra.strip() != ""]

    return " ".join(lista_limpia).strip()

def marcar_tarea(tareas: list[dict], index: int):
    if index < 0 or index >= len(tareas):
        print('No existe esa tarea')
        return None

    tareas[index]['hecha'] = True
