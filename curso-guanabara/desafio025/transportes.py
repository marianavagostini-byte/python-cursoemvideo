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
        
    def calc_frete(self):
        self.frete = self.distancia * Moto.fator
        return self.frete
    
class Caminhao(Transporte):
    fator = 1.20
    
        
    def calc_frete(self):
        if self.distancia < 50:
            self.frete =0
            return "Raio minimo de 50km"
        else:
            self.frete = self.distancia * Caminhao.fator
            return self.frete
        
    
class Drone(Transporte):
    fator=9.50
        
    def calc_frete(self):
        if self.distancia > 10:
            self.frete =0
            return "Raio maximo de 10km"
        else:
            self.frete= self.distancia * Drone.fator
            return self.frete
    
    
