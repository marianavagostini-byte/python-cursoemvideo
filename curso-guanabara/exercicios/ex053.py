# ex053 - Detector de Palíndromo
# Fonte: Curso em Vídeo - desafio oficial (seu código)

frase=str(input('Digite uma frase: ')).upper().strip()
palavras=frase.split()
junto= ''.join(palavras)
inverso=junto[::-1]
print('O inverso de {} e {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
