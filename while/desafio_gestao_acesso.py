usuario = 'admin'
senha = '123456'
tentativas = 3

while tentativas > 0:
    if input('informe o usuario -> ') == usuario:
        if input('informe a senha -> ') == senha:
          print(f'bem vindo {usuario}')
        break
    else:
        print('senha incorreta , tente novamente')

        tentativas -= 1

        print(f'tentativas restantes {tentativas}')
else:
     print(f'usuario incorreto , temte novamente')    

     tentativas -= 1 

     print(f'tentativas restantes {tentativas}')   
              



