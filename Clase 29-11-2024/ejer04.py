"""Ejercicio 04
"""

import math

def perimetro_circulo(radio):
    return 2 * math.pi * radio

def area_circulo(radio):
    return math.pi * radio ** 2

def main():
    radio = float(input("Ingrese el radio del circulo: "))
    print(f"El perimetro del circulo es: {perimetro_circulo(radio):.2f}")
    print(f"El area del circulo es: {area_circulo(radio):.2f}")

if __name__ == "__main__":
    main() 
    