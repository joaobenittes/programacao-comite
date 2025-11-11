frutas = ['maça', 'banana', 'morango', 'uva', 'abacaxi']

with open('frutas.txt', 'w', encoding='utf-8') as arquivo:
    for fruta in frutas:
        arquivo.write(fruta + '\n')