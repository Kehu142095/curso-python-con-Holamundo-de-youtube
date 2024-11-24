def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado


print("\nFrank D. Berntkient saluda al mundo")
k = largo("hola mundo")
print(k)
