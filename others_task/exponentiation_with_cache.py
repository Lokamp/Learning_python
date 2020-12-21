# Простая функция возвездения в квадрат целого числа с кэшем


cache = {}

while True:

    def exponentiation_function(number: int) -> int:
        if number in cache:
            return cache[number]
        else:
            exponentiation = number ** 2
            cache[number] = exponentiation
            return exponentiation


    input_menu = input('1. Посчитать корень числа \n'
                       '2. Выход \n')
    if input_menu == '1':
        number_input = int(input('Введите цело число '))
        print(f'Корень числа {number_input} равен {exponentiation_function(number_input)} \n'
              f'******************')
    elif input_menu == '2':
        exit('Выходим из программы')
