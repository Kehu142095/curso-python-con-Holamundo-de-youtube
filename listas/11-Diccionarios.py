# los diccionarios son una coleccion de datos que se encuentran agrupoados por una llave y un valor
def diccionarios():
    # lo de la izquierda es un string y lo de la derecha cualquier cosa
    punto = {"x": 25, "y": 50}
    print(punto)
    print(punto["x"])
    print(punto["y"])

    punto["z"] = 56  # <-hasi podemos agregar otra llave al diccionario
    # print(punto, punto["lala"])
    if "lala" in punto:
        print("\nEncontre lala: ", punto["lala"])

    print(punto.get("x"))
    print(punto.get("lala", 564))

    del punto["x"]  # <-hasi si quiero eliminar una llave asociada con su valor

    del (punto["y"])  # <-hasi puedo eliminar una llave asociada con el diccio.

    print(punto, " aqui elimine dos llaves una con su valor y tra asociada al diccionario")

    punto["x"] = 856
    # si yo quiero iterar todas las llaves con su valor dentro de python puedo usar "for"
    for valor in punto:
        # para acceder a sus valores seria (valor, punto[valor])
        print("\n", valor)
        print(valor, punto[valor])

    # o podemos usar otra forma mas conveniente para llamar o acceder a sus valores
    for valor in punto.items():
        print("\n", valor)  # nos devuelve Tuplas

    # tambien podemos hacer un desempaquetado de las Tuplas para acceder a sus valores al igual con las listas
    for llave, valor in punto.items():
        print(llave, valor)


diccionarios()

# un uso mas realista de los Diccionarios
# Por Ejemplo:


def Realista():
    usuarios = [
        {"id": 1, "nombre": "Roberto"},
        {"id": 2, "nombre": "Tomasho"},
        {"id": 3, "nombre": "Federico"},
        {"id": 4, "nombre": "Julian"},
        {"id": 5, "nombre": "Yuldani"},
    ]

    for usuario in usuarios:
        print("\n", usuario["nombre"])


Realista()
