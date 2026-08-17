# ex172
# Fonte: Curso em Vídeo / prática (seu código)


produtos=list()

def cadastra(lista):
    while True:
        dados={}
        dados['nome']=input('Nome do produto: ')
        dados['qtd']=int(input('Quantidade: '))
        dados['preco']=float(input('Preco unitario: '))
        lista.append(dados)
        resp=input('Deseja continuar? [S/N]')
        if resp.upper()=='N':
            break



def relatorio(lista):
    for p in lista:
        print(f'{p['nome']} -- {p['qtd']} -- {p['preco']}')



def repor(lista):
    nomes=[]
    for p in lista:
        if p['qtd']<10:
            nomes.append(p['nome'])
    return nomes

def valor_total(lista):
    total=0
    for p in lista:
        total+= p['qtd'] * p['preco']
    return total


cadastra(produtos)
relatorio(produtos)
print(f'Produtos para repor: {repor(produtos)}')
print(f'Valor total em estoque: R$ {valor_total(produtos):.2f}')
