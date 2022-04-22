# 2. Напишите программу, которая выводит на экран максимальное число, не
# оканчивающееся на 3, из семи натуральных чисел, вводимых
# пользователем.

nums = input("nums= :")
nums = nums.split(", ")
result = 0

for i in range(0, len(nums)):
    num = int(nums[i])
    if num%10 != 3:
        if num > result:
            result = num

print(result)