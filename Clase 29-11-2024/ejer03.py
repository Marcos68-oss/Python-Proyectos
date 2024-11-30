"""Ejercicio 03
"""
import math
# Funcion para calcular el perimetro de un rectangulo
def perimetro_rectangulo(largo,ancho):
    return (largo + ancho) * 2

# Funcion para calcular el area de un rectangulo
def area_rectangulo(largo,ancho):
    return largo * ancho

def main():
    largo = float(input("Largo: "))
    ancho = float(input("Ancho: "))
    print((f"Perimetro del rectangulo es: {perimetro_rectangulo(largo,ancho):.2f}"))
    print((f"Area del rectangulo es: {area_rectangulo(largo,ancho):.2f}"))
    
if __name__ == "__main__":
    main()