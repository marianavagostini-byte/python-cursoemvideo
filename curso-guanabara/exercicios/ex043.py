# ex043 - Índice de Massa Corporal (IMC)
# Fonte: Curso em Vídeo - desafio oficial (seu código)

peso=float(input('Qual o seu peso? '))
altura=float(input('Qual a sua altura? '))
imc= peso / ( altura ** 2 )
print(f'Seu IMC {imc:.1f}%')
if imc <18.5:
    print('esta abaixo do peso')
elif imc <25:
    print('Esta no peso ideal')
elif imc<30:
    print('Esta com sobrepeso')
elif imc <=40:
    print('Esta com obesidade')
else:
    print('Obesidade morbida')
