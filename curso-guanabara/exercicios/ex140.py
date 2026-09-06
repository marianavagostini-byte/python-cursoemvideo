# ex140
# Fonte: Curso em Vídeo / prática (seu código)

dicionario={}
from operator import itemgetter
for c in range(1,5):
    nome=input('Nome do prato: ')
    dicionario[nome]=float(input(f'Preco da {nome}: '))

print('-=-=-=-=-CARDAPIO=-=-=-=-')
ranking=sorted(dicionario.items(),key=itemgetter(1))
for i,v in enumerate(ranking):
    print(f' {i +1} - {v[0]} - R$: {v[1]:.2f}')
