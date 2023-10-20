# algebra = input('Решившие алгебру: ').split()
# geom = input('Решившие геометрию: ').split()
# trigonom = input('Решившие тригонометрию: ').split()

algebra = 'Иванов Петров Сидоров Михайлов'.split()
geom = 'Иванов Михайлов'.split()
trigonom = 'Сидоров Михайлов'.split()

all_student = {}

for i in algebra:
    if i in all_student.keys():
        all_student[i] += 1
    else:
        all_student[i] = 1
for i in geom:
    if i in all_student.keys():
        all_student[i] += 1
    else:
        all_student[i] = 1
for i in trigonom:
    if i in all_student.keys():
        all_student[i] += 1
    else:
        all_student[i] = 1

passed = []
for i in all_student:
    if all_student[i] == 3:
        passed.append(i)

if len(passed) != 0:
    print('Сдавшие все задачи:')
    for i in passed:
        print(i, end=', ')
else:
    print('Никто не сдал 3 задачи')