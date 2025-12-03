class produto:
    def __init__(self,  nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar_info(self):
        print(f'produto: {self.nome} | preco: r${self.preco:2f}')

p1 = produto('notebook', 3500.00)
p1.mostrar_info()
    