from hashlib import sha256
from pwinput import pwinput


class CofreJogador:
    def __init__(self, jogador_id: int, dono: str, moedas: int = 0, chave: str = None):
        self._jogador_id = jogador_id
        self._dono = dono
        self.__ouro = max(0, moedas)

        if chave is None:
            chave = self._pede_codigo()
        self.__hash = sha256(chave.encode()).hexdigest()

        self.historico = []
        print(f"Cofre #{self._jogador_id} ativado para o aventureiro {self._dono}.")

    def _pede_codigo(self) -> str:
        while True:
            codigo = str(pwinput("Digite o código de acesso do cofre: ")).strip()
            if len(codigo) >= 4:
                break
            print("O código deve ter pelo menos 4 dígitos.")
        return codigo

    def validar_codigo(self, chave: str) -> bool:
        return sha256(chave.encode()).hexdigest() == self.__hash

    def guardar_ouro(self, quantidade: int):
        quantidade = abs(quantidade)
        if quantidade <= 0:
            print("Quantidade inválida para depósito.")
            return

        self.__ouro += quantidade
        self.historico.append({"tipo": "Depósito", "qtd": quantidade})
        print(f"{quantidade} moedas de ouro guardadas. Total no cofre: {self.__ouro}")

    def retirar_ouro(self, quantidade: int, chave: str = None):
        quantidade = abs(quantidade)
        if quantidade <= 0:
            print("Quantidade inválida para saque.")
            return

        if chave is None:
            chave = self._pede_codigo()

        if not self.validar_codigo(chave):
            print("Código incorreto! O alarme do cofre foi acionado.")
            return

        if quantidade > self.__ouro:
            print(f"Tentativa de saque negada: saldo insuficiente ({self.__ouro} moedas disponíveis).")
        else:
            self.__ouro -= quantidade
            self.historico.append({"tipo": "Saque", "qtd": quantidade})
            print(f"{quantidade} moedas retiradas. Restante: {self.__ouro}")

    @property
    def dono(self):
        return self._dono

    @dono.setter
    def dono(self, novo_dono: str):
        chave = self._pede_codigo()
        if self.validar_codigo(chave):
            if novo_dono and len(novo_dono.strip()) >= 3:
                self._dono = novo_dono.strip()
                print(f"Posse do cofre transferida para {self._dono}.")
            else:
                print("Nome de aventureiro inválido.")
        else:
            print("Código incorreto. A transferência de posse foi impedida.")

    def consultar_balanco(self):
        print(f"\n--- Extrato do Cofre #{self._jogador_id} ({self._dono}) ---")
        if not self.historico:
            print("Nenhuma movimentação registrada.")
        else:
            for acao in self.historico:
                print(f"{acao['tipo']}: {acao['qtd']} moedas")
        print(f"Saldo restante: {self.__ouro} moedas\n")



if __name__ == "__main__":
    bau = CofreJogador(jogador_id=101, dono="Geralt", moedas=500)
    bau.guardar_ouro(150)
    bau.retirar_ouro(100)
    bau.consultar_balanco()