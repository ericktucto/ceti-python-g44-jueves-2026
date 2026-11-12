nota = int(input("Coloca tu nota: "))

print(type(nota))

if nota == 20:
    print("Aprobaste con nota sobresaliente")
elif 11 <= nota <= 19:
    print("Aprobaste")
    print("Felicidades")
elif 5 <= nota <= 10:
    print("Necesitas tomar examen de recuperacion")
elif 0 <= nota <= 4:
    print("Reprobaste")
else:
    print("No ingresaste una nota valida")

print("Final del programa")

