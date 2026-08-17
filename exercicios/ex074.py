# ex074 - Maior e Menor Valores em Tupla
# Fonte: Curso em Vídeo - desafio oficial (seu código)

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os valores sorteados sao {numeros}',end='')
for n in numeros:
    print(f'{n}',end='')

print(f'\nO maior valor sorteado foi: {max(numeros)}')
print(f'\nO menor valor sorteado foi: {min(numeros)}')
