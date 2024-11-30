"""Ejercicio 09
Calcular el factorial de un número dado con recursividad
Ejemplo:
    5! = 1 * 2 * 3 * 4 * 5 = 120
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Ingrese un número: "))
print("El factorial de", num, "es:", factorial(num))