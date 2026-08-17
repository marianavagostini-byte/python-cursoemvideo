# ex108
# Fonte: Curso em Vídeo / prática (seu código)

produtos=[]
precos=[]
while True:
    n=input('Digite o nome do produto [Digite sair para sair] : ').upper().strip()
    if n == 'SAIR':
        print('Finalizando programa..')
        break

    while True:
        try:
            p=float(input('Digite o preco: '))
            break
        except ValueError:
            print('ERRO!! Digite um numero.')
    produtos.append(n)
    precos.append(p)
maior=max(precos)
pos=precos.index(maior)
print(f'Produtos: {produtos}')
print(f'Precos: {precos}')
print(f'O mais caro: {produtos[pos]} - R$:{maior:.2f}')
print(f'Total: {sum(precos):.2f}')
