count_city = int(input('Введите количество городов: '))

print('Введите города:')
cities = {}
for i in range(count_city):
    city = input('>> ')
    if city in cities.keys():
        cities[city] += 1
    else:
        cities[city] = 1

all_retry = 0
for i in cities:
    if cities[i] > 1:
        all_retry += cities[i]

print(f'Всего повторений: {all_retry}')