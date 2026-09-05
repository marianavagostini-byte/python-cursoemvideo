# ex105
# Fonte: Curso em Vídeo / prática (seu código)

numbers=[]
while True:
    n=int(input('Type a positive number: '))
    if n ==0:
        break
    if n <0:
        print('Only type positive numbers !!')
        continue
    numbers.append(n)
print(f'List: {numbers}')

