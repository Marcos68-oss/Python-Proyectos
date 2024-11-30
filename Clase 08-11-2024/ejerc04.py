"""Eejercicio 04
Escriba un programa que haga la tabla de multiplicar de cualquier numero entero dado por el usuario
la tabla debe ser del 0 al 12.
"""
x = int(input("Ingrese un nro: "))

for i in range(0,13):
    print(f"{x} x {i} = {x * i}")