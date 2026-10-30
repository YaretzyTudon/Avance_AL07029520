seguidores = int(input("¿Cuántos seguidores tienes? "))

if seguidores < 0:
    print("Número de seguidores no válido")
elif seguidores < 1000:
    print("Nivel: Principiante")
elif seguidores < 10000:
    print("Nivel: Microinfluencer")
elif seguidores < 100000:
    print("Nivel: Influencer")
else:
    print("Nivel: Celebridad digital")