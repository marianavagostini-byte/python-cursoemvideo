# ex050 - Soma dos Pares
# Fonte: Curso em Vídeo - desafio oficial (seu código)

soma = 0 

for c in range(1, 7): 
    num = int(input('Digite o {}º número: '.format(c))) 
    
    if num % 2 == 0: 
        soma = soma + num 

print('A soma de todos os números PARES digitados é: {}'.format(soma))
