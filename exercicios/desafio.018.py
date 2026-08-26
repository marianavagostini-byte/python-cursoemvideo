from rich import print
from rich.panel import Panel

class Churras:
    carne=0.400
    preco_carne=85.90
    
    def __init__(self,titulo,qtd_pessoas):
        self.titulo=titulo
        self.qtd_pessoas=qtd_pessoas
        
    def qtd_carne(self):
        return self.carne* self.qtd_pessoas
    
    def custo_total(self):
        return self.qtd_carne()*self.preco_carne
    
    def custo_individual(self):
        return self.custo_total() / self.qtd_pessoas
    
    def analisar(self):
        conteudo = f"Analisando {self.titulo} com {self.qtd_pessoas} convidados"
        conteudo += f"\nCada participante comerá {self.carne}Kg e cada Kg custa R${self.preco_carne:,.2f}"
        conteudo += f"\nRecomendo comprar {self.qtd_carne():.3f}Kg de carne"
        conteudo += f"\nO custo total será de R${self.custo_total():,.2f}"
        conteudo += f"\nCada pessoa pagará R${self.custo_individual():,.2f} para participar."
        
        painel= Panel(conteudo, title=self.titulo)
        print(painel)
c1=Churras(titulo='Churras com amigos', qtd_pessoas=10)
c1.analisar()