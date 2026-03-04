"""
Написать функцию (без регулярных выражений), которая принимает текстовую строку 
и возвращает словарь, который содержит информацию о количестве 
символов, слов, строк и предложений в тексте. 
Затем создайте вторую функцию, которая принимает этот словарь, 
и выводит его содержимое в удобном и красивом формате. 

"""
def analyze_text(text):
    char_count = len(text)
    words = text.split()
    word_count = len(words)
    lines = text.split('\n')
    line_count = len(lines)
    sentence_count = 0
    for char in text:
        if char in '.!?':
            sentence_count += 1
    if text.strip() and sentence_count == 0:
        sentence_count = 1
    return {
        'char_count': char_count,
        'words': word_count,
        'lines': line_count,
        'sentences': sentence_count
    }
    

def print_stats(stats):
    print("=" * 40, "АНАЛИЗ ТЕКСТА", "=" * 40,sep='\n')
    print(f"| {'Параметр':<20} | {'Значение':^12} |")
    print("=" * 40)

    print(f"| {'Символов':<20} | {stats['char_count']:^12} |")
    print(f"| {'Слов':<20} | {stats['words']:^12} |")
    print(f"| {'Строк':<20} | {stats['lines']:^12} |")
    print(f"| {'Предложений':<20} | {stats['sentences']:^12} |")
    print("=" * 40 + "\n")

text = """Первая строка текста.
Вторая строка с вопросом?
Третья строка с восклицанием!

Пустая строка выше.
Финальное предложение."""

stats = analyze_text(text)

print_stats(stats)
