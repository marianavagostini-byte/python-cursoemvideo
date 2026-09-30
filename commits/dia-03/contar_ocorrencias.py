def contar_ocorrencias(lista, alvo):

    contador = 0

    for elemento in lista:
        if elemento == alvo:
            contador += 1

    return contador


numeros = [1, 2, 3, 2, 4, 2, 5]

alvo = 2

quantidade = contar_ocorrencias(numeros, alvo)

print(f"Lista: {numeros}")
print(f"O número {alvo} aparece {quantidade} vezes.")
