"""
Дан список пользователей след. формата: 
[{"name":"some_name", "login":"some_login", "password":"some_password" },
 ...
]

Отфильтровать используя функцию filter() список на предмет паролей 
которые менее 5 символов.

*Отфильтровать используя функцию filter() список на предмет валидных логинов. 
Валидный логин должен содержать только латинские буквы, цифры и черту подчеркивания. 
Каждому пользователю с плохим логином вывести текст 
"Уважаемый user_name, ваш логин user_login не является корректным."

"""
def is_valid(login):  
    for ch in login:
        if not (ch.isalnum() or ch == '_'):
            return False
    return True

users = [{"name":"some_name", "login":"some_login", "password":"some_password" },
        {"name":"jhkjh", "login":"ddddgdh", "password":"aasfsf" },
        {"name":"dd1212dd", "login":"ddddgdh", "password":"afsf" },
       {"name":"dddddd", "login":"ddddgdh!ss", "password":"asf" }
]

users_pass = list(filter(lambda user: len(user['password']) > 5 , users))
print(users_pass)

users_login = list(filter(lambda user: not is_valid(user['login']), users))
print(users_login)

users_invalid_login = list(filter(lambda user: not is_valid(user['login']), users))

for user in users_invalid_login:
    print(f"Уважаемый {user['name']}, ваш логин {user['login']} не является корректным.")