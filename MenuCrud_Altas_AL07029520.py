id_producto = input("ID del producto: ")
producto = input("Nombre del producto: ")
talla = input("Talla: ")
precio = float(input("Precio: "))
stock = int(input("Cantidad disponible: "))

guardar = input("¿Deseas guardar? (S/N): ").upper()

if guardar == "S":
    print("Producto guardado correctamente")
    print("ID:", id_producto)
    print("Producto:", producto)
    print("Talla:", talla)
    print("Precio:", precio)
    print("Stock:", stock)
elif guardar == "N":
    print("Alta cancelada")
else:
    print("Opción no válida")