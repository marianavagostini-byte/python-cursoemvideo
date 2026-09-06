# ex094
# Fonte: Extra - fora do curso (seu código / variação)


frutas = ('Maçã', 'Banana', 'Laranja', 'Uva', 'Manga')
precos = (3.50, 2.00, 4.00, 6.50, 5.00)

print('=' * 30)
print(f'{"MENU DE FRUTAS":^30}')
print('=' * 30)

for pos in range(0, len(frutas)):
    print(f'[{pos + 1}] {frutas[pos]:.<20} R$ {precos[pos]:.2f}')

print('-' * 30)


while True:
    try:
        opcao = int(input('Escolha uma fruta (1 a 5): '))
        if 1 <= opcao <= 5:
            indice = opcao - 1  
            break
        else:
            print('Opção inválida! Digite um número de 1 a 5.')
    except ValueError:
        print('Erro! Digite apenas um número inteiro.')
while True:
    try:
        pagamento = int(input('''Qual a sua forma de pagamento?
[1] -- CARTAO CREDITO
[2] -- CARTAO DEBITO
[3] -- PIX
Sua opção: '''))
        if pagamento == 1:
            print('\nSua compra foi aprovada no cartão de crédito!')
            break
        elif pagamento == 2:
            print('\nSua compra foi aprovada no cartão de débito!')
            break
        elif pagamento == 3:
            print('\nSua compra foi aprovada no PIX!')
            break
        else:
            print('Opção de pagamento inválida! Escolha 1, 2 ou 3.\n')
    except ValueError:
        print('Erro! Digite apenas o número da opção desejada.\n')


print(f'Você escolheu {frutas[indice]} que custa R$ {precos[indice]:.2f}')