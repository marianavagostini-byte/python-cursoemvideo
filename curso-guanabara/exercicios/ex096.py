# ex096
# Fonte: Curso em Vídeo / prática (seu código)

nome = []
nota = []
for c in range(1, 5):
    nome.append(input(f'Digite o seu nome [{c}]: '))
    nota.append(int(input(f'Digite a sua nota [{c}]: ')))
maior = max(nota)
pos_maior = nota.index(maior)
print(f'A maior nota foi: {maior} e quem tirou foi: {nome[pos_maior]}')
menor = min(nota)
pos_menor = nota.index(menor)
print(f'A menor nota foi: {menor} e quem tirou foi: {nome[pos_menor]}')
media = sum(nota) / len(nota)
print(f'A média da turma foi: {media}')
