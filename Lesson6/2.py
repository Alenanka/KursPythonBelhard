"""
2. Создать структуру данных сотрудников фирмы с 
    тремя сотрудниками. каждый сотрудник должен иметь:
        ФИО, 
        должность, 
        год рождения, 
        список навыков, 
        список детей с их именем и годом рождения. 
    
    Запросить ФИО сотрудника и вывести по нему информацию.
    
    ** задать вопрос о желании добавить сотрудника,
        если ответ да - добавить сотрудника через несколько input
        (после добавления сотрудника вывести всю структуру консоль)

"""

users = {
    "Обуховская Елена Сергеевна": {
        "position": "engineer",
        "year": 1984,
        "skills": ["PHP", "Java", "C"],
        "kids": ["Liza", "Nastia"],
        "years_kids": {"Liza": 2012, "Nastia": 2015}
    },
    "Иванов Иван Иванович": {
        "position": "lead",
        "year": 1984,
        "skills": ["PHP", "Java", "C", "Python"],
        "kids": ["Anton"],
        "years_kids": {"Anton": 2000}
    },
    "Петров Петр Петрович": {
        "position": "manager",
        "year": 1979,
        "skills": [ "Excel", "SQL"],

    }
}

name = input("Введите ФИО сотрудника: ")
search_result = users.get(name, "Сотрудник не найден")

__import__('pprint').pprint(search_result)

add_new = input("Хотите добавить сотрудника? (да/нет): ").strip().lower()

if add_new == "да":
    new_name = input("ФИО: ")
    position =input("Должность: ")
    year = int(input("Год рождения: "))
    skills=input("Навыки (через запятую): ").split(",")
    add_kids = input("Хотите добавить ребенка:(да/нет): ").strip().lower()
    if add_kids == "да":
        name_kid = input("Имя ребенка : ")
        age_kids = int(input("Год рождения ребенка : "))
    else :
        name_kid = 'нет детей'
        age_kids = 0
    users[new_name] = {
        "position":position,
        "year": year,
        "skills": skills,
        "kids": [name_kid],
        "years_kids": {name_kid : age_kids} }
users["Обуховская Елена Сергеевна"]

__import__('pprint').pprint(users)
