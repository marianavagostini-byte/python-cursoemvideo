# ex177
# Fonte: Curso em Vídeo / prática (seu código)

livros = list()
def cadastra(lista):
    while True:
        dados = {}
        dados['titulo'] = input('Titulo: ')
        dados['autor'] = input('Autor: ')
        dados['paginas'] = int(input('Paginas: '))
        dados['preco'] = float(input('Preco: R$ '))
        lista.append(dados)

        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp == 'N':
            break

def acervo(lista):
    for p in lista:
        print(f'{p["titulo"]} -- {p["autor"]}   {p["paginas"]} pag | R$ {p["preco"]}') 
def longos(lista):
    mais=[]    
    for p in lista:
        if p['paginas'] > 300:
            mais.append(p['titulo'])
    return mais

def mais_caro(lista):
    campeaocaro=lista[0]
    for p in lista:
        if p['preco'] > campeaocaro['preco']:
            campeaocaro=p
    return campeaocaro['titulo']

def mais_barato(lista):
    campeaobarato=lista[0]
    for p in lista:
        if p['preco']< campeaobarato['preco']:
            campeaobarato=p
    return campeaobarato['titulo']
cadastra(livros)
acervo(livros)
print(f'Livro com mais de 300 pag: {longos(livros)}')
print(f'Livro mais caro: {mais_caro(livros)}')
print(f'Livro mais barato: {mais_barato(livros)}')

