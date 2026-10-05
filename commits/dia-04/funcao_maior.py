def encontrar_maior(numeros):
    maior = numeros[0]

    for numero in numeros:
        if numero > maior:
            maior = numero

    return maior


numeros = [15, 42, 8, 91, 23]

print(f"Maior número: {encontrar_maior(numeros)}")
