class Carrinho:
    def __init__(self):
        self.itens=[]
    def adicionar(self, nome:str, preco:float):
        produto={"nome":nome, "preco": preco}
        self.itens.append(produto)
    def total(self):
        soma=0
        for item in self.itens:
            soma += item['preco']
        return soma
    def mostrar(self):
        for item in self.itens:
          print(f"{item['nome']:<10} R$ {item['preco']:>6.2f}")
        print("-" * 25)
        print(f"Total: R$ {self.total():.2f}")
c = Carrinho()
c.adicionar("Caneta", 2.50)
c.adicionar("Caderno", 18.90)
c.mostrar()