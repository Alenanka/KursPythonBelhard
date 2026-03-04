'''

Дан списк:
['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']
Для каждого элемента в списке 
    - вывести на экран сначала номер элемента 
    - сам элемент 
    - символ данного элемента, соответствующий номеру его позиции в списке. 
Образец:
1 - qwertyu - q
2 - asdfggh - s
3 - zxcvbnm - c
и так далее...


'''

data = ['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']

print("Вариант 1:")
for element in data:
    print (data.index(element)+1,element ,element[data.index(element)],sep=' - ')

print("Вариант 2:")
for i, element in enumerate(data):
    print(f'{i+1} - {element} - {element[i]}')

print("Вариант 3:")
for i in range(len(data)):
    print(f'{i+1} - {data[i]} - {data[i][i]}')