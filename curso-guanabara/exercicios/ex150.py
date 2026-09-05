# ex150
# Fonte: Curso em Vídeo / prática (seu código)

dados={}
lista=[]
dados['nome']=str(input('Nome do Atleta: '))
qtd=int(input(f'Quantos saltos {dados["nome"]} deu? '))
for c in range(0,qtd):
    lista.append(float(input(f'Distancia do {c+1}º salto: ')))
dados['saltos']=lista[:]
dados['media']=sum(dados['saltos'])/len(lista)

print(f'Atleta {dados["nome"]} obteve os resultados: ')
for i,v in enumerate(dados['saltos']):
    print(f' => {i+1} salto: {v}m .')

print(f'Sua media de saltos foi de {dados["media"]}m .')
