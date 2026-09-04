class Livro:
    def __init__(self, titulo: str, autor: str, paginas_totais: int):
        self.titulo = titulo
        self.autor = autor
        self.paginas_totais = paginas_totais
        self.pagina_atual = 0

    def ler(self, paginas: int):
        self.pagina_atual += paginas
        if self.pagina_atual > self.paginas_totais:
            self.pagina_atual = self.paginas_totais
        print(f"Você está na página {self.pagina_atual} de {self.paginas_totais}.")

    def progresso(self):
        porcentagem = (self.pagina_atual / self.paginas_totais) * 100
        print(f"Progresso de '{self.titulo}': {porcentagem:.1f}% lido.")


meu_livro = Livro("O Hobbit", "J.R.R. Tolkien", 300)
meu_livro.ler(60)
meu_livro.progresso()
meu_livro.ler(300)
meu_livro.progresso()