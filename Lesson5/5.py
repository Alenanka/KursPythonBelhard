'''
Дан список
['samsung', 'lg', 'xerox', 'bosch']
Удалить элемент с именем 'xerox'
Добавить элемент на 2 место 'indesit'

'''

a = ['samsung', 'lg', 'xerox', 'bosch']
a.pop(a.index('xerox'))
print('xerox удален:',a)


a.insert(1,'indesit')
print(a)

