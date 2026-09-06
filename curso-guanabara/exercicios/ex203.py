lista=[]
while True:
    print(f'CLIENTE {len(lista)+1}')
    produtos=0
    total=0
    while True:
        try:
            preco=float(input('Preco do produto (0 para fechar): '))
        except ValueError:
            print('ERRO! Digite um valor valido.')
            continue

        if preco == 0:
            break
        if preco <0:
            print('ERRO! preco nao pode ser negativo')
            continue

        produtos+=1
        total= total + preco
    print()
    print(f'{produtos} produtos --> Total: R${total:.2f}')
    lista.append(total)

    while True:
        resp = input('Próximo cliente? [S/N] ').strip().upper()
        if resp in ['S', 'N']:
            break
        print('Digite apenas S ou N.')

    if resp == 'N':
        break

print('-' * 30)
print(f'Atendemos {len(lista)} clientes.')
print(f'Faturamento do dia: R${sum(lista):.2f}')
print(f'Maior compra: R${max(lista):.2f}')