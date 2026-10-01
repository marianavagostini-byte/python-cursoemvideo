nums = [2, 4, 2, 7, 2, 9, 4]

contagem = {}

for num in nums:
    contagem[num] = contagem.get(num, 0) + 1

print(contagem)
