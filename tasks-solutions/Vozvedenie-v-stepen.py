'''
Программа принимает действительное положительное число x и целое отрицательное число y. 
Необходимо выполнить возведение числа x в степень y. 
Задание необходимо реализовать в виде функции my_func(x, y). 
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами. 
Первый — возведение в степень с помощью оператора *. 
Второй — более сложная реализация без оператора *, предусматривающая использование цикла.
'''
def my_pow_fun(x, y):
    try:
        res = x ** y
    except TypeError:
        return "Enter a float number and a negative power"
    return res

print(my_pow_fun(4.5, -2))

# вариант решения

def power(x, y):
    try:
        x, y = float(x), int(y)
        res = x
        for _ in range(abs(y)-1):
            res *= x
        return f"{1/res:.4f}"
    except ValueError:
        return "Value Error"

print(power(input("Первое значение - "), input("Второе значение - ")))