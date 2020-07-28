# Генератор простых паролей

import random

length = int(input('Введите количество символов для пароля: '))
counts = int(input('Введите количество паролей для создания: '))
passwd = list('!@#$%^&*()-=_?abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')

for i in range(counts):
    random.shuffle(passwd)
    password = ''.join([random.choice(passwd) for x in range(length)])
    print (password)
