# ex152
# Fonte: Curso em Vídeo / prática (seu código)

dados={}
lista=[]
acima=0
abaixo=0

dados['produto']=str(input('Nome do produto: '))
qtd=int(input(f'Quantos {dados["produto"]} foram cadastrados? '))

for c in range(0,qtd):
    lista.append(int(input(f'Estoque do {c+1} produto: ')))

dados['quantidade']=lista[:]
dados['total']=sum(dados['quantidade'])
dados['media']=(dados['total'])/len(lista)
dados['menor']=min(dados['quantidade'])
dados['maior']=max(dados['quantidade'])

for quant in dados['quantidade']:
    if quant > dados['media']:
        acima+=1
    if quant ==0:
        abaixo+=1

print('A loja tem o seguinte estoque: ')
for i,v in enumerate(dados['quantidade']):
    print(f' => Produto {i+1}: {v} unidades. ')

print(f'Total de {dados["total"]} itens, media de {dados["media"]} por produto.')
print(f'maior estoque: {dados["maior"]} / Menor estoque: {dados["menor"]}')
print(f'{acima} produtos acima da media')
print(f'{abaixo} produtos abaixo da media')
