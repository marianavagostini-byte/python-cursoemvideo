class Pessoa:

    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print(f"Meu nome é {self.nome}")


class Desenvolvedor(Pessoa):

    def __init__(self, nome, linguagem):
        super().__init__(nome)
        self.linguagem = linguagem

    def programar(self):
        print(f"{self.nome} está programando em {self.linguagem}.")


dev = Desenvolvedor("Mariana", "Python")

dev.apresentar()
dev.programar()
