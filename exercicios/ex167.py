# ex167
# Fonte: Curso em Vídeo / prática (seu código)



def maior(*num):
    maiorvalor=num[0]
    for valor in num:
        if valor > maiorvalor:
            maiorvalor=valor

    print('Analisando os valores passados...')

    for valor in num:
        print(f'{valor} ',end='')

    print(f'Foram informados {len(num)} valores ao todo.')

    print(f'O maior valor informado foi {maiorvalor}.')

maior(10,60,30,90,150)
maior(0,0,0)
maior(10000000,1000000000001,1010101010101010)
