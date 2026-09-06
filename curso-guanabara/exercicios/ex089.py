# ex089 - Soma de números S/N (versão while True)
# Fonte: Extra - fora do curso (seu código / variação)

soma=cont=maiorvalor=menorvalor=0

while True:
    numero=int(input('Digite um numero:  '))
    opcao=input('Quer continuar ? [S/N]  ').strip().upper()
    if cont ==1:
        maiorvalor+=numero
        menorvalor+=numero
    elif numero > maiorvalor:
        maiorvalor=numero
    elif numero < menorvalor:
        menorvalor=numero
    soma+=numero
    cont+=1
    media=soma/cont
    if opcao =='N':
        print(f'Voce digitou {cont} numeros e a media foi de: {media}',end='')
        print(f'O maior valor foi {maiorvalor} e o menor foi {menorvalor}')
        break
