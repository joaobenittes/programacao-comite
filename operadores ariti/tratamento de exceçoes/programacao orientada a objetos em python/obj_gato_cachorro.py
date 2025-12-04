class animal:
    def fazer_som(self):
        print('o animal esta fazendo um som!')

class gato(animal):
    def fazer_som(self):
        print('miau!')

class cachorro(animal):
    def fazer_som(self):
        print('au au!')

g = gato()
c = cachorro()

g.fazer_som()
c.fazer_som()