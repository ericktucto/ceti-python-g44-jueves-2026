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
    
def guardar_tareas(tareas):
    pass

def listar_tareas(tareas):
    """Mostra la lista de tareas
    1. [ ] Estudiar python
    2. [ ] Salir al mall
    3. [x] Terminar proyecto
    """
    # codigo
    pass