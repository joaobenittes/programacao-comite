def valores_repetidos(lista):
    repetidos = []
    for item in lista:
        if lista.count(item) > 1 and item not in repetidos:
            repetidos.append(item)
    
    return repetidos

def main():
    numeros = [1, 2, 3, 4, 2, 5, 6, 1, 7, 8, 3]
    nova_lista = valores_repetidos(numeros)

    print('valores repetidos:', nova_lista)

main()


                       