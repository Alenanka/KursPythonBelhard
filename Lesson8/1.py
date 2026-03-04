"""
Написать функцию  которая принимает фамилию имя и отчество одной стройкой, 
а возвращает в виде краткого формата. 
Функция должна содержать необязательный параметр в виде логического значения 
и в зависимости от него возвращала ФИО в двух следующих форматах:
 -  Николаев И.С. 
 -  И.С.Николаев


"""
def fio(full_name, surname_first=True):
    parts = full_name.split()
    if len(parts) != 3:
        return "Ошибка: Введите ФИО полностью"
    surname = parts[0] 
    name = parts[1]  
    secname = parts[2] 

    initials = f"{name[0]}.{secname[0]}."
    if surname_first:
        return f"{surname} {initials}"
    else:
        return f"{initials} {surname}"



fio_input = input('Введите ФИО: ')

fio_for_print= fio(fio_input,surname_first=False)
print(fio_for_print)
