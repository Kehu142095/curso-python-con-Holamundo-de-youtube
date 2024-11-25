# los diccionarios son una coleccion de datos que se encuentran agrupoados por una llave y un valor
def diccionarios():
    # lo de la izquierda es un string y lo de la derecha cualquier cosa
    punto = {"x": 25, "y": 50}
    print(punto)
    print(punto["x"])
    print(punto["y"])

    punto["z"] = 56
    print(punto)


diccionarios()
