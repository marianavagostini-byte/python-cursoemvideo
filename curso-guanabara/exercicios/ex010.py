# ex010 - Conversor de Moedas
# Fonte: Curso em Vídeo - desafio oficial (complementado)

real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 5.40  # ajuste a cotação do dia
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
