from random import randint

class Dados:
    faces=6
    def __init__(self):
        self.ultimo_result=None
    def rolar(self):
        self.ultimo_result = randint(1,Dados.faces)
    def mostrar(self, nome_dado: str = "Dado"):
        print(f'{nome_dado} caiu em: {self.ultimo_result}')
dado1= Dados()
dado2=Dados()
dado1.rolar()
dado2.rolar()
dado1.mostrar('Dado 1')
dado2.mostrar('Dado 2')