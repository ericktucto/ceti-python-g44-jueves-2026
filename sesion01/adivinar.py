import random

numero_aleatorio = random.randint(1, 100)

intento = 1

print("=== ADIVINA EL NUMERO ===")

while True:
    numero = int(
        input("Di un numero entre 1-100: ")
    )

    if numero_aleatorio == numero:
        break
    elif numero < numero_aleatorio:
        print("El que escogiste esta muy pequeño")
    elif numero > numero_aleatorio:
        print("El que escogiste esta muy grande")

    # intento = intento + 1
    intento += 1

print("Felicidades, adivinaste el número")
print(f"Lo hiciste en {intento} intento(s)")