boleto = input("¿Tienes boleto? (s/n): ")
edad = int(input("¿Cuántos años tienes?: "))

if boleto == "s" and edad >= 15:
    print("Puedes entrar al concierto")
else:
    print("No puedes entrar al concierto")