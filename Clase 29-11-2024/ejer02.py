"""Ejercicio 02
"""

import math
# Funcion para calcular el perimetro de un cuadrado
def perimetro_cuadrado(lado):
    return lado * 4

# Funcion para calcular el area de un cuadrado
def area_cuadrado(lado):
    return lado ** 2

def main():
    lado = float(input("Ingrese el lado del cuadrado: "))
    print((f"El Perimetro del cuadrado es: {perimetro_cuadrado(lado):.2f}"))
    print((f"El Area del cuadrado es: {area_cuadrado(lado):.2f}"))
    
if __name__ == "__main__":
    main()