# ex161
# Fonte: Curso em Vídeo / prática (seu código)


def sucesso(nome, idade):
    print(f'{nome}, {idade} anos — cadastrado com sucesso!')

lista = []
while True:
    dados = {}
    dados['nome'] = input('Nome: ')
    dados['idade'] = int(input('Idade: '))
    lista.append(dados)    

    sucesso(dados['nome'], dados['idade'])

    resp = input('Continuar? [S/N] ').upper()[0]
    if resp == 'N':
        break




