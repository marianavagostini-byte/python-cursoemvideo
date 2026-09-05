# ex113
# Fonte: Curso em Vídeo / prática (seu código)

nomes = []
pesos = []
while True:
    n = input('Nome: ')
    if n.upper() == 'SAIR':
        break
    p = int(input('Peso: '))
    nomes.append(n)
    pesos.append(p)
print(f'Foram cadastradas {len(nomes)} pessoas.')
for i in range(len(nomes)):
    print(f'{nomes[i]} pesa {pesos[i]} kg.')
maior = max(pesos)
print(f'Pessoas mais pesadas ({maior} kg): ', end='')
for i in range(len(pesos)):
    if pesos[i] == maior:
        print(f'[{nomes[i]}] ', end='')
print()
menor = min(pesos)
print(f'Pessoas mais leves ({menor} kg): ', end='')
for i in range(len(pesos)):
    if pesos[i] == menor:
        print(f'[{nomes[i]}] ', end='')
print()
