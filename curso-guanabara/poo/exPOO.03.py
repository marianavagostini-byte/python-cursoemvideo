from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados= qtd_lados
    
    @abstractmethod
    def perimetro(self):
        pass
    
    @abstractmethod
    def area(self):
        pass
    
class  Quadrado (Poligono):
    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado
     
    def perimetro(self):
        return self.lado * 4
    
    def area(self):
        return self.lado * self.lado
    
class Circulo (Poligono):
    def __init__(self, raio):
        super().__init__(1)
        self.raio = raio
        
    def perimetro(self):
        return 2 * 3.14 * self.raio
    
    def area(self):
        return 3.14* self.raio * self.raio

q = Quadrado(5)
c = Circulo(3)

print(f'Quadrado: {q.qtd_lados} lados, perímetro {q.perimetro():.2f}, área {q.area():.2f}')
print(f'Círculo: {c.qtd_lados} lado, perímetro {c.perimetro():.2f}, área {c.area():.2f}')