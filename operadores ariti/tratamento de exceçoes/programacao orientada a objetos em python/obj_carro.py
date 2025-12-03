class carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano


    def ligar(self):
        print(f'o carro {self.modelo} ({self.ano}) esta ligando...')

c1 = carro('fusca', 1979)
c1.ligar()
