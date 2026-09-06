# ex067 - Tabuada v3.0
# Fonte: Curso em Vídeo - desafio oficial (seu código)

c=0
while True:
    numero=int(input('Voce quer ver a tabuada de que numero?  '))
    if numero <0:
        break
    c+=1
    for c in range (1,101):
        print(f'{numero} x {c} = {numero*c}')
