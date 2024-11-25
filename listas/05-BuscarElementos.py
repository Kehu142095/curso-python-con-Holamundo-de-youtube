
def BuscarElementos(texto):
    frase = texto
    mascotas = ["Owlmansito", "Skay", "Panda", "Mishin",
                "Klimber", "Skay", "mascota", "Tomasho", "Skay", "Paco feliz"]

    print(mascotas.count(frase))
    if frase in mascotas:
        print(mascotas.index(frase))


def iniciar():
    frase = input("Que buscas: ")
    print(BuscarElementos(frase))


iniciar()
