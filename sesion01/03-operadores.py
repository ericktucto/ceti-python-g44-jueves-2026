print("--- OPERADORES ARITMETICOS ---")

# + - / * 
print(5 + 7)
print(5 + 3.3)
print("Erick" + " Tucto")
# print("5" + 7)
# print(5 + "7")
print(30 - 21)
print(30 / 10)
print(3 * 30)
print("-" * 30)
# // %
print(20 / 7)
print(20 // 7)
print(20 % 7)
print(2 ** 5)

print("--- OPERADORES COMPARACION ---")

# > >= < <= == !=
print(5 > 7)

edad = 18

print(edad >= 18)
print(5 == 5)
print("5" == 5)
print("erick" == "erick")
print("r" in "erick")

print("--- OPERADORES LOGICOS ---")

print("True  and True  ->",   True  and True)
print("True  and False ->",  True  and False)
print("False and True  ->",   False and True)
print("False and False ->",  False and False)
print("-" * 5)
print("True  or True ->",   True  or True)
print("True  or False ->",  True  or False)
print("False or True ->",   False or True)
print("False or False ->",  False or False)
print("-" * 5)
print("not False ->", not False)
print("not True ->", not True)

correo_verificado = True
edad = 15
es_adulto = edad >= 18
# Pueden comprar si es adulto y tiene correo verificado
print("Pueden comprar si es adulto y tiene correo verificado", es_adulto and correo_verificado)
