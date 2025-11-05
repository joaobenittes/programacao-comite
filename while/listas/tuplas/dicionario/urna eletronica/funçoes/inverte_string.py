def inverter_string(texto):
    return texto[::-1]

def main():
    palavra = input('digite um texto: ')
    resultado = inverter_string(palavra)
    print('texto invertido:', resultado)

main()