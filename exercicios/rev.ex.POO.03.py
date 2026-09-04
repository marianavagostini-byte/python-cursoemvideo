from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor: float):
        self.valor = valor

    @abstractmethod
    def processar(self):
        pass


class CartaoCredito(Pagamento):
    def __init__(self, valor: float, taxa_percentual: float):
        super().__init__(valor)
        self.taxa_percentual = taxa_percentual

    def processar(self):
        acrescimo = self.valor * (self.taxa_percentual / 100)
        total = self.valor + acrescimo
        print(f"Pagamento Cartão: R$ {self.valor:.2f} + taxa R$ {acrescimo:.2f} = Total: R$ {total:.2f}")


class Pix(Pagamento):
    def __init__(self, valor: float):
        super().__init__(valor)

    def processar(self):
        desconto = self.valor * 0.05
        total = self.valor - desconto
        print(f"Pagamento PIX: R$ {self.valor:.2f} - desconto R$ {desconto:.2f} = Total: R$ {total:.2f}")


pagamentos = [
    CartaoCredito(valor=100.0, taxa_percentual=10.0),
    Pix(valor=100.0)
]

for pag in pagamentos:
    pag.processar()