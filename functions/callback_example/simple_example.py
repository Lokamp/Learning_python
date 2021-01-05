
start_color = '\033[34m'
end_color = '\033[0m'
print(f'{start_color}Первый пример{end_color}')


def first_func():
    print(f'Исполняется функция {first_func.__name__}')


def call_func_twice(callback):
    print('Исполняется функция call_func_twice')
    callback()
    callback()


call_func_twice(first_func)

print('_' * 40)
print(f'{start_color}Второй пример{end_color}')


def new_func(a, callback):
    print(f'Функция {new_func.__name__}. Выполняем операцию - {a + 1}')
    callback()


def call_func():
    print(f'Исполняется функция {call_func.__name__}, выполняем операцию - {1 + 1}')


new_func(100, call_func)