class senhaincorretaError(Exception):
    pass


class senhafracaError(Exception):
    pass

def fazer_login(senha_usuario):
    logar = input('\n\ninforme sua senha -> ')

    if logar == senha_usuario:
        print('\login efetuado com sucesso!\n\n')
    else:
        print('\ntente novamente!')
        raise senhaincorretaError('senha incorreta!\n')
    

def cadastrar_senha():
    print('\nCADASTRO DE SENHA')
    senha_usuario = input('informe a senha -> ')

    if len(senha_usuario) > 10:
        print('\ntente novamente!')
        raise senhafracaError('senha deve conter 10 caracteres!\n')
    else:
        print('\nsenha cadastrada com sucesso\n')
        return senha_usuario
    

def menu():
    senha_usuario = '0'
    while True:
        try:
            opcao = int(input(F'1 - criar senha\n' '2 - fazer login \n' '3 - sair\n' '-> '))
            if opcao == 1:
                senha_usuario = cadastrar_senha()
            elif opcao == 2:
                fazer_login(senha_usuario)
            elif opcao == 3:
                break
            else:
                print('opcao invalida!\n')
                continue
        except senhafracaError as erro:
            print(erro)
        except senhaincorretaError as erro:
            print(erro)

def main():
    menu()

main()
         

