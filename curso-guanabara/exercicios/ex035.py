# ex035 - Analisando Triângulo v1.0
# Fonte: Curso em Vídeo - desafio oficial (seu código)

r1=float(input('Primeiro segmento: '))
r2=float(input('Segundo segmento: '))
r3=float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos acima \33[32mPODEM FORMAR\33[m um triangulo')
else:
    print('\33[31mNAO\33[m podem formar um triangulo')
