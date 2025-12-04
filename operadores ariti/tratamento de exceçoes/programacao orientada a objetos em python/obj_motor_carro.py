class motor:
    def __init__(self, potencia, tipo):
        self.potencia = potencia
        self.tipo = tipo

    def exibir_info(self):
        print(f'motor: {self.potencia}cv, tipo: {self.tipo}')


class carro:
    def __init__(self, modelo, ano, motor):
        self.modelo = modelo
        self.ano = ano
        self.motor = motor

    def exibir_info(self):
        print(f'carro: {self.modelo}, ano: {self.ano}')
        self.motor.exibir_info()

meu_motor = motor(150, 'gasolina')
meu_carro = carro('toyota corolla', 2023, meu_motor)
meu_carro.exibir_info()
        
