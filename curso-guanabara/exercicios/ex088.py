# ex088 - Detector de Palíndromo (versão colorida)
# Fonte: Extra - fora do curso (seu código / variação)

print('\033[36m-=\033[m' * 20) 
print('\033[1;36m       DETECTOR DE PALÍNDROMO\033[m') 
print('\033[36m-=\033[m' * 20)

frase = str(input('\n\033[34mDigite uma frase: \033[m')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print('\n\033[33mAnalisando...\033[m\n') 
print('O inverso de \033[1;33m{}\033[m é \033[1;33m{}\033[m'.format(junto, inverso))
print('-' * 40) 

if inverso == junto:
    print('\033[1;32m✅ Temos um palíndromo!\033[m') 
else:
    print('\033[1;31m❌ A frase digitada não é um palíndromo!\033[m')

print()
