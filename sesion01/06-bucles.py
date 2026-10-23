print("-- FOR ---")
for numero in range(1, 21):
    if numero % 2 == 0:
        print("es par")
        continue
        print("No me voy a imprimir")
    if numero == 17:
        break
    print(numero)

print("estoy fuera de la iteracion")

print("-- WHILE ---")
contador = 1
while contador < 21:
    if contador % 2 == 0:
        print("es par")
        contador += 1
        continue
        print("No me voy a imprimir")
    if contador == 17:
        break
    print(contador)
    # contador = contador + 1
    contador += 1


print("estoy fuera de la iteracion")