tarea = input("¿Terminaste la tarea? (s/n): ")
casa = input("¿Ayudaste en la casa? (s/n): ")

if tarea == "s" and casa == "s":
    print("Tienes permiso para ir a la pijamada")
else:
    print("No tienes permiso para ir a la pijamada")

    if tarea == "n" and casa == "n":
        print("Te falta terminar la tarea y ayudar en casa")
    elif tarea == "n":
        print("Te falta terminar la tarea")
    elif casa == "n":
        print("Te falta ayudar en casa")