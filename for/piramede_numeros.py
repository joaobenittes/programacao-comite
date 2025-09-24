saida = ''
tamanho_piramede = int(input('informe o tamanho da piramede -> '))

for n in range(1,  tamanho_piramede+1):
    for n2 in range(1, n+1):
        print(n2, end='')
    print()