
class Contador:
    def __init__(self):
        self.contagem = 0

    def somar(self):
        self.contagem += 1

    def zerar(self):
        self.contagem = 0

    def mostrar(self):
        print(f"Contagem: {self.contagem}")



c1 = Contador()

c1.somar()

c1.mostrar() 

