class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1
        print(f"Parabéns {self.nome}! Agora você tem {self.idade} anos.")

    def detalhar(self):
        print(f"Nome: {self.nome} | Idade: {self.idade}")


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.curso = curso

    def pagar_mensalidade(self):
        print(f"Mensalidade do aluno(a) {self.nome} paga com sucesso!")

    def detalhar(self):
        super().detalhar()
        print(f"Matrícula: {self.matricula} | Curso: {self.curso}")


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, salario):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.salario = salario

    def receber_aumento(self, valor):
        self.salario += valor
        print(f"O professor {self.nome} recebeu um aumento de R$ {valor:.2f}. Salário atual: R$ {self.salario:.2f}")

    def detalhar(self):
        super().detalhar()
        print(f"Especialidade: {self.especialidade} | Salário: R$ {self.salario:.2f}")



if __name__ == "__main__":
    aluno1 = Aluno("Ana Clara", 17, "2024A10", "Desenvolvimento de Sistemas")
    prof1 = Professor("Carlos Silva", 42, "Programação Python", 4500.0)

    print("--- Dados do Aluno ---")
    aluno1.detalhar()
    aluno1.pagar_mensalidade()
    aluno1.fazer_aniversario()

    print("\n--- Dados do Professor ---")
    prof1.detalhar()
    prof1.receber_aumento(800.0)