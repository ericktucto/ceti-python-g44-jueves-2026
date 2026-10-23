edad = input("Dame tu edad: ")

try:
    edad = int(edad)
except ValueError:
    print("El numero ingresado no es valido")
else:
    print(f"Tu en 10 años tendras, {edad + 10}")