import math
# Funcion para verificar si los lados pertenecen a un triangulo
from ejer01 import es_triangulo
# Funcion para calcular el perimetro de un triangulo
from ejer01 import perimetro_triangulo
# Funcion para calcular el area de un triangulo
from ejer01 import area_triangulo
# Funcion para calcular el perimetro de un cuadrado
from ejer02 import perimetro_cuadrado
# Funcion para calcular el area de un cuadrado
from ejer02 import area_cuadrado
# Funcion para calcular el perimetro y area de un rectangulo
import ejer03
# Funcion para calcular el perimetro y area de un circulo
import ejer04

# Menu principal
def main():
    print("Calculo de perimetros y areas de poligonos")
    print("1. Triangulo")
    print("2. Cuadrado")
    print("3. Rectangulo")
    print("4. Circulo")
    print("5. Salir")

    while True:
        opcion = int(input("\nIngrese una opcion: "))
        if opcion == 1:
            lado1 = float(input("Lado 1: "))
            lado2 = float(input("Lado 2: "))
            lado3 = float(input("Lado 3: "))
            if es_triangulo(lado1,lado2,lado3):
                print((f"El Perimetro de un triangulo es: {perimetro_triangulo(lado1,lado2,lado3):.2f}"))
                print((f"El Area de un triangulo es: {area_triangulo(lado1,lado2,lado3):.2f}"))
            else:
                print("Los datos ingresados no corresponden a un triangulo")
        elif opcion == 2:
            lado = float(input("Ingrese el lado del cuadrado: "))
            print((f"El Perimetro del cuadrado es: {perimetro_cuadrado(lado):.2f}"))
            print((f"El Area del cuadrado es: {area_cuadrado(lado):.2f}"))
        elif opcion == 3:
            largo = float(input("Largo: "))
            ancho = float(input("Ancho: "))
            print((f"Perimetro del rectangulo es: {ejer03.perimetro_rectangulo(largo,ancho):.2f}"))
            print((f"Area del rectangulo es: {ejer03.area_rectangulo(largo,ancho):.2f}"))
        elif opcion == 4:
            ejer04.main()
        elif opcion == 5:
            print("Sliendo del programa...")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")
 
# Ejecutar el programa        
if __name__ == "__main__":
    main()