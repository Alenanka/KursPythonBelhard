'''
Запросить высоту елочки - число от 3 до 20. 
Напечатать на экране елочку где ее высота равна числу строк. 
Пример елочки из 4 строк:
   *
  ***
 *****
*******

* - елочка со снегом
'''

while True:
    height = input('Введите высоту елочки - число от 3 до 20: ')
    if  height.isdigit() and 3 <= int(height) <= 20:
        height = int(height)
        break
        print("Введено неверное число.")
    else:
        print("Введено неверное число.")

for i in range(1,height+1):
    stars = i*2-1
    spases = height-i
    print(' '*spases +"*"*stars)

