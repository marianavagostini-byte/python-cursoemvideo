# ex054 - Grupo da Maioridade
# Fonte: Curso em Vídeo - desafio oficial (seu código)

from datetime import date
ano = date.today().year
totmaior = 0
totmenor = 0
for c in range(1,8):
    nascimento=int(input(f'Em que ano a {c} pessoa nasceu?  '))
    idade = ano - nascimento 

    if idade >=21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maior de idade')
print(f'Ao todo tivemos {totmenor} pessoas menores de idade')
