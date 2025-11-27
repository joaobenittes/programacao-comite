def abrir_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.readlines()
        return conteudo
    except FileNotFoundError:
        return None
    

def main():
    arquivo = abrir_arquivo('arq11.txt')
    if arquivo == None:
        print('ARQUIVO NAO ENCONTRADO')
    else:
        print(arquivo)


main()