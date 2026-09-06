class Pessoa:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
    
    def apresentar(self):
        conteudo= f"Ola, meu nome e {self.nome} e tenho {self.idade} anos."
        print(conteudo)

p1=Pessoa("Mariana" , 19)
p1.apresentar()