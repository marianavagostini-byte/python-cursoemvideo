# ex071 - Simulador de Caixa Eletrônico
# Fonte: Curso em Vídeo - desafio oficial (seu código)

valor=int(input('Qual o valor a ser sacado? '))
cedula=50
totced=0
total=valor
while True:
    if total >= cedula:
        total-=cedula
        totced+=1
    else:
        if totced >0:
            print(f'Total de {totced} cedula de R$ {cedula}')
        if cedula ==50:
            cedula=20
        elif cedula ==20:
            cedula= 10
        elif cedula ==10:
            cedula=1
        totced=0
        if total ==0:
            break
