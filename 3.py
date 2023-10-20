# str_1 = input('Введите строку 1: ').lower()
# str_2 = input('Введите строку 2: ').lower()

str_1 = 'машина'
str_2 = 'анишам'

words_1 = {}
words_2 = {}

for i in str_1:
    if i in words_1.keys():
        words_1[i] += 1
    else:
        words_1[i] = 1

for i in str_2:
    if i in words_2.keys():
        words_2[i] += 1
    else:
        words_2[i] = 1
        
anagrama = True
if len(words_1) != len(words_2):
    anagrama = False
else:
    for i in words_1:
        if words_1[i] != words_2[i]:
            anagrama = False

if anagrama:
    print('Это анаграмма')
else:
    print('Это не анаграмма')
