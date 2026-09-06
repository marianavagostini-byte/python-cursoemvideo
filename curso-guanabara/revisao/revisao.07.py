
class Termometro:
    min = 15
    max = 30

    def __init__(self):
        self.inicio = 20

    def aumentar(self):
        if self.inicio < Termometro.max:
            self.inicio += 1

    def diminuir(self):
        if self.inicio > Termometro.min:
            self.inicio -= 1

    def mostrar(self):
        tela = f"Temperatura: {self.inicio}"
        print(tela)


t1 = Termometro()
t1.aumentar()
t1.mostrar()