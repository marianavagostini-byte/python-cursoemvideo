# moeda - Modulo de funcoes financeiras (usado nos desafios 107 a 112)


def metade(n , format=False):
    num=n/2
    return num if format is False else moeda(num)

def dobro(n,format=False):
    num=n*2
    return num if format is False else moeda(num)

def aumentar(n,taxa,format=False):
    num=n+n*(taxa/100)
    return num if format is False else moeda(num)

def diminuir(n,taxa,format=False):
    num=n-n*(taxa/100)
    return num if format is False else moeda(num)

def moeda(n):
    num=f'R${n:.2f}'.replace('.',',')
    return num

def resumo(num=0,taxaA=10,taxaR=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'preco analisado: \t{moeda(num)}')
    print(f'Dobro do preco: \t{dobro(num,True)}')
    print(f'Metade do preco: \t{metade(num,True)}')
    print(f'Taxa {taxaA}% de aumento: \t{aumentar(num,taxaA,True)}')
    print(f'Taxa {taxaR}% de reducao: \t{diminuir(num,taxaR,True)}')
    print('-'*30)