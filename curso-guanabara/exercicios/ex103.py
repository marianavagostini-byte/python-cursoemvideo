# ex103
# Fonte: Curso em Vídeo / prática (seu código)

numeros=[]
maiores10=[]
menores10=[]
for c in range (1,7):
    while True:
        try:
            valor=int(input(f'Digite o [{c}] valor: '))
            numeros.append(valor)
            break
        except ValueError:
            print('Digite apenas numero !!')
    if valor <=10:
        menores10.append(valor)
    else:
        maiores10.append(valor)

print(f'A quantia de numeros acima de 10 sao: {len(maiores10)}',end='')
print(f' e os valores sao: {maiores10}')
print(f'A quantia de numeros abaixo de 10 sao: {len(menores10)}',end='')
print(f' e os valores sao: {menores10}')
