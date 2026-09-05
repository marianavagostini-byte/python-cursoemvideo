class Cofre:
    def __init__(self):
        self.saldo=0
    def depositar(self,valor):
        self.saldo+=valor
    def mostrar(self):
        text=f"Saldo: {self.saldo}"
        print(text)
    
c1=Cofre()
c1.depositar(500)
c1.mostrar()