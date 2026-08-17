# ex157
# Fonte: Curso em Vídeo / prática (seu código)

galera=[]
salarios = []
media=soma=0
while True:
    dados={}
    dados['nome']=input('Nome: ')
    while True:
        dados['setor']=input('Setor [V/T/A]: ').upper()[0]
        if dados['setor'] in 'VTA':
            break
        print('ERRO! Digite apenas [V/T/A] ..')
    dados['salario']=float(input('Salario: '))
    soma+=dados['salario']
    galera.append(dados)
    resp=input('Quer continuar? [S/N] ')
    if resp.upper()=='N':
        break
media=soma/len(galera)
print(f'Foram cadastrados {len(galera)} pessoas.')
print(f'A media salarial de R$ {media:.2f}.')
print('Funcionarios do setor tecnico: ',end='')
for p in galera:
    if p["setor"]=='T':
        print(f'{p["nome"]}')
print()
print('Acima da media salarial: ',end='')
for p in galera:
    if p['salario']>=media:
        print(f'{p['nome']} - R$ {p['salario']} .')
print()
for p in galera:
    salarios.append(p['salario'])

maior = max(salarios)

for p in galera:
    if p['salario'] == maior:
        print(f'Maior salário: {p["nome"]}, com R$ {maior:.2f}')
