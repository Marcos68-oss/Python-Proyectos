def contar_caracteres(cadena):
    vocales = "aeiouáéíóú"
    consonantes = "bcdfghjklmnñpqrstvwxyz"
    
    cantidad_vocales = 0
    cantidad_consonantes = 0
    otros = 0
    
    for caracter in cadena:
        if caracter.lower() in vocales:
            cantidad_vocales += 1
        elif caracter.lower() in consonantes:
            cantidad_consonantes += 1
        else:
            otros += 1
    return cantidad_vocales, cantidad_consonantes, otros

cadena = input("Ingresa una cadena de texto: ")

vocales, consonantes, otros = contar_caracteres(cadena)

cantidad_palabras = len(cadena.split())

def contar_mayúsculas_minúsculas(cadena):
    
    cantidad_mayusculas = 0
    cantidad_minusculas = 0
    
    for caracter in cadena:
        if caracter.isalpha():
            if caracter.isupper():
                cantidad_mayusculas += 1
            else:
                cantidad_minusculas += 1
    return cantidad_mayusculas, cantidad_minusculas

mayusculas, minusculas = contar_mayúsculas_minúsculas(cadena)


print("")
print(f"La cantidad de vocales es: {vocales}")
print(f"La cantidad de consonanates: {consonantes}")
print(f"La cantidad de otros caracteres es: {otros}")
print(f"la cantidad de palabras es: {cantidad_palabras}")
if "que" in cadena.lower():
    print(f"La palabra 'que' está en la palabra '{cadena}'")
else:
    print(f"La palabra 'que' no está en la cadena '{cadena}'")
print(f"La cantidad de letras mayúsculas es: {mayusculas}")
print(f"La cantidad de letras minúsculas es: {minusculas}")

if "a" in cadena.lower():
    print(f"La letra 'a' está {cadena.lower().count("a")} veces en la cadena '{cadena}'")
else:
    print(f"La letra 'a' NO en la palabra {cadena}")

if "f" in cadena.lower():
    print(f"La letra 'f' está {cadena.lower().count("f")} veces en la cadena '{cadena}'")
else:
    print(f"La letra 'f' NO en la palabra '{cadena}'")