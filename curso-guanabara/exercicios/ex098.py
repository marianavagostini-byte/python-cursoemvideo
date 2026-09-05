# ex098
# Fonte: Curso em Vídeo / prática (seu código)

valores=[]
while True:
    valor=int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
    else:
        print('Valor duplicado, tente novamente outro numero..')
    resp=input('Deseja continuar [S/N] ?  ').upper().strip()
    if resp =='N':
        break
valores.sort()
print(f'Os valores digitados foram: {valores}')
print(f'E a soma deles e: {sum(valores)}')
