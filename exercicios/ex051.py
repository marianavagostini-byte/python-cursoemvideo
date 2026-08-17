# ex051 - Progressão Aritmética v1.0
# Fonte: Curso em Vídeo - desafio oficial (complementado)

print('-' * 30)
print('   10 TERMOS DE UMA P.A.')
print('-' * 30)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da P.A.: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU')
