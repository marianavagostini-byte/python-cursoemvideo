def cabecalho(msg):
    print('-'*40)
    print(msg.center(40))
    print('-'*40)

def leiaInt(msg):
	while True:
		entrada = str(input(msg)).strip()
		try:
			n = int(entrada)
		except:
			print(f'ERRO! "{entrada}" não é um número inteiro válido.')
		else:
			return n


def menu(lista):
    cabecalho('ESTOQUE DA LOJA')
    for c in range (0,len(lista)):
        print(f'[ {c+1} ] {lista[c]}')
    print('-'*40)
    opc=leiaInt('Sua opcao: ')
    return opc 

def leiaFloat(msg):
    while True:
        entrada = str(input(msg)).strip()
        try:
            n = float(entrada)
        except:
            print(f'ERRO! "{entrada}" não é um número real válido.')
        else:
            return n