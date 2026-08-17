# ex189 - Desafio 107: Modulo moeda
# Fonte: Curso em Vídeo - desafio oficial (seu código)

from moeda import metade, dobro , aumentar , diminuir

num=float(input('digite um preco: '))
print(f'A metade de {num} e {metade(num)} ')
print(f'O dobro de {num} e {dobro(num)}')
print(f'Aumentando 10% temos {aumentar(num,10)}')
print(f'Reduzindo 13% temos {diminuir(num,13)}')