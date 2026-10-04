def fatorial(numero):
    if numero <= 1:
        return 1

    return numero * fatorial(numero - 1)


numero = 5

print(f"{numero}! = {fatorial(numero)}")
