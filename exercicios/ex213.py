from hashlib import sha256
from pwinput import pwinput


class CartaoDeCredito:
    def __init__(self, titular: str, limite: float = 1000.0, chave: str = None):
        self._titular = titular
        self._limite_total = float(abs(limite))
        self.__fatura_atual = 0.0

        if chave is None:
            chave = self._pede_senha()
        self.__hash = sha256(chave.encode()).hexdigest()

        self.fatura = []
        print(f"Cartão de {self._titular} emitido com limite de R$ {self._limite_total:,.2f}")

    def _pede_senha(self) -> str:
        while True:
            senha = str(pwinput("Digite a senha do cartão (4 dígitos): ")).strip()
            if len(senha) == 4 and senha.isdigit():
                break
            print("A senha deve conter exatamente 4 dígitos numéricos.")
        return senha

    def validar_senha(self, chave: str) -> bool:
        return sha256(chave.encode()).hexdigest() == self.__hash

    def comprar(self, estabelecimento: str, valor: float, chave: str = None):
        valor = abs(valor)
        if valor <= 0:
            print("Valor de compra inválido.")
            return

        if chave is None:
            chave = self._pede_senha()

        if not self.validar_senha(chave):
            print("Senha incorreta! Transação negada pela operadora.")
            return

        limite_disponivel = self._limite_total - self.__fatura_atual
        if valor > limite_disponivel:
            print(f"Compra NEGADA de R$ {valor:,.2f}: limite insuficiente (disponível: R$ {limite_disponivel:,.2f}).")
        else:
            self.__fatura_atual += valor
            self.fatura.append({"estabelecimento": estabelecimento.strip(), "valor": valor})
            print(f"Compra de R$ {valor:,.2f} aprovada em '{estabelecimento}'.")

    def pagar_fatura(self, valor: float):
        valor = abs(valor)
        if valor <= 0:
            print("Valor de pagamento inválido.")
            return

        if valor > self.__fatura_atual:
            print(f"Pagamento excede a fatura atual de R$ {self.__fatura_atual:,.2f}.")
            return

        self.__fatura_atual -= valor
        print(f"Pagamento de R$ {valor:,.2f} efetuado. Fatura restante: R$ {self.__fatura_atual:,.2f}")

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, novo_nome: str):
        chave = self._pede_senha()
        if self.validar_senha(chave):
            if novo_nome and len(novo_nome.strip()) >= 5:
                self._titular = novo_nome.strip()
                print(f"Nome do titular alterado com sucesso para {self._titular}.")
            else:
                print("Nome muito curto. Digite pelo menos 5 caracteres.")
        else:
            print("Senha incorreta! Alteração de cadastro bloqueada.")

    def total_gasto(self) -> float:
        return sum(item["valor"] for item in self.fatura)

    def ver_extrato_fatura(self):
        print(f"\n--- Fatura Aberta: {self._titular} ---")
        if not self.fatura:
            print("Nenhuma compra realizada no ciclo atual.")
        else:
            for item in self.fatura:
                print(f"- {item['estabelecimento']}: R$ {item['valor']:,.2f}")
        print(f"Total da fatura atual: R$ {self.__fatura_atual:,.2f}")
        limite_livre = self._limite_total - self.__fatura_atual
        print(f"Limite disponível: R$ {limite_livre:,.2f}\n")


if __name__ == "__main__":
    meu_cartao = CartaoDeCredito(titular="Mariana", limite=2500)
    meu_cartao.comprar("Supermercado", 180.50)
    meu_cartao.comprar("Livraria", 95.00)
    meu_cartao.ver_extrato_fatura()
    meu_cartao.pagar_fatura(100.00)