func_count = [0]


def count_call_functions(func):
    def wrapper(*args):
        func(*args)
        count = func_count.pop(0)
        count += 1
        func_count.append(count)
        wrapper.__name__ = func.__name__
    return wrapper


@count_call_functions
def custom_sum(a, b):
    print(f'{a + b}')


custom_sum(2, 2)
custom_sum(2, 3)
custom_sum(2, 4)
custom_sum(2, 5)
custom_sum(2, 6)

print(f'Функция {custom_sum.__name__} была вызвана {func_count[0]} раз')
