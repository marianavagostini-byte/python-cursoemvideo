def parenteses_validos(expressao):
    pilha = []

    pares = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    aberturas = set(pares.values())

    for caractere in expressao:
        if caractere in aberturas:
            pilha.append(caractere)

        elif caractere in pares:
            if not pilha or pilha[-1] != pares[caractere]:
                return False

            pilha.pop()

    return len(pilha) == 0


expressoes = [
    "({[]})",
    "([)]",
    "{[()]}",
    "((("
]

for expressao in expressoes:
    print(expressao, "->", parenteses_validos(expressao))
