class contabancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'deposito de r$ {valor:.2f} realizado. saldo atual: r$ {self.saldo:.2f}')
        else:
            print('valor de deposito invalido!')

    def sacar(self, valor):
        if valor <= 0:
            print('valor do saque invalido!')
        elif valor > self.saldo:
            print('saldo insufisiente!')
        else:
            self.saldo -= valor
            print(f'saque de r${valor:.2f} realizado. saldo atual: r$ {self.saldo:.2f}')

conta = contabancaria(100)
conta.depositar(50)
conta.sacar(30)
conta.sacar(200)
    