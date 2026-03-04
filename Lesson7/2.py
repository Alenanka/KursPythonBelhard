
'''
Запросить фразу состоящую минимум из трех слов. 
Сформировать фразу из этих слов в которой каждая буква слова, 
продублирована то количество раз, которое соответствует номеру позиции 
данной буквы в слове этой буквы. 
Например: Привет как дела => Прриииввввееееетттттт кааккк деелллаааа

'''

while True:
    phrase = input("Введите фразу состояющую из трех слов: ").split()

    if(len(phrase) != 3):
        print("ВВедите три слова!")
        continue
    else: break

new_phrase_list = []

for word in phrase:
    i = 1 
    new_word = ''
    for letter in word:
        new_word += i*letter
        i += 1   
    new_phrase_list.append(new_word)

new_phrase = ' '.join(new_phrase_list)  
print (new_phrase)
   