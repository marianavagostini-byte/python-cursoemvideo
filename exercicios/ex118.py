# ex118
# Fonte: Curso em Vídeo / prática (seu código)

lista=[[ ], [ ] ]
valor=0
for c in range (1,8):
    valor=int(input(f'Digite o [{c}] numero: '))
    if valor %2==0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista.sort()
print(f'Os valores pares sao:{lista[0]} ')
print(f'Os valores impares sao: {lista[1]}')
