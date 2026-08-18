# ex190 - Desafio 108: Funcao moeda()
# Fonte: Curso em Vídeo - desafio oficial (complementado)

from moeda import metade, dobro, aumentar, diminuir, moeda

num = float(input('Digite um preço: R$ '))
print(f'A metade de {moeda(num)} é {moeda(metade(num))}')
print(f'O dobro de {moeda(num)} é {moeda(dobro(num))}')
print(f'Aumentando 10% temos {moeda(aumentar(num, 10))}')
print(f'Reduzindo 13% temos {moeda(diminuir(num, 13))}')