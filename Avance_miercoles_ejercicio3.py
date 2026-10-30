dia = input("¿Qué día es hoy? ").strip().lower()
if dia == "sábado" or dia == "sabado" or dia == "domingo":
    print("¡Es fin de semana, a descansar!")
else:
    print("Día de escuela.")