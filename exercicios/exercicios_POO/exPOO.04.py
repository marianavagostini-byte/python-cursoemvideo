# Desafio Sistema de Cadastro de funcionarios

from abc import ABC, abstractmethod

class Funcionario (ABC):
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    def apresentar(self):
        print(f'=== {self.nome} ({self.matricula}) ===')
    
    @abstractmethod
    def funcao(self):
        pass
    @abstractmethod
    def jornada(self):
        pass

class Vendedor(Funcionario):
    
    def __init__(self, nome, matricula, regiao):
        super().__init__(nome, f'V-{matricula}')
        self.regiao = regiao
    
    def funcao(self):
        print(f'Vende para a regiao {self.regiao}.') 
    
    def jornada(self):
        print('Trabalha das 8h as 18h no escritorio')

class Tecnico(Funcionario):
    def __init__(self, nome, matricula,area):
        super().__init__(nome, f'T-{matricula}')
        self.area = area
    def funcao(self):
        print(f'Faz assistencia na area de {self.area}')
    def jornada(self):
        print('Trabalha em campo, com horário variável.')
        

p1 = Vendedor('Mariana', 157, 'Sul')
p1.apresentar()
p1.funcao()
p1.jornada()

print()

p2 = Tecnico('Carlos', 204, 'Redes')
p2.apresentar()
p2.funcao()
p2.jornada()
