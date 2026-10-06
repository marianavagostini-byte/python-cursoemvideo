class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.05

    def mostrar_dados(self):
        bonus = self.calcular_bonus()

        print(f"Nome: {self.nome}")
        print(f"Salário: R$ {self.salario:.2f}")
        print(f"Bônus: R$ {bonus:.2f}")


class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.15


class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.10


funcionarios = [
    Funcionario("Ana", 3000),
    Gerente("Carlos", 7000),
    Desenvolvedor("Mariana", 6000)
]

for funcionario in funcionarios:
    funcionario.mostrar_dados()
    print("-" * 30)
