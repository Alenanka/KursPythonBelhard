'''
Буква "a" стоит 10 очков, "b" - 20, "c" - 30, "d" - 40
Запросить кодовою фразу из пяти символов используя только a, b, c, d.
Вывести на экран общее количество очков введенной фразы.

'''
letters = {"a" : 10,
           "b" : 20,
           "c" : 30,
           "d" : 40,
          }
allowed = set(letters.keys())

code = input('Введте фразу из пяти символов: ')[:5]
is_allowed = set(code).issubset(allowed)
if  (len(code)) == 5  and is_allowed :
    c =sum(list(map(letters.get,code)))
    print(f'Общее количество очков {c}')
    
else : print ('Недостаточно символов либо есть запрещенные')