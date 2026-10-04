numeros = [1, 2, 3, 4, 5, 6, 7, 8]

esquerda = 0
direita = len(numeros) - 1

while esquerda < direita:
    print(f"{numeros[esquerda]} <-> {numeros[direita]}")

    esquerda += 1
    direita -= 1
