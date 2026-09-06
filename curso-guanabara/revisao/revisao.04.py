class Lampada:
    def __init__(self):
        self.ligado=False
    def ligar(self):
        self.ligado=True
    def desligar(self):
        self.ligado=False
    def estado(self):
        if self.ligado:
            print('A lampada esta acesa')
        else:
            print('A lampada esta apagada')
l1= Lampada()
l1.estado()
l1.ligar()
l1.estado()