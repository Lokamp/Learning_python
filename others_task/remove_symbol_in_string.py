# Удалить символ + в строке

string = '38 + 45 55 6.5 + 44 55 4.5 +'
new_string = string.split(' ')
new_lst = []

for item in new_string:
    if item != '+':
        new_lst.append(item)

print(new_lst)

# Второй пример с удалением, если + является частью числа
new_string = '38+ 45 + 55 6.5+ 44 + 55 4.5+'

print(new_string.replace('+', '').split())


