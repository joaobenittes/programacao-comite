def converter(texto):
    try:
        num = float(texto)
        print(f'{type(num)} | {num}')
        return True
    except ValueError:
        print('informacao digitada nao e um numero')
        print('tente novamente')
        return False
    

def obter_informacao():
    while True:
        info = input('informe um numero -> ')

        if converter(info):
            break
        
def main():
    obter_informacao()


main()
