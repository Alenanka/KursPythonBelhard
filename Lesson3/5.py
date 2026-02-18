'''
Запросить количество секунд. 
Вывести на экран время в формате ЧЧ:ММ:СС равное эти секундам.
Пример: 35457 -> 09:50:57
Сделать 2 варианта с форматной строкой и без.

'''

number =int(input("Введите количество секунд:"));

hours = number // 3600 
minutes = (number % 3600) // 60 
seconds = number % 60 

print(number,"->","{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))
print(f"{number} -> { hours:02d}:{minutes:02d}:{seconds:02d}")
 