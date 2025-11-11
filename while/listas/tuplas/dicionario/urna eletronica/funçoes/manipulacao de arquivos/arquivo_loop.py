try:
    with open('meu nome.txt',) as arquivo:
        for linha in arquivo:
            print(linha)
except FileNotFoundError:
    print('arquivo nao encontrado!')
                