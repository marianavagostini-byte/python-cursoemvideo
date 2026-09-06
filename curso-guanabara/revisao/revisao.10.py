class Retangulo:
    def __init__(self, largura:int, altura:int):
        self.largura = largura 
        self.altura = altura
    
    def area(self):
        return self.largura * self.altura
    
    def perimetro(self):
        return 2 * (self.largura + self.altura)
    
    def mostrar(self):
        print(f'Retangulo {self.largura} x {self.altura}')
        print(f'Area: {self.area()}')
        print(f'Perimetro: {self.perimetro()}')
r1=Retangulo(5,3)
r1.mostrar()

