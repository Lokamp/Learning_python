# Пользователь вводит произвольные целые числа и нужно создать словарь,
# у которого ключами будут только четные числа, а значениями – квадраты этих чисел.

number_input = list(input('Введите целое число '))

print(number_input)

dict_number = {}

for number in number_input:
    if int(number) % 2 == 0:
        dict_number[number] = int(number) * 2

print(f'Словарь {dict_number}')