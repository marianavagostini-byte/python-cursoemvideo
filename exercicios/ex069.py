# ex069 - Análise de Dados do Grupo
# Fonte: Curso em Vídeo - desafio oficial (seu código)

pessoas18=homens=mulheres20=0
while True:
    idade=int(input('Qual a sua idade ?  '))
    sexo=str(input('Qual o seu sexo [M/F] ? ')).strip().upper()[0]
    continuar=str(input('Quer continuar [S/N] ? ')).strip().upper()[0]
    if continuar == 'N':
        print('Fim do programa.. ')
        break

    if idade >18:
        pessoas18+=1
    if sexo == 'M':
        homens+=1
    if sexo == 'F' and idade < 20:
        mulheres20+=1
print(f'Tem {pessoas18} pessoas maiores de 18 anos ..',end='')
print(f'Foram cadastrados {homens} homens..',end='')
print(f'Tem {mulheres20} mulheres abaixo de 20 anos')
