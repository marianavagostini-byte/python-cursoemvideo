# ex066 - Vários Valores com Flag (break)
# Fonte: Curso em Vídeo - desafio oficial (seu código)

sum = 0
c = 0

while True:
    n = int(input('Type a number [999 to stop]: '))
    if n == 999:
        break
    sum += n
    c += 1

print(f'You typed {c} numbers and the sum was {sum}.')
