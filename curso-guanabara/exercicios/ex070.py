# ex070 - Estatísticas em Produtos
# Fonte: Curso em Vídeo - desafio oficial (seu código)

tot=p1000=0
pbarato=''
valorbarato=0
c=0
while True:
    nome=str(input('Nome do Produto: '))
    preco=int(input('Preco do Produto: '))
    continuar=' '
    c+=1
    tot+=preco

    while continuar not in 'SN':
        continuar=str(input('Quer continuar [S/N] ?')).strip().upper()[0]
        
    if preco >=1000:
        p1000+=1
    if c ==1 or preco < valorbarato:
        valorbarato=preco
        pbarato=nome
    if continuar == 'N':
            print('FIM do programa..')
            break

print(f'total da compra: {tot}')
print(f'{p1000} produtos custam mais de 1.000,00 ')
print(f'O nome do produto mais barato e: {pbarato} , e seu valor e: {valorbarato}')
