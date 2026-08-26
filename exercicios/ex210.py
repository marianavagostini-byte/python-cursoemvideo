from rich import print
from rich.panel import Panel
from rich.align import Align
from rich import box

class Churrasco:
    # Atributos de Classe
    consumo_padrao: float = 0.400  # 400g por pessoa
    preco_kg: float = 82.40        # R$82.40 por Kg

    def __init__(self, titulo: str, quant: int):
        self.titulo = titulo
        self.participantes = quant

    def __str__(self):
        carne_total = self.participantes * Churrasco.consumo_padrao
        custo_total = carne_total * Churrasco.preco_kg
        custo_pessoa = custo_total / self.participantes

        conteudo = (
            f"Analisando [bold green]{self.titulo}[/] com [cyan]{self.participantes}[/] convidados\n"
            f"Cada participante comerá {Churrasco.consumo_padrao}Kg e cada Kg custa R${Churrasco.preco_kg:.2f}\n"
            f"Recomendo [blue]comprar {carne_total:.3f}Kg[/blue] de carne\n"
            f"O custo total será de [green]R${custo_total:.2f}[/green]\n"
            f"Cada pessoa pagará [yellow]R${custo_pessoa:.2f}[/yellow] para participar."
        )

        painel = Panel(
            conteudo,
            title=self.titulo,
            box=box.ROUNDED,
            expand=False  # Faz a moldura abraçar o texto
        )

        return painel


# Teste:
churras = Churrasco("Churras dos Jv", 15)
print(churras.__str__())  # ou simplesmente: print(churras)