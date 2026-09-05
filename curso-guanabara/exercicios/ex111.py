# ex111
# Fonte: Curso em Vídeo / prática (seu código)

filme=[]
nota=[]
while True:
    nome=input('Nome do filme [Digite sair para encerrar ]: ').strip()
    if nome.upper()=='SAIR':
        break
    if nome in filme:
        print('Ja tem esse filme ! Tente outro..')
        continue
    while True:
        try:
            n=float(input('Nota do filme: '))
            if n <0 or n >10:
                print('Nota invalida, tente entre 0 e 10 !')
                continue
        except ValueError:
            print('Erro!')
            continue
        break
    filme.append(nome)
    nota.append(n)
if filme:
    print(f'Os filmes foram: {filme}')
    print(f'As notas foram: {nota}')
    maior=max(nota)
    posmaior=nota.index(maior)
    print(f'o filme: {filme[posmaior]} - tem a maior nota: {maior}')
    menor=min(nota)
    posmin=nota.index(menor)
    print(f'O filme: {filme[posmin]} - tem a menor nota: {menor}')
else:
    print('Nenhum filme cadastrado !')
