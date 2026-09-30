def encontrar_maior(lista):

    maior = lista[0]

    for numero in lista:
        if numero > maior:
            maior = numero

    return maior


numeros = [15, 42, 7, 89, 23, 64]

resultado = encontrar_maior(numeros)

print(f"Lista: {numeros}")
print(f"Maior elemento: {resultado}")
