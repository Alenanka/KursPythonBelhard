"""
дан словарь
d = {'one':11, 'two':22, 'hello':'python', True:False}
запросить номер элемента и удалить его из словаря с помощью del.

"""

d = {'one':11, 'two':22, 'hello':'python', True:False}

number = int(input("Введите номер элемента для удаления (1-4): "))
keys = list(d.keys())
del d[keys[number - 1]]

print(d)