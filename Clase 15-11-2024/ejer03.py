# Escritura en  un archivo
try:
    with open('ejemplo.txt', 'w') as archivo:
        archivo.write("Esta es una línea de texto. \n")
        archivo.write("Esta es la segunda linea de texto. \n")
    print("Se escribió correctamente en ele archivo.")
    
except Exception as e:
    print(f"Error al escribir en el archivo: {e}")
    
# Lectura de un archivo
try:
    with open('ejemplo.txt', 'r') as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)
        
except FileNotFoundError:
    print("Error: El archivo no fue encontrado.")
    
except Exception as e:
    print(f"Ocurrio un error al leer el archivo: {e}")