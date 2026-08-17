# ex041 - Classificando Atletas
# Fonte: Curso em Vídeo - desafio oficial (seu código)

ano=int(input('Qual o ano de nascimento do atleta? '))
idade=2026-ano
print(f'Sua idade e {idade} anos')
if idade <=9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <=19:
    print('JUNIOR')
elif idade <=20:
    print('SENIOR')
elif idade >20:
    print('MASTER')
