"""
try:
    nota = int(input("Coloca tu nota: "))
except ValueError:
    print("Nota invalida")
"""


try:
    resultado = 10 / int(input("Coloca divisor: "))
except ValueError:
    print("No es un numero")
except ZeroDivisionError:
    print("No puedes dividir en cero")
else:
    print(f"Tu resultado es {resultado}")
finally:
    print("Yo siempre me ejecuto")