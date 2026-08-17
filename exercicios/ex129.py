# ex129
# Fonte: Curso em Vídeo / prática (seu código)

lista=[]
while True:
    nome=input('Nome: ')
    salario1=float(input('Salario mes 1: '))
    salario2=float(input('Salario mes 2: '))
    media=(salario1+salario2)/2
    lista.append([nome,[salario1,salario2],media])
    resp=input('Deseja continuar? [S/N]')
    if resp.upper()=='N':
        break
for c in lista:

    print(f'funcionario(a): {c[0]} - media salario: {c[2]:.2f}')

while True:
    opc=int(input('Qual funcionario ? (999 - para sair)'))
    if opc == 999:
            break
    print(f'Nome: {lista[opc][0]}')
    print(f'Salario: {lista[opc][1]}')
    print(f'Media : {lista[opc][2]}')
