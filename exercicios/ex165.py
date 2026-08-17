# ex165
# Fonte: Curso em Vídeo / prática (seu código)

from time import sleep

def contador(i,f,p):
    if p ==0:
        p=1

    p=abs(p)

    print(f'Contagem de {i} ate {f} de {p} em {p}..')
    sleep(1)

    if i < f :
        f+=1
    else:
        f-=1
        p =-p

    for c in range (i,f,p):
        print(f'{c} ', end='' , flush=True)
        sleep(0.5)
    print( 'FIM')

contador(1,10,1)
contador(10,0,2)
print('Agora é sua vez de personalizar a contagem!')
inicio=int(input('Inicio: '))
fim=int(input('Fim: '))
passo=int(input('Passo: '))
contador(inicio,fim,passo)
