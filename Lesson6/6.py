'''
Запросить 3 раза строку из нескольких чисел через пробел
    - вывести все уникальные числа по возрастанию
    - вывести числа которые есть в каждой строке
    -* вывести числа которые есть только в одной из трех строк
    
    выполнить без циклов и условий
    
    пример:
    >>> 1 2 11 22
    >>> 1 2 22 33
    >>> 1 2 33 44


    1) 1 2 11 22 33 44
    2) 1 2
    3) 11 44
    
'''
text_for_user ='Введите строку из нескольких чисел через пробел: '

str1, str2, str3 = input(text_for_user).split(),input(text_for_user).split(),input(text_for_user).split()

set1 = set(map(int,str1))
set2 = set(map(int,str2))
set3 = set(map(int,str3))

set_union = sorted(set1 | set2 | set3)
print('Уникальные числа по возрастанию:', *set_union)

inter = (set1 &  set2 & set3)
print('Числа которые есть в каждой строке:', *inter)

only_set1 = set1 - set2 - set3
only_set2 = set2 - set1 - set3
only_set3 = set3 - set2 - set1

only_one = (only_set1 | only_set2 | only_set3)

print('Числа которые есть только в одной из трех строк:', *only_one)