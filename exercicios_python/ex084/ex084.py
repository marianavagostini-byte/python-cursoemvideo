# ex084 - Adivinhação 'mais para cima'
# Fonte: Extra - fora do curso (seu código / variação)

from random import randint
from time import sleep
computador=randint(0,10)
sleep(2)
print('Sou seu computador... acabei de pensar em um numero entre 0 e 10..')
sleep(0.5)
print('Tente advinhar qual foi ..')
sleep(0.5)
jogador=int(input('Qual e o seu palpite ?  '))
sleep(0.5)
while jogador != computador:
        print(f'Errou...')
        if computador > jogador:
                print('Tente mais para cima...')
        jogador=int(input('Digite outro numero:  '))
print(f'ACERTOU !! Pensamos no numero: {computador}')
