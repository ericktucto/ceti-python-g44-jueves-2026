def saludar(nombre: str, saludo: str = "Hola") -> str:
    return f"{saludo} {nombre}"

def area(base: float, altura: float) -> float:
    """Calcula el area de un cuadrado
    Ejm:
        area(5, 3) # esto retornará 15
    """
    return base * altura


print(area("5", 3))

