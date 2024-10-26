""" Ejercicio 01
Escribir un programa que pida dos numeros y me de la suma, la rsta, la multiplicacion, la division y el modulo
"""
var1=float(input("Escriba un nro: "))
var2=float(input("Escriba un nro: "))

suma = var1 + var2
print(f"La suma es: {suma}")
r= var1 - var2
print(f"La resta es: {r}")
multip= var1 * var2
print(f"La multiplicacion es: {multip}")
d= var1 / var2 if var2 != 0 else 0
print(f"La division es: {d:.2f}")
modulo= var1 % var2 if var2 != 0 else 0 
print(f"El modulo es: {modulo}")