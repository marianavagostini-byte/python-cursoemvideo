nums = [4, 8, 15, 16, 23, 42]
alvo = 23

for i in range(len(nums)):
    if nums[i] == alvo:
        print(f"Elemento encontrado no índice {i}")
        break
else:
    print("Elemento não encontrado")
