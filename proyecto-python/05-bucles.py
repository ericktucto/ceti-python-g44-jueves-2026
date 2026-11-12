
contador = 1

while contador <= 30:
    # print("--- inicio ---")

    if contador % 2 == 0:
        print("es par")
        contador += 1
        continue
    
    if contador == 17:
        break

    print(contador)
    
    # contador = contador + 1
    contador += 1
    # print("--- final ---")

print("final del bucle")

print("---BUCLE FOR ---")


for letra in "hola mundo":
    print(letra)

for numero in range(1, 31):
    # print("--- inicio ---")

    if numero % 2 == 0:
        print("es par")
        continue
    
    if numero == 17:
        break

    print(numero)

    # print("--- final ---")
