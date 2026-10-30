print("=== CAMBIOS ===")

inventario = {"101": "Playera", "102": "Gorra"}

id_producto = input("Ingresa el ID del producto: ")

if id_producto in inventario:
    print("Producto actual:", inventario[id_producto])
    nuevo = input("Ingresa el nuevo nombre: ")

    inventario[id_producto] = nuevo
    print("Producto actualizado")
    print(inventario)
else:
    print("Producto no encontrado")