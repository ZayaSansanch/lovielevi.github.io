from unittest import result


# 1. Напишите программу, которая выводит на экран произведение нечётных
# чисел из пятнадцати натуральных, вводимых пользователем.

nums = input("nums= :")
result = 1

nums = nums.split(", ")

for i in range(0, len(nums)):
    num = int(nums[i])
    if num%2 == 1:
        result *= num

print(result)