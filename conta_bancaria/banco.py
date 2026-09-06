from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal, InvalidOperation


class OperacaoInvalida(ValueError):
    """Indica uma operação bancária que não pode ser realizada."""


@dataclass
class ContaBancaria:
    numero: int
    titular: str
    saldo: Decimal = Decimal("0.00")
    movimentacoes: list[str] = field(default_factory=list)

    def __post_init__(self):
        self.saldo = self._valor_monetario(self.saldo, permitir_zero=True)
        if not self.titular.strip():
            raise OperacaoInvalida("O nome do titular não pode ficar vazio.")

    @staticmethod
    def _valor_monetario(valor, permitir_zero=False):
        try:
            valor = Decimal(str(valor)).quantize(Decimal("0.01"))
        except (InvalidOperation, ValueError):
            raise OperacaoInvalida("Informe um valor monetário válido.")
        if valor < 0 or (valor == 0 and not permitir_zero):
            raise OperacaoInvalida("O valor deve ser maior que zero.")
        return valor

    def depositar(self, valor):
        valor = self._valor_monetario(valor)
        self.saldo += valor
        self._registrar(f"Depósito: +R$ {valor:.2f}")

    def sacar(self, valor):
        valor = self._valor_monetario(valor)
        if valor > self.saldo:
            raise OperacaoInvalida("Saldo insuficiente para realizar o saque.")
        self.saldo -= valor
        self._registrar(f"Saque: -R$ {valor:.2f}")

    def extrato(self):
        linhas = [f"Conta {self.numero} - {self.titular}", "-" * 40]
        linhas.extend(self.movimentacoes or ["Nenhuma movimentação realizada."])
        linhas.extend(("-" * 40, f"Saldo atual: R$ {self.saldo:.2f}"))
        return "\n".join(linhas)

    def _registrar(self, descricao):
        horario = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.movimentacoes.append(f"{horario} | {descricao}")


def encontrar_conta(contas, numero):
    for conta in contas:
        if conta.numero == numero:
            return conta
    raise OperacaoInvalida("Conta não encontrada.")
