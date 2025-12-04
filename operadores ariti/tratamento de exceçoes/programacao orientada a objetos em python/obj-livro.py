class livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_info(self):
        print(f'titulo: {self.titulo}')
        print(f'autor: {self.autor}')

meu_livro = livro('dom casmurro', 'machado de assis')
meu_livro.exibir_info()
        