"""Ejercicio 03
Calcular el nuevo salario del empleado por el incremento en x%
"""
def calcular_nuevo_salario(salario, incremento):
    """Calcular el nuevo salario del empleado por el incremento en x%
    """
    return salario + (salario * (incremento/100))

salario = int(input("Ingrese el salario: "))
incre = int(input("Ingrese el porcentaje de aumento: "))


print(f" El salario anterior es de {salario} ")
print(f" El aumento es de {incre}% ")
print(f" El salario nuevo es {calcular_nuevo_salario(salario,3.5):.2f} ")
