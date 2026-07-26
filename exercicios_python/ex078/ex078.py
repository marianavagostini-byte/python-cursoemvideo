# ex078 - Média com operador ternário
# Fonte: Extra - fora do curso (seu código / variação)

n1=float(input('Sua primeira nota foi: '))
n2=float(input('Sua segunda nota foi: '))
média = (n1+n2)/2
print('A sua média foi {:.1f}'.format(média))
print('Parabéns'if média>=6.0 else 'Recuperação')
