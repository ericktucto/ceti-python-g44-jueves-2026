frutas = ["manzana", "pera", "uva", "kiwi", "mango"]

print(frutas[2])
print("Primer valor", frutas[0])
print("Ultimo valor", frutas[-1])
print(frutas[1:3])
print(frutas)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numeros[::3])

frutas.append("naranja")
print(frutas)
frutas.insert(0, "sandia")
print(frutas)

eliminado = frutas.pop(1)
print(frutas)
print(f"El valor eliminado es: {eliminado}")

print(frutas)
frutas[3] = "piña"
print(frutas)

print("--- ITERANDO LA LISTA DE FRUTAS ---")
for fruta in frutas:
    print(fruta)

print("--- TUPLAS ---")

mitupla = ("lima", "arequipa")

print(mitupla[1])

print("--- ITERANDO MI TUPLA ---")

for departamento in mitupla:
    print(departamento)