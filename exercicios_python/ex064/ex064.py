# ex064 - Tratando Vários Valores v1.0
# Fonte: Curso em Vídeo - desafio oficial (seu código)

soma = 0
cont = 0

numero = int(input('Digite um numero, para parar digite 999: '))

while numero != 999:
    soma += numero
    cont += 1
    numero = int(input('Digite um numero, para parar digite 999: '))

print(f'Voce digitou {cont} numeros e a soma foi {soma}.')
