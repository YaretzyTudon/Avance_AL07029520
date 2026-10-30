print("¿Cómo te sientes hoy?")
print("1 = Feliz")
print("2 = Triste")
print("3 = Con energía")
print("4 = Estudiando")
mood = input("Escribe el número que corresponde a tu estado de ánimo: ")
if mood == "1":
    print("Te recomiendo escuchar pop.")
elif mood == "2":
    print("Te recomiendo escuchar baladas.")
elif mood == "3":
    print("Te recomiendo escuchar reggaetón o K-pop.")
elif mood == "4":
    print("Te recomiendo escuchar lo-fi.")
else:
    print("Ese mood no está en la lista.")