# ex131
# Fonte: Curso em Vídeo / prática (seu código)

lista=[]
while True:
    nome=input('Nome filme: ')
    notap=float(input('Nota publico [de 0 a 10]: '))
    notac=float(input('Nota critica [de 0 a 10: '))
    media=(notac+notap)/2
    lista.append([nome,[notap,notac],media])
    respo=input('Deseja continuar? [S/N]')
    if respo.upper()=='N':
        break

for c in lista:

    print(f'Filme: {c[0]} - media: {c[2]}')

while True:
    opc=int(input('Qual filme? [digite 999 para parar]: '))
    if opc == 999:
        break
    print(f'Filme: {lista[opc][0]} - notas: {lista[opc][1]} - media:{lista[opc][2]}')
