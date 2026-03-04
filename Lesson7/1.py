"""
Запросить у учителя оценки ученика по одной до тех пор пока он не введет 0. 
Выдать средний бал ученика.

"""
grade_list = []

while True:
    grade_input = input('Введите оценку: ')
    if not grade_input.isdigit():
        print('Ошибка: Введите целое число!')
        continue
    grade = int(grade_input)
    if grade == 0:
        break    
    grade_list.append(grade)

if grade_list:
    avg = sum(grade_list) / len(grade_list)
    print(f'Средний балл ученика: {avg:.2f}')
else:
    print('Оценки не были введены.')