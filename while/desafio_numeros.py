import random

n = random.randint(1, 100)
chute = 0
ganhou = 0

while true:
    chute = int(input('chute um numero -> '))
    tentativas += 1

    if chute == n:
        print('parabens vocw acertou com {tentativas} tentativas!!!')
        break
    elif chute < n:
        print(f'o numero {chute} e menor que o numero secreto')
    elif chute > n:
        print(f'o numero {chute} e maior que o numero secreto')

