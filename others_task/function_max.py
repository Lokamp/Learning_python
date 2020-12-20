# Функция принимаяющая на вход список необходимо найти максимальное число,
# в спике могут быть отрицательные значения


def max_custom(items: list) -> int:
    max_item = [items[0]]
    for item in items:
        if item > max_item[0]:
            max_item[0] = item

    return max_item[0]


print(max_custom([-8, 66, 6, -4, 9, -6, -1, 5, -11, 44]))
