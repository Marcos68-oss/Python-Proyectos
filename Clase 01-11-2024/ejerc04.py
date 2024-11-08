"""Funciones sobre cadenas"""

cad = input("Introduzca una cadena: ")
mayus = cad.upper()
minus = cad.lower()
cap = cad.capitalize()
print(mayus)
print(minus)
print(cap)

if cad.islower():
    print("Esta en minuscula")
elif cad.isupper():
    print("Esta en mayuscula")
elif cad.istitle():
    print("Es capital")
else:
    print("Es otro")