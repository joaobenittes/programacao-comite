def calcular_porcentagem(valor, porcentagem):
    novo_valor = valor + (valor * (porcentagem / 100))
    return novo_valor

def main():
    valor = int(input('informe o valor -> '))
    porcentagem = int(input('informe a % -> '))

    novo_valor = calcular_porcentagem(valor, porcentagem)

    print(f'o valor atualizado e -> {novo_valor}')

main()