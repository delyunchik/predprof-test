f = open('task 14.csv', newline='', encoding='utf-8-sig')
f.readline()  # пропускаю заголовок
count = 0
sum = 0
subjects = {}  # словарь для вычисления средних по предметам
for line in f.readlines():
    a = line.split(';')
    subject = a[3]
    mark = int(a[4])
    sum += mark
    count += 1
    if subject in subjects:
        subjects[subject]['sum'] += mark
        subjects[subject]['count'] += 1
    else:
        subjects[subject] = { 'sum': mark, 'count': 1 }
    if a[0] == 'Колесникова' and a[1] == 'Ксения':
        print(f'Ты получил: {a[4]}, за предмет {a[3]}')

avg = round(sum / count, 3)
print(f'Средний балл по классу: {avg}')

for subject in sorted(subjects):
    if subjects[subject]['count'] > 0:
        avg = round(subjects[subject]['sum'] / subjects[subject]['count'], 3)
        print(f'Средний балл по предмету {subject}: {avg}')
