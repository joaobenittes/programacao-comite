def contar_positivos(lista):
    qt = 0
    for numero in lista:
        if numero > 0:
            qt += 1
    return qt 

def main():
    numeros = [3, -2, 7, 0, -1, 10, 5]
    total = contar_positivos(numeros)
    print('quantidade de numeros positivos:', total)

main()