# ex049 - A Tabuada v2.0
# Fonte: Curso em Vídeo - desafio oficial (seu código)

numero=int(input('Digite um numero e veja sua tabuada:  '))
for c in range (1,11):
    print( '{} x {} = {}'.format(numero,c,numero*c))
