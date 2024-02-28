import pandas as pd

df = pd.read_excel('task 14.xls')

loc = df.loc[(df['Фамилия'] == 'Колесникова') & (df['Имя'] == 'Ксения')]

for row in loc.values:
    print(f'Ты получил: {row[4]}, за предмет {row[3]}')

avg = round(df['Оценка за любимый предмет'].mean(), 3)
print(f'Средний балл по классу: {avg}')
