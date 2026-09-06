# Programa principal 

from capa import front, estoqueez207
opcoes = ['Cadastrar produto', 'Listar produtos', 'Valor total do estoque', 'Sair']
lista=[]
        
while True:
    opc=front.menu(opcoes)
    if opc ==1:
        estoqueez207.cadastrar(lista)
    elif opc ==2:
        estoqueez207.listar(lista)
    elif opc ==3:
        print(f'Valor total do estoque: R${estoqueez207.total(lista):.2f}')
    elif opc ==4:
        print('VOLTE SEMPRE !!')
        break
    else:
        print(f'Numero invalido, digite entre 1 e {len(opcoes)} !!')
      
  
        
        
        
        