"""Ejercicio 07
simular el telebingo y que se genere 8 números aleatorio de 1 a 20 y que el usuario tenga 5 números para acertar y que imprima el nro de aciertos
"""
from random import randint
bingo = set()

while len(bingo) < 5:
    bingo.add(randint(1, 20))
    
usuario = set()
aciertos = 0

while len(usuario) < 5:
    usuario.add(int(input("Introduzca un número: ")))
print("Numeros del bingo: ")
print(bingo)
for i in bingo:
    if i in usuario:
        aciertos += 1
print(f"Tienes {aciertos} aciertos")
if aciertos == 5:
    print("HAS GANADO!")
else:
    print("Mejor suerte para la próxima")
