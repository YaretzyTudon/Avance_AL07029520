nombre = input("¿Cómo te llamas? ")
nacimiento = int(input("¿En qué año naciste? "))
red = input("¿Cuál es tu red social favorita? ")

edad = 2026 - nacimiento

print("Hola", nombre)
print("Tu red social favorita es", red)
print("Tienes", edad, "años")

if edad >= 13:
    print("Tu cuenta fue creada")
else:
    faltan = 13 - edad
    print("Te faltan", faltan, "años para crear tu cuenta")

if edad >= 18:
    print("Compras dentro de la app activadas")
else:
    print("Compras dentro de la app desactivadas")
