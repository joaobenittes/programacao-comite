def ler_logs(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:

        logs = arquivo.readlines()

        resultados = {'info': 0, 'error': 0, 'warning': 0}


        for linha in logs:
            if 'INFO' in linha:
                resultados['info'] += 1
            elif 'ERROR' in linha:
                resultados['error'] += 1
            elif 'WARNING' in linha:
                resultados['warning'] += 1
    
    return resultados

def gerar_relatorio(resultados):
    with open('relatorio.txt', 'w') as arquivo:
        arquivo.write('relatorio de logs\n')
        for chave, valor in resultados.items():
            arquivo.write(f'existem {valor} ocorrencias do log {chave}')

    print('relatorio de logs')
    for chave, valor in resultados.items():
        print(f'existem {valor} ocorrencia do log {chave}')

def main():
    nome_arquivo = 'logs_desafio.txt'
    resultados = ler_logs (nome_arquivo)
    gerar_relatorio(resultados)


main()
                                                                    