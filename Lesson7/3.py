'''
Запросить любое число. Заменить каждую цифру этого числа буквой, 
у которой номер в алфавите равен этой цифре. 
Алфавит считаем от 0. a-0, b-1, c-3 и т.д.
Например: 13520 -> bdfca.
'''

alphabet = 'abcdefghij'

user_input = input('Введите число: ')

if user_input.isdigit():
    result = ''.join(alphabet[int(d)] for d in user_input)
    print(f'{user_input} -> {result}')
else:
    print('Введите только цифры!')