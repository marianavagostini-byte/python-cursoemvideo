# ex093 - Menu com 4 opções
# Fonte: Extra - fora do curso (seu código / variação)

n1=int(input('Digite o 1 numero:  '))
n2=int(input('Digite o 2 numero: '))
opcao=0
while opcao !=4:
    print('''          [1] SOMA  
          [2] MULTIPLICA
          [3] NOVOS NUMEROS
          [4] SAIR''')
    opcao=int(input('Qual a sua opcao? '))
    if opcao ==1:
        soma=n1+n2
        print(f'A soma de {n1} + {n2} = {soma}')
    elif opcao ==2:
        multi=n1*n2
        print(f'A multiplicacao de {n1} x {n2} = {multi}')
    elif opcao ==3:
        print('Digite os novos numeros ..')
        n1=int(input('Numero 1: '))
        n2=int(input('Numero 2: '))
    elif opcao ==4:
        print('Desligando programa..')
    else:
        print('Resposta invalida, tente novamente...')
        opcao=int(input('Qual a sua opcao?'))
print('Programa finalizado..')
