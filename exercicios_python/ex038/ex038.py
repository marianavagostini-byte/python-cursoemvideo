# ex038 - Comparando Números
# Fonte: Curso em Vídeo - desafio oficial (seu código)

n1=int(input('Digite um valor inteiro: '))
n2=int(input('Digite outro valor inteiro: '))
if n1 > n2:
    print('O \033[42mprimeiro\33[m valor e \33[32mMAIOR!!!\33[m]')
elif n2  > n1:
    print('O \033[42msegundo\33[m valor e \33[32mMAIOR!!!\33[m]')
elif n1 == n2:
    print('\033[31mNAO existe valor maior, sao IGUAIS!!!\33[m]')
