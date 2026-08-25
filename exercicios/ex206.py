# Revisao exercicio 08 - Sistema de estoque com menu

from loja import interface, estoque

produtos = []
opcoes = ['Cadastrar produto', 'Listar produtos', 'Valor total do estoque', 'Sair']

while True:
    opc = interface.menu(opcoes)
    if opc == 1:
        interface.cabecalho('NOVO PRODUTO')
        nome = str(input('Nome do produto: ')).strip()
        preco = interface.leiaFloat('Preço: R$ ')
        estoque.cadastrar(produtos, nome, preco)
        print(f'O produto {nome} foi cadastrado com sucesso.')
    elif opc == 2:
        interface.cabecalho('PRODUTOS CADASTRADOS')
        estoque.listar(produtos)
    elif opc == 3:
        interface.cabecalho('VALOR TOTAL')
        soma = total = estoque.total(produtos)
        print(f'O estoque vale R$ {soma:.2f}.')
    elif opc == 4:
        print('Volte sempre !!')
        break
    else:
        print('ERRO!! Digite uma opcao valida.')