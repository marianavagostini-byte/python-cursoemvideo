from abc import ABC,abstractmethod

class Transporte(ABC):
    def __init__(self,distancia):
        self.distancia = distancia
        self.frete = 0
    
    @abstractmethod
    def calc_frete(self):
        pass
    
class Moto(Transporte):
    fator=0.50 
    
    def __init__(self, distancia):
        super().__init__(distancia)
        
    def calc_frete(self):
        self.frete = self.distancia * self.fator
        return self.frete
    
class Caminhao(Transporte):
    fator = 1.20
    def __init__(self, distancia):
        super().__init__(distancia)
        
    def calc_frete(self):
        self.frete = self.fator * self.distancia
        return self.frete
    
class Drone(Transporte):
    fator=9.50
    def __init__(self, distancia):
        super().__init__(distancia)
        
    def calc_frete(self):
        self.frete = self.fator * self.distancia
        return self.frete
m = Moto(20)
print(m.calc_frete())