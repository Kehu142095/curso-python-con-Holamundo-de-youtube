# """aplicaion que detecta si es palindromo o no"""

# 1.Necesita una funcion que nos permita eliminar los espacios en blanco de un string
# 2.necesita una funcion que tome un texto y le de vuelta, o le aplique un "reverse"
# (la funcion "reverse" se puede construir sin buscarlo en internet)
# para los dos puntos anteriores, las funciones van a tener a aplicar "for" e iterar cada uno de los caracteres
# y dependiendo del caracter que estas resiviendo es que si le aplicas una operacion o no

# palindromo es una frase o palabra que se escribe esactamente igual si la escribimos al reves o al derecho


def no_espacio(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char  # += asi concateno un caracter, char igual a caracter
    return nuevo_texto


def reverso(texto):
    texto_de_reverso = ""
    for char in texto:
        # asi concateno los caracteres de derecha a izquierda
        texto_de_reverso = char + texto_de_reverso
    return texto_de_reverso


def es_palindromo(texto):
    texto = no_espacio(texto)
    texto_de_reverso = reverso(texto)
    return texto.lower() == texto_de_reverso.lower()


def iniciar():
    frase = input("Pon una palabra o una frase: ")
    print(frase, es_palindromo(frase))
    iniciar()


iniciar()
# print(es_palindromo(pon_palabra("")))

# print("Abba", es_palindromo("Abba"))
# print("Reconocer", es_palindromo("Reconocer"))
# print("Amo la paloma", es_palindromo("Amo la paloma"))
# print("hola mundo", es_palindromo("hola mundo"))
