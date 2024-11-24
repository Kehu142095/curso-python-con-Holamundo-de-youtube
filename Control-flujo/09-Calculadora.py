print("\n--Bienvenido señor usuario--")
print("\n para salir escribe \"salir\"")
print("las operaciones son: suma, resta, multi, div")

Num1 = ""

while True:
    if not Num1:
        Num1 = input("\ningresa el primer numero:")
        if Num1.lower() == "salir":
            break
        Num1 = int(Num1)
    Op = input("\ningresa la Operación: ")

    if Op.lower() == "salir":
        break
    Num2 = input("\ningresa el segundo numero:")
    if Num2.lower() == "salir":
        break

    Num2 = int(Num2)

    if Op.lower() == "suma":
        Num1 += Num2
    elif Op.lower() == "resta":
        Num1 -= Num2
    elif Op.lower() == "multi":
        Num1 *= Num2
    elif Op.lower() == "div":
        Num1 /= Num2
    else:
        print("Operacion No valida")
        break
    print(f"\nEl resultado es: {Num1}")
