# ex040 - Aquele Clássico da Média
# Fonte: Curso em Vídeo - desafio oficial (seu código)

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
print(f'Sua média foi: {media:.1f}')
if media < 5.0:
    print('Sua média foi abaixo de 5.0, REPROVADO!!')
elif 5.0 <= media <= 6.9:
    print('Sua média foi entre 5.0 e 6.9, RECUPERAÇÃO!!')
else:
    print('Sua média foi 7.0 ou superior, APROVADO!!')
