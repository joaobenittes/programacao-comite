class retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura
    
r1 = retangulo(5, 3)
print(f'a area do retangulo e: {r1.area()}')
    