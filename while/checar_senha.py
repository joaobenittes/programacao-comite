senha = ''

while senha != "comite":
    senha = input('digite a senha -> ')

while true:
    if senha == 'comite':
        print('acesso liberado!')
        break
    else:
        senha = input('informe a senha -> ')