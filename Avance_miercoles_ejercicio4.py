uv = int(input("¿Cuál es el índice UV del día (1 a 11)?: "))
bloqueador = input("¿Ya te pusiste bloqueador? (s/n): ")

if uv >= 6 and not (bloqueador == "s"):
    print("¡Ponte bloqueador, el sol está fuerte!")
else:
    print("Todo bien, disfruta tu día")