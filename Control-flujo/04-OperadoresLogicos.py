# and, or, not

# baso = input("\nhay un baso en el suelo?: ")
# cerveza = input("esta lleno?: ")

baso = False
cerveza = True
edad = 22

if not baso and (cerveza or edad > 21):
    print("\npuedes beber")
else:
    print("\nno bebas")
