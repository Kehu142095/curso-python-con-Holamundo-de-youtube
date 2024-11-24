edad = input("\npon tu edad: ")
edad = int(edad)

if edad > 65:
    print("\n puedes disfrutar una pelicula con un superdescuento")
elif edad > 55:
    print("\n puedes disfrutar una pelicula con descuento")
elif edad > 18:
    print("\n puedes disfrutar de la pelicula")

# IMPORTAANTE: El orden de if,elif,elif, etc...  hacia abajo,
# en caso de usar numeros debe ser de mayor a menor hacia abajo

# else:
#     print("\n no podras entrar al cine, eres menor de edad")
#     print("puedes volver acompañad@ con alguien mayor de edad")
print("\nListo")
