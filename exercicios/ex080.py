# ex080 - Categorias de natação (versão com date.today)
# Fonte: Extra - fora do curso (seu código / variação)

from datetime import date

atual = date.today().year 

nascimento = int(input('Qual a sua data de nascimento?  '))

idade = atual - nascimento 

if idade <=9:
    categoria=('MIRIM')
elif idade <=14:
    categoria=('INFANTIL')
elif idade <=19:
    categoria=('JUNIOR')
elif idade <=25:
    categoria=('SENIOR')
else:
    categoria=int(input('MASTER'))

print(f'Voce tem {idade} anos, por isso compete na categoria: {categoria}')
