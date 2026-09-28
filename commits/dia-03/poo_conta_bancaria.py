class ContaBancaria:

    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Saque realizado.")
        else:
            print("Saldo insuficiente.")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: R")


conta = ContaBancaria("Mariana", 1000)

conta.depositar(500)
conta.sacar(200)
conta.mostrar_saldo()
