print("MENÚ DE BEBIDAS")
print("1 = Chico ($55)")
print("2 = Mediano ($70)")
print("3 = Grande ($85)")

opcion = int(input("Elige el tamaño de tu bebida: "))

if opcion == 1:
    print("Elegiste Chico. Precio: $55")
elif opcion == 2:
    print("Elegiste Mediano. Precio: $70")
elif opcion == 3:
    print("Elegiste Grande. Precio: $85")
else:
    print("Opción no válida")