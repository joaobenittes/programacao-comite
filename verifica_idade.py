idade = int(input("informe uma idade -> "))

if idade >= 0 and idade <= 12:
    print("voce e crianca!")
elif idade  >= 13 and idade <= 17:
    print("voce e adolecente!")
elif idade > 17:
    print("voce e adulto")
else:
    print("voce e  invalida")