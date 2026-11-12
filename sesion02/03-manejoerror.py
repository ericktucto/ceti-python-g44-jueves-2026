def obtener_numero() -> int:
    while True:
        try:
            numero = int(
                input("Di un numero entre 1-100: ")
            )
            return numero
        except ValueError:
            print("El numero es incorrecto")

# print(obtener_numero())

mostrar_spinner = False

def dividir(dividendo, divisor):
    try:
        mostrar_spinner = True
        resultado = dividendo / divisor
    except ZeroDivisionError:
        print("No puedes dividir en 0")
        return None
    except TypeError:
        print("El dividendo y el divisor deben ser numeros, no texto")
        return None
    else:
        mostrar_spinner = False
        return resultado
    finally:
        print("Siempre me ejecuto")

print(dividir(10, 0))