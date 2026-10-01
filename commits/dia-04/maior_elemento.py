nums = [12, 5, 89, 34, 7, 56]

maior = nums[0]

for num in nums:
    if num > maior:
        maior = num

print(f"Maior elemento: {maior}")
