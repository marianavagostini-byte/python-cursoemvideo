class ContaBancaria:

    banco = 'Banco Central'                    # atributo de classe

    def __init__(self, titular, saldo=0.0):
        self.titular = titular                 # veio de fora
        self.saldo = saldo                     # veio de fora, com padrão
        self.ativa = True                      # bool fixo
        self.bloqueada = False                 # bool fixo
        self.extrato = []                      # lista vazia

    def depositar(self, valor):
        if self.bloqueada:
            print('Conta bloqueada.')
        elif valor <= 0:
            print('Valor inválido.')
        else:
            self.saldo = self.saldo + valor
            self.extrato.append(f'Depósito: R$ {valor:.2f}')
            print(f'Depósito feito. Saldo: R$ {self.saldo:.2f}')

    def sacar(self, valor):
        if self.bloqueada:
            print('Conta bloqueada.')
        elif valor > self.saldo:
            print('Saldo insuficiente.')
        else:
            self.saldo = self.saldo - valor
            self.extrato.append(f'Saque: R$ {valor:.2f}')
            print(f'Saque feito. Saldo: R$ {self.saldo:.2f}')

    def bloquear(self):
        self.bloqueada = True
        print('Conta bloqueada.')

    def total_movimentado(self):
        return len(self.extrato)

    def mostrar_extrato(self):
        print(f'{self.titular} — {self.banco}')
        for linha in self.extrato:
            print(linha)
        print(f'Saldo final: R$ {self.saldo:.2f}')
c1=ContaBancaria('Mariana',1500)
c1.depositar(2000)
c1.sacar(500)
c1.mostrar_extrato()