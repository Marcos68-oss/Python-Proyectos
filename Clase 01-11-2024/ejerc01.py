"""
Ejercicio 01
Escribir un programa que pida al ususario adivinar un número entre 1 y 100
"""
import random

numero_secreto = random.randint(1,100)
intentos = 0

print("Bienvenido al juego de adivinanzas!")
print("Estoy pensando en un numero entre 1 y 100")

while True:
    suposicion = int(input("Adivina el número: "))
    intentos +=1
    
    if suposicion < numero_secreto:
        print("Demasiado bajo")
    elif suposicion > numero_secreto:
        print("Demasiado alto")
    else:
        print(f"Correcto! lo adivinaste en {intentos} intentos.")
        break