from rich import *
class Funcionario:
    empresa='SlifTio'
    def __init__(self,nome,setor,cargo):
        self.nome=nome
        self.setor=setor
        self.cargo=cargo
    
    def apresentar(self):
        return(f"Olá! Sou [bold green]{self.nome}[/], atuo como [bold green]{self.cargo}[/] no setor de {self.setor} na empresa [underline green]{Funcionario.empresa}[/].")

f1 = Funcionario("Mariana", "TI", "Developer")

print(f1.apresentar())


