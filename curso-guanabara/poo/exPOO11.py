from hashlib import sha256
from pwinput import pwinput


class ContaBancaria:
    def __init__(self, id, nome: str = None, saldo: float = 0, chave: str = None):
        self._titular = nome
        self._id = id
        self.__saldo = float(saldo)

        if chave is None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode()).hexdigest()

        self.extrato = []
        print(f"Conta {self._id} criada com sucesso. Saldo atual de R$ {self.__saldo:,.2f}")

    def pede_senha(self) -> str:
        while True:
            senha = str(pwinput("Senha: ")).strip()
            if len(senha) >= 6:
                break
            print("A senha deve conter no mínimo 6 caracteres.")
        return senha

    def validar_senha(self, chave: str) -> bool:
        usuario = sha256(chave.encode()).hexdigest()
        return usuario == self.__hash

    def depositar(self, valor: float):
        if valor <= 0:
            print("Valor inválido para depósito.")
            return

        self.__saldo += valor
        self.extrato.append({"tipo": "Depósito", "valor": valor})
        print(f"Depósito de R$ {valor:,.2f} realizado. Saldo atual: R$ {self.__saldo:,.2f}")

    def sacar(self, valor: float, chave: str = None):
        valor = abs(valor)
        if valor <= 0:
            print("Valor inválido para saque.")
            return

        if chave is None:
            chave = self.pede_senha()

        if not self.validar_senha(chave):
            print("Senha não confere. Saque não autorizado!")
            return

        if valor > self.__saldo:
            print(f"Saque NEGADO de R$ {valor:,.2f} na conta {self._id}: SALDO INSUFICIENTE")
        else:
            self.__saldo -= valor
            self.extrato.append({"tipo": "Saque", "valor": valor})
            print(f"Saque de R$ {valor:,.2f} autorizado. Saldo atual: R$ {self.__saldo:,.2f}")

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, novonome: str = None):
        chave = self.pede_senha()
        if self.validar_senha(chave):
            if novonome and len(novonome.strip()) >= 5:
                self._titular = novonome.strip()
                print(f"Nome alterado com sucesso para {self._titular}.")
            else:
                print("Nome inválido. Deve ter pelo menos 5 caracteres.")
        else:
            print("Senha não confere. Não posso alterar o nome.")

    def total_movimentado(self) -> float:
        return sum(item["valor"] for item in self.extrato)

    def mostrar_extrato(self):
        print(f"\nExtrato: {self._titular} — Conta nº {self._id}")
        if not self.extrato:
            print("Nenhuma movimentação realizada.")
        else:
            for item in self.extrato:
                print(f"{item['tipo']}: R$ {item['valor']:,.2f}")
        print(f"Saldo final: R$ {self.__saldo:,.2f}\n")