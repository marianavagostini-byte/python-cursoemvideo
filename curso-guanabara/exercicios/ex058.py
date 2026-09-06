# ex058 - Jogo da Adivinhação v2.0
# Fonte: Curso em Vídeo - desafio oficial (seu código)

from random import randint
computador=randint(0,10)
print('Eu sou o computador e acabei de pensar em um numero entre 0 e 10 ...')
print('Sera se voce vai acertar o meu numero? ...')
acerto=False
tentativa=0
while not acerto:
    jogador=int(input('Qual o seu palpite?  '))
    tentativa+=1
    if jogador == computador:
        acerto=True
        print('Parabens voce acertou o numero')
    else:
        if jogador < computador:
            print('Mais...')
        if jogador > computador:
            print('Menos...')
print(f'O seu total de tentativas foi: {tentativa}')
