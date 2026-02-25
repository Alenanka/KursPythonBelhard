"""
Запросить трижды ввод наименования товаров и их цену через пробел. 
"пример: 
>>>яблоко 10"
>>>груша 15
>>>малина 20
    
    - создать из введенных данных словарь где ключ это наименование, а цена значение
    - запросить имя товара, найти его в словаре, и вывести его цену, увеличенную на 15%. 
    - вывести сумму всех товаров

"""

text = 'Введите  наименование и цену  товара {a}: '

products = [input(text.format(a=1)).split(),
            input(text.format(a=2)).split(),
            input(text.format(a=3)).split()]
products_dict= dict(map(tuple,products)) 

search_key = input('Введите наименовние товара :')

search_result=float(products_dict[search_key])*1.15
sum_products= sum(list(map(int,products_dict.values())))

print(f'Цена товара + 15%: {search_result:.3f}')
print(f'Сумма всех товаров {sum_products } ')

