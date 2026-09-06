# ex137
# Fonte: Curso em Vídeo / prática (seu código)

from random import randint          # ferramenta de sorteio
from time import sleep              # ferramenta de pausa
from operator import itemgetter     # ferramenta de critério de ordenação

# "simule o lançamento de dados de 4 jogadores, guardando em um dicionário"
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

# mostrar o que cada um tirou
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

# "coloque esse dicionário em ordem" + "o vencedor tirou o maior número"
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('-=' * 30)
print(' == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
