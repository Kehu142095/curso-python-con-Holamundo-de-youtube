def BuscarElementos(texto):
    frase = texto
    mascotas = ["Owlmansito",
                "Skay", "Panda", "Mishin",
                "Klimber", "Skay", "mascota",
                "Tomasho", "Skay", "Paco feliz",
                "Owlmansito"]
    print("\nLista actual--> ", mascotas)
    mascotas.insert(2, frase)
    mascotas.append("Paco triste")  # inserta al final de la lista
    mascotas.remove(frase)  # elimina al prinsipio donde se agrego
    mascotas.pop()  # elimina el ultimo de lista
    mascotas.pop(1)
    # del mascotas[0]
    # mascotas.clear()
    print(mascotas)


def iniciar():
    frase = input("\nQue palabra: ")
    print(BuscarElementos(frase))


iniciar()
