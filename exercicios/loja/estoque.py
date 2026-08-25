def cadastrar(lista, nome , preco):
        dicionario={}
        dicionario['nome']=nome
        dicionario['preco']=preco
        lista.append(dicionario)
        
def listar(lista):
    print('-' * 40)
    print(f'{"NOME":<25}{"PREÇO":>15}')
    print('-' * 40)
    for p in lista:
        preco = f'R$ {p["preco"]:.2f}'
        print(f'{p["nome"]:<25}{preco:>15}')
    print('-' * 40)


def total(lista):
    soma = 0
    for p in lista:
        soma = soma + p['preco']
    return soma