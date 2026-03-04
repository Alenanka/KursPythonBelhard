"""
1. Запросить у пользователей имя и отзыв о магазине. 
Программа должна запрашивать данные пока не введено слово "stop". 
Все данные сложить в словарь.
    -распечатать количество отзывов
    -распечатать отдельно имена пользователей
    -распечатать отдельно отзывы

"""
reviews_dict={}

while True:
     user_input = input('Введите имя и отзыв(или "stop" для выхода): ')
     if user_input.lower() == 'stop':
         break
     
     input_parts = user_input.split()
     user_name = input_parts[0] 
     review_text = ' '.join(input_parts[1:]) 
     reviews_dict[user_name] = review_text

print(f"Количество отзывов: {len(reviews_dict)}")

print("Имена: ")
for user in reviews_dict.keys():
    print(f"{user}")

print("Отзывы: ")
for i, review in enumerate(reviews_dict.values()):
    print(f"{i+1}. {review}")