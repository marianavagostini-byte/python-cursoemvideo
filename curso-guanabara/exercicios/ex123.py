# ex123
# Fonte: Curso em Vídeo / prática (seu código)

from random import randint

quantas_senhas = int(input('Quantas senhas? '))
tamanho_senha = int(input('Qual o tamanho da senha? '))
lista_principal = []

for c in range(quantas_senhas):
    lista_qtdsenhas = []
    
    while len(lista_qtdsenhas) < tamanho_senha:
        num = randint(0, 9)
        if num not in lista_qtdsenhas:
            lista_qtdsenhas.append(num)
            
    
    lista_qtdsenhas.sort()
    lista_principal.append(lista_qtdsenhas[:])


for c in range(len(lista_principal)):
    print(f'{c + 1} - {lista_principal[c]}')
