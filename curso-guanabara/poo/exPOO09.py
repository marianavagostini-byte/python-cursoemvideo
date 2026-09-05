from rich import print

class Diario:
    def __init__(self,senhamestra = 123):
        self.__segredos = []
        self.__senha = senhamestra
        
    def escrever(self, msg):
        if isinstance(msg , str) and len(msg) > 0:
            self.__segredos.append(msg)
    
    def ler(self, senha = None):
        if senha != self.__senha:
            raise PermissionError("[red]Senha invalida ![/]")
        else:
            print("[green]Diario LIBERADO[/]")
            for segredo in self.__segredos:
                print(f'- {segredo}')
    
    @property
    def senha(self):
        raise PermissionError(f"[red]Ninguem tem a permissao de ver a senha[/]")