def saudacao(nome, idade):
    return f'ola {nome}, parabens peols seus {idade} anos!'

def main():
    nome = input('informe seu nome -> ')
    idade = int(input('informe sua idade -> '))

    boas_vindas = saudacao(nome, idade)

    print(boas_vindas)


main()