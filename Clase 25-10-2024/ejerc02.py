"""Ejercicio 02
Escribir un programa que pida una cadena de caracteres e imprima la longitud de la cadena
"""
cad = input('Introduce una cadena:')
longitud= len(cad)
print(f"Tiene {longitud} caracteres")
print(cad[::-1])