'''

Написать функцию, которая возвращает любое число в виде денежной величины 
с разделителями групп разрядов в качестве пробела и валютой в конце. 
Денежная величина всегда должна содержать количество копеек в виде дух 
знаков после точки, даже если исходное число целое. 
*Нельзя использовать форматную строку.
Например: 1234567 -> "1 234 567.00 руб."

с помощью try перехватить возможные ошибки.
'''

def format_currency(amount):
    try:
        amount = float(amount)
        
        int_part = int(amount)
        dec_part = int((amount - int_part) * 100)

        int_str = str(int_part)
        formatted_int = ""
        while len(int_str) > 3:
            formatted_int = " " + int_str[-3:] + formatted_int
            int_str = int_str[:-3]
        formatted_int = int_str + formatted_int
        
        if dec_part < 10:
            dec_str = "0" + str(dec_part)
        else:
            dec_str = str(dec_part)
        
        result = formatted_int + "." + dec_str + " руб."
        
        return result
    
    except (ValueError, TypeError):
        return "Ошибка: введите корректное число"
    

print(format_currency(3344))      
print(format_currency(1000))        
print(format_currency(999))         
print(format_currency(1234.5))      
print(format_currency(1234.56733))    
print(format_currency(0))            
print(format_currency("abc"))     