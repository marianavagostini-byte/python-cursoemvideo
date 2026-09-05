# Desafio 24 - POO Guanabara

from abc import ABC , abstractmethod

class BebidaQuente(ABC):
   
    def preparar(self):
        self.ferver_agua()
        self.misturar()
        self.servir()
    def ferver_agua(self):
        print('Fervendo a água...')
    
    @abstractmethod
    def misturar(self):
        pass
    
    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):
    
    def misturar(self):
        print('Misturando o pó de café na água quente.')
    def servir(self):
        print('Servindo o café na xícara.')
    
class Cha(BebidaQuente):
    
    def misturar(self):
        print('Misturando o cha na água quente.')
    def servir(self):
        print('Servindo o cha na xícara.')

class Leite(BebidaQuente):
    
    def misturar(self):
         print('Misturando o cafe no leite quente.')
    def servir(self):
        print('Servindo o cafe com leite na xícara.')

c=Cafe()
c.preparar()

print()
ch=Cha()
ch.misturar()
ch.servir()