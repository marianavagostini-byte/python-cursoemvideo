from abc import ABC , abstractmethod
class Funcionario(ABC):
    sal_min = 1612
    inss = 7.5
    
    def __init__(self,nome):
        self.nome = nome
        self.salario = 0 
    
    @abstractmethod
    def calc_sal(self):
        pass
    
    
    def analisar_sal(self):
        pass
    
    

class FuncionarioHorista(Funcionario):
    def __init__(self, nome,valor_hora , qtd_horas):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.qtd_horas = qtd_horas
        
    def calc_sal(self):
        self.calc_sal = self.valor_hora * self.qtd_horas
        return self.calc_sal
        

class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, salario_bruto):
        super().__init__(nome)
        self.salario_bruto = salario_bruto
        
    def calc_sal(self):
        self.salario = self.salario_bruto - (self.salario_bruto * self.inss / 100)
        return self.salario
    
