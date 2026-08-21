
lista=[]

while True:
    dados={}
    dados['nome']=str(input('Nome: ')).strip()
    dados['idade']=int(input('Idade: '))
    lista.append(dados.copy())

    resp=input('Deseja continuar ? [S/N]')
    if resp.upper()=='N':
        break
print(f'Foram caddastradas {len(lista)} pessoas.')

soma=0
for p in lista:
    soma = soma + p['idade']

media=soma/len(lista)

print(f'A media de idade e de {media:.2f} anos.')


print('Maiores de idade: ',end='')
for p in lista:
    if p['idade'] >=18:
        print(p['nome'], end='')

print()

maior=0
maisvelho=''
for p in lista:
    if p['idade'] > maior:
        maior=p['idade']
        maisvelho=p['nome']
print(f'A pessoa mais velha e {maisvelho}, com {maior} anos.')