class aluno:
    def __init__(self, nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        media = (self.nota1 + self.nota2) / 2 
        return media
    
aluno1 = aluno(8.5, 7.0)
print('media do aluno:', aluno1.calcular_media())
        