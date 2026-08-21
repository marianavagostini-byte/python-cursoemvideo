# Revisao exercicio 02 - Analisador de numeros

def validacao(msg):
    while True:
        frase=str(input(msg)).strip()
        try:
            n=int(frase)
        except:
            print(f'ERRO! "{frase}" nao e um numero inteiro valido.')
        else:
            if n <0:
                print('ERRO! Nao aceita numero negativo.')
            else:
                return n
lista=[]
for c in range(0,5):
    numeros=validacao(f'Digite o {c+1} numero: ')
    lista.append(numeros)
print(f'Voce digitou: {lista}')
print(f'Maior: {max(lista)}')
print(f'Menor: {min(lista)}')
print(f'Soma: {sum(lista)}')
soma=sum(lista)
print(f'Media: {soma/len(lista)}')
