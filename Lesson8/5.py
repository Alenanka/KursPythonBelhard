'''
Написать функцию count_char, которая принимает строковое значение,
из которого создает и возвращает словарь, следующего вида:
{'буква': 'количество-вх-ождений-встроку'}
Нельзя пользоваться collections.Counter!

'''


def count_char(input_str):
    result = {char: input_str.count(char) for char in input_str}
    return result


print(count_char("ddnn wer"))