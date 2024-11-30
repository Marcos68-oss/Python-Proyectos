"""Ejercicio 02 
Escribir un programa que calcule el iva de un producto sobre el valor de la compra total, siendo el iva 10%
"""
n = float(input("Ingrese la cantidad de productos: "))
p = float(input("Ingrese el valor del producto: "))

compra_total = p * n
iva = compra_total * 0.10

print(f"El total es : {compra_total:.2f}")
print(f"El IVA es : {iva:.2f}")