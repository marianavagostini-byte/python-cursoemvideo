# ex091 - Gerador de P.A. com nomes descritivos (REVISAR)
# Fonte: Extra - fora do curso (seu código / variação)

# Você marcou este desafio para REVISAR
print('-=' * 20)
print('GERADOR DE P.A')
print('-=' * 20)

numero_inicial = int(input('Digite o numero inicial da P.A: '))
razao = int(input('Digite a razao (de quanto em quanto pula): '))

valor_que_vai_aparecer = numero_inicial
quantidade_pedida = 10
limite_da_sequencia = 0
numero_atual_da_contagem = 1

while quantidade_pedida != 0:
    limite_da_sequencia += quantidade_pedida
    
    while numero_atual_da_contagem <= limite_da_sequencia:
        print(f'{valor_que_vai_aparecer} -> ', end='')
        numero_atual_da_contagem += 1
        valor_que_vai_aparecer += razao
        
    print('PAUSA')
    quantidade_pedida = int(input('Quantos termos quer mostrar a mais? '))

print(f'Progressao finalizada com {limite_da_sequencia} termos mostrados.')
