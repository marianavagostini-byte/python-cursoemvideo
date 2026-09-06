# ex151
# Fonte: Curso em Vídeo / prática (seu código)

dados={}
lista=[]
acima=0

dados['nome']=str(input('Nome da cidade: '))
qtd=int(input(f'Quantos dias foram medidos em {dados["nome"]} ? '))

for c in range(0,qtd):
    lista.append(float(input(f'Temperatura do {c+1}º dia: ')))

dados['temp']=lista[:]
dados['media']=sum(dados['temp'])/len(lista)
dados['maxima']=max(dados['temp'])
dados['minima']=min(dados['temp'])

for temp in dados['temp']:
    if temp > dados['media']:
        acima+=1

print(f'A cidade de {dados["nome"]} registrou: ')
for i,v in enumerate(dados['temp']):
    print(f' => {i+1} dia: {v}ºC')
print(f'Media: {dados["media"]}ºC')
print(f'Maxima: {dados['maxima']}ºC / Minima: {dados['minima']}ºC')
print(f'Foram {acima} dias acima da media. ')

