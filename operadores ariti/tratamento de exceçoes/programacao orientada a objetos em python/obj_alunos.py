class aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2
    
    def exibir_info(self):
        print(f'aluno: {self.nome}, media: {self.calcular_media():.2f}')

class turma:
    def __init__(self, alunos):
        self.alunos = alunos

    def exibir_turma(self):
        print('informacoes da turma:')
        for aluno in self.alunos:
            aluno.exibir_info()

aluno1 = aluno('joao', 8, 7)
aluno2 = aluno('maria', 9, 10)
aluno3 = aluno('pedro', 6, 5)

turma = turma([aluno1, aluno2, aluno3])
turma.exibir_turma()
  
        
        