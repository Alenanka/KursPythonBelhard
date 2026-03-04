'''
Написать функцию, которая вычисляет  факториал переданного в нее числа без рекурсии.

'''

def factorial (n):
    result = 1
    if n and n != 1 :
        for i in range(1,n+1):
            result = i*result
        return(result)
    else: return 1

print(factorial(10))
print(factorial(1))
print(factorial(0))
