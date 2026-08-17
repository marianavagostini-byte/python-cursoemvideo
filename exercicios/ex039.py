# ex039 - Alistamento Militar
# Fonte: Curso em Vídeo - desafio oficial (seu código)

ano = int(input('Em que ano voce nasceu ? '))
idade = 2026 - ano

# 1. Primeiro testamos a menor idade
if idade < 18:
    faltam = 18 - idade
    print('Você ainda não tem 18 anos mas faltam {} anos para conseguir se alistar!!!'.format(faltam))

# 2. Depois testamos a maior exceção (mais de 30 anos)
elif idade >= 30:
    print('Vish, mais de 30 anos la passou da idade!')

# 3. Depois os maiores de 18 genéricos (entre 19 e 29 anos)
elif idade > 18:
    print('Voce ja se alistou? Porque voce tem {} anos !!!'.format(idade))

# 4. E por fim, quem tem exatamente 18
elif idade == 18:
    print('Esta na hora de se alistar, 18 anos!!')
