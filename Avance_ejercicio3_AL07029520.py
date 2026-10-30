contrasena_correcta = "Latte2026"

nombre = input("¿Cómo te llamas? ")
contrasena = input("Escribe la contraseña del Wi-Fi: ")
gasto = float(input("¿Cuánto gastaste en el café? "))

if contrasena == contrasena_correcta:
    print("Conectado al Wi-Fi, bienvenida", nombre)
else:
    print("Contraseña incorrecta")

if gasto >= 100:
    print("Tienes 1 hora de Wi-Fi")
else:
    print("Tienes 30 minutos de Wi-Fi")
