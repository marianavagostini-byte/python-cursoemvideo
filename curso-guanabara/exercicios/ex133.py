# ex133
# Fonte: Curso em Vídeo / prática (seu código)

aluno={}
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))

if aluno ['media'] >=6:
    aluno["situacao"] = 'Aprovado'
elif aluno ['media'] >=5:
    aluno['situacao'] = 'Reprovado'
else:
    aluno ['situacao'] = 'Reprovado'

print()
print(f'Nome: {aluno["nome"]}')
print(f'Media de {aluno["nome"]}: {aluno["media"]}')

for chave , valor in aluno.items():
    print(f'{chave} e igual a {valor}')
