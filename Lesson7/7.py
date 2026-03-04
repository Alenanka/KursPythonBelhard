"""
Запросить любое число не менее 10. 
Вывести на экран сумму квадратов каждой цифры составляющей это число. 
Например: дано 236 => 2*2 + 3*3 + 6*6 = 49 

"""


while True:
    user_input = input('Введите число не менее 10: ')
    if  user_input.isdigit() and  int(user_input) > 10 :
        number = int(user_input)
        break
    else :
        print('Ошибка: введено либо неверное число либо не число вовсе!')
        
digits_sum = 0
calculation_string = []

for char in user_input:
    square = int(char) ** 2
    digits_sum += square
    calculation_string.append(f'{char}*{char}')


print(f'{number} => { ' + '.join(calculation_string)} = {digits_sum}')