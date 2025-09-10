numero_1 = float(input("informe um numero -> "))
operacao = input("informe a operacao -> ")
numero_2 = float(input("informe o outro numero -> "))

if operacao == "+":
   resultado = numero_1 + numero_2
   print (f"a soma e{resultado}!")
elif operacao == "-":
     resultado = numero_1 - numero_2
     print(f"a subtracao e {resultado}!")
elif operacao == "*":
    resultado = numero_1 * numero_2
    print (f"a multiplicacao e { resultado}!")
elif operacao == "/":
    if numero_2 == 0:
       print("uma das condicoes e zero!")
    else:
        resultado = numero_1 / numero_2
        print (f"a divisao e {resultado}!")
else:
    print ("operacao invalida!")
    
