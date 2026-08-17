# ex122
# Fonte: Curso em Vídeo / prática (seu código)

from random import randint
lista_20=[]
equipes=int(input('Quantas equipes? '))
alunos=int(input('Quantos alunos por equipe? '))
for c in range(equipes):
    lista=[]
    while len(lista) < alunos:
        num=randint(1,20)
        if num not in lista:
            lista.append(num)
    lista.sort()
    lista_20.append(lista[:])
for c in range(len(lista_20)):
    print(f'{c +1} - {lista_20[c]}')
