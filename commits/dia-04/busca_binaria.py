numeros = [2, 5, 8, 12, 16, 23, 38, 56, 72]
alvo = 23

inicio = 0
fim = len(numeros) - 1

while inicio <= fim:
    meio = (inicio + fim) // 2

    if numeros[meio] == alvo:
        print(f"Elemento encontrado no índice {meio}")
        break

    if numeros[meio] < alvo:
        inicio = meio + 1
    else:
        fim = meio - 1
else:
    print("Elemento não encontrado")
