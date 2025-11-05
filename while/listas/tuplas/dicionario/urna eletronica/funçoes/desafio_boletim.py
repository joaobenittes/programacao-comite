def boletim(nome, nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        situacao = 'aprovado'
    else:
        situacao = 'reprovado'

    return {'nome': nome, 'media': round(media, 2), 'situacao': situacao}

def main():
    nome = input('digite o nome do aluno')
    nota1 = float(input('digite a primeira nota: '))
    nota2 = float(input('digite a segunda nota: '))
    nota3 = float(input('digitea terceira nota: '))

    resultado = boletim(nome, nota1, nota2, nota3)

    print('\n---boletim---')
    print(f'nome: {resultado['nome']}')
    print(f'media: {resultado['media']}')
    print(f'situacao: {resultado['situacao']}')

main()