"""El Operador es el * """


def Operador():
    lista1 = [1, 2, 3, 4, 5, 6]
    # print(lista)
    # print(1, 2, 3, 4, 5, 6)
    # print(*lista)
    lista2 = [56, 34, 89, 7, 8, 9]

    combinada = ["Hi", *lista1, "World", *lista2, "Mishin"]
    print("\n")
    print(combinada)
    print(*combinada)


Operador()

# este operador * tambien se puede usar con Diccionarios
# solo que con otra sintaxis en lugar de una seran dos **


def puntos():
    # Recuerda que las llaves {} son para definir un diccionario
    punto1 = {"x": 56}
    punto2 = {"y": 32}

    NuevoPunto = {**punto1, "Lolo": "Hi world", **punto2, "z": 25}
    print("\n")
    print(NuevoPunto)


puntos()
