lado_1 = int(input("informe o valor do primeiro lado "))
lado_2 = int(input("informe o valor do segundo lado "))
lado_3 = int(input("informe o valor do terceiro lado"))

if lado_1 + lado_2 > lado_3 or \
    lado_2 + lado_3 > lado_1 or \
    lado_1 + lado_3 > lado_2:
    print("triangulo valido!")

    if lado_1 == lado_2 == lado_3:
        print("tringulo equilatero")
    elif lado_1 == lado_2 or \
         lado_2 == lado_3 or \
         lado_1 == lado_3:
        print("triangulo isoceles")
    elif lado_1 != lado_2 != lado_3:
        print("triangulo escaleno")
     else:
         print("outro tipo")   
else:
    print("tringulo invalido")

