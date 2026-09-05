# Revisao exercicio 04 - Tabuada que nao quebra 

def inteiro(msg):
    while True:
        entrada=str(input(msg)).strip()
        try:
            n=int(entrada)
        except:
            print(f'ERRO! "{entrada}" - Digite um numero inteiro !!')
        else:
            return n

while True:
    n=inteiro('digite um numero e veja sua tabuada: ')
    if n < 0:
        break
    print('-' * 30)
    print('TABUADA'.center(30))
    print('-' * 30)
    
    for c in range (1,11):
        print(f'{n} x {c:2} = {n * c:3}')
print('PROGRAMA ENCERRADO. Volte sempre!')