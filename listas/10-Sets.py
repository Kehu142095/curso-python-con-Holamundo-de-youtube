def Grupo():
    # set significa grupo o conjunto
    # un set es una coleccion de datos que no se pueden repetir y tampoco esta ordenada
    primerSet = {1, 1, 2, 2, 3, 4, 56}
    primerSet.add(7)
    primerSet.remove(1)
    print("\nmi primer set es: ", primerSet)

    segundoSet = [3, 4, 5, 6, 7, 8, 9]
    segundoSet = set(segundoSet)
    print("mi segundo set es: ", segundoSet, "\n")

    # el operador | se conoce como union
    print(primerSet | segundoSet, "_____es la union de los dos sets")
    # el operador & es interseccion, va a mostrar el numero comun entre los dos sets
    print(primerSet & segundoSet, "_____es la interseccion de los dos sets")
    # el operador - se conoce como diferencia
    print(primerSet - segundoSet, "_____es la diferencia de los dos sets")
    # el operador ^ es la diferencia simetrica
    print(primerSet ^ segundoSet, "_____es la diferencia simetrica de los dos sets")

    if 5 in segundoSet:
        print("\nHola mundo")


Grupo()
