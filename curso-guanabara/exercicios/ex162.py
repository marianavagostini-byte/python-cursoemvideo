# ex162
# Fonte: Curso em Vídeo / prática (seu código)

def desconto(preco, porcentagem):
    valor = preco * porcentagem / 100
    final = preco - valor
    print(f'\nDesconto de {porcentagem}% sobre R$ {preco:.2f}')
    print(f'Você economiza R$ {valor:.2f}')
    print(f'Preço final: R$ {final:.2f}')


preco = float(input('Preço do produto: R$ '))
porcentagem = float(input('Desconto (%): '))

desconto(preco, porcentagem)
