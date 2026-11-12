frutas = ["manzana", "pera", "uva", "kiwi", "mango"]

print(frutas)

for fruta in frutas:
    print(f"Mi fruta es {fruta}")

print(frutas[0])

frutas[0] = "naranja"
print(frutas)

print(frutas[-1])

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    print(f"Mi numero es {numero}")

print(numeros)
print(numeros[::3])

frutas.append("sandia")

print(frutas)

frutas.insert(0, "platano")

print(frutas)

eliminado = frutas.pop()

print(frutas)
print("fruta eliminada", eliminado)

ciudades = ("lima", "quito", "los cabos", "madrid")

print(ciudades[0])
# ciudades[0] = "new york"
# ciudades.pop()
# ciudades.insert()

print(ciudades[1:3])

ciudades = ("lima", "madrid")
print(ciudades)

ciudades = 34
print(ciudades)
