# ex170
# Fonte: Curso em Vídeo / prática (seu código)

def analisa(* t):
    for c in t:
        print(f'{c}',end='')
        print()
    maior=menor= t[0]
    for valor in t:
        if valor > maior:
            maior=valor
        if valor < menor :
            menor=valor
    print(f'O menor valor e: {menor} - e o maior e: {maior}')
    print(f'Tem {len(t)} temp registradas.')
    print(f'A media e {sum(t)/len(t)}')

analisa(28.5, 31.0, 26.5, 33.0, 29.0)
