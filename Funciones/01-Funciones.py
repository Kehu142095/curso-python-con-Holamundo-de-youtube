
# para definir nuestra funcion tenemos que usar palabra reservada de "def" def de definir
# seguido por el nombre que le queremos poner a la funcion por ejemplo Hola lo que ira dentro de la funcion ira identado

def Hola(nombre, apellido):
    print("\nKonnichiha Mundo!")
    print("ultimador pitones")
    print(f"\nBienvenido {nombre} {apellido}")
    # lo que ira dentro del parentesis es un parametro cuando defino la funcion, a la hora de definir
    # si pongo mas parametros iran separados por una coma


Hola("Kluf", "bernkient")
# lo que pongo dentro del parentesis despues de definir es un argumento o argumentos, por ejemplo la palabra que pase "Kluf" es un argumento


# para cuando estoy muuy abansado en el codigo del archivo y no tengo claro cual seria el orden de los argumentos que pasare
Hola(apellido="bernkient", nombre="Kluf")
