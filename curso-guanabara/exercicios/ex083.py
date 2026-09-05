# ex083 - Menu de opções (primeira versão)
# Fonte: Extra - fora do curso (seu código / variação)

from time import sleep
opcao=soma=0
n1=float(input('Digite um valor:  '))
n2=float(input('Digite outro valor: '))
print('''
[1] - SOMAR
[2] - MULTIPLICAR
[3] - MAIOR
[4] - NOVOS NÚMEROS
[5] - SAIR DO PROGRAMA
''')
while opcao != 5:
    opcao=int(input('Qual a sua escolha ? '))
    if opcao ==1:
        soma=n1+n2
        print(f'A soma dos dois numeros foi: {soma:.1f}')
    elif opcao ==2:
        multiplica=n1*n2
        print(f'A multiplicacao resultou: {multiplica}')
    elif opcao ==3:
        if n1>n2:
            print(f'O {n1} e maior que {n2}')
        if n1<n2:
            print(f'O {n2} e maior que {n1}')
        else:
            print('os valores sao iguais !!')
    elif opcao ==4:
        print('Informe novos numeros : ')
        n11=float(input('Digite um valor: '))
        n22=float(input('Digite outro valor:  '))
    elif opcao ==5:
        print('Finalizando o programa ..')
    else:
        print('Opcao invalida')
