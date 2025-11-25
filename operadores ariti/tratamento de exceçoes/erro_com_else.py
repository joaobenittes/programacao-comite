def obtem_valor():
    try:
        valor = float(input('informe um numero -> '))
    except ValueError:
        print('valor invalido!' , end=' ')
        print('necessario ser um numero inteiro!')
    else:
        print(f'valor informadoe (valor)')
        return int(input('informe um valor -> '))
    
def main():
    obtem_valor()

main()
