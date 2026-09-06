# ex112
# Fonte: Curso em Vídeo / prática (seu código)

lista=list()
dados=list()
maior=0
while True:
    dados.append(input('Nome: '))
    dados.append(int(input('Peso: ')))
    lista.append(dados[:])
    dados.clear()
    resp=input('Deseja continuar [S/N] ? ')
    if resp.upper()=='N':
        break
menor=lista[0][1]

for p in lista:
    print(f'Foram cadastradas = {p[0]} com o peso: {p[1]} kg.')
for p in lista:
    if p[1] > maior:
        maior =p[1]
    elif p[1] < menor:
        menor=p[1]
print('Pessoas mais pesadas:')
for p in lista:
    if p[1]==maior:
        print(f'  {p[0]} com {p[1]} kg.')
print('pessoas mais leves:')
for p in lista:
    if p[1]==menor:
        print(f'  {p[0]} com {p[1]} kg.')
print(f'Foram cadastradas {len(lista)} pessoas.')
