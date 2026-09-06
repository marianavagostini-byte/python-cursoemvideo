# ex079 - Jokenpô (versão 1 a 3)
# Fonte: Extra - fora do curso (seu código / variação)

from random import randint 
computador = randint(1,3)
jogador=int(input('Escolha um numero - [1]pedra  [2]papel  [3]tesoura: '))
print(f'   Computador: {computador}    |    jogador:  {jogador}')
if computador == 1:
    if jogador== 1:
        print('EMPATE!!')
    elif jogador ==2:
        print('Voce venceu, papel ganha da pedra')
    elif jogador ==3: 
        print('Voce perdeu, tesoura perde da pedra')
if computador == 2:
    if jogador == 2:
        print('EMPATE')
    if jogador == 3:
        print('GANHOU, tesoura ganha do papel ')
    if jogador ==1:
        print('PERDEU, pedra nao mata papel  ')
if computador ==3:
    if jogador ==3:
        print('EMPATE')
    if jogador ==1:
        print('GANHOU, pedra mata tesoura')
    if jogador ==2:
        print('GANHOU, papel mata pedra')
