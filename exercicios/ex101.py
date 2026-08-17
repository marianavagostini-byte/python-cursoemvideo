# ex101
# Fonte: Curso em Vídeo / prática (seu código)

expressao = input('Digite a expressão: ')
contador = 0
for letra in expressao:
    if letra == '(':
        contador += 1
    elif letra == ')':
        contador -= 1
    if contador < 0:
        break
if contador == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')
