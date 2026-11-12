def saludar(nombre, saludo = 'Hola'):
    return f"{saludo} {nombre}"

texto = saludar("Erick", "Buenas noches")

print(texto)

x = 5
def fn():
    y = 10
    print(x)
    return x + y

fn()
# print("y ->", y)