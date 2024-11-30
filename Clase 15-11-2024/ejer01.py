try:
    # Intentamos realizar una operación que podría generara un error
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    resultado = num1 / num2
    print(f"El resultado de la división es : {resultado}")

except ZeroDivisionError:
    # Se ejecuta si hay un intento de dividir por cero
    print("Error : No se puede dividir por cero.")
    
except ValueError:
    # Se ejecuta si la entrada no es un número válido
    print("Error: por favor ingrese solo números.")

except Exception as e:
    #Se ejecuta para cualquier otro error
    print(f"Ocurió un error inesperado: {e}")

finally:
    # Este bloque se ejecuta siempre sin importar si hubo una excepción o no
    print("Fin del manejo de excepciones.")