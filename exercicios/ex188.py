# ex106 - Desafio 106: PyHELP
# Fonte: Curso em Vídeo - desafio oficial (complementado)


def titulo(msg):
    print('~' * 42)
    print(msg.center(42))
    print('~' * 42)


# Programa Principal
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    titulo(f'Acessando o manual do comando {comando}')
    help(comando)
titulo('ATÉ LOGO!') 