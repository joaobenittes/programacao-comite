import os

def criar_pasta(nome_pasta):
    os.mkdir(nome_pasta)
    print('pasta criada com sucesso!')

def main():
    criar_pasta(input('qualda pasta que deseja criar? -> '))

main()