# ex036 - Aprovando Empréstimo
# Fonte: Curso em Vídeo - desafio oficial (seu código)

print('-='*20)
valorcasa=float(input('Qual o valor da casa? ').replace('.','').replace(',','.'))
print('-='*20)
salario=float(input("qual o salario do comprador? ").replace('.','').replace(',','.'))
print('-='*20)
anos=int(input('Em quantos anos vai pagar? '))
meses= anos * 12
prestacao= valorcasa / meses
limite= salario * 30 / 100
print('-='*20)
print('Para pagar uma casa de R${} em {} anos'.format(valorcasa,anos))
print('-='*20)
print('A prestacao sera de R${:.2f}'.format(prestacao))
print('-='*20)
if prestacao <= limite:
    print('Emprestimo \033[32m PODE SER \033[m concedido')
else:
    print('Emprestimo \033[31m NAO PODE \033[m ser concedido, exede 30% do seu salario ')
print('-='*20)
