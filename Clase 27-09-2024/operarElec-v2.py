"""_summary_
Crear un algoritmo que pida dos números y me de la suma, la resta, la multiplicación y la división segun la opcion elegida
"""

a = int(input("Ingrese un número: "))
b = int(input("Ingrese un número: "))

print("Elija que operación desea hacer:")
print("1 Suma 2-Resta 3-Producto 4-Cociente")
op = int(input("Opción: "))

match op:
    case 1:
        print(f"La suma de {a} + {b} = {a+b}")
    case 2:
        print(f"La resta de {a} - {b} = {a-b}")
    case 3:
        print(f"El producto de {a} * {b} = {a*b}")
    case 4:
        if b== 0: print(f"No se puede dividir por Cero...")
        else:
            print(f"El cociente de {a} / {b} = {a/b}")
    case _:
        print("Operacion no valida")