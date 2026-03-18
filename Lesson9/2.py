'''
Написать рекурсивную функцию, которая вычисляет  
факториал переданного в нее числа.

'''

def recursia(n):
    if n == 0 :
        return 1
    return n * recursia(n-1)
    
print(recursia(0))


