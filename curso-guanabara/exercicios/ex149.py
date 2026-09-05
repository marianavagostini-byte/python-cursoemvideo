# ex149
# Fonte: Curso em Vídeo / prática (seu código)

dados={}
lista=[]
dados['nome']=input('Nome do aluno: ')
tot=int(input(f'Quantas provas {dados["nome"]} fez? '))
for c in range(0,tot):
    lista.append(int(input(f'Nota da prova {c+1}: ')))
dados['notas']=lista[:]
dados['media']= sum(dados['notas']) / len(dados['notas'])
for i,v in enumerate(dados['notas']):
    print(f'  => Na prova {i+1} - tirou {v}')
print(f'A media foi {dados["media"]}')
if dados['media'] >= 7:
    print(f'{dados["nome"]} esta APROVADO')
elif dados['media'] >= 5:
    print(f'{dados["nome"]} esta de RECUPERACAO')
else:
    print(f'{dados["nome"]} REPROVOU')
