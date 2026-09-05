# ex121
# Fonte: Curso em Vídeo / prática (seu código)

from random import randint 
quant=int(input('Quantos jogos? '))
todos_jogos=[]
for c in range(quant):
    jogos=[]
    while len(jogos)<6:
        numeros=randint(1,60)
        if numeros not in jogos:
            jogos.append(numeros)
    jogos.sort()
    todos_jogos.append(jogos)
for c in range(len(todos_jogos)):
    print(f'{c +1} - {todos_jogos[c]}')
