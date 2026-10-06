memoria = {}


def fibonacci(n):
    if n in memoria:
        return memoria[n]

    if n <= 1:
        return n

    resultado = fibonacci(n - 1) + fibonacci(n - 2)

    memoria[n] = resultado

    return resultado


for numero in range(15):
    print(f"Fibonacci({numero}) = {fibonacci(numero)}")
