def calcular_media(notas):
    return sum(notas) / len(notas)


notas = [8, 7, 9, 10]

media = calcular_media(notas)

print(f"Notas: {notas}")
print(f"Média: {media:.2f}")
