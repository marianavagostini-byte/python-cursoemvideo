# ex075 - Análise de Dados em uma Tupla
# Fonte: Curso em Vídeo - desafio oficial (seu código)

def ler_numero(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('Erro! Digite apenas números inteiros!!')

num = (
    ler_numero('Digite o 1 valor: '),
    ler_numero('Digite o 2 valor: '),
    ler_numero('Digite o 3 valor: '),
    ler_numero('Digite o 4 valor: ')
)

print(f'\nVocê digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O primeiro valor 3 foi digitado na posicao: {num.index(3)+1}')
else:
    print('O valor 3 nao foi digitado em nenhuma posicao.')
print(f'Os numeros pares foram:',end='')
for n in num:
    if n %2==0:
        print(f'{n} ',end='')
