frutas_lidas = []
with open('frutas.txt', 'r',encoding='utf-8') as arquivo:
    for linha in arquivo:
        frutas_lidas.append(linha.strip())

print(frutas_lidas)