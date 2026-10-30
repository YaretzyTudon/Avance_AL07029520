print("=== BAJAS ===")

inventario = {"101": "Playera", "102": "Gorra"}

id_producto = input("Ingresa el ID del producto: ")

if id_producto in inventario:
    print("Producto:", inventario[id_producto])
    confirmar = input("¿Eliminar producto? (S/N): ").upper()

    if confirmar == "S":
        del inventario[id_producto]
        print("Producto eliminado")
    elif confirmar == "N":
        print("Baja cancelada")
    else:
        print("Opción no válida")
else:
    print("Producto no encontrado")