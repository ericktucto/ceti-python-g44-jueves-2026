def saludar(nombre, saludo = 'Hola'):
    return f"{saludo}, {nombre}"

def mostrar(nombre, saludo = 'Hola'):
    print(f"{saludo}, {nombre}")

valor_de_mostrar = mostrar("Julio")

print(valor_de_mostrar)

mensaje = saludar("Erick")

print(mensaje)

mensaje2 = saludar("Pedro", "Buenas noches")

print(mensaje2)



def sumas(numero1, numero2):
    numero1 + numero2

sumas(20, 12)

variable = print("Hola")


print("-" * 30)

print(variable)



def area(base: int, altura: int) -> int:
    return base * altura

print(
    area("4", 5)
)

