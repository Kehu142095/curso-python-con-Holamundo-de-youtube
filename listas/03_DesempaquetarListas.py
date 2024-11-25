# numeros = [1, 2, 3]

# feo!
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]  esto que estoy haciendo es HORRIBLE
# primero, segundo, tercero = numeros

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 56]
primero, segundo, tercero, * otros = numeros
primero, *otros, penul, ultimo = numeros

print(primero, otros, ultimo)
print(primero, segundo, tercero, otros)
print(primero, segundo, otros, ultimo)
print(primero, penul, otros)
