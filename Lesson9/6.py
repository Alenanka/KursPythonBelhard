"""
Дан словарь наблюдения за температурой 
{"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}. 
Отсортировать словарь по температуре в порядке возрастания и обратно.

"""
temp = {"day1":18, "day2":22, "day3":7, "day4":11, "day5":14} 


temp_sort = dict(sorted(temp.items(), key=lambda x: x[1]))
temp_sort_desc = dict(sorted(temp.items(), key=lambda x: x[1], reverse=True))
print(temp_sort)
print(temp_sort_desc)