def calculadora(numero1, numero2, operacao):
    if operacao == '+':
        return numero1 + numero2
    elif operacao == '-':
        return numero1 - numero2
    elif operacao == '*':
        return numero1 * numero2
    elif operacao == '/':
        if numero2 != 0:
            return numero1 / numero2
        else:
            return 'erro: divisao por zero!'
    else:
        return 'operacao invalida!'
    
def main():
    n1 = float(input('digite o primeiro numero: '))
    n2 = float(input('digite o segundo numero: '))
    op = input('digite a operacao (+, -, *, /): ')

    resultado = calculadora(n1, n2, op)
    print('resultado:', resultado)

main()