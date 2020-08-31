print('Эта небольшая программа проверяет является ли введенное слово полидромом.\n'
    'Для завершения работы программы просто введите пустую строку.\n')

def palindrome(word):
    '''
    Функция для определения, является ли введнное слово полидромом.
    '''
    try:
        if str(word) == str(word)[::-1]:
            return True
        else:
            return False
    except ValueError:
        return 'Неверный ввод!'


while True:
    word = input('Пожалуйста, введите слово для проверки: ').lower()
    if word != '':
        print(palindrome(word))
    else:
        break
