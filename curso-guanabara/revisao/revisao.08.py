from rich import print


class Semaforo:
    def __init__(self):
        self.sinal = "verde"

    def proximo(self):
        if self.sinal == "verde":
            self.sinal = "amarelo"
        elif self.sinal == "amarelo":
            self.sinal = "vermelho"
        elif self.sinal == "vermelho":
            self.sinal = "verde"

    def mostrar(self):
    
        cores = {
            "verde": "[green]verde[/]",
            "amarelo": "[yellow]amarelo[/]",
            "vermelho": "[red]vermelho[/]"
        }
        print(f"Sinal: {cores[self.sinal]}")


# Teste:
s1 = Semaforo()

s1.mostrar()   # Sinal: verde (colorido)
s1.proximo()
s1.mostrar()   # Sinal: amarelo (colorido)
s1.proximo()
s1.mostrar()   # Sinal: vermelho (colorido)
s1.proximo()
s1.mostrar()   # Sinal: verde (colorido)