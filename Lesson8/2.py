'''
Написать функцию которая принимает 2 стороны прямоугольника 
и возвращает либо площадь либо периметр в зависимости от дополнительного параметра.

'''
def rectangle(width, length, mode="area"):
    if mode == "perimeter":
        return (width + length) * 2
    else:
        return width * length


print(rectangle(5, 10))                    
print(rectangle(5, 10, "area"))            
print(rectangle(5, 10, "perimeter"))    