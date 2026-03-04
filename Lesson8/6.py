"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
а возвращает список из Yes или No для каждого элемента, 
Yes - если число уже встречалось и No, если нет
[1,2,3,1,4] => [no, no, no, yes, no]

если в списке не все целые числа вернуть False.

"""

def  yes_or_no(numbers):
    result = []
    for n in numbers:
        if not isinstance(n, int) :
            return False 
        
    for i,n in enumerate(numbers):
        if not numbers[:i].count(n):
            result.append('no')
        else: result.append('yes')
    return result


print(yes_or_no([1,'r',3,1,4,4,1,7]))