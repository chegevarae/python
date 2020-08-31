# Все возможные комбинации списков
from itertools import product

a1 = [1,2,3]
a2 = [4,5,6]
a3 = [7,8,9]

cnt = 0
for i in list(product(a1,a2,a3)):
    cols = list(product(a1,a2,a3))
    for t in cols:
        cnt += 1
        print(f'{cnt} {t}', end='\n')
