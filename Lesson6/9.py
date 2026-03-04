'''
Запросить 3 числа. Вывести наибольшее  из них. Решить используя if.
'''

nums = list(map(int, input("Введите 3 числа через пробел: ").split()))
max_value = nums[0]

if nums[1] > max_value:
    max_value = nums[1]
if nums[2] > max_value:
    max_value = nums[2]

print(f"Наибольшее: {max_value}")