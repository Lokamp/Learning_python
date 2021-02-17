import sys
import time


def check_even_list_append(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num * num)
    return even


def check_even_generator_yield(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num * num


def check_even_list_comprehension(numbers):
    return [num * num for num in numbers if num % 2 == 0]


def check_even_generator_expression(numbers):
    return (num * num for num in numbers if num % 2 == 0)


size = 100000000

for check_even in (
        check_even_list_append,
        check_even_generator_yield,
        check_even_list_comprehension,
        check_even_generator_expression,
):
    t1 = time.time()
    cubes = check_even(range(size))
    result = sum(cubes)
    t2 = time.time()
    print(f"function: {check_even.__name__:31} duration:{t2 - t1:8.4f} s size:{sys.getsizeof(cubes):10}")
