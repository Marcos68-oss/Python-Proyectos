import random 

lista_aleatoria = [random.randrange(1, 99) for _ in range(13)] 


elementos_pares = []
elementos_impares = []

for elemento in lista_aleatoria:
    if elemento % 2 == 0:
        elementos_pares.append(elemento)
    else:
        elementos_impares.append(elemento)

multiplos_3 = []

for elemento in lista_aleatoria:
    if elemento % 3 == 0:
        multiplos_3.append(elemento)

        

tamaño_lista1 = len(lista_aleatoria)
tamaño_lista2 = len(elementos_pares)
tamaño_lista3 = len(elementos_impares)
tamaño_lista4 = len(multiplos_3) 


lista_aleatoria_orden = sorted(lista_aleatoria)
elementos_pares_orden = sorted(elementos_pares)
elementos_impares_orden = sorted(elementos_impares)
multiplos_3_orden = sorted(multiplos_3)

suma1 = 0
suma2 = 0
suma3 = 0
suma4 = 0
for i in range(len(lista_aleatoria)):
    suma1 += lista_aleatoria[i]

for i in range(len(elementos_pares)):
    suma2 += elementos_pares[i]

for i in range(len(elementos_impares)):
    suma3 += elementos_impares[i]

for i in range(len(multiplos_3)):
    suma4 += multiplos_3[i]
    
promedio1 = suma1 / len(lista_aleatoria)
promedio2 = suma2 / len(elementos_pares)
promedio3 = suma3 / len(elementos_impares)
promedio4 = suma4 / len(multiplos_3)

    
print("___Tamaño de las listas___")
print("")
print(f"El tamaño de la lista aleatoria es: {tamaño_lista1}")
print(f"El tamaño de la lista de números pares es: {tamaño_lista2}")
print(f"El tamaño de la lista de números impares es: {tamaño_lista3}")
print(f"El tamaño de la lista de números múltiplos de 3 es: {tamaño_lista4}")
print("")
print("___Contenido de las listas___")
print("")
print(f"Lista aleatoria: {lista_aleatoria}")
print(f"Lista de Números pares: {elementos_pares}")
print(f"Lista de Números impares: {elementos_impares}")
print(f"Lista de Números múltiplos de 3: {multiplos_3}")
print("")
print("___Contenido de las listas Ordenadas___")
print("")
print(f"Lista aleatoria: {lista_aleatoria_orden}")
print(f"Lista de Números pares: {elementos_pares_orden}")
print(f"Lista de Números impares: {elementos_impares_orden}")
print(f"Lista de Números múltiplos de 3: {multiplos_3_orden}")
print("")
print("___Promedio de las listas___")
print("")
print(f"Promedio de la Lista aleatoria: {promedio1:.2f}")
print(f"Promedio de la Lista de Números pares: {promedio2:.2f}")
print(f"Promedio de la Lista de Números impares: {promedio3:.2f}")
print(f"Promedio de la Lista de Números múltiplos de 3: {promedio4:.2f}")
