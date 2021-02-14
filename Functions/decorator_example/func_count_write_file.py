from datetime import datetime


def function_call_count(func):
    def wrapper(*args):
        func(*args)
        func_name = wrapper.__name__ = func.__name__
        with open('file.txt', 'a') as file:
            file.write(f'{datetime.now()};{func_name};\n')
    return wrapper


@function_call_count
def custom_sum(a, b):
    print(f'{a + b}')


custom_sum(2, 2)
custom_sum(2, 3)
custom_sum(2, 4)
custom_sum(2, 5)
custom_sum(2, 6)
