def compren():
    usuarios2 = [["carlos", 3], ["yuldani", 1], ["mishin", 9],
                 ["daniela", 5], ["sara", 12], ["poncho", 0]]

    # nombres = []
    # for usuario in usuarios2:
    #     nombres.append(usuario[0])
    # print(nombres)

    # __--forma mas elegante de hacer lo mismo de lo anterior incluso en una sola linea--__

    # transformar - map
    # nombres = [usuario[0] for usuario in usuarios2]
    # print(nombres)
    # filtrar - filter
    # nombres = [usuario for usuario in usuarios2 if usuario[1] > 2]
    # print(nombres)
    # filtrar y transformar
    # nombres = [usuario[0] for usuario in usuarios2 if usuario[1] > 2] ##prefiero estas formas<--
    # print(nombres)
    # __--Metodos map y filter (otra forma de transformar y filtrar)
    nombres = list(map(lambda usuario: usuario[0], usuarios2))
    print(nombres)
    menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios2))
    print(menosUsuarios)


compren()
