# Подсчет выделения памяти под переменные

import sys

class SumMemory:
    def __init__(self):
        '''
        Класс для посчета памяти под переменные
        Использование класса:
        import SumMemory
        sum_mem = sum_memory.SumMemory()
        sum_mem.extend(num, even, odd)
        sum_mem.extend(num, even, odd, i, {'0', '2', '4'})
        sum_mem.print_sum()
        ------------
        _sum_memory - общее количество занятой памяти
        _types - словарь вида {'type': [count, size]}
        '''
        self._sum_memory = 0
        self._types = {}

    def _add(self, obj):
        '''
        Анализирует полученный объект.
        Формирует словарь по типам объектов и 
        учитывает их количество и потребляемую память.
        Работает рекурсивно для составных объектов.
        '''
        spam = sys.getsizeof(obj)
        eggs = str(obj.__class__)
        self._sum_memory += spam
        if eggs in self._types:
            self._types[eggs][0] += 1
            self._types[eggs][1] += spam
        else:
            self._types[eggs] = [1] * 2
            self._types[eggs][1] = spam

        if hasattr(obj, '__iter__'):
            if hasattr(obj, 'items'):
                for xx in obj.items():
                    self._add(xx)
            elif not isinstance(obj, str):
                for xx in obj:
                    self._add(xx)

    def extend(self, *args):
        '''
        В цикле отправляет переменные для оценки во внутренний метод _add
        '''
        for obj in args:
            self._add(obj)

    def print_sum(self):
        '''
        Вывод результата в консоль
        '''
        print(f'Переменные заняли в сумме {self._sum_memory} байт')
        for key, value in self._types.items():
            print(f'Объекты класса {key} в количестве {value[0]} заняли {value[1]} байт')
