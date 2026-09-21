def busca_binaria(lista, numero):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == numero:
            return meio

        if lista[meio] < numero:
            inicio = meio + 1

        else:
            fim = meio - 1

    return -1