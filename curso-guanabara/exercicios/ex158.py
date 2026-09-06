# ex158
# Fonte: Curso em Vídeo / prática (seu código)

lista=[]
soma=media=0
while True:
    dados={}
    dados['nome']=input('Nome: ')
    while True:
        dados['categoria']=input('Categoria [I/A/P]: ').upper()[0]
        if dados['categoria'] in 'IAP':
              break
        print('ERRO! Digite apenas as categorias.')

    dados['qtd vitorias']=int(input('Quantidade de vitorias: '))
    soma+=dados['qtd vitorias']
    lista.append(dados)
    while True:
        resp=input('Deseja continuar [S/N] ? ')
        if resp.upper()in'SN':
              break
        print('ERRO! Digite apenas S ou N.')
    if resp.upper()=='N':
              break

print(f'Foram cadastrados: {len(lista)} atletas.')
media=soma/len(lista)
print(f'A media de vitorias: {media}')
for p in lista:
    if p['categoria']=='P':
            print(f'Todos os profissionais: {p["nome"]}')
for p in lista:
     if p['qtd vitorias']>=media:
                print(f'{p["nome"]} -> {p["qtd vitorias"]} vitorias.')
