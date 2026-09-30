numeros = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

contagem = {}

for numero in numeros:
    if numero in contagem:
        contagem[numero] += 1
    else:
        contagem[numero] = 1

print("Contagem dos números:")

for numero, quantidade in contagem.items():
    print(f"{numero}: {quantidade} vez(es)")
