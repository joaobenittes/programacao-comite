def verifica_idade(idade):
    if idade < 0:
        raise ValueError('a idade nao pode ser negativa')
    print(f'idade correta {idade}')
    return

def obtem_idade():
    return int(input('informe sua idade -> '))

def main():
    while True:
        try:
            idade = obtem_idade()
            if verifica_idade(idade):
                break
        except ValueError as erro:
            print(erro)
            print('tente novamente\n')

main()