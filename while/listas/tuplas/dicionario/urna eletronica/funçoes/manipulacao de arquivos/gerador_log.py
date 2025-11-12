from datetime import datetime

def gerar_logs():
    with open('log.txt', 'w') as arquivo:
        for i in range(3):
            now = datetime.now()
            arquivo.write(f'{now} log {1+1} \n')

    print('log gerado com sucesso!')

def main():
    gerar_logs()

main()