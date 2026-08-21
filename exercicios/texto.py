#Revisao exercicio 06 - Modulo de texto

def cabecalho(msg):
    print('-='*30)
    print(msg.center(30))
    print('-='*30)


def formatar_nome(nome):
    return nome.title()
  
def contar_vogais(frase):
    total=0
    for letra in frase.upper():
        if letra in 'AEIOU':
            total+=1
    return total
