temperatura = float(input("¿Cuál es la temperatura del día en grados? "))
if temperatura < 10:
    print("Te recomiendo usar chamarra, bufanda y botas.")
elif 10 <= temperatura <= 19:
    print("Te recomiendo usar sudadera y jeans.")
elif 20 <= temperatura <= 29:
    print("Te recomiendo usar playera y tenis.")
else:  # 30 o más
    print("Te recomiendo usar short, gorra y tomar mucha agua.")