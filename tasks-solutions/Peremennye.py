# Типы переменных:
# Целое число - int
# Число с плавающей точкой - float
# Логический тип (истина/ложь) - bool
# Ничего (пустой тип) - None
# Строка - str
# Изменение типа переменной:
# str(int)
# int('10')

# Определяем переменные
name = 'Vlad'
age = 45
print(type(name)) # Вывести тип переменной

# Разделители
print(name, age, sep='/')   # Выводим через разделитель '/'
print(name, end=';')        # Вывод данных через разделитель в конце строки
print(age, end=';') 
print('\n') 

# Получаем данные от пользователя
name = input('Введите Ваше имя: ')                 # Текст
family = str(input('Введите Вашу фамилию: '))      # Текст
age = int(input('Введите Ваш возраст: '))          # Число
print('Name - %s, Family - %s, Age - %d' %(name, family, age))
print('Здравствуйте, {} {}! Вам {}?'.format(name, family, age))
print(f'Здравствуйте, {name} {family}! Вам {age/2:.2f}?') # .2f - age разделить и оставить 2 знака после запятой
# Вывод данных и форматирование см. в файле 'Строки'

# Арифметика
print(5 + 10)
print(3 * 7, (17 - 2) * 8)
print(2 ** 16)  # две звёздочки — это возведение в степень
print(37 / 3)   # один слэш — это деление с ответом-дробью
print(37 // 3)  # два слэша — это целая часть от деления
                # это как операция div в других языках
print(37 % 3)   # процент — это остаток от деления
                # это как операция mod в других языках2

# Четное / нечетное
a = int(input('Введите число - '))
if a % 2 == 0: # Делится на 2 без остатка - Четное
    print('Четное!')
if a % 2 != 0: # Делится на 2 с остатком - Нечетное
    print('Нечетное!')
