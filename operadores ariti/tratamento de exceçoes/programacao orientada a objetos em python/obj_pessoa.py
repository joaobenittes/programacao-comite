class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'ola! meu nome e {self.nome} e eu tenho {self.idade} anos.')

p1 = pessoa('joao', 55)
p1.apresentar()