# ex135
# Fonte: Curso em Vídeo / prática (seu código)

aluno={}
aluno['nome']= str(input('Nome:  '))
aluno['media']=float(input(f'Media de {aluno["nome"]}  '))
if aluno ['media'] >=7:
    aluno['situacao']='Aprovado'
elif aluno ['media']<7:
    aluno['situacao']='Reprovado'
else:
    aluno['situacao']='Recuperacao'

for k,v in aluno.items():
    print(f'{k}: {v}')
