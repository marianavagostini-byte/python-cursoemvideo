# ex125
# Fonte: Curso em Vídeo / prática (seu código)

from random import randint 
quant=int(input('Quantas placas? '))

todas_placas=[]

for c in range(quant):
    placa=[]

    while len(placa) < 4:
        num=randint(0,9)
        if num not in placa:
            placa.append(num)
    placa.sort()
    todas_placas.append(placa[:])
for c in range(len(todas_placas)):
    print(f'{c+1} - {todas_placas[c]}')
