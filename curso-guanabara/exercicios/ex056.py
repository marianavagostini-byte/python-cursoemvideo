# ex056 - Analisador Completo
# Fonte: Curso em Vídeo - desafio oficial (seu código)

nomevelho=''
totmulher20=0
somaidade = 0  # correção: esta variável precisava ser inicializada antes do laço
for c in range (1,5):
    print(f'------ {c} PESSOA -------')
    nome=str(input('Qual o seu nome:  ')).strip()
    idade=int(input('Qual a sua idade: '))
    sexo=str(input('Qual o seu sexo [F/M]: ')).strip()
    somaidade += idade 
    if c ==1 and sexo in 'Mm':
        maioridadehomem=idade
        nomevelho=nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem= idade
        nomevelho=nome
    if sexo in "Ff" and idade > 20:
        totmulher20 += 1
        
mediaidade= somaidade / 4 
print(f'A media de idade do grupo foi de {mediaidade} anos')
print(f'O homem mais velho se chama {nomevelho} e ele tem {maioridadehomem} anos ')
print(f'Ao todo sao {totmulher20} mulheres com menos de 20 anos')
