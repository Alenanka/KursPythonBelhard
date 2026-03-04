"""
Даны 4 переменные - a1, a2, a3, a4.
1 - вывести True если все они дробные числа
2 - вывести True если одна из них строка
3 - вывести True если  одна пара переменных является целочисленным типом. 
    Пары могут образовать только следующие переменные - a1-a3, a2-a4, a3-a4"
"""

a1 = 10.3        
a2 = 5.5       
a3 = 20.4        
a4 = 'rrr'

res_float = all(isinstance(x, float) for x in [a1, a2, a3, a4]) 
print(f"1. Все дробные: {res_float}")

res_str = any(isinstance(x, str) for x in [a1, a2, a3, a4])
print(f"2. Есть строка: {res_str}")

res_int = all(isinstance(x, int) for x in [a1,a3]) or all(isinstance(x, int) for x in [a2,a4]) or all(isinstance(x, int) for x in [a4,a3])
print(f"3. Хотя бы одна пара int: {res_int}")
    

