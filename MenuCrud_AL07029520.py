print("=== FUERZA REGIDA MERCH ===")
print("1. Altas")
print("2. Bajas")
print("3. Cambios")
print("4. Consultas")
print("5. Imprimir inventario")
print("6. Salir")

opcion = int(input("Elige una opción: "))

if opcion == 1:
    print("Entraste a Altas")
elif opcion == 2:
    print("Entraste a Bajas")
elif opcion == 3:
    print("Entraste a Cambios")
elif opcion == 4:
    print("Entraste a Consultas")
elif opcion == 5:
    print("Entraste a Imprimir inventario")
elif opcion == 6:
    print("Gracias por usar Fuerza Regida Merch")
else:
    print("Opción no válida")