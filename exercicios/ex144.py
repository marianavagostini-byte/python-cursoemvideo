# ex144
# Fonte: Curso em Vídeo / prática (seu código)

from datetime import datetime

dicionario={}
dicionario['nome']=input('Nome: ')
nasc=int(input('Data de nascimento: '))
dicionario['idade']=datetime.now().year-nasc
ct=int(input('Carteira de trabalho [0 nao tem]: '))
if ct !=0:
    dicionario['contratacao']=int(input('Ano de contratacao: '))
    dicionario['salario']=float(input('Salario: '))
    dicionario['aposentadoria']=dicionario['idade']+ ((dicionario['contratacao']+35)-datetime.now().year)

for k,v in dicionario.items():
    print(f'- {k} - {v}')
