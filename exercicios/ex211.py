from hashlib import sha256
from pwinput import pwinput


class DiarioSecreto:
    def __init__(self, dono: str, titulo: str = "Meu Diário", chave: str = None):
        self._dono = dono
        self._titulo = titulo

        if chave is None:
            chave = self._pede_senha()
        self.__hash = sha256(chave.encode()).hexdigest()

        self.entradas = []
        print(f"Diário de {self._dono} inicializado com sucesso!")

    def _pede_senha(self) -> str:
        while True:
            senha = str(pwinput("Digite a senha do diário: ")).strip()
            if len(senha) >= 6:
                break
            print("A senha deve conter no mínimo 6 caracteres.")
        return senha

    def validar_senha(self, chave: str) -> bool:
        return sha256(chave.encode()).hexdigest() == self.__hash

    def adicionar_entrada(self, texto: str, chave: str = None):
        if chave is None:
            chave = self._pede_senha()

        if not self.validar_senha(chave):
            print("Senha incorreta! Não foi possível salvar a anotação.")
            return

        if not texto.strip():
            print("Anotação vazia não permitida.")
            return

        self.entradas.append({"conteudo": texto.strip(), "caracteres": len(texto.strip())})
        print("Nova anotação registrada com sucesso.")

    def ler_diario(self, chave: str = None):
        if chave is None:
            chave = self._pede_senha()

        if not self.validar_senha(chave):
            print("Acesso negado: senha incorreta.")
            return

        print(f"\n=== {self._titulo} ({self._dono}) ===")
        if not self.entradas:
            print("Nenhuma página escrita ainda.")
        else:
            for idx, item in enumerate(self.entradas, 1):
                print(f"Página {idx}: {item['conteudo']}")
        print("===============================\n")

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, novo_titulo: str):
        chave = self._pede_senha()
        if self.validar_senha(chave):
            if novo_titulo and len(novo_titulo.strip()) >= 3:
                self._titulo = novo_titulo.strip()
                print(f"Título alterado para: {self._titulo}")
            else:
                print("Título muito curto.")
        else:
            print("Senha incorreta! Alteração cancelada.")

    def total_caracteres_escritos(self) -> int:
        return sum(item["caracteres"] for item in self.entradas)


if __name__ == "__main__":
    meu_diario = DiarioSecreto(dono="Mari")
    meu_diario.adicionar_entrada("Hoje comecei a estudar programação orientada a objetos.")
    meu_diario.ler_diario()
    print(f"Total de caracteres escritos: {meu_diario.total_caracteres_escritos()}")