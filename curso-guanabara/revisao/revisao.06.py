class Cofre:
    def __init__(self):
        self.saldo=0
    def depositar(self,valor):
        if valor <=0:
            print('Valor invalido. Deposito recusado.')
        else:
            self.saldo += valor
            print(f"Deposito de R$ {valor:.2f} aceito. Saldo: R${self.saldo:.2f}")
            
    def mostrar(self):
        print(f" Saldo: R$ {self.saldo:.2f}")
        
    
c1=Cofre()
c1.depositar(400)
c1.depositar(-500)
c1.mostrar()