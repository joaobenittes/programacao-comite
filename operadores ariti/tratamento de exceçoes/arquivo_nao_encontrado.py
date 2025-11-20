def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        print('arquivo nao encontrado!')

def main():
    ler_arquivo('logs_empresa,txt')

main()