class Playlist:
    def __init__(self,lista):
        self.lista=lista
        self.posicao_atual=0
    def proxima(self):
        self.posicao_atual += 1
        if self.posicao_atual >=len(self.lista):
            self.posicao_atual=0
    def anterior(self):
        self.posicao_atual -=1
        if self.posicao_atual <0:
            self.posicao_atual = len(self.lista)-1
    def tocando(self):
        print(f'Tocando agora: {self.lista[self.posicao_atual]}')


p = Playlist(["Música A", "Música B", "Música C"])

p.tocando()   
p.proxima()
p.tocando()  
p.proxima()
p.tocando()   
p.proxima()
p.tocando()   