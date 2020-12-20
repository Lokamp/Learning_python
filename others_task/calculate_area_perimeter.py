# Считаем площадь или периметр прямогульника, в завимости от запрошенного типа


def calculate(calculate_type, length, width):
    if calculate_type == 'area':
        return f'Перметр прямогульника составляет {length * width}'
    elif calculate_type == 'perimeter':
        return f'Перметр прямогульника составляет {2 * (length + width)}'
    else:
        return 'Вы нерпавильно ввели слово'


calculate_type_input = input('Введите слово area, если хотите посчитать площадь'
                             'и perimeter, если хотите посчитать периметр ')
length_input = float(input('Ведите длинну '))
width_input = float(input('Ведите ширину '))

print(calculate(calculate_type_input, length_input, width_input))
