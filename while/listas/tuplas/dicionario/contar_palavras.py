palavras = ['ola', 'mundo', 'python', 'comite', 'pinoia', 'dia']

qtd_letras = {}


for palavra in palavras:

    chave = f'qtd_palavras - {len(palavra)}'
    valor = len(palavra)

    qtd_palavras.update