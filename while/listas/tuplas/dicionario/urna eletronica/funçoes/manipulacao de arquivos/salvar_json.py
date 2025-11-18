import json

def salvar_json(dicionario, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dicionario, arquivo, indent=4)


def main():
    dicionario = {'nome': 'ralph', 'idade': 33, 'profissao': 'engenheiro', 'pais': 'brasil'}

    nome_arquivo = 'dados.json'

    salvar_json(dicionario, nome_arquivo)



main()