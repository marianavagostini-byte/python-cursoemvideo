def analisar_aluno(aluno):
    media = sum(aluno["notas"]) / len(aluno["notas"])

    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    return media, situacao


aluno = {
    "nome": "Mariana",
    "notas": [8, 7, 9]
}

media, situacao = analisar_aluno(aluno)

print(f"Aluno: {aluno['nome']}")
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")
