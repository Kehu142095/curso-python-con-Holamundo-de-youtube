# estas tuplas NO SE PUEDEN MODIFICAR solo se puede crear nuevas tuplas en base a las existentes
# estas tuplas se usan cuando no queremos modificar de forma accidental un listado
def tuplist():
    numeros = (1, 2, 3)+(4, 5, 6)
    print(numeros)

    punto = tuple([1, 2])
    print(punto)

    menosNumeros = numeros[:2]  # crea una nueva lista
    print(menosNumeros)

    primero, segundo, *otros = numeros
    print(primero, segundo, otros)

    for n in numeros:
        print(n)

    listaNumers = list(numeros)
    # NO MODIFICAMOS LA TUPLA lo que hicimos fue crear una lista y la modificamos en base a la tupla
    listaNumers[0] = "paco feliz"
    print(listaNumers)


tuplist()
