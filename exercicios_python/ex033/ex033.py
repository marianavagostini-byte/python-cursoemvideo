# ex033 - Maior e Menor Valores
# Fonte: Curso em Vídeo - desafio oficial (seu código)

a=int(input('Digite o primeiro valor: '))
b=int(input('Digite o segundo valor:'))
c=int(input('Digite o terceiro valor:'))
menor=a
if b < a and b < c:
    menor=b
if c < a and c < b:
    menor=c
maior=a
if b > a and b > c:
    maior=b
if c > a and c > b:
    maior=c
print('O menor valor digitado e: {}\n'.format(menor))
print('O maior valor digitado e: {}\n '.format(maior))
