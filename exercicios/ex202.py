# revisao exercicio 07 - Jogo da adivinhação com histórico

from random import randint 
partidas=[]
while True:
    computador=randint(1,100)
    tentativas=0
    print('Pensei em um numero entre 1 e 100.. Tente advinhar !!')
    while True:
        try:
            jogador=int(input('Digite um numero: '))
        except ValueError:
            print('Valor invalido, digite novamente!')
            continue
        tentativas+=1
        if jogador < computador:
            print(f'E MAIOR que {jogador}')
        elif jogador > computador:
            print(f'E MENOR que {jogador}')
        else:
            print(f'GANHOU !! Escolhi o numero {jogador}, voce acertou em {tentativas} tentativas.')
            break
    partidas.append(tentativas)
    while True:
        resp=input('Deseja jogar novamente? [S/N]')
        if resp.upper()in['S','N']:
            break
    if resp.upper()=='N':
        break
print('-='*30)
print(f'Voce jogou {len(partidas)} partidas.')
print(f'Sua melhor partida foi com {min(partidas)} tentativas.')