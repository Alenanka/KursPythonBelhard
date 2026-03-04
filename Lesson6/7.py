"""
Запросить у пользователя год рождения и в соответствии с его возрастом 
охарактеризовать пользователя - 
ребенок, подросток, юноша, в расцвете сил, пожилой, старик.
"""
from datetime import datetime

year = int(input("Введите год рождения: "))
age = datetime.now().year - year

if age <= 12:
    category = "ребенок"
elif age <= 18:
    category = "подросток"
elif age <= 25:
    category = "юноша"
elif age <= 55:
    category = "в расцвете сил"
elif age <= 70:
    category = "пожилой"
else:
    category = "старик"

print(f"Ваш возраст: {age} лет. Категория: {category}")