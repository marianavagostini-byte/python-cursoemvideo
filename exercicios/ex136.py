# ex136
# Fonte: Curso em Vídeo / prática (seu código)

produto={}
produto['nome']=str(input('Nome do produto :'))
produto['preco']=float(input('Preco do produto: '))
if produto ['preco']<50:
    produto['Resultado']='Barato'
elif produto ['preco'] > 200:
    produto['Resultado']='Caro'
else:
    produto ['preco']= 'Intermediario'

for k,v in produto.items():
    print(f' {k} e igual a {v}')
