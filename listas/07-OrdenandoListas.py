"""Tuplas"""


def tuplas():
    numeros = [56, 86, 54, 12, 35, 25, 65, 0, 70, 356]

    # numeros.sort(reverse=True)  # los ordena al reves
    # crea una nueva lista ordenada al derecho
    numeros2 = sorted(numeros, reverse=True)
    print(numeros)
    print(numeros2)

    # _____________
    print("-------------------")

    usuarios = [[3, "carlos"], [1, "yuldani"], [8, "Mishin"],
                [5, "daniela"], [10, "sara"], [0, "poncho"]]

    usuarios.sort()
    print(usuarios)

    # _____________
    print("-------------------")

    usuarios2 = [["carlos", 3], ["yuldani", 1], ["mishin", 9],
                 ["daniela", 5], ["sara", 12], ["poncho", 0]]

    def orden(elemen):
        return elemen[1]

    usuarios2.sort(key=orden)
    print(usuarios2)


tuplas()

# ---------Tuplas, Funciones anonimas, lambda
print("\n-----Lambda, funciones anonimas-----\n")

usuarios2 = [["carlos", 3], ["yuldani", 1], ["mishin", 9],
             ["daniela", 5], ["sara", 12], ["poncho", 0]]

usuarios2.sort(key=lambda el: el[1], reverse=True)
print(usuarios2)
