# ex081 - Adivinhação com contador de tentativas
# Fonte: Extra - fora do curso (seu código / variação)

from time import sleep
from random import randint
tentativas=0

computador=randint(0,10)
print('Vou pensar em um numero entre 0 e 10, tente advinhar... ')
sleep(2)

jogador=int(input('Pensou em qual numero?  '))

while jogador != computador:
        print('PROCESSANDO...')
        sleep(0.5)
        print('Numero ERRADO, tente novamente...')
        sleep(0.5)
        jogador=int(input('Qual o seu novo palpite? '))
        tentativas+=1
print('PROCESSANDO..')
sleep(1)
print('PARABENS, voce acertou o numero !!!')
