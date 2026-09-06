# Revisao Geral ex 01 - Boletim do aluno 
galera=[]
while True:
    dados={}
    dados['nome']=input('Nome do aluno(a): ')
    dados['nota1']=float(input('1 nota: '))
    dados['nota2']=float(input('2 nota: '))
    soma=dados['nota1']+dados['nota2']
    dados['media']=soma/2

    if dados['media']>=7:
        dados['situacao']='APROVADO'
    elif dados['media']<5:
        dados['situacao']='REPROVADO'
    else:
        dados['situacao']='RECUPERACAO'
    
    galera.append(dados.copy())

    resp=input('Deseja continuar? [S/N]')
    if resp.upper()=='N':
        break

for dados in galera:
    print(f"Aluno: {dados['nome']}")
    print(f"Notas: {dados['nota1']:.1f} e {dados['nota2']:.1f}")
    print(f"Média: {dados['media']:.1f}")
    print(f"Situação: {dados['situacao']}")
    print('-' * 35)