# ex045 - Gnabry, Pedra, Papel e Tesoura (Jokenpô)
# Fonte: Curso em Vídeo - desafio oficial (seu código)

from random import randint

computador = randint(0, 2)
jogador = int(input('Escolha (0=Pedra, 1=Papel, 2=Tesoura): '))

print(f'Computador: {computador} | Jogador: {jogador}')
print('---')

if computador == 0:  
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Você venceu! Papel ganha de Pedra.')
    elif jogador == 2:
        print('Computador venceu! Pedra ganha de Tesoura.')

elif computador == 1:  
    if jogador == 0:
        print('Computador venceu! Papel ganha de Pedra.')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Você venceu! Tesoura ganha de Papel.')

elif computador == 2:  
    if jogador == 0:
        print('Você venceu! Pedra ganha de Tesoura.')
    elif jogador == 1:
        print('Computador venceu! Tesoura ganha de Papel.')
    elif jogador == 2:
        print('Empate!')
