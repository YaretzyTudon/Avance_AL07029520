print("=== CONSULTAS ===")

inventario = {
    "101": "Playera",
    "102": "Gorra",
    "103": "Sudadera"
}

buscar = input("Nombre del producto: ").lower()
encontrado = False

for id_producto, producto in inventario.items():
    if producto.lower() == buscar:
        print("ID:", id_producto)
        print("Producto:", producto)
        encontrado = True

if encontrado == False:
    print("No hay resultados")