# Пусть имеется вот такая строка:
# "int= целое число, dict =словарь, list=список, str=строка, bool=булевый тип"
# Требуется из нее создать словарь с ключам
# int, dict, list, str, bool
#
# и соответствующими значениями.

string = "int= целое число, dict =словарь, list=список, str=строка, bool=булевый тип"
string = string.replace('=', ', ').split(', ')
dict_string = {}
count = 0

for item in string:
    if count <= len(string) - 1:
        dict_string[string[count]] = string[count + 1].strip()
        count += 2

print(dict_string)
