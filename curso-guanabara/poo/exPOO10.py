from hashlib import sha256
from rich import print
from rich.console import Console

console = Console()


class Credencial:
    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, chave: str):
        if len(chave) > 0:
            self.__hash = sha256(chave.encode("utf-8")).hexdigest()
        else:
            raise ValueError("[red on white]Senha Inválida![/]")

    def validar(self, chave: str) -> bool:
        # Corrigido de 'uft-8' para 'utf-8'
        usuario = sha256(chave.encode("utf-8")).hexdigest()
        if usuario == self.__hash:
            print("[green on white]Senha correta![/]")
            return True
        else:
            print("[red]Senha inválida![/]")
            return False


