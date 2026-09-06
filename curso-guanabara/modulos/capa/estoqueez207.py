# Estoque
from capa import front 

def cadastrar(lista):
    p={}
    p['nome']=str(input('Nome do produto: ')).strip()
    p['qtd']=front.leiaint('Quantidade: ')
    p['preco']=front.leiafloat('preco unitario: R$ ')
    lista.append(p.copy())
    print(f'Produto "{p["nome"]}" cadastrado com sucesso!')
    
def listar(lista):
    print('-' * 60)
    print(f'{"PRODUTO":<25}{"QTD":>5}{"UNITÁRIO":>15}{"TOTAL":>15}')
    print('-' * 60)
    for p in lista:
        preco = f'R$ {p["preco"]:.2f}'
        subtotal= f'R$ {p["qtd"] * p["preco"]:.2f}'
        print(f'{p["nome"]:<25}{p["qtd"]:>5}{preco:>15}{subtotal:>15}')
    print('-' * 60)
    

def total(lista):
    soma=0
    for p in lista:
        soma= soma + p['preco'] * p['qtd']
    return soma