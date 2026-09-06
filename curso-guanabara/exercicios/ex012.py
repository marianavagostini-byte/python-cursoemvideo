# ex012 - Calculando Descontos
# Fonte: Curso em Vídeo - desafio oficial (complementado)

preco = float(input('Qual é o preço do produto? R$ '))
desc = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com 5% de desconto vai custar R${:.2f}'.format(preco, desc))
