'''
запросить у пользователя логин пароль и возраст
вывести доступ разрешен:
    логин:admin   пароль:123456    возраст: любой    
    логин:vasya   пароль: vas123   возраст: менее 60
    логин:guest   пароль: любой    возраст:более 18
    
в остальных случаях - "доступ запрещен".

'''

login = input("Введите логин: ")
password = input("Введите пароль: ")
age = int(input("Введите возраст: "))

is_allow = False

if login == "admin" and password == "123456":
    is_allow = True
elif login == "vasya" and password == "vas123" and age < 60:
    is_allow = True
elif login == "guest" and age > 18:
    is_allow = True

print("Доступ разрешен" if is_allow else "Доступ запрещен")