"""Ejercicio 01
Escribir un programa que tome tres notas de un alumno y de la nota final y su calificación.
Tenga en cuenta que la primera y segunda nota tiene un peso de 30% y la tercera de 40%
"""

nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))

nota_final = (nota1 * (30/100)) + (nota2 * (30/100)) + (nota3 * (40/100))

print(f"La nota final es {nota_final}")

if nota_final >= 6:
    print("Aprobado! ")
else:
    print("Rebrobado ")