def busca_linear(lista, alvo):

    for indice in range(len(lista)):

        if lista[indice] == alvo:
            return indice

    return -1


numeros = [10, 25, 31, 42, 57, 63]

alvo = 42

resultado = busca_linear(numeros, alvo)

if resultado != -1:
    print(f"Valor encontrado no índice {resultado}.")
else:
    print("Valor não encontrado.")
