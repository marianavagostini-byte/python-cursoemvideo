# moeda - Modulo de funcoes financeiras (usado nos desafios 107 a 112)

def dobro(n):
    num=n*2
    return num 

def metade(n):
    num=n/2
    return num 

def aumentar(n,taxa):
    num=n+n*(taxa/100)
    return num 

def diminuir(n,taxa):
    num=n-n*(taxa/100)
    return num

def moeda(n):
    num=f'R${n:.2f}'.replace('.',',')
    return num