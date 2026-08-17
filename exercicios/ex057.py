# ex057 - Validação de Dados
# Fonte: Curso em Vídeo - desafio oficial (seu código)

from time import sleep
sexo=input('Informa seu sexo -- [F/M]: ').strip().upper()
while sexo != 'M' and sexo != 'F':
    print('Dados invalidos...')
    sleep(1)
    print('Tente novamente digitando o que foi pedido.')
    sleep(0.5)
    sexo=input('Informe seu sexo -- [F/M]: ').strip().upper()
print(f'Sexo {sexo} registrado com sucesso')
