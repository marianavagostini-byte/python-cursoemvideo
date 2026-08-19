# dado - Modulo de tratamento de dados (funcoes chegam no desafio 112)

def leiadinheiro(msg):
    valido=False
    while not valido:
        entrada=str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada=='':
            print(f'ERRO: "{entrada}" e um preco invalido!')
        else:
            valido=True
    return float(entrada)