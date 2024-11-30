"""
Ejercicio 07
Utilizando rangos, suma el valor de todos los números pares desde el 2 (inclusive) hasta el 100 (inclusive).
"""
suma = 0

for i in range(2,101,2): # El tercer nro indica que recorra de 2 en 2
    suma += i
print (f"La suma es : {suma} ")