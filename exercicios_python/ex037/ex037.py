# ex037 - Conversor de Bases Numéricas
# Fonte: Curso em Vídeo - desafio oficial (seu código)

numero= int(input('Digite um numero inteiro:  '))
print('''Escolha uma das bases para conversao: 
      
    [ 1 ] - converter para BINARIO
    [ 2 ] - converter para OCTAL
    [ 3 ] - converter para HEXADECIMAL''')
opcao=int(input('Sua opcao: '))
if opcao ==1:
    print('{} convertido para BINARIO fica {}'.format(numero,bin(numero)))
elif opcao ==2:
    print('{} convertido para OCTAL fica {}'.format(numero,oct(numero)))
elif opcao ==3:
    print('{} convertido para HEXADECIMAL fica {}'.format(numero,hex(numero)))
