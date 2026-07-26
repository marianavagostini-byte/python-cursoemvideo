# ex034 - Aumentos Múltiplos
# Fonte: Curso em Vídeo - desafio oficial (seu código)

salario=float(input('Qual o valor do seu salario? R$ '))
if salario <= 1250:
    novo = salario + (salario*15/100)
else:
    novo= salario+(salario*10/100)
print('Quem ganhava {:.2f} reais passa a ganhar {:.2f} reais'.format(salario,novo))
