"""Ejercicio 4 
Escribir un priograma que pida datos por teclado y de su tipo de datos
"""

dat = input("Introduce un dato: ")
print("raw", type(dat), dat)
try:
    ent = int(dat)
    print("int", type(ent), ent)
except:
    print("Error! No es un dato entero")
try:
    flt = float(dat)
    print("float", type(flt), flt)
except:
    print("Error! No es un dato decimal")