# Interface funcoes 


def cabecalho (msg):
    print('-'*42)
    print(msg.center(42))
    print('-'*42)

def leiaint(n):
    while True:
        numero=str(input(n)).strip()
        try:
            num=int(numero)
        except ValueError:
            print(f'ERRO!! -{numero}- Digite apenas numeros validos.')
        else:
            return num 

def leiafloat(msg):
    while True:
        entrada=str(input(msg)).strip().replace(',','.')
        try:
            n=float(entrada)
        except ValueError:
            print(f'ERRO!! -{entrada}- digite um numero valido.')
        else:
            return n

def menu(lista):
    cabecalho(' CADASTRO DE VENDAS ')
    for c in range(0,len(lista)):
        print(f'{c+1}  {lista[c]}')
    print('-'*42)
    opc=leiaint('Sua opcao: ')
    return opc