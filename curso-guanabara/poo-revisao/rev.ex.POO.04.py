class Inventario:
    capacidade_maxima = 5

    def __init__(self):
        self.itens = []

    def coletar(self, nome: str, peso: float):
        if len(self.itens) >= Inventario.capacidade_maxima:
            print(f"Inventário cheio! Não é possível carregar '{nome}'.")
            return

        self.itens.append({"nome": nome, "peso": peso})
        print(f"Item '{nome}' coletado!")

    def peso_total(self):
        return sum(item["peso"] for item in self.itens)

    def listar_itens(self):
        if not self.itens:
            print("Inventário vazio.")
            return

        print("=== Itens na Mochila ===")
        for item in self.itens:
            print(f"- {item['nome']}: {item['peso']} kg")
        print("-" * 25)
        print(f"Peso Total: {self.peso_total():.1f} kg")


# Teste:
mochila = Inventario()
mochila.coletar("Espada", 3.5)
mochila.coletar("Poção", 0.5)
mochila.coletar("Escudo", 5.0)
mochila.listar_itens()