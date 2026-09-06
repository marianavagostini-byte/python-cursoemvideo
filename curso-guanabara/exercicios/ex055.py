# ex055 - Maior e Menor da Sequência
# Fonte: Curso em Vídeo - desafio oficial (seu código)

for c in range(1,6):
    peso=float(input('Peso da {} pessoa: '.format(c)))
    if c ==1:
        maior=peso
        menor=peso
    else:
        if peso > maior:
            maior=peso
        if peso < menor:
            menor=peso
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')
