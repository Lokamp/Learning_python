# Функция принимаяющая на вход список необходимо найти максимальное число,
# в спике могут быть отрицательные значения


def max_custom(items: list) -> int:
    max_item = 0
    for item in items:
        if item > max_item:
            max_item = item

    return max_item


print(max_custom([-8, 66, 6, -4, 9, -6, -1, 5, -11, 44]))


def max_custom_(items: list) -> int:
    max_item = float('inf')
    for item in items:
        if item < max_item:
            max_item = item

    return max_item


print(max_custom_([-8, 66, 6, -4, 9, -6, -1, 5, -11, 44]))
