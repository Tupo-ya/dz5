string = 'на этом заканчиваю свое сочинение. поставьте пятерку, Мария Ивановна! я очень старалась!'

# ? На этом заканчиваю свое сочинение. Поставьте пятерку, Мария Ивановна! Я очень старалась!

new_str = ''

sym_up = -1
for i, elem in enumerate(string):
    if elem in ['.', '!', '?']:
        sym_up = i + 2

    if i == 0:
        new_str += elem.upper()
    elif i == sym_up:
        new_str += elem.upper()
    else:
        new_str += elem

print(new_str)