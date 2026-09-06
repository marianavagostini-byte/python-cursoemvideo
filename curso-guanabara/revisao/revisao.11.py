class Aluno:
    
    def __init__(self,nome:str):
        self.nome=nome
        self.notas=[]
    def adicionar_nota(self,nota):
        self.notas.append(nota)
    def media(self):
        return sum(self.notas)/len(self.notas)
    def boletim(self):
        notas_formatadas = ", ".join(str(n) for n in self.notas)
        print(f"{self.nome}: {notas_formatadas} - média {self.media():.2f}")
a1 = Aluno("Mariana")
a1.adicionar_nota(8.0)
a1.adicionar_nota(7.5)
a1.adicionar_nota(9.0)
a1.boletim()

a2 = Aluno("Pedro")
a2.adicionar_nota(5.0)
a2.adicionar_nota(6.5)
a2.boletim()