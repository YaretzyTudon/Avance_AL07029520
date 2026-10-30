usuario = input("¿Cuál es tu nombre de usuario? ")
seguidores = int(input("¿Cuántos seguidores tienes? "))
likes = int(input("¿Cuántos likes tiene tu último video? "))

if seguidores >= 1000:
    print("Ya puedes hacer lives")
else:
    faltan = 1000 - seguidores
    print("Te faltan", faltan, "seguidores para hacer lives")

if likes > seguidores:
    print("¡Tu último video se hizo viral!")
else:
    print("Sigue publicando, vas bien")