# Получение выборки из датасета по количеству символов в ячейке без использования циклов
import pandas as pd
from collections import Counter

# Разбивает строку и выводит кол-во самых распространенных слов по убыванию
words = Counter('this one and that one for one time'.split()).most_common() 
df = pd.DataFrame(words, columns=['key','value'])
print(df)

print('*' * 50)

k = df.loc[(df['key'].apply(lambda x: len(str(x)) == 3) == True)]
print(k)
