class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aplicar_aumento(self, percentual):
        aumento = self.salario * (percentual / 100)
        self.salario += aumento

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R$ {self.salario:.2f}")


funcionario = Funcionario("Mariana", 3000)

funcionario.aplicar_aumento(10)
funcionario.mostrar_dados()
