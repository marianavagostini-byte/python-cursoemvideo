# ex178
# Fonte: Curso em Vídeo / prática (seu código)

cardapio = list()
def cadastra(lista):
    while True:
        dados = {}
        dados['prato'] = input('Prato: ')
        dados['categoria'] = input('Categoria [entrada/principal/sobremesa]: ')
        dados['preco'] = float(input('Preco: R$ '))
        dados['tempo'] = int(input('Tempo de preparo (min): '))
        lista.append(dados)

        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp == 'N':
            break

def menu(lista):
    for p in lista:
        print(f'{p["prato"]} - {p["categoria"]} | R$ {p["preco"]} | tempo preparo: {p["tempo"]}min')        


def rapidos(lista):
    rapido=[]
    for p in lista:
        if p['tempo'] <=20:
            rapido.append(p['prato'])   
    return rapido


def sobremesas(lista):
    sobremesaa=[]
    for p in lista:
        if p['categoria'] == 'sobremesa':
            sobremesaa.append(p['prato'])
    return sobremesaa

def demorado(lista):
    longo=lista[0]
    for p in lista:
        if p['tempo'] > longo['tempo']:
            longo=p
    return longo['prato']


def barato(lista):
    barato=lista[0]   
    for p in lista:
        if p['preco']<barato['preco']:
            barato=p
    return barato['prato']

cadastra(cardapio)
menu(cardapio)
print(f'Os pedidos mais rapidos sao: {rapidos(cardapio)}')
print(f'Os mais demorados sao: {demorado(cardapio)}')
print(f'As sobremesas sao: {sobremesas(cardapio)}')
print(f'Os mais baratos sao: {barato(cardapio)}')
