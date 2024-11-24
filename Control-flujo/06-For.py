Buscar = input("\n Que numero buscas: ")
Buscar = int(Buscar)

for numero in range(10):
    print(numero)
    if numero == Buscar:
        print("\nEnvontrado.", Buscar)
        break
else:
    print("\n No encontrado :( .")
