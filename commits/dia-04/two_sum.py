def two_sum(nums, alvo):
    vistos = {}

    for i, numero in enumerate(nums):
        complemento = alvo - numero

        if complemento in vistos:
            return [vistos[complemento], i]

        vistos[numero] = i

    return []


nums = [2, 7, 11, 15]
alvo = 9

resultado = two_sum(nums, alvo)

print("Índices encontrados:", resultado)
