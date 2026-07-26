# ex061 - Progressão Aritmética v2.0
# Fonte: Curso em Vídeo - desafio oficial (complementado)

print('Gerador de P.A. (10 primeiros termos, usando while)')
print('-' * 30)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
