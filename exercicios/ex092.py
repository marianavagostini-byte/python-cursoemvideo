# ex092 - Par ou Ímpar (versão 2, com 'Deu PAR')
# Fonte: Extra - fora do curso (seu código / variação)

from random import randint
soma=0
v=0
d=0
while True:
    jogador=int(input('Digite um valor: '))
    computador=randint(0,10)
    soma=jogador+computador
    opcao=' '
    while opcao not in 'PI':
        opcao=str(input('Par ou Impar [P/I] ?  ')).upper().strip()[0]
    print(f'Voce jogou {jogador} e o computador jogou {computador} , total de: {soma}')
    print('Deu PAR ' if soma %2 ==0 else 'Deu IMPAR')
    if opcao =='P':
        if soma %2==0:
            print('Voce VENCEU ')
            v+=1
        else:
            print('Voce PERDEU')
            d+=1
            break 
            
    elif opcao == 'I':
        if soma %2 !=0:
            print('voce VENCEU')
            v+=1
        else:
            print('Voce PERDEU')
            d+=1
            break
    print('Vamos jogar novamente ..')
print(f' GAME OVER .. Voce venceu {v} vezes e perdeu {d} vezes. ')
