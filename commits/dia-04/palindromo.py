palavra = "radar"

invertida = palavra[::-1]

if palavra == invertida:
    print(f"{palavra} é um palíndromo")
else:
    print(f"{palavra} não é um palíndromo")
