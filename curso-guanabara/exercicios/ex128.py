# ex128
# Fonte: Curso em Vídeo / prática (seu código)

lista=[]
while True:
    nome=input('Nome: ')
    nota1=float(input('Nota 1: '))
    nota2=float(input('Nota 2: '))
    media=(nota1+nota2)/2
    lista.append([nome, [nota1,nota2],media])
    
    resp=input('Deseja continuar? [S/N]')
    if resp.upper()=='N':
        break

print('-=-=-=-=-= BOLETIM -=-=-=-=--')
for c in lista:

    print(f'Aluno(a): {c[0]} - nota: {c[2]}')

while True:
    opc=int(input('Escolha um aluno(a): (999 para parar)'))
    if opc ==999:
        break
    print(f'Nome: {lista[opc][0]} - notas: {lista[opc][1]}')
