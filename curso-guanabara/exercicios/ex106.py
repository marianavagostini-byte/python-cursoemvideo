# ex106
# Fonte: Curso em Vídeo / prática (seu código)

numeros=[]
for c in range(1,6):
    n=int(input(f'Digite o {c} numero: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('esse numero ja foi digitado! Tente outro numero.')
pares=[]
impares=[]
for n in numeros:
    if n %2==0:
        pares.append(n)
    else:
        impares.append(n)
print(f'Os numeros pares digitados foram: {pares}')
print(f'Os numeros impares digitados foram: {impares}')
