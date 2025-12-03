class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar_info(self):
        print(f'produto: {self.nome} | preco: r${self.preco:.2f}')

    def aplicar_desconto(self, percentual):
        '''aplica um desconto em % sobre o preco do produto.'''
        desconto =self.preco * (percentual / 100)
        self.preco -= desconto
        print(f'desconto de {percentual} % aplicado! novo preco: r%{self.preco:.2f}')

p1 = produto('notebook', 3500.00)
p1.aplicar_desconto(10)
p1.mostrar_info()
    