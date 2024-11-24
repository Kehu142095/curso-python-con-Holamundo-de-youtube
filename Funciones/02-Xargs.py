def Suma(*numeros):  # el simbolo * convierte nuestro parametros en iterables
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)  # el print va fuera del for, sin la identación del for


Suma(1, 2, 8, 9)
Suma(1, 2)
Suma(2, 8, 5, 45, 22)  # es iterable si es iterable se le puede poner en un "for"
