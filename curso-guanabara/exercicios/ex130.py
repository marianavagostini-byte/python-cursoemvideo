# ex130
# Fonte: Curso em Vídeo / prática (seu código)

lista=[]
while True:
    nome=input('Nome do produto: ')
    custo=float(input('Preco de custo: '))
    venda=float(input('Preco de venda: '))
    lucro=(venda-custo)
    lista.append([nome,[custo,venda],lucro])
    resp=input('Deseja continuar? [S/N]')
    if resp.upper()=='N':
        break
for c in lista:

    print(f'Produto: {c[0]} - Lucro: {c[2]}')

while True:
    opc=int(input('Consulte um produto (999 para parar) : '))
    if opc==999:
        break
    print(f'Produto: {lista[opc][0]} - custo: {lista[opc][1]} - lucro: {lista[opc][2]}')
