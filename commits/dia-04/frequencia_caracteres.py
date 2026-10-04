texto = "programacao"

frequencia = {}

for caractere in texto:
    frequencia[caractere] = frequencia.get(caractere, 0) + 1

print(frequencia)
