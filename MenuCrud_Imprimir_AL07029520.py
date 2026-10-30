print("=== INVENTARIO ===")

inventario = {
    "101": "Playera",
    "102": "Gorra",
    "103": "Sudadera"
}

if len(inventario) > 0:
    print("ID | PRODUCTO")
    print("-------------")

    for id_producto, producto in inventario.items():
        print(id_producto, "|", producto)
else:
    print("No hay registros")