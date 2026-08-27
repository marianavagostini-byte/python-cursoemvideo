class Cofre:
    def __init__(self):
        self.saldo=0
    def depositar(self,valor):
        self.saldo+=valor
    def mostrar(self):
        texto=f"Saldo: {self.saldo}"
        print(texto)
        
c1=Cofre()
c1.mostrar()
c1.depositar(500)
c1.mostrar()
c1.depositar(500)