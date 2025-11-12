def encontrar_palavra(nome_arquivo, palavra):
    try:
        with open(nome_arquivo) as arquivo:
            texto = arquivo.readlines()
            cont = 0
            for linha in texto:
                if palavra.lower() in linha.lower():
                    cont += 1 
                    print(f'palavra.lower()}', f'encontrada! | qtd palavras encontradas -> ')
    
    except FileNotFoundError:
        print('print nao encontrado!!!!!')

def main():
    nome_arquivo = 'novo_texto.txt'
    palavra = input('qual a palavra esta procurando? -> ')
    encontrar_palavra(nome_arquivo,palavra)

main()