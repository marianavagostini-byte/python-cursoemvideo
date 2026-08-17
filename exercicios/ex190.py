# ex190 - Desafio 108: Funcao moeda()
# Fonte: Curso em Vídeo - desafio oficial (complementado)

from moeda import metade, dobro, aumentar, diminuir, moeda

num = float(input('Digite um preço: R$ '))
print(f'A metade de {moeda(num)} é {metade(num, True)}')
print(f'O dobro de {moeda(num)} é {dobro(num, True)}')
print(f'Aumentando 10% temos {aumentar(num, 10,True)}')
print(f'Reduzindo 13% temos {diminuir(num, 13,True)}')