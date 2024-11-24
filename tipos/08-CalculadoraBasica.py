
# input es la funcion que nos permite obtener datos del usuario
N1 = input("\npon el primer numero: ")
N2 = input("pon el segundo numero: ")

# Int es la funcion que nos permite cambiar datos string a integer, texto a numero
N1 = int(N1)
N2 = int(N2)

Suma = N1 + N2
Resta = N1 - N2
Multi = N1 * N2
Dividir = N1 / N2

Resultado = f"""

para los numeros {N1} y {N2},

el resultado de Sumar es :{Suma}.
el resultado de Restar es :{Resta}.
el resultado de Multiplicar es :{Multi}.
el resultado de Dividir es :{Dividir}.
"""
print(Resultado)
