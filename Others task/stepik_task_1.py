# Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор,
# пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму квадратов
# всех считанных чисел.
# Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0,
# после этого считывание продолжать не нужно.

flag = True
sum_zero = []
while flag:
    input_number = int(input())
    sum_zero.append(input_number)
    if sum(sum_zero) == 0:
        flag = False

result = sum([number ** 2 for number in sum_zero])
print(result)