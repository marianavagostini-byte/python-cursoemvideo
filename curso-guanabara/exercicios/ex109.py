# ex109
# Fonte: Curso em Vídeo / prática (seu código)

aluno = []
nota = []

while True:
    nome = input('Nome: ').strip()
    if nome.upper() == 'PARAR':
        break

    
    while True:
        try:
            n = float(input('Nota de 0 a 10: '))
            if 0 <= n <= 10:
                break
            else:
                print('Nota inválida! Deve ser entre 0 e 10.')
        except ValueError:
            print('Erro! Digite um número.')

    
    aluno.append(nome)
    nota.append(n)


if nota:
    menor = min(nota)
    pos = nota.index(menor)

    print(f'Alunos: {aluno}')
    print(f'Notas: {nota}')
    print(f'A menor nota foi do aluno: {aluno[pos]} e a nota foi: {menor}')
    print(f'A média da turma: {sum(nota)/len(nota):.2f}')
else:
    print('Nenhum aluno foi cadastrado.')
