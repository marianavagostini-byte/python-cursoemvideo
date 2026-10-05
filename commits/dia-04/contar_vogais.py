texto = "programacao"

vogais = "aeiou"
contador = 0

for caractere in texto.lower():
    if caractere in vogais:
        contador += 1

print(f"Quantidade de vogais: {contador}")
