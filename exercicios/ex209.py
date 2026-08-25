from rich import print
from rich.panel import Panel
from rich import box

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        preco_formatado = f"R${self.preco:,.2f}"
        linha_nome = f"{self.nome:^30}"
        linha_tracejada = "-" * 30
        linha_preco = f"{preco_formatado:.^30}"

        conteudo = f"{linha_nome}\n{linha_tracejada}\n{linha_preco}"

        print(Panel(conteudo, title="Produto", box=box.ROUNDED, expand=False))


 
p1 = Produto("iPhone 17 Pro Max", 25000.85)
p2 = Produto("Mouse", 120)

p1.etiqueta()
p2.etiqueta()