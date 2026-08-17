# ex097
# Fonte: Curso em Vídeo / prática (seu código)

lista=[]
for c in range (1,6):
    lista.append(int(input(f'Escolha o [{c}] valor: ')))
print(f'Voce digitou os valores: {lista}')
maior=max(lista)
pos_maior=lista.index(maior)
print(f'O maior numero e: {maior} e ele esta na posicao: {pos_maior}')
menor=min(lista)
pos_menor=lista.index(menor)
print(f'O menor numero e: {menor} e ele esta na posicao: {pos_menor}')
