# ex048 - Soma dos Ímpares Múltiplos de Três
# Fonte: Curso em Vídeo - desafio oficial (complementado)

soma = cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))
