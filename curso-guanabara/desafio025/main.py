

from rich.console import Console
from rich.table import Table
from transportes import Moto, Caminhao, Drone


console = Console()

dist = 80
viagem = [Moto(dist), Caminhao(dist), Drone(dist)]

tabela = Table(title='Tabela de Fretes')
tabela.add_column('Distância')
tabela.add_column('Tipo')
tabela.add_column('Frete')

for item in viagem:
	tabela.add_row(f'{dist}Km', type(item).__name__, f'{item.calc_frete()}')

console.print(tabela)