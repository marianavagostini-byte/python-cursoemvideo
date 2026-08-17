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