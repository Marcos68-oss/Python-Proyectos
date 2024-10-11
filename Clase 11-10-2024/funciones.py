"""
Calcular el area de un cuadrado con una funcion
"""
def area_cuadrado(l):
    p = l*4
    a=l**2
    print(f"El perimetro del cuadrado es : {p}")
    print(f"El area del cuadrado es: {a}")
# sale de la funcion
print(__name__)
if __name__ == '__main__':
    l = float(input("Ingrese el valor del lado del cuadrado: "))
    area_cuadrado(l)