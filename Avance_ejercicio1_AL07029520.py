bateria = int(input("¿Qué porcentaje de batería tienes? "))
espacio = float(input("¿Cuántos GB tienes libres? "))
notificaciones = int(input("¿Cuántas notificaciones sin leer tienes? "))

if bateria <= 20:
    print("Batería baja, conecta tu cargador")

if espacio < 5:
    print("Poco espacio, borra fotos o apps que no uses")

if notificaciones > 0:
    print("Tienes", notificaciones, "notificaciones sin leer")
else:
    print("Estás al día, no tienes notificaciones")