"""Tarea 01
Escribir un programa que haga una factura de venta varios productos, calcule los ivas de 5% y 10% dependiendo del producto.
Debe dar cuanto va a pagar el cliente y el iva total de la compra
Los productos son:
nro producto    precio  iva
1   teclado      50$     10%
2   raton        20$     5%
3   monitor 15"  80$     10% 
4   monitor 17" 110$     10%
5   monitor 19" 135$     10%
6   raton rgb    40$     5%
7   teclado rgb  70$     10%
8   monitor 21" 160$     10%
9   monitor 27" 200$     10%
"""

productos = {
    1:{"precio": 50, "iva": 10, "nombre": "Teclado"},
    2:{"precio": 20, "iva": 5, "nombre": "Raton"},
    3:{"precio": 80, "iva": 10, "nombre": "Monitor 15'"},
    4:{"precio": 110, "iva": 10, "nombre": "Monitor 17'"},
    5:{"precio": 135, "iva": 10, "nombre": "Monitor 19'"},
    6:{"precio": 40, "iva": 5, "nombre": "Raton rgb"},
    7:{"precio": 70, "iva": 10, "nombre": "Teclado rgb"},
    8:{"precio": 160, "iva": 10, "nombre": "Monitor 21'"},
    9:{"precio": 200, "iva": 10, "nombre": "Monitor 27'"},
    10:{"precio": 350, "iva": 10, "nombre": "AMD Ryzen 9"}
}

print("__PRODUCTOS__")

for i in range(1,11):
    print("{:<3} {:<15} $ {:<9.2f}".format(i, productos.get(i).get("nombre"), productos.get(i).get("precio")))
    

print("")

productos_factura = {}


total_subtotal = 0
total_iva = 0
total_general = 0


while True:
    print("\n1. Agregar producto")
    print("2. Finalizar carga de productos")
    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        # Carga de datos del producto
        x = int(input("Ingrese el numero del producto: "))
        nombre = productos.get(x).get("nombre")
        cantidad = int(input(f"Ingrese la cantidad del producto '{nombre}': "))
        precio = productos.get(x).get("precio")
        iva = productos.get(x).get("iva")

        
        subtotal = cantidad * precio
        iva_producto = subtotal * (iva / 100)

       
        productos_factura[nombre] = {
            "cantidad": cantidad,
            "precio": precio,
            "iva": iva,
            "subtotal": subtotal,
            "iva_producto": iva_producto
        }

        
        total_subtotal += subtotal
        total_iva += iva_producto
        total_general += subtotal + iva_producto

    elif opcion == "2":
        
        break

    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")


print("\nResumen de productos:")
print("---------------------------------------------------------------")
for producto, datos in productos_factura.items():
    print(f"Producto: {producto}")
    print(f"Cantidad: {datos['cantidad']}")
    print(f"Precio: ${datos['precio']:.2f}")
    print(f"IVA: {datos['iva']}%")
    print(f"Subtotal: ${datos['subtotal']:.2f}")
    print(f"IVA: ${datos['iva_producto']:.2f}")
    print(f"Total: ${datos['subtotal'] + datos['iva_producto']:.2f}")
    print()
    print("-------------------------------------")

print(f"Total subtotal: ${total_subtotal:.2f}")
print(f"Total IVA: ${total_iva:.2f}")
print(f"Total general: ${total_general:.2f}")