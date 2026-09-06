# ex117
# Fonte: Curso em Vídeo / prática (seu código)

principal=[]
temporaria=[]
maior=menor=0
linha=('-='*40)
while True:
    temporaria.append(str(input('Nome: ')))
    temporaria.append(float(input('Peso: ')))
    if len(principal)==0:
        maior=menor=temporaria[1]
    else:
        if temporaria[1] < menor:
            menor=temporaria[1]
        if temporaria[1] > maior:
            maior=temporaria[1]

    principal.append(temporaria[:])
    temporaria.clear()
    resp=str(input('Deseja continuar? [S/N]'))
    if resp.upper()=='N':
            break
if len(principal)==0:
    print('Ninguem cadastrado')
else:

    print(f'Foram cadastradas {len(principal)} pessoas.')
print(linha)
for p in principal:
    print(f' {p[0]} - peso: {p[1]}Kg.')
print(linha)
for p in principal:
    if p[1] == maior:
        print(f'As pessoas mais pesadas sao: {p[0]} - com {maior}Kg.')
print(linha)
for p in principal:
    if p[1] == menor:
        print(f'As pessoas mais leves sao: {p[0]} - com {menor}Kg')
print(linha)
