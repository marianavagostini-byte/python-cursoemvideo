# ex153
# Fonte: Curso em Vídeo / prática (seu código)

dados={}
lista=[]
adultos=menor=idoso=0
dados['nome']=str(input('Nome do evento: '))
qtd=int(input('Quantas pessoas foram entrevistadas? '))
for c in range(0,qtd):
    lista.append(int(input(f'Idade da {c+1}ª pessoa: ')))
dados['idade']=lista[:]
dados['media']=sum(dados['idade'])/len(lista)

for p in dados['idade']:
    if p < 18:
        menor+=1
    elif p >= 18 and p <=59:
        adultos+=1
    else:
        idoso+=1
print(f'No {dados["nome"]} foram entrevistadas: ')
for i,v in enumerate(dados['idade']):
    print(f' => {i+1}ª pessoa: {v} anos.')
print(f'Media de idade: {dados["media"]} anos.')
print(f' Mais velho: {max(dados["idade"])} anos / Mais novo: {min(dados["idade"])} anos.')
print(f'{menor} menor de idade.')
print(f'{adultos} adultos.')
print(f'{idoso} idosos.')
