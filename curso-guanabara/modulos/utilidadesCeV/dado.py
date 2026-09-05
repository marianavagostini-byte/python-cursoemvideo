def leiaInt(msg):
    while True:
        entrada = str(input(msg)).strip()
        try:
            n = int(entrada)
        except (ValueError, TypeError):
            print(f'ERRO! "{entrada}" não é um número inteiro válido.')
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        entrada=str(input(msg)).strip()
        try:
            r=float(entrada)
        except(ValueError, TypeError):
            print(f'ERRO! "{entrada}" nao e um numero Real valido.  ')
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida pelo usuario.')
            return 0
        else:
            return r