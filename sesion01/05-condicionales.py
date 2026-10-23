nota = int(input("Ingresa tu nota: "))

# Mensajes y notas (1-20) si tienes 11 - 20 aprobastes
# 20 -> Aprobaste con nota sobresaliente
# mayor a 10 -> Aprobaste
# 6 a 10 -> Necesitas un examen para subir tu nota
# 0 a 5 -> No aprobastes

if nota == 20:
    print("Aprobaste con nota sobresaliente")
elif nota > 10:
    print("Aprobaste")
elif nota > 5:
    print("Necesitas un examen para subir tu nota")
elif nota >= 0:
    print("No aprobaste")
else:
    print("No es una nota valida")