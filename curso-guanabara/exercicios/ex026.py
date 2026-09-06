# ex026 - Primeira e Última Ocorrência de uma String
# Fonte: Curso em Vídeo - desafio oficial (complementado)

frase = input('Digite uma frase: ').strip().upper()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A') + 1))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A') + 1))
