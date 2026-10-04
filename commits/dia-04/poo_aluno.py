class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
        if self.calcular_media() >= 7:
            return "Aprovado"
        return "Reprovado"


aluno = Aluno("Mariana", [8, 7, 9])

print(f"Aluno: {aluno.nome}")
print(f"Média: {aluno.calcular_media():.2f}")
print(aluno.verificar_aprovacao())
