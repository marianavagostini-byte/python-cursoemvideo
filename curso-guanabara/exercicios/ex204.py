boletim=[]
while True:
    dados={}
    dados['nome']=input('Nome: ')
    soma=0
    provas=0
    while True:
        try:
            nota=float(input('Nota (-1 para encerrar): '))
        except ValueError:
            print('ERRO! digite apenas numeros.')
            continue
        if nota == -1:
            break
        if nota <0 or nota > 10:
            print('ERRO! Digite uma nota entre 0 e 10')
            continue
        
        soma=soma+nota
        provas=provas+1  
    
    media=soma/provas
    dados['media']=media
    boletim.append(dados.copy())  

    if media >= 7:
        dados['situacao']='APROVADO'
    else:
        dados['situacao']='REPROVADO'

    print(f'{dados["nome"]} fez {provas} provas.')
    print(f'Media: {media:.2f} --> {dados['situacao']}')

    while True:
        resp=input('Outro aluno? [S/N]')
        if resp.upper()in['S','N']:
            break
        print('Digite apenas S ou N.')
    if resp.upper()=='N':
            break
print(f'{len(boletim)} alunos avaliados')
print(f'Media geral da turma: {dados['media']:.2f}')
maior=0
maiorn=''
for p in boletim:
    if p['media'] > maior:
        maior=p['media']
        maiorn=p['nome']
print(f'Melhor media: {maiorn}, com {maior:.2f} ')