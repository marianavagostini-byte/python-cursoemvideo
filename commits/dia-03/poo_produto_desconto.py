class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        self.preco -= self.preco * percentual / 100


produto = Produto("Teclado", 200)

produto.aplicar_desconto(10)

print(f"Produto: {produto.nome}")
print(f"Preço final: R")
