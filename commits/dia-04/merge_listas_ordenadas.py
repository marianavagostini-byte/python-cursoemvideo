def mesclar_listas(lista1, lista2):
    resultado = []

    i = 0
    j = 0

    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    while i < len(lista1):
        resultado.append(lista1[i])
        i += 1

    while j < len(lista2):
        resultado.append(lista2[j])
        j += 1

    return resultado


lista1 = [1, 4, 7, 10]
lista2 = [2, 3, 8, 12]

resultado = mesclar_listas(lista1, lista2)

print("Lista final:", resultado)
