'''
Дана строка - "Это тестовая <start>строка для изучения<end> строковых операций". 
Программа должна вывести на экран текст из данной строки     
заключенный между тэгами <start> и <end>. 
Программа должна работать с любой другой строкой с подобными тэгами.

'''
string  = "Это тестовая <start>строка для изучения<end> строковых операций"

start= string.find("<start>")+ len('<start>')
finish= string.find("<end>")
print(string[start:finish])

result = string.split("<start>")[1].split("<end>")[0]

print(result)