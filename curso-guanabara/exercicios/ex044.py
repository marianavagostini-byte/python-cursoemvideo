# ex044 - Elevador de Pagamento
# Fonte: Curso em Vídeo - desafio oficial (seu código)

preco=float(input('Qual o valor total da compra? R$'))
print('''OPÇÕES DE PAGAMENTO:
[ 1 ] DINHEIRO/CHEQUE -- 10% DESCONTO
[ 2 ] À VISTA CARTÃO -- 5% DESCONTO
[ 3 ] 2X NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO -- 20% JUROS''')
opcao=int(input('Qual a opcao de pagamento?'))
if opcao == 1:
    total=preco-(preco*10/100)
elif opcao == 2:
    total=preco-(preco*5/100)
elif opcao == 3:
    total=preco
    parcela=total/2
    print(f'A sua compra sera parcelada em 2x sem juros, no valor de R${parcela} cada parcela')
elif opcao ==4:
    total=preco+(preco*20/100)
    parcelas=int(input('Qual o total de parcelas? '))
    parcela=total/parcelas
    print(f'A sua compra sera parcelada em {parcelas} parcelas, no valor de R${parcela:.2f} com juros ')
print(f'A sua compra de R${preco:.2f} vai custar no final R${total:.2f}')
