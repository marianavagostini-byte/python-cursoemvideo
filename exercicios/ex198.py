# revisao exercicio 03 - Analisador de frases 
c=0
frase=str(input('Digite uma frase: ')).strip().replace(' ','')
print('-='*30)
print(f'letras sem espaco: {len(frase)}')
for letra in frase:
    if letra.upper() in 'AEIOU':
        c+=1
print(f'Sao {c} vogais.')
print(f'Maiusculo: {frase.upper()}')
print(f'De tras para frente: {frase[::-1]}')