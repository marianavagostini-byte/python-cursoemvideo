quantidade = 10

a = 0
b = 1

for _ in range(quantidade):
    print(a)

    proximo = a + b
    a = b
    b = proximo
