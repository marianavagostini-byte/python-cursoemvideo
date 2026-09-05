# ex059 - Criando um Menu de Opções
# Fonte: Curso em Vídeo - desafio oficial (seu código)

print('-='*20)
n1=float(input('Digite um numero:  '))
print('-='*20)
n2=float(input('Digite outro valor:  '))
print('-='*20)
opcao=0
while opcao !=5:
    print('''    [1] - SOMAR
    [2] - MULTIPLICAR
    [3] - MAIOR
    [4] - NOVOS NÚMEROS
    [5] - SAIR DO PROGRAMA''')
    print('-='*20)
    opcao=int(input('Qual a sua opcao ? '))
    print('-='*20)
    if opcao ==1:
        soma=n1+n2
        print(f'A soma de {n1} e {n2} e: {soma:.2f}')
        print('-='*20)
    elif opcao ==2:
        multiplicacao=n1*n2
        print(f'A multiplicacao entre {n1} e {n2} e: {multiplicacao}')
        print('-='*20)
    elif opcao ==3:
        if n1>n2:
            maior=n1
        else:
            maior=n2
        print(f'Entre {n1} e {n2} o maior e: {maior}')
        print('-='*20)
    elif opcao ==4:
        print('Informe os numeros novamente: ')
        n1=int(input('Primeiro valor:  '))
        n2=int(input('Segundo valor:  '))
    elif opcao ==5:
        print('Finalizando..')
    else:
        print('Incorreto, tente novamente')
print('Fim do programa!!')
