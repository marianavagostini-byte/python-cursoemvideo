# ex082 - Fatorial com while (versão manual)
# Fonte: Extra - fora do curso (seu código / variação)

numero=int(input('Escolha um numero para virar fatorial : '))
contador=numero
multiplicacao=1
while contador > 0:
    multiplicacao *=contador
    contador -=1
print(f'Seu numero {numero} vira {multiplicacao}')
