# ex099
# Fonte: Curso em Vídeo / prática (seu código)

numeros=[]
while True:
    numeros.append(int(input('Digite um numero: ')))
    resp=input('Quer continuar [S/N] ? ').upper()
    if resp == 'N':
        break

print(f'Os numeros digitados foram: {numeros}')
print(f'Foram digitados {len(numeros)} numeros')
print(f'Decrescente: {sorted(numeros, reverse=True)}')
if 5 in numeros:
    print('Tem o numero 5 ')
else:
    print('Nao tem o numero 5')
