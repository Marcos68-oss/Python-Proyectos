"""Ejercicio 08
Calcular el factorial de un número dado
Ejemplo:
    5! = 1 * 2 * 3 * 4 * 5 = 120
"""
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

num = int(input("Ingrese un número: "))
print("El factorial de", num, "es:", factorial(num))
