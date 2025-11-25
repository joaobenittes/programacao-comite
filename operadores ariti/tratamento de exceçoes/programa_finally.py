def obtem_valor():
    try:
        valor = int(input('informe um valor inteiro -> '))
    except ValueError:
        print('valor invalido!', end=' ')
        print('necessario ser um numero inteiro!')
    else:
        print(f'valor informado e {valor}')

    finally:
        print('programa encerrado!')

def main():
    obtem_valor()

main()