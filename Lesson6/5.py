"""
Запросить фразу 
    - вывести на экран количество уникальных символов
    - вывести на экран количество уникальных слов
    -* вывести символ который встречался чаще всего

"""

from collections import Counter

phrase = input('Введите фразу: ')

phrase_set = set(phrase)

print(f'Количество уникальных символов: {len(phrase_set)}')

phrase_byword_set = set(phrase.split())

print(f'Количество уникальных  слов: {len(phrase_byword_set)}')

char_counter = Counter(phrase)
most_common_char = char_counter.most_common(1)[0]

print(f'Чаще всего встречается символ: "{most_common_char[0]}" {most_common_char[1]} раз')
