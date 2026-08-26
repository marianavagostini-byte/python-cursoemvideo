from rich import print 
from rich.panel import Panel
from rich import box

class Gamer:
    def __init__(self, nome: str, nick: str):
        self.nome = nome
        self.nick = nick
        self.jogos = []

    def add_favoritos(self, jogo: str):
        self.jogos.append(jogo)

    def ficha(self):
        conteudo = f"Nome real [bold on blue] {self.nome} [/]\n"
        conteudo += "Jogos favoritos: \n"
        
        for jogo in sorted(self.jogos):
            conteudo += f" :video_game: [blue]{jogo}[/]\n"
        
        painel = Panel(
            conteudo.strip(),
            title=f"Jogador <{self.nick}>",
            box=box.ROUNDED,
            expand=False
        )
        print(painel)


j1 = Gamer('Mariana', 'MVA157')
j1.add_favoritos('Fortnite')
j1.add_favoritos('Rainbow Six Siege')
j1.add_favoritos('Paladins')
j1.ficha()