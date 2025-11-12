def contar_linhas():
    try:
        with open('log.txt') as arquivo:
            return len(arquivo.readline())
    except FileNotFoundError:
        print('arquivo nao encontrado!!!')

def main():
    qtd_linhas = contar_linhas()
    print(f'o arquivo lido tem {qtd_linhas} linhas!')

main()