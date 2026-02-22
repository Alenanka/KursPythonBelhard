'''
Запросить по очереди у пользователя 5 имен. Добавить все в список. 
Отсортировать. 
Вывести на экран.
Вывести True при наличии в списке имени 'Вася'
'''

name1 = input('Введите певрое имя:')
name2 = input('Введите второе имя:')
name3 = input('Введите третье имя:')
name4 = input('Введите четвертое имя:')
name5 = input('Введите пятое имя:')

names_list = [name1, name2, name3, name4, name5]
print(*names_list)

names_list.sort()
print(*names_list)

print('Вася'in names_list)