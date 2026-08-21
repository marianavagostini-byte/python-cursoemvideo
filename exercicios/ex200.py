# Revisao exercicio 05 - Cadastro de pessoas
lista=[]
soma=0
while True:
    dados={}
    dados['nome']=input('Nome: ')
    dados['idade']=int(input('Idade: '))
    soma+=dados['idade']
    lista.append(dados.copy())

    resp=input('Deseja continuar? [S/N]')
    if resp.upper()=='N':
        break
print('-' * 40)
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'A média de idade é de {soma / len(lista):.2f} anos.')

print('Maiores de idade: ', end='')
for p in lista:
    if p['idade'] >= 18:
        print(p['nome'], end='  ')
print()

maior = 0
nome_maior = ''
for p in lista:
    if p['idade'] > maior:
        maior = p['idade']
        nome_maior = p['nome']
print(f'A pessoa mais velha é {nome_maior}, com {maior} anos.')
print('-' * 40)
  