# ex090 - Gerador de P.A. com pausa (versão 2)
# Fonte: Extra - fora do curso (seu código / variação)

print('-=' * 20)
print('GERADOR DE P.A')
print('-=' * 20)

cont = 1
Primeiro = int(input('Digite um numero para a P.A: '))
razao = int(input('Digite sua razao: '))

termo = Primeiro
mais = 10
total = 0

while mais != 0:
    total += mais
    
    while cont <= total:
        print(f'{termo} -> ', end='')
        cont += 1
        termo += razao
        
    print('PAUSA')
    mais = int(input('Quantos termos quer mostrar a mais? '))

print(f'Progressao finalizada com {total} termos mostrados.')
