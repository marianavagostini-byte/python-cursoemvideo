numeros = [4, 7, 2, 9, 1, 8]

menor = numeros[0]

for numero in numeros:
    if numero < menor:
        menor = numero

print(f"Lista: {numeros}")
print(f"Menor elemento: {menor}")
