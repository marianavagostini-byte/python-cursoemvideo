# ex120
# Fonte: Curso em Vídeo / prática (seu código)

print()
print('-=-=-=-= MEGA SENA -=-=-=-=')
print()
from random import randint
palpite=int(input('Quer quantos palpites? '))
lista=[]

for p in range(palpite):
    jogo=[]
    while len(jogo)<6:
        num=randint(1,60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    lista.append(jogo)
for c in range (len(lista)):
    print(f'{c+1} - {lista[c]}')
